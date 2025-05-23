// Controle da visibilidade dos botões de ação Gerenciar Locais
function inicializarEventosBotoes() {
    document.querySelectorAll("[id^='btn-editar_local_']").forEach(btnEditar => {
        btnEditar.addEventListener("click", function () {
            let id = this.id.split("_").pop();

            // Mostrar os botões de confirmar e cancelar
            document.getElementById(`btn-confirmar_local_${id}`).style.display = "block";
            document.getElementById(`btn-cancelar_local_${id}`).style.display = "block";
            document.getElementById(`btn-deletar_local_${id}`).style.display = "block";
            this.style.display = "none";

            // Chama a função de edição
            EdicaoLocais(id);
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

//Controle dos botões de Edição dos Locais
function EdicaoLocais(id) {
    console.log("EdicaoLocais recebendo ID:", id);
    // Ativar os inputs para edição
    document.getElementById(`input-form_local_${id}`).removeAttribute("disabled");
    document.getElementById(`input-form_status_${id}`).removeAttribute("disabled");

    // Aplicar estilo visual
    document.getElementById(`input-form_local_${id}`).style.borderBottom = "2px solid yellow";

    // Salvar valores originais
    document.getElementById(`input-form_local_${id}`).setAttribute("data-original", document.getElementById(`input-form_local_${id}`).value);
    document.getElementById(`input-form_status_${id}`).setAttribute("data-original", document.getElementById(`input-form_status_${id}`).value);
}

// Função para restaurar a edição caso o usuário cancele
function RestaurarEdicao(id) {
    console.log("Restaurando edição para ID:", id);
    // Ocultar os botões de confirmar e cancelar
    document.getElementById(`btn-confirmar_local_${id}`).style.display = "none";
    document.getElementById(`btn-cancelar_local_${id}`).style.display = "none";
    document.getElementById(`btn-deletar_local_${id}`).style.display = "none";

    // Remover estilo visual
    document.getElementById(`input-form_local_${id}`).style.borderBottom = "none";

    // Mostrar o botão de edição novamente
    document.getElementById(`btn-editar_local_${id}`).style.display = "block";

    // Desativar os inputs
    document.getElementById(`input-form_local_${id}`).setAttribute("disabled", "true");
    document.getElementById(`input-form_status_${id}`).setAttribute("disabled", "true");

    // Restaurar valores originais
    document.getElementById(`input-form_local_${id}`).value = document.getElementById(`input-form_local_${id}`).getAttribute("data-original");
    document.getElementById(`input-form_status_${id}`).value = document.getElementById(`input-form_status_${id}`).getAttribute("data-original");
}


// Requisição AJAX ==========================================================

document.addEventListener("click", function (e) {
    const target = e.target.closest("button[type='submit']");
    if (target) {
        botaoClicado = target;
    }
});

function inicializarEventosAjaxLocais() {
    const forms = document.querySelectorAll("#form-geren_locais");

    if (forms.length === 0) {
        console.warn("Formulário de Gerenciamento de Locais não encontrado.");
        return;
    }

    forms.forEach(form => {
        form.addEventListener("submit", function (e) {
            e.preventDefault();

            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            const formData = new FormData(form);

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
                    // Em caso de redirect
                    window.location.href = response.url;
                }
            })
            .then(data => {
                if (data?.status === "success") {
                    const url = "/listar-locais-json/";

                    // Recarrega a tabela de locais
                    $("#table-config_locais").load(url + " #table-config_locais > *", function () {
                        inicializarEventosBotoes();     // se necessário
                        inicializarEventosAjaxLocais(); // reinicializa AJAX nos novos elementos
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
