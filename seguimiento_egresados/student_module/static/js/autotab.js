$(function() {
    $('input.autotab').autotab({ format: 'custom', pattern: 's9', maxlength: 9 });
});

$(document).ready(function() {
    $("#id_username_0, #id_username_1, #id_username_2, #id_username_3, #id_username_4, #id_username_5, #id_username_6, #id_username_7, #id_username_8").keyup(function() {
        var index = $(this).attr('maxlength');
        if (this.value.length === this.maxLength) {
            $(this).next(":input").focus();
        }
    });
});