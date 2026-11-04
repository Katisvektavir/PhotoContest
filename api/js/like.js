function getCookie(name) {
    const match = document.cookie.match(new RegExp('(^|;\\s*)' + name + '=([^;]*)'));
    return match ? decodeURIComponent(match[2]) : null;
}

function togglePostLike() {
    const post_id = $(this).data('post-id');
    const post = $('#post-' + post_id);

    $.ajax({
        url: '/posts/' + post_id + '/like/',
        method: 'post',
        headers: { 'X-CSRFToken': getCookie('csrftoken')},
        success: function (data) {
            post.find('.like_count').text(data.likes_count);
            const likeBtn = post.find('.like-post-btn');
            const icon = likeBtn.find('i');
            icon.toggleClass('bi-heart', !data.liked);
            icon.toggleClass('bi-heart-fill', data.liked);
            }
        });
}

function toggleCommentLike(){
    const comment_id = $(this).data("comment-id")
    const comment = $('#comment-' + comment_id);

    $.ajax({
        url: '/comments/' + comment_id + '/like/',
        method: 'post',
        headers: { 'X-CSRFToken': getCookie('csrftoken')},
        success: function (data) {
            comment.next('.like_count').text(data.likes_count);
            const icon = comment.find('i');
            icon.toggleClass('bi-heart', !data.liked);
            icon.toggleClass('bi-heart-fill', data.liked);
            }
        });
}

$(document).ready(function (){
    $("#posts_container").on("click", ".like-post-btn", togglePostLike);
    $("#posts_container").on("click", ".like-comment-btn", toggleCommentLike);
})
