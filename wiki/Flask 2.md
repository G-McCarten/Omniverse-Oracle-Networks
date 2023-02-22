# Deploy to heroku

-  Signup for a free heroku account. https://signup.heroku.com/login

![image](https://user-images.githubusercontent.com/589439/166157575-9795d68d-de4a-48a1-8baa-de7ff05aeeb1.png)

-  Login to <a href="https://dashboard.heroku.com/apps">Heroku</a> and "create a new app."

![image](https://user-images.githubusercontent.com/589439/166157603-2fba5291-1a7b-4f64-83ef-f57877abc63c.png)

-  Name the app to whatever you please.

![image](https://user-images.githubusercontent.com/589439/166157679-42545a53-a70d-49c6-ba50-9d85d55a05a2.png)

-  Open the CLI and move to the root of this repo in VSCode.

![image](https://user-images.githubusercontent.com/589439/166157688-88483874-8cbc-44dd-bb28-4e5ed3786522.png)

-  Login to heroku via the CLI. (Proceed to browser by entering any key in the CLI.)

`$ heroku login`

![image](https://user-images.githubusercontent.com/589439/166157718-1215954b-b507-4eb4-b334-8b500cd0e64c.png)

-  Run the following commands.

`$ git init`

`$ git add .`

`$ git commit -am "Heroku"`

![image](https://user-images.githubusercontent.com/589439/166157765-6b4c8749-edd6-4821-83ee-6052a04231c7.png)

-  Git push to heroku to deploy the app.

`$ git subtree push --prefix flask_server/ heroku main`

![image](https://user-images.githubusercontent.com/589439/166157816-0861c7cc-793e-4cb7-8eb2-a08b7a6bf54e.png)

-  Go to your <a href="https://dashboard.heroku.com/apps"> Heroku Dashboard </a> and navigate to your application.

-  Click Open App to see if your API server is running.

![image](https://user-images.githubusercontent.com/589439/166157855-5afc420c-b8f3-40f3-a13d-1a3149e58118.png)

![image](https://user-images.githubusercontent.com/589439/166157894-2d8a2aed-053c-404c-a288-262121e47427.png)
