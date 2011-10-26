/***********************************************
* Deshabilita el click derecho del mouse 
* Fernando Zapata Miranda,Andy Villaverde Mancilla
* ONPE-LIMA-PERU
* IE 4+, NS4+
***********************************************//*
var isNS = (navigator.appName == "Netscape") ? 1 : 0;
var EnableRightClick = 0;
if(isNS) 
document.captureEvents(Event.MOUSEDOWN||Event.MOUSEUP);
function mischandler(){
  if(EnableRightClick==1){ return true; }
  else {return false; }
}
function mousehandler(e){
  if(EnableRightClick==1){ return true; }
  var myevent = (isNS) ? e : event;
  var eventbutton = (isNS) ? myevent.which : myevent.button;
  if((eventbutton==2)||(eventbutton==3)) return false;
}
function keyhandler(e) {
  var myevent = (isNS) ? e : window.event;
  if (myevent.keyCode==96)
    EnableRightClick = 1;
  return;
}
document.oncontextmenu = mischandler;
document.onkeypress = keyhandler;
document.onmousedown = mousehandler;
document.onmouseup = mousehandler;
/***********************************************
* Deshabilita las teclas Ctrl / Alt / Shift 
* Fernando Zapata Miranda,Andy Villaverde Mancilla
* ONPE-LIMA-PERU
* IE 4+, NS4+
***********************************************/
/*function mouseDown(e) {
 var ctrlPressed=0;
 var altPressed=0;
 var shiftPressed=0;
 if (parseInt(navigator.appVersion)>3) {
  if (navigator.appName=="Netscape") {
   var mString =(e.modifiers+32).toString(2).substring(3,6);
   shiftPressed=(mString.charAt(0)=="1");
   ctrlPressed =(mString.charAt(1)=="1");
   altPressed  =(mString.charAt(2)=="1");
  }else{
   shiftPressed=event.shiftKey;
   altPressed  =event.altKey;
   ctrlPressed =event.ctrlKey;
  }
  if (shiftPressed || altPressed || ctrlPressed) 
    alert("Copyright © ONPE. Derechos Reservados 2011");
 }
 return true;
}

if (parseInt(navigator.appVersion)>3) {
 document.onmousedown = mouseDown;
 if (navigator.appName=="Netscape") 
  document.captureEvents(Event.MOUSEDOWN);
}

function keyhandler2(e) {
  var myevent = (isNS) ? e : window.event;
  if(isNS){
	  if(myevent.keyCode==10 || myevent.keyCode==13){
	    alert("Copyright © ONPE. Derechos Reservados 2011");
	 	return false;
	  }
  }else{
	  if(event.shiftKey || event.altKey || event.ctrlKey){	
		alert("Copyright © ONPE. Derechos Reservados 2011");
		return false;
	  }
  }
}
document.onkeypress = keyhandler2;
document.onmouseup = keyhandler2;*/