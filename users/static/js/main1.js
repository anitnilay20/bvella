// JavaScript Document
var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  if (n > x.length) {slideIndex = 1;}
  if (n < 1) {slideIndex = x.length;}
  for (i = 0; i < x.length; i++) {
     x[i].style.display = "none";
  }
  x[slideIndex-1].style.display = "block";
  $("#ranmain").val(0);
}

function start(){
	myvar = setInterval(function(){plusDivs(1);},4000);
	myvarr = setInterval(function(){x=$("#ranmain").val();x++;$("#ranmain").val(x);},40);
}