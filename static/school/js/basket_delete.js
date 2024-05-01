$(document).on('click', 'a.basket-remove', function(e) {
    e.preventDefault();  // Отменить действие по умолчанию (переход по ссылке)

    var url = $(this).attr('href');  // Получить URL из атрибута href ссылки

    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            if (data.success) {
                // Запросить обновленный HTML для корзины
                $.ajax({
                    url: '/auth/basket/',  // URL вашего эндпоинта для получения HTML корзины
                    type: 'GET',
                    success: function(html) {
                        var parser = new DOMParser();
                        var doc = parser.parseFromString(html, "text/html");
                        var bodyContent = doc.body.innerHTML;
                        $('body').html(bodyContent);
                    }
                });
            } else {
                alert('Произошла ошибка при удалении корзины.');
            }
        }
    });
});
