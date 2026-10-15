function sortHandler() {
    const sort = $(this).data('sort');
    $.ajax({
        url: '/posts/sort/',
        method: 'GET',
        data: { sort: sort },
        success: function (html) {
            $('#posts_container').html(html);
            }
        });
}

$(document).ready(function (){
    $(".sort-btn").on("click", sortHandler)
})


