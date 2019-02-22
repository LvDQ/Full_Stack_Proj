# Full_Stack_Proj
estate estimation




### Dependency between sources:

`./bin/www` is the entrance of web_server(creating) binding with localhost `port 3000`, this server require `app.js` to get into node logical level

and this file import express framework to create a http server which leads to the listened  `req` to app.js


`app.js` set how to create a http server by using `Express` framework and `register` all kinds of `Middleware`

app.js also sets `view engine` as `Jade`

`Jade` is express framework's default view engine.


`./routes/index.js` is main direction file. 

`GET method HTTP: `

-  If url matches '/', then check if has session and show the home page

-  If url mathes '/Login', go to login page, website page render with `login.jade`

-  If url mathes '/Register', go to Register page, website page render with `Register.jade`

`POST method HTTP:`

- matches '/login', we can get `req.body.email` & `req.body.password` , then query if the user exsits and check if the password is correct by using package `password-hash` to keep password. If correct, `req.session.user = user.email`, then redirect to '/', and now req.session.user is passed to home page.

- matches '/register', check if there's the same username, if good, then create and save to db. then do the login step.

- matches '/logout', `req.session.reset()`, then redirect to home page