$(function () {
    let contentModal = $('#contentModal');

    $(contentModal).on('show.bs.modal', function (event) {
        let button = $(event.relatedTarget);
        let imageSrc = button.data('lct-isrc');
        let author = button.data('lct-author');
        let created = button.data('lct-date');
        let modal = $(this);
        modal.find('#submissionViewer').attr('src', imageSrc);
        modal.find('#submissionLink').attr('href', imageSrc);
        modal.find('#submissionAuthor').val(author);
        modal.find('#submissionDate').val(created);
    });
});

