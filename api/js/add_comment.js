function toggleCommentForm() {
    const btn = $(this);
    const target = btn.data('target');
    const form = $(target);
    const post_id = btn.data('post-id');

    $('#post-' + post_id).find('.comment-form').not(form).addClass('d-none');
    form.toggleClass('d-none');
    if (!form.hasClass('d-none')) {
        form.find('textarea').focus();
    }
}

function submitComment(event) {
    event.preventDefault();
    const form = $(this);
    const post_id = form.data('post-id');

    $.ajax({
        url: '/posts/' + post_id + '/comments/add/',
        method: 'POST',
        data: form.serialize(),
        success: function (data) {
            form.find('textarea').val('');
            form.addClass('d-none');
            $('#comments-' + post_id).html(data.html);
            $('#post-' + post_id).find('.comment_count_post').text(data.comments_count);
        }
    });
}


$(document).ready(function () {
    $(document).on('click', '.comments-write-btn', toggleCommentForm);
    $(document).on('submit', '.comment-form', submitComment);
});