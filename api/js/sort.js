function sortHandler() {
    const sort = $(this).data('sort');
    $.ajax({
        url: '/posts/sort/',       // ваш URL эндпоинта
        method: 'GET',
        data: { sort: sort },
        success: function (html) {
            // html — это отрендеренный _posts_list.html
            $('#posts_container').html(html);
            }
        });
}

$(document).ready(function (){
    $(".sort-btn").on("click", sortHandler)
})


