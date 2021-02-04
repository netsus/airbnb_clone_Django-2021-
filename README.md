Cloning Airbnb using Python, Django, Tailwind CSS and more... in WSL2

#2.5 Django Applications
장고 프로젝트는 application의 집합. application은 function의 집합.
project 계획 방법.
airbnb 숙소(rooms)보기 -> room 폴더에 넣을 function 계획
rooms app: 숙소 생성, 검색, 삭제, 수정, 디테일페이지 보여주기, 모든 room 보여주기
app 폴더를 크게만들면 안된다. -> 주로 생성, 검색, 삭제, 수정 기능을 메인으로하는 app들을 생성
-> 한 문장으로 app을 표현할 수 있는 정도. (and 들어가면 별개의 app으로 빼는게 좋다.)