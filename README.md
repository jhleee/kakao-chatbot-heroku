# kakao-chatbot-heroku
Simple kakaotalk chatbot with heroku.

## 1. Heroku 가입하기
https://dashboard.heroku.com

## 2. App 만들기
대쉬보드 우측상단에 `New > Create New App`을 클릭하여 새로운 App을 만든다.

## 3. Heroku CLI
https://devcenter.heroku.com/articles/heroku-command-line를 참고하여 HerokuCLI를 설치한다.

<pre><code>$ heroku login
$ heroku git:remote -a <APP_NAME>
$ git add .
$ git commit -am "message."
$ git push heroku master
</code></pre>
