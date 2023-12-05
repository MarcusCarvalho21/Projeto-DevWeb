
//Funções que controlam o iFrame da tela de cadastro de tarefas
function abrirCadastro(){
    document.getElementById('telaCadastro').style.display = "block"
}

function fecharCadastro(){
    document.getElementById('telaCadastro').style.display = "none"
}

function abrirTarefa(){
    document.getElementById('telaTarefa').style.display = "block"
 }
function fecharTarefa(){
    document.getElementById('telaTarefa').style.display = "none"
}

const temaEscuro = document.getElementById('temaEscuro');
const navbar = document.getElementById('BarraNavegacao');
const temaEscuroAtivo = localStorage.getItem('temaEscuroAtivo');

// Função para aplicar o tema escuro
function aplicarTemaEscuro() {
    document.body.classList.add('tema-escuro');
    navbar.classList.add('navbar-dark');
}

// Função para remover o tema escuro
function removerTemaEscuro() {
    document.body.classList.remove('tema-escuro');
    navbar.classList.remove('navbar-dark');
}

// Função para verificar se o modo escuro está ativo
if (temaEscuroAtivo === 'true') {
    aplicarTemaEscuro();
    temaEscuro.checked = true;
} else {
    removerTemaEscuro();
}

// Função para verificar se o modo escuro foi ativa ou desativado
temaEscuro.addEventListener('change', () => {
    if (temaEscuro.checked) {
        aplicarTemaEscuro();
    } else {
        removerTemaEscuro();
    }
    localStorage.setItem('temaEscuroAtivo', temaEscuro.checked);
});


// Temporizador da mensagem de sessão
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        document.querySelectorAll('.messages li').forEach(function(message) {
            message.classList.add('hidden');
        });
    }, 3000);
});