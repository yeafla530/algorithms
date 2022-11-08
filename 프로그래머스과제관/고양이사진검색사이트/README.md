# 고양이 사진첩 사이트

[참고사이트]: https://velog.io/@z6su3/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B3%A0%EC%96%91%EC%9D%B4-%EC%82%AC%EC%A7%84-%EA%B2%80%EC%83%89-%EC%82%AC%EC%9D%B4%ED%8A%B8-%EA%B0%9C%EB%B0%9C-%EA%B2%80%EC%83%89-%ED%8E%98%EC%9D%B4%EC%A7%80	"참고사이트"



> thecatapi 에서 크롤링한 데이터를 이용해 이미지를 검색하는 베이스 코드가 주어짐

[TOC]



# 1. API 분석

## 🥕코드 구조 관련

- ES6 module 형태로 코드를 변경합니다.
  - `webpack` , `parcel` 과 같은 번들러를 사용하지 말아주세요.
  - 해당 코드 실행을 위해서는 `http-server` 모듈을(로컬 서버를 띄우는 다른 모듈도 사용 가능) 통해 `index.html` 을 띄워야 합니다.
- **API fetch 코드를 `async` , `await` 문을 이용하여 수정**해주세요. 해당 코드들은 에러가 났을 경우를 대비해서 적절히 처리가 되어있어야 합니다.
- **`필수`** API 의 **status code 에 따라 에러 메시지를 분리하여 작성**해야 합니다. 아래는 예시입니다.

```js
const request = async (url: string) => {
	try {       
		const result = await fetch(url);       
		return result.json();     
	} catch (e) {       
		console.warn(e);     
	}   
}    

const api = {     
	fetchGif: keyword => {       
		return request(`${API_ENDPOINT}/api/gif/search?q=${keyword}`);     
	},     
	fetchGifAll: () => {       
		return request(`${API_ENDPOINT}/api/gif/all`);     
	}   
};
```

- SearchResult 에 각 아이템을 클릭하는 이벤트를 Event Delegation 기법을 이용해 수정해주세요.
- 컴포넌트 내부의 함수들이나 Util 함수들을 작게 잘 나누어주세요.



## 🥕 랜덤한 고양이 50개 요청

- GET : /cats/random50

```jsx
HTTP/1.1 200 OK
{
  "data": [{
    id: string
    url: string
    name: string
  }]
}
```

## 🥕 사용자의 검색 요청

Get : /cats/search | query ⇒ q=””

```jsx
HTTP/1.1 200 OK
{
  "data": [{
    id: string
    url: string
    name: string
  }]
}
```

## 🥕 이미지 상세보기 시 고양이 데이터 요청

Get : /cats/:id

```jsx
HTTP/1.1 200 OK
{
  "data": {
    name: string
    id: string
    url: string
    width: number
    height: number
    temperament: string
    origin: string
  }
}
```



#  2. API해결

> cats를 기반으로 `랜덤한 고양이 사진`, `사용자 검색 요청`, `고양이 데이터` 세가지로 구분되므로, 인자에 구분할 수 있는 type과 데이터인 payload를 받아 활용

```javascript
// fetch를 async await를 활용하여 진행
// 에러가 나는 경우 적절히 처리
// status code에 따라 에러메세지를 분리하여 작성
const API_ENDPOINT =
  "https://q9d70f82kd.execute-api.ap-northeast-2.amazonaws.com/dev";


export const request = async (type, payload) => {
  let API_SUB_POINT = "";

  switch (type) {
    case "search":
        API_SUB_POINT = `/search?q=${payload}`;
        break;
    case "random":
      API_SUB_POINT = `/random50`
      break
    default:
      API_SUB_POINT = `/${payload}`
    
  }

  const res = await fetch(`${API_ENDPOINT}${API_SUB_POINT}`)
  switch (res.status / 100) {
    case 3:
      return `Redirects Error with status code ${res.status}`;
    case 4:
      return `Client Error with status code ${res.status}`;
    case 5:
      return `Server Error with status code ${res.status}`;
    default:
      return res.json();

  }
}


// const api = {
//   fetchCats: keyword => {
//     return fetch(`${API_ENDPOINT}/api/cats/search?q=${keyword}`).then(res =>
//       res.json()
//     );
//   }
// };

```



# 3. 개발 (컴포넌트 재구성)

* 기존 모듈 삽입 방식과 함수형 컴포넌트로 재구성을 진행

