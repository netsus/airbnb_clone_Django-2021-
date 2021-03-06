Cloning Airbnb using Python, Django, Tailwind CSS and more... in WSL2

#2.5 Django Applications

장고 프로젝트는 application의 집합. application은 function의 집합.
project 계획 방법.
airbnb 숙소(rooms)보기 -> room 폴더에 넣을 function 계획
rooms app: 숙소 생성, 검색, 삭제, 수정, 디테일페이지 보여주기, 모든 room 보여주기
app 폴더를 크게만들면 안된다. -> 주로 생성, 검색, 삭제, 수정 기능을 메인으로하는 app들을 생성
-> 한 문장으로 app을 표현할 수 있는 정도. (주요 기능 정의에 있어서 and 들어가면 별개의 app으로 빼는게 좋다.)
#2.7 Explaining the Apps

Django는 Framework이기 때문에 폴더이름과 코드의 이름을 바꾸면안된다.
apps.py는 configuration 파일
models.py는 Database가 어떻게 생겼는지 설명하는 곳
views.py가 사용자들이 보게될 기능 만드는 곳.

#11.0 HomeView
view를 만드는 3가지 방법
1) python only
2) python + django
3) django magic (almost no coding)
3가지를 하는 이유 django가 백그라운드에서 어떻게 돌아가는지 이해하기 위해서


#19.0 Intro to TailwindCSS
https://tailwindcss.com/
Tailwindcss : class 이름으로써 css를 쉽게 적용할 수 있게해주는 Framework
코드의 재사용은 @apply를 이용해서 원하는 클래스에 모두 적용되도록 할 수 있다.
장점
1. 이미 완성된 style 제공
2. Tailwind color palette 제공
3. Tailwind는 내가 모두 디자인할 수 있기 때문에 Tailwind로 제작된 웹사이트들은 천차만별. bootstrap이나 foundation은 어느정도 사이트들이 비슷해보인다는 한계가 존재.

#19.1 Setting Up TailwindCSS with Gulp
1. npm 업데이트
sudo npm install -g npm
2. gulp, sass 개발자 모드(-D) 설치
npm i gulp gulp-postcss gulp-sass gulp-csso node-sass -D 
3. tailwindcss 개발자 모드(-D) 설치
npm install tailwindcss -D   
4. tailwind init
npx tailwind init  
5. gulpfile.js 작성
6. autoprefixer 설치
npm i autoprefixer  
7. scss파일을 css파일로 변환(위치는 static/css 폴더) 
npm i 
npm run css  