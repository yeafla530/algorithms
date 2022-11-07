import SearchInput from "./components/SearchInput.js";
import SearchResult from "./components/SearchResult.js";
import ImageInfo from "./components/ImageInfo.js";
import Loading from "./Loading.js"
import SearchError from "./SearchError.js"
import SearchKeyword from "./SearchKeyword.js"

import {setLocalStorage, getLocalStorage} from "./lib/LocalStorage.js"
import { request } from "./api/api.js";

export default function App($app) {
    this.state = {
      loading: false,
      error: false,
      visible: false,
      image: null, 
      data: [],
      keyword: [],
    }
    
    const loading = new Loading({
      $app, 
      initialState: this.state.loading
    })


    const searchInput = new SearchInput({
      $app,
      onSearch: async (keyword) => {
        const searchData = await request("search", keyword);
        setLocalStorage(searchData)
        // 데이터가 존재하지 않을때
        if (!searchData.data || !searchData.data.length) {
          //?
          this.setState({
            ...this.state,
            error: true
          })
          return 
        }

        //데이터가 존재하는 경우 Error UI처리
        this.setState({
          ...this.state,
          data:searchData.data,
          error: false
        })
        
        // 5개 넘어가면 SLICE
        if (nextKeyword.length > 5) {
          nextKeyword = nextKeyword.slice(0, 5)
        }
      },

      onClick: async (keyword) => {
        const randomData = await request("random")
        setLocalStorage(randomData)
        this.setState({
          ...this.state,
          data: randomData.data
        })
      }
    });

    const searchKeyword = new SearchKeyword({
      $app, 
      initialState: this.state.keyword,
      onClick: async (keyword) => {
        const keywordData = await request("search", keyword)
        setLocalStorage(keywordData)
        // 검색한키워드가 최근 기록에 있으면 배제
        const nextKeyword = [
          keyword,
          ...this.state.keyword.filter((word) => word != keyword)
        ]

        this.setState({
          ...this.state,
          data: keywordData.data,
          keyword: nextKeyword
        })
      }

    })

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

    const searchError = new SearchError({
      $app,
      initialState: this.state.error,
    })

    const searchResult = new SearchResult({
      $app,
      initialData: this.data,
      onClick: image => {
        this.imageInfo.setState({
          visible: true,
          image
        });
      }
    });


    const imageInfo = new ImageInfo({
      $app,
      data: {
        visible: false,
        image: null
      }
    });
  

  this.setState = (nextData) => {
    this.state = nextData;
    searchResult.setState(this.state.data);
    imageInfo.setState({
      image: this.state.image,
      visible: this.state.visible
    })
    loading.setState(this.state.loading)
    searchError.setState(this.state.error)
    searchKeyword.setState(this.setState.keyword)
  }

}