```
main.js ← App.js ← api/api.js (api)
← components(floder) (컴포넌트) ← SearchInput.js (검색창)
← SearchResult.js (검색결과)
← ImageInfo.js (모달)
```



## 🐇 프로젝트 재구성

### 🥕 main 모듈 및 모듈 삽입

`index.html`

```

...
  <head>
		...
    <link rel="stylesheet" href="src/style.css" />
    <script type="module" src="src/main.js"></script>
    <title>Cat Search</title>
  </head>
  <body>
    <div id="App"></div>
  </body>
...
```

`main.js`

```
import App from "./App.js";

new App(document.querySelector("#App"));
```



## 🐰 컴포넌트 재구성

### 🥕 App.js 재구성

```
App.js
import SearchInput from "./components/SearchInput.js";
import SearchResult from "./components/SearchResult.js";
import ImageInfo from "./components/ImageInfo.js";

import { request } from "./api/api.js";

export default function App($app) {
  this.state = {
    visible: false,
    image: null,
    data: [],
  };

  const searchInput = new SearchInput({
    $app,
    onSearch: async (keyword) => {
      const searchData = await request("search", keyword);
      this.setState({
        ...this.state,
        data: searchData.data,
      });
    },
  });

  const searchResult = new SearchResult({
    $app,
    initialState: [],
    onClick: (image) => {
      this.setState({
        visible: true,
        image,
      });
    },
  });

  const imageInfo = new ImageInfo({
    $app,
    initialState: {
      visible: false,
      image: null,
    },
  });

  this.setState = (nextState) => {
    this.state = nextState;
    searchResult.setState(this.state.data);
		imageInfo.setState({
      image: this.state.image,
      visible: this.state.visible,
    });
  };
}
```

### 🥕 SearchInput.js 재구성

`SearchInput.js`

```
export default function SearchInput({ $app, onSearch }) {
  this.$target = document.createElement("input");
  this.$target.className = "SearchInput";
  this.$target.placeholder = "고양이를 검색해보세요.|";
  $app.appendChild(this.$target);

  this.onSearch = onSearch;

  this.$target.addEventListener("keyup", (e) => {
    if (e.keyCode === 13) {
      this.onSearch(e.target.value);
    }
  });
}
```

### 🥕 SearchResult.js 재구성

EventDelegation을 이용하여 클릭 이벤트를 수정 => closest를 이용해서 이벤트 위임을 통한 최적화를 진행해준다. 

```
export default function SearchResult({ $app, initialState }) {
  this.state = initialState;
  this.$target = document.createElement("div");
  this.$target.className = "SearchResult";
  $app.appendChild(this.$target);

  this.setState = (nextState) => {
    this.state = nextState;
    this.render();
  };

  this.render = () => {
		if (this.state.data) {
	    this.$target.innerHTML = this.state.data
	      .map(
	        (cat, index) => `
	        <div class="item" data-index="${index}">
	          <img src=${cat.url} alt=${cat.name} />
	        </div>
	        `
	      )
	      .join("");
		}
  };

  this.onClick = onClick;

  this.$target.addEventListener("click", (e) => {
    const $searchItem = e.target.closest(".item");
    const { index } = $searchItem.dataset;
    this.onClick(this.state[index]);
  });

  this.render();
}
```



### 🥕 ImageInfo.js 재구성

`ImageInfo.js`

```javascript
export default function ImageInfo({ $app, initialState }) {
  this.state = initialState;
  this.$target = document.createElement("div");
  this.$target.className = "ImageInfo";
  $app.appendChild(this.$target);

  this.setState = (nextState) => {
    this.state = nextState;
    this.render();
  };

  this.render = () => {
    if (this.state.image) {
      const { name, url, temperament, origin } = this.state.image;

      this.$target.innerHTML = `
        <div class="content-wrapper">
          <div class="title">
            <span>${name}</span>
            <div class="close">x</div>
          </div>
          <img src="${url}" alt="${name}"/>        
          <div class="description">
            <div>성격: ${temperament}</div>
            <div>태생: ${origin}</div>
          </div>
        </div>`;
    }
    this.$target.style.display = this.state.visible ? "block" : "none";
  };

  this.render();
```



# 4. 개발 (검색 페이지)

검색페이지 구성도

> main.js ← App.js ← api/api.js
> ← components(floder) ← SearchInput.js
> ← SearchError.js
> ← SearchKeyword.js
> ← SearchResult.js
> ← ImageInfo.js
> ← Loading.js
> ← lib ← LocalStorage.js
> ← LazyLoading.js



## 🐰검색창

