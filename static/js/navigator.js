  var newURL = window.location.protocol + "//" + window.location.host + "/" + window.location.pathname + window.location.search;
  var isAutomated = navigator.webdriver;
  var appName = navigator.appName;
  var appVersion = navigator.appVersion;
  var cookieEnabled = navigator.cookieEnabled;
  var geolocation = navigator.geolocation;
  var platform = navigator.platform;
  var userAgent = navigator.userAgent;
  var javaEnabled = navigator.javaEnabled();
  var windowHeight = window.innerHeight;
  var windowWidth = window.innerWidth;
  var windowOutHeight = window.outerHeight;
  var windowOutWidth = window.outerWidth;
  var opener = window.opener;
  var evalBrowser = eval.toString().length;
  var result = "undefined";
//-----------------------------------------------------------------------------------------------------------
  if (isAutomated || windowOutHeight==984 && windowOutWidth==1296){
    result = 'exactly_bot';
  }
//-----------------------------------------------------------------------------------------------------------
window.onload = function() {
var server_data = [
  {"URL": newURL},
  {"Automated": isAutomated},
  {"AppName": appName},
  {"AppVersion": appVersion},
  {"CookieEnabled": cookieEnabled},
  {"GeoLocation": geolocation},
  {"Platform": platform},
  {"Useragent": userAgent},
  {"JavaEnabled": javaEnabled},
  {"WindowHeight": windowHeight},
  {"WindowWidth": windowWidth},
  {"WindowOutHeight": windowOutHeight},
  {"WindowOutWidth": windowOutWidth},
  {"Opener": opener},
  {"Eval": evalBrowser},
  {"Result": result}
 ];
 $.ajax({
    type: "POST",
    url: "/",
    data: JSON.stringify(server_data),
    contentType: "application/json",
    dataType: 'json'
  }).done(function (data) {
    if (data['result'] == 'ok')
      console.log('ok')
    else {
      console.log('err')
    }
  });
}
