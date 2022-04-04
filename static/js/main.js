$(document).ready(function() {
    $('.hamburger').click(function(){
        $(this).toggleClass("is-active");
        $(".mobile-nav").toggleClass("mobile-nav-active");
    });
});