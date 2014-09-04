// Defered event trigger by using '.on()' because the form is not loaded at
// page load but at opening of the Bootstrap modal window. 
$('body').on('submit', 'form.modal-form', function (event) {
    console.log(event);
    var form_id_name = $(this).attr('id').replace('_form', '');
    $.ajax({
        type: $(this).attr('method'),
        url: this.action,
        data: $(this).serialize(),
        context: this,
        success: function(data, status) {
            // Close the modal window
            //$('.modal-content').html(null);
            $('#closeMyModal').click();
            //$('#myModal').modal('hide')
            // Add message to original form to tell user create was successful
            $('#' + form_id_name + '-wrapper').before(data.django_messages);
            // Add new item to hidden select and deck
            add_new_element_to_deck(form_id_name, data.pk, data.name);
        }
    }).done(function( msg ) {
    });
    return false;
});

//$('.modal').on('hidden', function() {
//    $(this).data('modal', null);
//});

function add_new_element_to_deck(form_id_name, newId, newRepr){
    // Add option to hidden select and deck
    var elem = document.getElementById(form_id_name);
    if (elem) {
        if ($(elem).is('select')) {
            var o = new Option(newRepr, newId);
            elem.options[elem.options.length] = o;
            o.selected = true;
        }
    }
};
