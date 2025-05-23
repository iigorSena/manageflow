//Controle da visibilidade dos menus da Configuração
$(document).ready(function () {
    $('.btn-config').click(function () {
        let url = $(this).data('url'); // Obtém a URL do botão clicado
        $('#area-config_view').load(url, function () {
            inicializarEventosBotoes(); // Agora os eventos são adicionados depois do carregamento
            inicializarEventosAjaxServico(); // Chama AJAX do Serviços
        });
    });
});

// Controle de destaque dos botões do Menu
document.addEventListener("DOMContentLoaded", function() {
const buttons = document.querySelectorAll(".btn-config");

buttons.forEach(button => {
    button.addEventListener("click", function() {
    // Remove o estilo dos outros botões
    buttons.forEach(btn => {
        btn.style.backgroundColor = ""; // Cor original
        btn.style.boxShadow = ""; // Sombra original
    });

    // Adiciona o estilo ao botão clicado
    this.style.backgroundColor = "#00c3ff";
    this.style.boxShadow = "0px 0px 20px #00c3ff";
    });
});
});


// Controle da visibilidade dos botões de ação
function inicializarEventosBotoes() {
    document.querySelectorAll("[id^='btn-editar_servico_']").forEach(btnEditar => {
        btnEditar.addEventListener("click", function () {
            let id = this.id.split("_").pop();

            // Mostrar os botões de confirmar e cancelar
            document.getElementById(`btn-confirmar_servico_${id}`).style.display = "block";
            document.getElementById(`btn-cancelar_servico_${id}`).style.display = "block";
            document.getElementById(`btn-deletar_servico_${id}`).style.display = "block";
            this.style.display = "none";

            // Chama a função de edição
            EdicaoServicos(id);
        });
    });

    document.querySelectorAll("[id^='img-acao_cancelar_']").forEach(btnCancelar => {
        btnCancelar.addEventListener("click", function () {
            let id = this.id.split("_").pop();

            // Chama a função para restaurar a edição ao clicar em Cancelar
            RestaurarEdicao(id);
        });
    });
}

//Controle dos botões de Edição dos Serviços
function EdicaoServicos(id) {
    console.log("EdicaoServicos recebendo ID:", id);
    // Ativar os inputs para edição
    document.getElementById(`input-form_sigla_${id}`).removeAttribute("disabled");
    document.getElementById(`input-form_servico_${id}`).removeAttribute("disabled");
    document.getElementById(`input-form_status_${id}`).removeAttribute("disabled");
    document.getElementById(`input-form_sigla_${id}`).style.borderBottom = "2px solid yellow"
    document.getElementById(`input-form_servico_${id}`).style.borderBottom = "2px solid yellow"

    // Salvar valores originais para restauração em caso de cancelamento
    document.getElementById(`input-form_sigla_${id}`).setAttribute("data-original", document.getElementById(`input-form_sigla_${id}`).value);
    document.getElementById(`input-form_servico_${id}`).setAttribute("data-original", document.getElementById(`input-form_servico_${id}`).value);
    document.getElementById(`input-form_status_${id}`).setAttribute("data-original", document.getElementById(`input-form_status_${id}`).value);
}

// Função para restaurar a edição caso o usuário cancele
function RestaurarEdicao(id) {
    console.log("Restaurando edição para ID:", id);
    // Ocultar os botões de confirmar e cancelar
    document.getElementById(`btn-confirmar_servico_${id}`).style.display = "none";
    document.getElementById(`btn-cancelar_servico_${id}`).style.display = "none";
    document.getElementById(`btn-deletar_servico_${id}`).style.display = "none";
    document.getElementById(`input-form_servico_${id}`).style.borderBottom = "none"
    document.getElementById(`input-form_sigla_${id}`).style.borderBottom = "none"

    // Mostrar o botão de edição novamente
    document.getElementById(`btn-editar_servico_${id}`).style.display = "block";

    // Desativar os inputs novamente
    document.getElementById(`input-form_sigla_${id}`).setAttribute("disabled", "true");
    document.getElementById(`input-form_servico_${id}`).setAttribute("disabled", "true");
    document.getElementById(`input-form_status_${id}`).setAttribute("disabled", "true");

    // Restaurar valores originais dos inputs
    document.getElementById(`input-form_sigla_${id}`).value = document.getElementById(`input-form_sigla_${id}`).getAttribute("data-original");
    document.getElementById(`input-form_servico_${id}`).value = document.getElementById(`input-form_servico_${id}`).getAttribute("data-original");
    document.getElementById(`input-form_status_${id}`).value = document.getElementById(`input-form_status_${id}`).getAttribute("data-original");
}


// Requisição AJAX ==========================================================
let botaoClicado = null;

document.addEventListener("click", function (e) {
    const target = e.target.closest("button[type='submit']");
    if (target) {
        botaoClicado = target;
    }
});

function inicializarEventosAjaxServico() {

    const forms = document.querySelectorAll("#form-cad_servico, #form-geren_servicos");

    if (forms.length === 0) {
        console.warn("Nenhum formulário dos Serviços encontrado.");
        return;
    }

    forms.forEach(form => {
        form.addEventListener("submit", function (e) {
            e.preventDefault();

            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            const formData = new FormData(form);
            // Se um botão de submit foi clicado, adiciona seus dados manualmente
            if (botaoClicado && botaoClicado.name) {
                formData.append(botaoClicado.name, botaoClicado.value);
            }
            fetch(form.action, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken,
                },
                body: formData
            })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    // Pode ser redirect (ex: delete)
                    window.location.href = response.url;
                }
            })
            .then(data => {
                if (data?.status === "success") {
                    const url = "/gerenciar-servicos/";

                    $("#area-config_opcoes").load(url, function () {
                        inicializarEventosBotoes();
                        inicializarEventosAjaxServico();
                    });
                } else if (data?.status === "error") {
                    alert("Erro: " + data.message);
                    console.log(data.errors);
                }
            })
            .catch(error => {
                console.error("Erro na requisição AJAX:", error);
            });
        });
    });
}

