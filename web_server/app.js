
/* dependencies(manually installed): node.js,mongodb, mongoose, client- sessions, password-hash

*/
var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

//mongoose is used to link mongodb, session as the word meaning by using cookie
var mongoose = require('mongoose');
var session = require('client-sessions');


var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();


// Connect to database.
mongoose.connect('mongodb://localhost:27017/estate_db');

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');


// Register session Midleware.
app.use(session({
  cookieName: 'session',
  secret: 'random_string',
  duration: 30 * 60 * 1000,
  activeDuration: 5 * 60 * 1000
}));


//app.use is to REGISTER middle middleware !!!!!!!!!!!!!!!!!!!! Initial order Affects!!!!!!
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/users', usersRouter);



// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;


