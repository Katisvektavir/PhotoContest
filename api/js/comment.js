function loadComments() {
    const post_id = $(this).data('post-id');
    const box = $('#comments-' + post_id);

    if (box.data('loaded')) {
        box.toggle();
        return;
    }

    $.ajax({
        url: '/posts/' + post_id + '/comments/',
        method: 'GET',
        success: function (html) {
            box.html(html);
            box.data('loaded', true);
            box.show();
            }
        });
}

$(document).ready(function (){
    $("#posts_container").on("click", ".comments-btn", loadComments);
})

