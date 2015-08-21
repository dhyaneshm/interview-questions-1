
var errors = [];
var displayErrors = function() {
  if (errors.length == 0){
    $(".errors").hide();
    $(".errors").html("");
  }
  if (errors.length > 0){
    $(".errors").show();
    $(".errors").html("");
  }
  $.each(errors, function(index, error) {
    var html = "<div class='error'>"+error+"</div>";
    $(".errors").append(html);
  });
  
}

$("input[name=username]").blur(function() {
  var username = $(this).val();
  
  var errIndex = errors.indexOf("Your username must be at least 2 characters.");
  var err2Index = errors.indexOf("Your username must be at most 20 characters");

  if (username.length < 2 && errors.indexOf("Your username must be at least 2 characters.") < 0) {
    if (errIndex < 0) {
      errors.push("Your username must be at least 2 characters.");
    }
  } else {
    if (errIndex >=0) {
      errors.splice(errIndex, 1);
    }
  }

  if (username.length > 20 && errors.indexOf("Your username must be at most 20 characters") < 0) {
    if (err2Index < 0) {
      errors.push("Your username must be at most 20 characters");
    }
  } else {
    if (err2Index >=0) {
      errors.splice(err2Index, 1);
    }
  }
  displayErrors(errors);
});



$("input[name=email]").blur(function() {
  var emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/
  var email = $(this).val();
  
  var errIndex = errors.indexOf("You must enter an email");
  if (email.length == 0) {
    if (errIndex < 0) {
      errors.push("You must enter an email");
    }
  } else {
    if (errIndex >= 0) {
      errors.splice(errIndex, 1);
    }
  }
  
  var err2Index = errors.indexOf("Invalid email") 
  if (email.length > 0 && !emailRegex.test(email)) {
    if (err2Index < 0){
      errors.push("Invalid email");
    }
  } else {
    if (err2Index >= 0) {
      errors.splice(err2Index, 1)
    }
  }
  displayErrors(errors);
});

$("input[name=password]").blur(function() {
  

  var password = $(this).val();
  
  var errIndex = errors.indexOf("You must enter an password");
  var err2Index = errors.indexOf("Your password must be at least 6 characters long");
  if (password.length == 0) {
    if (errIndex < 0) {
      errors.push("You must enter an password");
    }
  } else {
    if (errIndex >= 0) {
      errors.splice(errIndex, 1);
    }
  }

  if (password.length < 6) {
    if (err2Index < 0) {
      errors.push("Your password must be at least 6 characters long");
    }
  } else {
    if (err2Index >= 0) {
      errors.splice(err2Index, 1);
    }
  }
  displayErrors(errors);
});

$("input[name=password_repeat]").blur(function() {
  var password_repeat = $(this).val();
  var password = $("input[name=password]").val()

  var errIndex = errors.indexOf("Your passwords must match");
  if (password !== password_repeat) {
    if (errIndex < 0) {  
      errors.push("Your passwords must match");
    }
  } else {
    if (errIndex >= 0) {
      errors.splice(errIndex, 1);
    }
  }
  displayErrors(errors);
});

$("input[name=tos]").change(function() {
  var tos = $(this);

  var errIndex = errors.indexOf("You must accept the terms of service");
  if (!tos.is(":checked")) {
    if (errIndex < 0) {  
      errors.push("You must accept the terms of service");
    }
  } else {
    if (errIndex >= 0) {
      errors.splice(errIndex, 1);
    }
  }
  displayErrors(errors);
});

