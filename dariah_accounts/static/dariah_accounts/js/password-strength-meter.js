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
