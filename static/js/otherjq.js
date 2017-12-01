// JavaScript Document
$(window).scroll(function() {    
    var scroll = $(window).scrollTop();

    if (scroll >= 50) {
        $("#h_two").addClass("header");
    } else {
        $("#h_two").removeClass("header");
    }
});

if (window.addEventListener) window.addEventListener('DOMMouseScroll', wheel, false);
window.onmousewheel = document.onmousewheel = wheel;

function wheel(event) {
    var delta = 0;
    if (event.wheelDelta) delta = event.wheelDelta / 120;
    else if (event.detail) delta = -event.detail / 3;

    handle(delta);
    if (event.preventDefault) event.preventDefault();
    event.returnValue = false;
}

function handle(delta) {
    var time = 2000;
	var distance = 600;
    
    $('html, body').stop().animate({
        scrollTop: $(window).scrollTop() - (distance * delta)
    }, time, "easeOutBack");
}





$(document).ready(function () {
    $("#sign-in").click(function () {
        $(".sign-in-container").stop().slideDown();
    });

    $("#sign-in1").click(function () {
        $(".sign-in-container").stop().slideDown();
    });

    $(":reset").click(function () {
        $(".sign-in-container").stop().slideUp();
    })

    $(document).ready(function() {
    $( '.dropdown' ).hover(
        function(){
            $(this).children('.sub-menu').slideDown(200,"easeOutBounce");
        },
        function(){
            $(this).children('.sub-menu').slideUp(200, "easeOutBack");
        }
    );
        $("#form-show").click(function () {
            $(".form.update").slideDown()

        })

        $("#form-hide").click(function () {
                $(".form.update").slideUp()

        })

        $("#right").click(function () {
            x=$(".scroll-main").scrollLeft();
            $(".scroll-main").stop().animate({
                scrollLeft:x+1000
            },{
                duration:2000,
                easing: "easeOutCubic"
            });
        })

        $("#left").click(function () {
            x=$(".scroll-main").scrollLeft();
            $(".scroll-main").stop().animate({
                scrollLeft:x-1000
            },{
                duration:2000,
                easing: "easeOutCubic"
            });
        })

        $("#gototop").click(function () {
            $('html, body').stop().animate({
        scrollTop: 0
    }, 2000, "easeOutBounce");
        });
        
});
});

function changeimg(x){
    $("#main-img").attr('src', x)
}
