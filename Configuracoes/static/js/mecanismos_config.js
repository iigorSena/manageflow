$(document).ready(function() {
    $('.btn-config').click(function() {
        let url = $(this).data('url'); // Obtém a URL do botão clicado
        $('#area-config_opcoes').load(url);
    });
});
