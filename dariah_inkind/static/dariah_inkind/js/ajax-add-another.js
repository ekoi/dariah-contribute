/*
 * DARIAH Contribute - DARIAH-EU Contribute: edit your DARIAH contributions.
 *
 * Copyright 2014 Data Archiving and Networked Services
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

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
            // Empty the form for next input.
            $(this).find('.resetModal').click();      // Fake a reset button click to reset the form.
            // Close the modal window
            $(this).closest('.modal').modal('hide');
            //$(this).filter('.closeModal').click();    // Alternative way to close the modal window.

            // Add message to original form to tell user create was successful
            $('label[for=' + form_id_name + ']').after(data.django_messages);
            // Add new item to hidden select and deck
            add_new_element_to_deck(form_id_name, data.pk, data.name, data.obj_class_name);
        }
    }).done(function( msg ) {
    });
    return false;
});

function add_new_element_to_deck(form_id_name, newId, newRepr, obj_class_name){
//	if (obj_class_name=='DcContributor')
//    	newChoiceTxt= '<a data-toggle="modal" data-target="#dc_contributor_detail_modal" href="/inkind/dc_contributor/' 
//			+ newId + '">' + newRepr + '</a>';
//    else
//    	newChoiceTxt= '<a data-toggle="modal" data-target="#dc_creatorr_detail_modal" href="/inkinddc_creator/' 
//			+ newId + '">' + newRepr + '</a>';
	var newChoiceTxt = '';
    if (obj_class_name=='DcContributor')
    	newChoiceTxt='<a href="/inkind/dc_contributor/' + newId + '" target="_blank">' + newRepr + '</a>';
    else
    	newChoiceTxt='<a href="/inkind/dc_creator/' + newId + '" target="_blank">' + newRepr + '</a>';
    
    // Add option to hidden select and deck
    // This code was taken and slightly adapted from the original
    // `autocomplete_light code <https://github.com/yourlabs/django-autocomplete-light/blob/80b1d689f482c85764909d2908f3bcb0bbc32237/autocomplete_light/static/autocomplete_light/addanother.js>`_
    // function ``dismissAddAnotherPopup``.
    var elem = document.getElementById(form_id_name);
    if (elem) {
        if ($(elem).is('select')) {
            var o = new Option(newChoiceTxt, newId);
            elem.options[elem.options.length] = o;
            o.selected = true;
        }
    }
};
