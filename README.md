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

#19.3 Setup Explanation part Two
1. styles.scss - css 편집과 관련된 모든것은 scss로 진행
2. gulpfile.js
 --> gulp - scss를 css로 변환
1) postCSS 단계: @tailwind, @apply 등을 css로 변환,
2) 브라우저에 보내는 파일은 static/css/styles.css
 --> npm run css : scss에서 작성한 코드를 css로 바꿔주는 명령어

#20.0 Sizes in Tailwind
1. CSS 기초 유닛
em : 현재 태그에 적용되고 있는 font-size의 배수.
ex) 가장 가까운 부모의 font-size가 10px이고 em=1 이면, 10px  의미. em=2 이면, 20px의미.
rem : root에 적용되고 있는 font-size의 배수.
ex) html에 적용되는 font-size가 10px이고, em=3이면, 30px의미.


#21.11 Done with Users!
django authentication and user management system.
1. 장고는 강력한 권한 엔진을 가지고있다. -> 유저에게 권한 부여가능. 그룹 생성 후, 그룹 권한 부여 가능
2. urls.py에 accounts/ url을 urlpattenrs 변수에 추가하면, 장고에 구현되어 있는 로그인 과련 view 들을 사용할 수 있다.
아래 1) ~ 5)는 모두 accounts/ 뒤에 존재 ex) accounts/login
 1) login, logout
 2) password_change, password_change/done
 3) password_reset, password_reset/done
 4) reset/<uidb64>/<token>/ : password 리셋할 때, 장고는 토큰 2개 생성하여 리셋 허용해주는 링크를 메일로 보내준다. 메일에서 링크 클릭하면 
 5) reset/done 으로 이동

#24.8 Calendar and BookedDay Recap
BookedDay 클래스를 활용해 예약한 시간을 저장하고, 검토하여 예약 날짜 겹치지 않도록 조절.
__ : Foreign Key 사용하는 방법
ex) reservation_models.BookedDay.objects.get(day=date, reservation__room=room)
--> reservation 클래스에서 objects.get을 이용하여 room(FK)에 해당하는 예약을 가져오도록함