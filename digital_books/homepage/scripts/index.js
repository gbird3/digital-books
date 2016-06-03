$(function() {

  if ($.fn.reflect) {
    $('.photos .cover').reflect();
  }

  $('.photos').coverflow({
    easing:			'easeOutElastic',
    duration:		'slow',
    index:			3,
    width:			320,
    height:			240,
    visible:		'density',
    selectedCss:	{	opacity: 1	},
    outerCss:		{	opacity: .1	},

    confirm:		function() {
      console.log('Confirm');
    },

    change:			function(event, cover) {
      var img = $(cover).children().andSelf().filter('img').last();
      $('#photos-name').text(img.data('name') || 'unknown');
    }

  });

  $('#leakdetect').click(function() {
    $('#leakbucket').empty();
    for (var i = 0; i < 100; ++i) {
      $('<div><div>test</div></div>').appendTo('#leakbucket').coverflow();
    }
  });
});
