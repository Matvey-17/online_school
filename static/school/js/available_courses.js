$(document).ready(function() {
    let page = 1;

    $('#coursesContainer').on('click', '#loadMore', function(e) {
        let url = $('#divBtn').data('url')
        e.preventDefault();
        page++;
        $.ajax({
            url: url,
            type: 'get',
            data: {
                page: page
            },
            dataType: 'json',
            success: function(data) {
                $.each(data, function(index, course) {
                    let row = $('<div>').addClass('row mt-4').appendTo('#coursesContainer');
                    let col = $('<div>').addClass('col-md-8').appendTo(row);
                    let card = $('<div>').addClass('card').css('border-radius', '.75rem').appendTo(col);
                    let card_body = $('<div>').addClass('card-body').appendTo(card);
                    let card_desc = $('<div>').addClass('card col-md-4 col-7 mb-3').css({'border-radius': '.20rem', 'margin-left': '-10px', 'background-color': '#c8f288'}).appendTo(card_body);
                    $('<span>').css('font-size', '11px').text(course.name_themes.name_items.name).appendTo(card_desc);
                    $('<h5>').addClass('card-title').text(course.name_themes.name).appendTo(card_body);
                    $('<p>').addClass('card-text').text(course.name).appendTo(card_body);
                    $('<a>').attr('href', '#').addClass('btn btn-primary mr-3').css({'border-radius': '.5rem', 'background-color': '#d2f1d9', 'color': 'black', 'border-color': '#dedce3'}).text('Конспект').appendTo(card_body);
                    $('<a>').attr('href', '#').addClass('btn').css('border-radius', '.5rem').text('Вебинар').appendTo(card_body);
                });
                $('#loadMore').remove();
                $('#divBtn').remove();
                let btn = $('<div>').attr('id', 'divBtn').addClass('mt-2 ml-2 mb-4').appendTo('#coursesContainer')
                $('<a>').attr({'href': url, 'id': 'loadMore'}).addClass('btn').css('border-radius', '.5rem').text('Показать еще').appendTo(btn);
                if (data.length < 5) {
                    $('#loadMore').remove();
                }
            }
        });
    });
});
