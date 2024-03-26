const axios = require('axios')                       // 1

const URL = 'https://jsonplaceholder.typicode.com/todos/1'
axios(
  {
    method: 'get',
    url: URL
  }
)                                                   // 2.
  .then(response => console.log(response.data))     // 3.
