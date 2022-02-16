  var isAutomated = navigator.webdriver;
  var appName = navigator.appName;
  var appVersion = navigator.appVersion;
  var cookieEnabled = navigator.cookieEnabled;
  var geolocation = navigator.geolocation;
  var platform = navigator.platform;
  var userAgent = navigator.userAgent;
  var javaEnabled = navigator.javaEnabled();
  var WindowHeight = window.innerHeight;
  var WindowWidth = window.innerWidth;
  var WindowOutHeight = window.outerHeight;
  var WindowOutWidth = window.outerWidth;
  var Opener = window.opener;
  var evalBrowser = eval.toString().length;
/*
  document.getElementById("WindowHeight").innerHTML = WindowHeight;
  document.getElementById("WindowWidth").innerHTML = WindowWidth;
  document.getElementById("WindowOutHeight").innerHTML = WindowOutHeight;
  document.getElementById("WindowOutWidth").innerHTML = WindowOutWidth;
  document.getElementById("Opener").innerHTML = Opener;
  document.getElementById("javaEnabled").innerHTML = javaEnabled;
  switch(evalBrowser){
    case 37:
      document.getElementById("eval").innerHTML = "Firefox/Safari";
      break;
    case 33:
      document.getElementById("eval").innerHTML = "Chrome";
      break;
    case 39:
      document.getElementById("eval").innerHTML = "Explorer";
      break;
    default:
      document.getElementById("eval").innerHTML = evalBrowser;
  */
/*
  navigator.permissions.query({name:'notifications'}).then(function(permissionStatus) {
    if(Notification.permission === 'denied' && permissionStatus.state === 'prompt') {
        document.getElementById("APIPerm").innerHTML = "Headless Chrome";
    } else {
        document.getElementById("APIPerm").innerHTML = "Not Headless Chrome";
    }
    //document.getElementById("APIPerm").innerHTML = Notification.permission+permissionStatus.state;
  });

  if(isAutomated){
    document.getElementById("IsAutomated").innerHTML = "automated";
  }
  else{
    document.getElementById("IsAutomated").innerHTML = "not automated";
  }
  document.getElementById("appName").innerHTML = appName;
  document.getElementById("appVersion").innerHTML = appVersion;
  document.getElementById("cookieEnabled").innerHTML = cookieEnabled;
  document.getElementById("geolocation").innerHTML = geolocation;
  document.getElementById("platform").innerHTML = platform;
  document.getElementById("userAgent").innerHTML = userAgent;
}*/
//-----------------------------------------------------------------------------------------------------------
/*
function SendJSON(){
let xhr = new XMLHttpRequest();
let url = "client_data.php"; //creating xhr object
xhr.open("POST", url, true); //opening connection
xhr.setRequestHeader("Content-Type", "application/json"); // Set the request header i.e. which type of content you are sending
// Create a state change callback
xhr.onreadystatechange = function () {
  if (xhr.readyState === 4 && xhr.status === 200) {
    // Print received data from server
  result.innerHTML = this.responseText;
   }
};
var data = JSON.stringify({ "isAutomated": isAutomated.value});
xhr.send(data);
}
*/
window.onload = function() {
var server_data = [
  {"Automated": isAutomated},
  {"Height": WindowOutHeight},
  {"Width": WindowOutWidth},
  {"Eval": evalBrowser},
  {"Useragent": userAgent}
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
