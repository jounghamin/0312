- data CRUD
- db table은 존재한다고 가정. - Article
### Article Create
- URL : `/articles/`
- http method : `POST`
- data : 어떤 article을 만들 것인지(제목, 내용 등등)
	- validation check
		- 성공 -> 저장
		- 실패 -> 에러메시지 전달, 등등
- 응답 : JSON
	- serialize 과정

### Article Read(전체)
- URL : `/articles/`
- method : `GET`
- 응답 : JSON
	- serializer


### Article Read(하나)
- URL : `/articles/<id>/`
- method : `GET`
- 응답 : json
	- serialize

### Article Delete
- URL : `/articles/<id>/`
- method : `DELETE`
- 응답 : 성공 여부만 보냄
	- 성공 : 200번대
	- 실패 : 400번대

### Article Update
- URL : `/articles/<id>/`
- method : `PUT`
- data : 어떻게 바꿀지(title, content와 같은)
	- validation check
		- 성공 -> 업데이트
		- 실패 -> 에러메시지
- 응답 : JSON
	- serialize

