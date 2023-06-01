# practice-django

for CI/CD django server



# APIs


### board

게시판

* POST board/create/ 
  * 게시글 생성


* GET board/update/\<id>/
  * id에 해당 하는 게시글 수정 페이지 반환


* POST board/update/\<id>/
  * id에 해당 하는 게시글 수정


* POST board/delete/
  * body 의 id 값에 해당 하는 게시글 삭제


* GET board/\<id>/
  * id에 해당 하는 게시글 페이지 반환



### actuator

서버 상태 확인

* actuator/healthcheck/
  * 서버 현재 상태 확인 api


* actuator/healthcheck/\<status>/
  * 서버 상태 테스트를 위한 api
  * status에 원하는 HTTP staus code를 요청하면 해당 응답 제공
  * eg. actuator/healthcheck/400/ 요청시 400 에러 응답



# Server Run

> pip install -r requirements.txt \
python manage.py runserver 