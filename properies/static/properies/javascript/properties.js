document.addEventListener( 'DOMContentLoaded', function() {
    var main = new Splide( '#main-slider', {
        type       : 'loop',
        heightRatio: 0.5,
        pagination : false,
        arrows     : true,
        cover      : true,
      } );
      
      var thumbnails = new Splide( '#thumbnail-slider', {
        rewind          : true,
        fixedWidth      : 104,
        fixedHeight     : 58,
        isNavigation    : true,
        gap             : 10,
        focus           : 'center',
        pagination      : false,
        cover           : true,
        arrows          : false,
        dragMinThreshold: {
          mouse: 4,
          touch: 10,
        },
        breakpoints : {
          640: {
            fixedWidth  : 66,
            fixedHeight : 38,
          },
        },
      } );
      
      main.sync( thumbnails );
      main.mount();
      thumbnails.mount();
  } );