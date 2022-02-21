var lastmousex=-1;
var lastmousey=-1;
var mousetravel = 0;
var cursorSpeed = 0;
var cursorSpeed2 = 0;
var can_be_bot_without_mouse = true;
var exactly_bot = false;
var mass=[];

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

var WindowOutHeight = window.outerHeight;
var WindowOutWidth = window.outerWidth;

/*lastmousex = screenX; != defaultcan_be_bot_without_mouse
document.getElementById("screenX_mon").innerHTML = lastmousex;*/
/*
let screenLog = document.querySelector('#screen-log');
document.addEventListener('mousemove', mousemoving_ex);

function mousemoving_ex(e) {
  screenLog.innerText = `
    Screen X/Y: ${e.screenX}, ${e.screenY}`;
}
*/
document.addEventListener('mousemove', mousemoving);

function mousemoving(e) {
    var mousex = e.screenX;
    var mousey = e.screenY;
    if (lastmousex > -1){
        mousetravel = Math.round(Math.sqrt(Math.pow((mousex-lastmousex),2)+ Math.pow((mousey-lastmousey),2)));}
    else {mousetravel=0;}
    setInterval(()=>mass.push(mousetravel),100);
    lastmousex = mousex;
    lastmousey = mousey;
}

setInterval(CursorSpeed,500);
function CursorSpeed(){ //average speed of cursor
 var sum_mousetravel=0;
 for (let a of mass){
   sum_mousetravel+=a;
 }
 mass=[];
 cursorSpeed = Math.round(sum_mousetravel/5);
  if(Math.abs(cursorSpeed2-cursorSpeed)>70){cursorSpeed2=cursorSpeed;} else {cursorSpeed=0;}
 document.getElementById("target").innerHTML=cursorSpeed;
 } ;
///////////////////////////////////////////////////////////////////////////////////////////////
var myLinks = document.getElementsByTagName("a"); //trigger for myLinks
for (let a of myLinks){
     a.addEventListener("click",check_trigger);
}
///////////////////////////////////////////////////////////////////////////////////////////////
 function check_trigger(){
   if(can_be_bot_without_mouse==true || exactly_bot==true){
     alert('bot!');
   }
 }
///////////////////////////////////////////////////////////////////////////////////////////////
 function alarm(){ //actions when bot was detected
   alert("Mouse actions weren't detected!");
   can_be_bot_without_mouse=true;
   clearTimeout(MouseAlert);  }
///////////////////////////////////////////////////////////////////////////////////////////////
 var MouseAlert=setTimeout(alarm,7000);

 addEventListener("mousedown", function () {
     //can_be_bot_without_mouse=false;
     //clearTimeout(MouseAlert);
 });

 addEventListener("mousemove", function () {
     can_be_bot_without_mouse=false;
     clearTimeout(MouseAlert);
 });
///////////////////////////////////////////////////////////////////////////////////////////////
var HidenLink = document.getElementById("HidenLink"); //HidenLink
//HidenLink.onload = alert("Bot Loading hiden link");
HidenLink.onload = function(){
  exactly_bot = true;
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