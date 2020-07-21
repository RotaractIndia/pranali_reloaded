/*
Just for Fun <3 for Tria Kila Kodika and friends
Forked from another Pen :)
Merry Christmas!
Dimitris
*/

 
 
buzz.defaults.formats = [ 'mp3' ];
buzz.defaults.preload = 'metadata';


var SleighRide = new buzz.sound("https://s3-us-west-2.amazonaws.com/s.cdpn.io/191814/9562523_silvanmusic_christmas-time", {
    formats: [ "mp3" ],
    preload: true,
    autoplay: false,
	volume: 100,
    loop: true
});
var hohoho = new buzz.sound("https://s3-us-west-2.amazonaws.com/s.cdpn.io/191814/hohoho", {
    formats: [ "mp3" ],
    preload: true,
    autoplay: false,
	volume: 100,
    loop: false
});

var SantaLaughing = new buzz.sound("https://s3-us-west-2.amazonaws.com/s.cdpn.io/191814/SantaLaughing", {
    formats: [ "mp3" ],
    preload: true,
    autoplay: false,
	volume: 100,
    loop: false
});



var MerryChristmas = new buzz.sound("https://s3-us-west-2.amazonaws.com/s.cdpn.io/191814/SantaMerryChristmas", {
    formats: [ "mp3" ],
    preload: true,
    autoplay: false,
	volume: 100,
    loop: false
});
var Jingle2 = new buzz.sound("https://s3-us-west-2.amazonaws.com/s.cdpn.io/191814/Jinglebells2", {
    formats: [ "mp3" ],
    preload: true,
    autoplay: false,
	volume: 100,
    loop: false
});


			
		
/***************************
Santa Magic Sound Effects
****************************/		

	
	SleighRide.play();Jingle2.play();hohoho.play();		
	setTimeout(function () {
    Jingle2.play();MerryChristmas.play();}, 8000
);
setTimeout(function () {
    SantaLaughing.play();}, 20000
);
setTimeout(function () {
    Jingle2.play();SantaLaughing.play();}, 35000
);
setTimeout(function () {
    hohoho.play();}, 50000
);
setTimeout(function () {
    Jingle2.play();MerryChristmas.play();}, 80000
);

setTimeout(function () {
    SantaLaughing.play();}, 100000
);
	
$('.santa').hover(function() {
				hohoho.play();Jingle2.play();
 
			}, function() {
				hohoho.stop();Jingle2.stop();
			});	
$('.santa').click(function() {
     MerryChristmas.play();
     hohoho.stop();Jingle2.stop();
			});		
			

/***************************
Grouping the sounds so I can toggle them off and on all at once 
****************************/		


var soundEffects = new buzz.group([ 
    hohoho, 
	SleighRide,
	Jingle2,
    MerryChristmas, 
	SantaLaughing

]);		
			
	
/***************************
Toggle Mute for all sounds using the sounds grouped.
****************************/

$('.toggle-sound').click(function() {
soundEffects.toggleMute();
$('h2').toggleText("♫ ON", "♫ OFF");
 });			
	
/***************************
A simple jQuery way to swap out text.  More elegant ways to achieve this. But this was expedient.
****************************/			
	
	
jQuery.fn.extend({
    toggleText: function (a, b){
        var that = this;
            if (that.text() != a && that.text() != b){
                that.text(a);
            }
            else
            if (that.text() == a){
                that.text(b);
            }
            else
            if (that.text() == b){
                that.text(a);
            }
        return this;
    }
});


/***************************
****************************
Forked from FindOff
http://codepen.io/findoff/pen/XJXNaa

Look closely.  It's a little phallic.  kinda why I chose dis.  :)

Simply added some CSS so the canvas was more responsive
and added an ID useful for stuff. Through in a jQuery Toggle example too.


****************************
***************************/



var canvas, ctx, w, h;
document.body.appendChild( canvas = document.createElement('canvas') );

/***************************
****************************
Simply Added an ID for the dynamically created Canvas -- Useful for Formatting
****************************
***************************/

canvas.id = 'Meteors';


ctx = canvas.getContext('2d');
canvas.style.border = '0px solid #000';
w = canvas.width = window.innerWidth - 30;
h = canvas.height = window.innerHeight - 30;
var wh = w/2;
var hh = h/2;
var meteors = [], nMeteors = 100;
var img = (function(){
  var canvas = document.createElement('canvas');
  var ctx = canvas.getContext('2d');
  canvas.width = canvas.height = 100;
  ctx.beginPath();
  ctx.fillStyle = '#25C7EE';
  //ctx.arc(50,50, 50, 0,Math.PI*2, 0);
  ctx.moveTo(40,100);
  ctx.quadraticCurveTo(50,0, 60,100);
  ctx.closePath();
  ctx.fill();
  ctx.beginPath();
  ctx.arc(30,90, 10, 0,Math.PI*2, 0);
  ctx.arc(70,90, 10, 0,Math.PI*2, 0);
  ctx.fill();
  return canvas;
})();
setInterval(function(){
  //ctx.clearRect(0,0, w, h);
  ctx.fillStyle = 'rgba(0,0,0, 0.1)';
  ctx.fillRect(0,0, w,h);
  gen();
  ctx.fillStyle = '#fff';
  ctx.save();
  ctx.translate(wh,hh);
  for(var i=0; i<meteors.length; ++i) {
    var t = meteors[i];
    var x = t.pos[0]/t.pos[2];
    var y = t.pos[1]/t.pos[2];
    if( x<-wh || x>wh || y<-hh || y>hh || t.pos[2]<0 ) {
      meteors.splice(i,1);
      --i;
      continue;
    }
    ctx.beginPath();
    //ctx.arc(x, y, t.r/t.pos[2], 0,Math.PI*2, 0);
    //ctx.drawImage(img, x,y, t.r/t.pos[2],t.r/t.pos[2]);
    ctx.save();
    ctx.translate(x,y);
    ctx.rotate(t.a);
    t.a += t.avel;
    ctx.drawImage(img, 0,0, t.r/t.pos[2],t.r/t.pos[2]);
    ctx.restore();
    t.pos[0] += t.vel[0];
    t.pos[1] += t.vel[1];
    t.pos[2] += t.vel[2];
    ctx.fill();
  }
  ctx.restore();
}, 16);
function gen() {
  while(meteors.length < nMeteors) {
    var z = 300;
    var xw = w*z;
    var xh = h*z;
    var rf = Math.PI/8;
    meteors.push({
      pos: [xw*Math.random()-wh*z, xh*Math.random()-hh*z, z],
      vel: [0,0,-2],
      a: 0,
      avel: rf*Math.random()-rf/2,
      r: 1550
    });
  }
};