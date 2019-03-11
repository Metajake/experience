$(document).ready(function(){
  updateForm();
});

function updateForm(){
  formType = $('#add #type').val()
  switch(formType){
    case 'exp':
      updateFieldsets('#experience');
      break;
    case 'work':
      updateFieldsets('#work');
      break;
    case 'eat':
      updateFieldsets('#eat');
      break;
    case 'private':
      updateFieldsets('#private');
      break;
  }
}

function updateFieldsets(type){
  resetFieldsets()
  $(type).show();
  setDisabledFields()
}

function resetFieldsets(){
  $('fieldset.type').each(function(){
    $(this).hide()
  })
}

function setDisabledFields(){
  $('fieldset input, fieldset select').prop('disabled', false);
  $('fieldset[style*="display: none"] input, fieldset[style*="display: none"] select').prop('disabled', true);
}

$("#add #type").change(function(){
  updateForm()
})

$('#add').submit(function(e){
  e.preventDefault()

  $.ajax({
    url: "/ajaxAdd/",
    type: "POST",
    data: $('#add').serialize(),
    success: function(data){
      if(data == '15min'){
        $('#notification').html("Hasn't been 15 minutes yet")
      }else{
        window.location = "/";
      }
    },
    error: function(error){
      $('#add').hide()
      $('#notification').html("Weird Error")
      console.log("Error")
      console.log(error)
    }
  })

})
