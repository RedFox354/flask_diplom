var lastmousex=-1;
var lastmousey=-1;
var mousetravel = 0;
var cursorSpeed = 0;
var cursorSpeed2 = 0;
var can_be_bot_without_mouse = true;
var exactly_bot = false;
var mass=[];

var isAutomated = navigator.webdriver;
var WindowOutHeight = window.outerHeight;
var WindowOutWidth = window.outerWidth;

if (isAutomated || WindowOutHeight==984 && WindowOutWidth==1296){
  exactly_bot = true;
  //alert("exactly bot!");
}
/*lastmousex = screenX; != defaultcan_be_bot_without_mouse
document.getElementById("screenX_mon").innerHTML = lastmousex;*/

let screenLog = document.querySelector('#screen-log');
document.addEventListener('mousemove', mousemoving_ex);

function mousemoving_ex(e) {
  screenLog.innerText = `
    Screen X/Y: ${e.screenX}, ${e.screenY}`;
}

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
}


//let timerId1 = setInterval(() => alert(lastmousex,lastmousey), 2000);
