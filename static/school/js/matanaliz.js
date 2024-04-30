$(document).ready(function() {
    $('.view-button').click(function() {
        var card = $(this).closest('.card');
        var title = card.find('.card-title');
        var description = card.find('.subtopic-description');

        if (description.is(':hidden')) {
            title.hide();
            description.show();
            $(this).text('Скрыть');
        } else {
            description.hide();
            title.show();
            $(this).text('Описание');
        }
    });
});
