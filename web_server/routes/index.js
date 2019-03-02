var express = require('express');
var router = express.Router();

var passwordHash = require('password-hash');
var session = require('client-sessions');

var User = require('../my_models/user_class');// user defined class type

var rpc_client = require('../rpc_client/rpc_client')

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
https://expressjs.com/en/api.html

*/

/* GET home page. */
router.get('/', function(req, res, next) {
    var user = checkLoggedIn(req, res); // defined at the end of this file
    res.render('index', { title: Title , logged_in_user: user });
});

/* GET Login page*/

router.get('/login',function(req,res, next){
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
        title : Title,
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
          title : Title,
          message : "Password incorrect. Or <a href='/register'>rigester</a>"
        });
      }
    }
  });
});


/* Register page */
router.get('/register', function(req, res, next) {
  res.render('register', { title: Title });
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
        title: Title,
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

/* Search page */
router.get('/search', function(req, res, next) {
  var query = req.query.search_text;
  console.log("search text: " + query)

  rpc_client.search_area(query, function(response) {
    results = [];
    if (response == undefined || response === null) {
      console.log("No results found");
    } else {
      results = response;
    }

    // Add thousands separators for numbers.
    addThousandSeparatorForSearchResult(results)

    res.render('search_result', {
      title: Title,
      query: query,
      results: results
    });

  });
});


/* Property detail page*/
router.get('/detail', function(req, res, next) {
  logged_in_user = checkLoggedIn(req, res)

  var id = req.query.id
  console.log("detail for id: " + id)

  rpc_client.getDetailsByZpid(id, function(response) {
    property = {}
    if (response === undefined || response === null) {
      console.log("No results found");
    } else {
      property = response;
    }

    // Add thousands separators for numbers.
    addThousandSeparator(property);

    // Split facts and additional facts
    splitFacts(property, 'facts');
    splitFacts(property, 'additional_facts');


    res.render('detail', 
      {
        title: 'ky_personal_Estate_Proj',
        query: '',
        logged_in_user: logged_in_user,
        property : property
      });
  });
});






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

function splitFacts(property, field_name) {
  facts_groups = []
  group_size = property[field_name].length / 3;
  facts_groups.push(property[field_name].slice(0, group_size))
  facts_groups.push(property[field_name].slice(group_size, group_size + group_size))
  facts_groups.push(property[field_name].slice(group_size + group_size))
  property[field_name] = facts_groups
}

function addThousandSeparatorForSearchResult(searchResult) {
  for (i = 0; i < searchResult.length; i++) {
    addThousandSeparator(searchResult[i])
  }
}

function addThousandSeparator(property) {
  property['list_price'] = numberWithCommas(property['list_price'])
  property['size'] = numberWithCommas(property['size'])
  property['predicted_value'] = numberWithCommas(property['predicted_value'])
}

function numberWithCommas(x) {
  if (x != null) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  }
}



module.exports = router;

