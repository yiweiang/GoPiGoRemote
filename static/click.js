$(function() {
  $(".controlButton.up").click(function() {
    callURL("http://"+window.location.host+"/control/up");
  });


  $(".controlButton.down").click(function() {
    callURL("http://"+window.location.host+"/control/down");
  });

  $(".controlButton.left").click(function() {
    callURL("http://"+window.location.host+"/control/left");
  });

  $(".controlButton.right").click(function() {
    callURL("http://"+window.location.host+"/control/right");
  });

  $(".controlButton.stop").click(function() {
    callURL("http://"+window.location.host+"/control/stop");
  });
  
  $(".controlButton.snap").click(function() {
    callURL("http://"+window.location.host+"/camera/snapshot");
  });

  $('body').on('keydown', function(e) {
    if (e.which == 37) {
      callURL("http://"+window.location.host+"/control/left")
      $(".controlButton.left").fadeOut(50)
      $(".controlButton.left").fadeIn(50)
    }
    if (e.which == 38) {
      callURL("http://"+window.location.host+"/control/up")
      $(".controlButton.up").fadeOut(50)
      $(".controlButton.up").fadeIn(50)
    }
    if (e.which == 39) {
      callURL("http://"+window.location.host+"/control/right")
      $(".controlButton.right").fadeOut(50)
      $(".controlButton.right").fadeIn(50)
    }
    if (e.which == 40) {
      callURL("http://"+window.location.host+"/control/down")
      $(".controlButton.down").fadeOut(50)
      $(".controlButton.down").fadeIn(50)
    }
    if (e.which == 32) {
      callURL("http://"+window.location.host+"/control/stop")
      $(".controlButton.snap").fadeOut(50)
      $(".controlButton.snap").fadeIn(50)
    }
  });

  function callURL(url) {
    jQuery.ajax({
      url: url,
      dataType: "html"
    }).done(function(responseText) {
      console.log(responseText)
    })
  }
});
