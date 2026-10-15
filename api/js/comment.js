function loadComments() {
    const post_id = $(this).data('post-id');
    const box = $('#comments-' + post_id);

    $.ajax({
        url: '/posts/' + post_id + '/comments/',
        method: 'GET',
        success: function (html) {
            box.html(html);
            }
        });
}

$(document).ready(function (){
    $(".comments-btn").on("click", loadComments)
})

