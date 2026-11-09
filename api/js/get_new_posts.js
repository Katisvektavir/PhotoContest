function addPostsHandler() {
    const btn = $(this);
    btn.prop('disabled', true).text('Загрузка...');
    const next_page = btn.data('next-page');

    $.ajax({
        url: '/?page=' + next_page,
        method: 'GET',
        headers: {'X-Requested-With': 'XMLHttpRequest'},
        success: function (data) {
            if (data.html) {
               $('#posts_container').append(data.html);
            }
            else {
               console.error('Сервер не вернул HTML:', data);
            }

            if (data.has_next) {
                btn.data('next-page', data.next_page_number);
                btn.prop('disabled', false).text('Загрузить еще');
            }
            else {
                btn.remove(); // Если постов больше нет — убираем кнопку
            }
        }
    });
}


$(document).ready(function (){
    $("#load-more-btn").on("click", addPostsHandler);
})
