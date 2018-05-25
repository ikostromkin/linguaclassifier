import './main.scss';
import 'bootstrap';
import autosize from 'autosize';
import $ from 'jquery';

autosize(document.querySelectorAll('textarea'));

window.jQuery = $;
window.$ = $;

$(function () {
    $('#add_group_form').submit(function (e) {
        var $form = $(this);

        $.ajax({
            type: $form.attr('method'),
            url: $form.attr('action'),
            data: $form.serialize()
        }).done(function () {
            console.log('success');
            $(".form-check-input:checked").parent().parent().detach();
            $(".form-control").val('');

            var count = $(".form-check-input").length;

            if (count === 0) {
                location.href = 'http://127.0.0.1:5000/respondent/end/' + /[^/]*$/.exec(location.pathname)[0];
            }
        }).fail(function () {
            console.log('fail');
        });

        e.preventDefault();
    });
});