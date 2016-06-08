$(function() {
  // Handler for .ready() called.
  $('#search').click(function(e){
    if(document.forms['search'].isearch.value === '')
    {
      e.preventDefault();
      $('#search-form').toggleClass("hidden");
    }
  })
});
