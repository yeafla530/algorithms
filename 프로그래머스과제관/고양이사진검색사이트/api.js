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