기존 검색창 코드의 placeholder를 보면 `|`이상한 문자가 있음을 알 수 있습니다.

해당 문자는 [고양시의 전용 서체](http://www.goyang.go.kr/www/www05/www05_3/www05_3_6/www05_3_6_tab1.jsp)로 고양고양이 캐릭터 일러스트를 딩벳으로 사용할 수 있습니다.

Local 연습 환경에서 해당 폰체를 사용하기 위해 다음과 같이 style을 수정해줍니다.

`style.css`

```
@font-face {
  font-family: "Goyang";
  /* src: url("fonts/Goyang.woff") format("woff"); */
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/Goyang.woff") format("woff");
  font-weight: normal;
  font-style: normal;
}
```



### 🥕 focus 처리

- 페이지 **진입 시 포커스가 `input` 에 가도록 처리**한다

`SearchInput.js`

```
export default function SearchInput({ $app, onSearch }) {
	...
  $app.appendChild(this.$target);

  this.$target.focus();
	...
}
```



### 🥕 기존 키워드 삭제

* **키워드를 입력한 상태에서 `input` 을 클릭할 시에는 기존에 입력되어 있던 키워드가 삭제되도록** 만들어야 합니다.
* 요소 클릭시 요소의 value값을 없애주도록 코딩 

```
export default function SearchInput({ $app, onSearch }) {
  ...
	//클릭 시 기존 키워드 삭제
  this.$target.addEventListener("click", (e) => {
    e.target.value = "";
  });

  this.$target.addEventListener("keyup", (e) => {
    ...
  });
}
```



## 🐇 사용자 UI

### 🥕 Loading UI

* **`필수`** 데이터를 불러오는 중일 때, 현재 데이터를 불러오는 중임을 유저에게 알리는 UI를 추가
* loading 여부에 따라 변경되는 컴포넌트를 생성하고 App에 렌더링 해줌

`Loading.js`

```
export default function Loading({$app, initialState}) {
    this.state = initialState
    this.$target = document.createElement("div")
    this.$target.classList = "Loading"
    $app.appendChild(this.$target)

    this.setState = (nextState) => {
        this.state = nextState
        this.render()
    }

    this.render = () => {
        this.$target.innerHTML = `
            <div class="content">
                <div class="loading">Loading...</div>
            </div>
        `

        this.$target.style.display = this.state ? "block" : "none"
    }

    this.render()
}
```



### 🥕 Error UI

* **`필수`** 검색 결과가 없는 경우, 유저가 불편함을 느끼지 않도록 UI적인 적절한 처리가 필요
* 검색 결과에 따라 변경되는 컴포넌트를 생성해 처리하고 APp에 렌더링한 뒤 검색결과가 없는 경우를 고려해서 App.js의 searchInput을 수정한다
* 해당 변경을 변수 `error`를 통해 처리

`SearchError.js`

```
export default function SearchError({ $app, initialState }) {
  this.state = initialState;
  this.$target = document.createElement("div");
  this.$target.className = "SearchError";
  $app.appendChild(this.$target);

  this.setState = (nextState) => {
    this.state = nextState;
    this.render();
  };

  this.render = () => {
    this.$target.innerHTML = `냐옹이들이 없어요. ┃ `;
    this.$target.style.display = this.state ? "block" : "none";
  };

  this.render();
}
```

`App.js`

```
import SearchError from "./components/SearchError.js";
...

export default function App($app) {
  this.state = {
    error: false,
		...
  };
	...
	const searchInput = new SearchInput({
    $app,
    onSearch: async (keyword) => {
      const searchData = await request("search", keyword);

			//데이터가 존재하지 않는 경우 Error UI처리
			if (!searchData.data || !searchData.data.length) {
        ...
        return;
      }

	    ...
			//데이터가 존재하는 경우 Error UI처리
			this.setState({
        ...
        error: false,
      });
    },
  });

  const searchError = new SearchError({
    $app,
    initialState: this.state.error,
  })

  this.setState = (nextState) => {
    this.state = nextState;
		...
    searchError.setState(this.state.error);
  };
}
```



## 🐇 검색 키워드

- 최근 검색한 키워드를 **`SearchInput` 아래에 표시**되도록 만들고, **해당 영역에 표시된 특정 키워드를 누르면 그 키워드로 검색이 일어나도록** 만듭니다. 단, 가장 최근에 검색한 **5개의 키워드만 노출**되도록 합니다.



1. 키워드 컴포넌트 생성
2. 키워드 변수 추가 및 렌더링
3. 키워드 로직 추가

### 🥕 키워드 컴포넌트 생성

* 해당 키워드를 선택할 시 검색요청이 발생하도록 구현
  * 버튼에 이벤트 할당 시 이벤트 위임(EventDelegation)을 고려하여 개발
  * 이벤트 위임은 [closest](https://velog.io/@z6su3/[https://velog.io/@z6su3/closest](https://velog.io/@z6su3/closest))를 활용하여 고려

`SearchKeyword.js`

```javascript
export default function SearchKeyword({$app, initialState, onClick}) {
    this.state = initialState
    this.$target = document.createElement("div")
    this.$target.className = "SearchKeyword"
    $app.appendChild(this.$target)

    this.setState = (nextState) => {
        this.state = nextState
        this.render()
    }

    this.render = () => {
        if (this.state) {
            this.$target.innerHTML = this.state
                .map((keyword) =>{
                    return `
                        <button class="Keyword" data-keyword="${keyword}">
                            ${keyword}
                        </button>
                    `
                }).join("")
        }
    }

    this.onClick = onClick

    this.$target.addEventListener("click", (e) => {
        const $keywordItem = e.target.closet(".Keyword")
        if ($keywordItem) {
            const {keyword} = $keywordItem.dataset

            const $input = document.querySelector(".SearchInput")
            $input.value = keyword

            this.onClick(keyword)

        }

    })

    this.render()
}
```





### 🥕 키워드 변수 추가 및 렌더링

* 변수 `Keyword`를 추가하고, App.js에 렌더링
* 키워드를 렌더링 하기 전 가장 최근 검색 및 클릭 한 키워드가 필두에 존재하도록 구현하여 App.js에 렌더링

`App.js`

```
import SearchKeyword from "./components/SearchKeyword.js";
...

export default function App($app) {
  this.state = {
		...
    keyword: [],
  };

	...

  const searchKeyword = new SearchKeyword({
    $app,
    initalState: this.state.keyword,
    onClick: async (keyword) => {
    	const keywordData = await request("search", keyword);

		//검색한 키워드가 최근 기록에 있으면 배제
      	const nextKeyword = [
        	keyword,
        	...this.state.keyword.filter((word) => word != keyword),
      	];

    	this.setState({
        	...this.state,
        	data: keywordData.data,
        	keyword: nextKeyword,
    	});
    },
  });

	...

  this.setState = (nextState) => {
    this.state = nextState;
		...
		searchKeyword.setState(this.state.keyword);
  };
}
```





### 🥕 키워드 로직 추가

* 키워드는 검색을 할 때 생성
  * 최근에 검색한 키워드 5개까지 등록
  * 검색 결과가 없는 경우 등록되지 않도록 구현

`App.js`

```JS
...
export default function App($app) {
	...

  const searchInput = new SearchInput({
    $app,
    onSearch: async (keyword) => {
      const searchData = await request("search", keyword);

      //검색 결과가 없는 경우 반환되어 keyword를 생성하지 않음
      if (!searchData.data || !searchData.data.length) {
        ...
        return;
      }

      //최근 키워드를 필두에 저장, 단 중복되는 단어는 제거
			var nextKeyword = [
        keyword,
        ...this.state.keyword.filter((word) => word != keyword),
      ];

      //키워드 추가 시 5개 이상 넘어가는 경우 처리
      if (nextKeyword.length > 5) {
        nextKeyword = nextKeyword.slice(0, 5);
      }

      ...
    },
  });

	...
}
```



## 🐇 검색결과 유지

* 페이지를 새로고침해도 마지막 검색 결과 화면이 유지되도록 처리합니다.
* 이를 위해 검색 요청이 일어나는 모든 부분에 localStorage를 활용하여 처리
* 해당 요청은 빈번하게 일어나기 때문에 따로 lib/LocalStorage.js로 생성하여 관리

`LocalStorage.js`

```
export const setLocalStorage = (data) => {
  localStorage.setItem("lastSearchData", JSON.stringify(data));
};

export const getLocalStorage = () => {
  return JSON.parse(localStorage.getItem("lastSearchData"));
};
```



`App.js`

```js
...
import { setLocalStorage, getLocalStorage } from "./lib/LocalStorage.js";

export default function App($app) {
  ...

  const searchInput = new SearchInput({
    $app,
    onSearch: async (keyword) => {
      const searchData = await request("search", keyword);

      ...
      setLocalStorage(searchData);
			...
    },
  });

	...

  const searchKeyword = new SearchKeyword({
    $app,
    initalState: this.state.keyword,
    onClick: async (keyword) => {
      const keywordData = await request("search", keyword);

      setLocalStorage(keywordData);
			
			...
    },
  });

	//페이지 새로고침으로 리렌더링 될 때 초기설정 진행
  const init = () => {
    const storage = getLocalStorage();
		
		//데이터가 비어있거나, 없거나, 잘못 저장된 경우
    if (!storage || !storage.data || !storage.data.length) {
      return;
    }

    this.setState({
      ...this.state,
      data: storage.data,
    });
  };
  init();
}
```



## 🐇 랜덤 검색 추가

- **`필수`** SearchInput **옆에 버튼을 하나 배치**하고, 이 **버튼을 클릭할 시 `/api/cats/random50` 을 호출**하여 화면에 뿌리는 기능을 추가합니다. 버튼의 이름은 마음대로 정합니다.
  - SearchInput에 section을 추가하고 검색창과 랜덤버튼을 하위 요소로 추가
  - 랜덤 버튼 관련한 이벤트 로직을 App.js의 searchInput에 추가

`SearchInput.js`

```
export default function SearchInput({ $app, onSearch, onClick }) {
  this.$target = document.createElement("section");
  this.$target.className = "SearchSection";

  this.$input = document.createElement("input");
  this.$input.type = "text";
  this.$input.className = "SearchInput";
  this.$input.placeholder = "고양이를 검색해보세요.|";

  this.$button = document.createElement("button");
  this.$button.className = "SearchRandom";
  this.$button.innerHTML = `<span>╅</span></br>랜덤냐옹`;

  this.$target.appendChild(this.$input);
  this.$target.appendChild(this.$button);
  $app.appendChild(this.$target);

  this.$target.focus();

  this.onSearch = onSearch;
  this.onClick = onClick;

  this.$input.addEventListener("click", (e) => {
    e.target.value = "";
  });

  this.$input.addEventListener("keyup", (e) => {
    if (e.keyCode === 13) {
      this.onSearch(e.target.value);
    }
  });

  this.$button.addEventListener("click", () => {
    this.onClick();
  });
}
```



`App.js`

```
...
export default function App($app) {
  ...
  const searchInput = new SearchInput({
    $app,
    onSearch: async (keyword) => {
			...
    },
    onClick: async () => {
      const randomData = await request("random");
      
      setLocalStorage(randomData);

      this.setState({
        ...this.state,
        data: randomData.data,
      });
    },
  });

	...
}
```



# 🐇 Lazy Load

- lazy load 개념을 이용하여, 이미지가 화면에 보여야 할 시점에 load 되도록 처리해야 합니다.
  - **lib/LazyLoading.js 로 파일을 관리**하고 **SearchResult.js에서 이미지가 렌더링 되는 시점**에 **lazy loading이 일어나도록 조절**
  - `Intersection Observer`를 활용해 개발

1. **`img tag`에 `src` 속성 아닌 `data-src`속성에 `url`을 할당할 것**. 또한 **lazy load가 적용된 태그는 `lazy`클래스를 할당**할 것.
2. **`lazy`클래스를 가진 모든 요소를 가져와** **Intersection의 Observer를 할당**
3. API를 통해 요소가 포착되면, lazy클래스를 삭제하고 url을 src속성으로 옮긴뒤 옵저버 제거



https://velog.io/@z6su3/lazyload











- `추가` 검색 결과 각 아이템에 마우스 오버시 고양이 이름을 노출합니다.









### HTML, CSS 관련

- 현재 HTML 코드가 전체적으로 `<div>` 로만 이루어져 있습니다. 이 **마크업을 시맨틱한 방법으로 변경**해야 합니다.
- 유저가 사용하는 디바이스의 가로 길이에 따라 검색결과의 **row 당 column 갯수를 적절히 변경**해주어야 합니다.
  - **992px 이하: 3개**
  - **768px 이하: 2개**
  - **576px 이하: 1개**
- **다크 모드(Dark mode)를 지원하도록 CSS를 수정**해야 합니다.
  - CSS 파일 내의 **다크 모드 관련 주석을 제거한 뒤 구현**합니다.
  - **모든 글자 색상은 `#FFFFFF` , 배경 색상은 `#000000` 로 한정**합니다.
  - 기본적으로는 OS의 다크모드의 활성화 여부를 기반으로 동작하게 하되, 유저가 테마를 토글링 할 수 있도록 좌측 상단에 해당 기능을 **토글하는 체크박스를 만듭니다**.