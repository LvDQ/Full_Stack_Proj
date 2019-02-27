var express = require('express');
var router = express.Router();

var passwordHash = require('password-hash');
var session = require('client-sessions');

var User = require('../my_models/user_class');// user defined class type

Title = "Ky's Estate personal project"



//http://javascript.ruanyifeng.com/nodejs/express.html


/*get方法则是只有GET动词的HTTP请求通过该中间件，它的第一个参数是请求的路径。when get方法的回调函数keyi没有调用next方法，所以只要有一个中间件被调用了，后面的中间件就不会再被调用了。

除了get方法以外，Express还提供post、put、delete方法，即HTTP动词都是Express的方法

router.get('/',function(req,res){
	next()
})

is the same as 

router.get('/',function(req,res,next){
	
})


req reference: https://expressjs.com/zh-cn/4x/api.html#req

*/

/* GET home page. */
router.get('/', function(req, res, next) {
    var user = checkLoggedIn(req, res); // defined at the end of this file
    res.render('index', { title: Title , logged_in_user: user });
});

/* GET Login page*/

router. get('/login',function(req,res, next){
	res.render('login',{ title: Title });
});


/* Login submit */
router.post('/login', function(req, res, next) {
  var email = req.body.email;			//from login.jade .form : name: email
  var password = req.body.password;

  User.find({ email : email }, function(err, users) {	//this function is from mongoose lib which is written by model.js
    console.log(users);
    if (err) throw err;
    // User not found.
    if (users.length == 0) {
      res.render('login', {
        title : TITLE,
        message : "User not found. Or <a href='/register'>rigester</a>"
      });
    } else {
      // User found.
      var user = users[0];
      if (passwordHash.verify(password, user.password)) {
        req.session.user = user.email;
        res.redirect('/');
      } else {
        res.render('login', {
          title : TITLE,
          message : "Password incorrect. Or <a href='/register'>rigester</a>"
        });
      }
    }
  });
});


/* Register page */
router.get('/register', function(req, res, next) {
  res.render('register', { title: TITLE });
});

/* Register submit */
router.post('/register', function(req, res, next) {
  // Get form values.
  var email = req.body.email;
  var password = req.body.password;
  var hashedPassword = passwordHash.generate(password);

  // Check if the email is already used.
  User.find({ email : email }, function(err, users) {
    if (err) throw err;
    if (users.length > 0) {
      console.log("User found for: " + email);
      res.render('register', {
        title: TITLE,
        message: 'Email is already used. Please pick a new one. Or <a href="/login">Login</a>'
      });
    } else {
        var newUser = User({
          email : email,
          password : hashedPassword,
        });
        // Save the user.
        newUser.save(function(err) {
          if (err) throw err;
          console.log('User created!');
          req.session.user = email;
          res.redirect('/');
        });
    }
  });
});





/* Search */

router.get('/search', function (req,res,next){
  var query = req.bod
})









/* Logout */
router.get('/logout', function(req, res) {
  req.session.reset();
  res.redirect('/');
});







function checkLoggedIn(req, res) {
  // Check if session exist
  if (req.session && req.session.user) { 
    return req.session.user;
  }
  return null;
}



module.exports = router;

