(function($){
  $(function(){

    $('.button-collapse').sideNav();

    $('.chips-initial').material_chip({
        data: [{
          tag: 'Apple',
        }, {
          tag: 'Microsoft',
        }, {
          tag: 'Google',
        }],
      });
    
  }); // end of document ready
})(jQuery); // end of jQuery name space