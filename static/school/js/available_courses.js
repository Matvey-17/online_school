$(document).ready(function() {
    let page = 1;

    $('#coursesContainer').on('click', '#loadMore', function(e) {
        let url = $('#divBtn').data('url')
        e.preventDefault();
        page++;
        $.ajax({
            url: url,  // Замените на URL вашего маршрута
            type: 'get',
            data: {
                page: page
            },
            dataType: 'json',
            success: function(data) {
                $.each(data, function(index, course) {
                    // Создание новой карточки и добавление ее на страницу
                    let row = $('<div>').addClass('row mt-4').appendTo('#coursesContainer');
                    let col = $('<div>').addClass('col-md-8').appendTo(row);
                    let card = $('<div>').addClass('card').css('border-radius', '.75rem').appendTo(col);
                    let card_body = $('<div>').addClass('card-body').appendTo(card);
                    $('<h5>').addClass('card-title').text(course.name_themes.name).appendTo(card_body);
                    $('<p>').addClass('card-text').text(course.name).appendTo(card_body);
                    $('<a>').attr('href', '#').addClass('btn btn-primary mr-3').css({'border-radius': '.5rem', 'background-color': '#61ffb3', 'color': 'black', 'border-color': 'red'}).text('Конспект').appendTo(card_body);
                    $('<a>').attr('href', '#').addClass('btn').css('border-radius', '.5rem').text('Вебинар').appendTo(card_body);
                });
                $('#loadMore').remove();
                $('#divBtn').remove();
                let btn = $('<div>').attr('id', 'divBtn').addClass('mt-2 ml-2 mb-4').appendTo('#coursesContainer')
                $('<a>').attr({'href': url, 'id': 'loadMore'}).addClass('btn').css('border-radius', '.5rem').text('Показать еще').appendTo(btn);
                if (data.length < 5) {
                    // Если мы получили менее 5 курсов, значит, это были последние курсы
                    $('#loadMore').fadeOut('slow');
                }
            }
        });
    });
});
