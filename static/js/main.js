$(document).ready(function() {
    $('.hamburger').click(function(){
        $(this).toggleClass("is-active");
        $(".mobile-nav").toggleClass("mobile-nav-active");
    });
});

$(document).ready(function(){
    $(".property-search-filter").click(function(){
      $(".search-filters").toggleClass("search-filter-open-js");
      $(".property-search-filter").toggleClass("property-search-filter-open-js").toggleClass("property-search-container-active-color-toogle");
    });
});