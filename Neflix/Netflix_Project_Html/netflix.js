$(function() {

  // Change background
  var backgroundImage = 'images/netflix-background.jpg';

  setInterval(function() {

    if (backgroundImage == 'images/netflix-background.jpg') {
      backgroundImage = 'images/netflix-background-2.jpg';
    } else {
      backgroundImage = 'images/netflix-background.jpg';      
    }

    $('#background-image').css('background-image', 'url("' + backgroundImage  + '")');

  }, 3000);

  // Open & Close Menu
  $('.js-menu').click(function() {
	$('nav').toggleClass('open-menu');
  });

});