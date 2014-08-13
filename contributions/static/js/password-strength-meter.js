$(document).ready(function() {
    $('input[id*="password1"]').keyup(function() {
        var meter_text_options = ["Very weak", "Weak", "Average", "Strong", "Very strong!"];
        var textValue = $(this).val();
        var result = zxcvbn(textValue);
        var meter_text = meter_text_options[result.score];
        $('td.password_strength_meter .text').html(meter_text);
        $('td.password_strength_meter .bar span').removeClass('bar0 bar1 bar2 bar3 bar4').addClass('bar'+result.score);
    });
});
