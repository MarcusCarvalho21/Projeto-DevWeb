
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
const pagina = document.querySelector('.pagina');
const setaNavegacao = document.querySelectorAll('.setaNavegacao');
const tituloHistorico = document.querySelector('.tituloHistorico');
const dashboardTitulo = document.querySelectorAll('.dashboard h4');
const dashboardValor = document.querySelectorAll('.dashboard span');
const mensagemSemTarefas = document.getElementById('mesagemSemTarefas');

// Função para aplicar o tema escuro
function aplicarTemaEscuro() {
    document.body.classList.add('tema-escuro');
    navbar.classList.add('navbar-dark');
    if(mensagemSemTarefas != null){
        mensagemSemTarefas.classList.add('mesagemSemTarefas-dark');
    }
    dashboardTitulo.forEach(function(seta) {
        seta.classList.add('dark');
    });
    dashboardValor.forEach(function(seta) {
        seta.classList.add('dark');
    });
    if (tituloHistorico != null){
        tituloHistorico.classList.add('dark');
    }
    if (pagina != null && setaNavegacao != null){
        pagina.classList.add('dark');
        setaNavegacao.forEach(function(seta) {
            seta.classList.add('dark');
        });
    }
}

// Função para remover o tema escuro
function removerTemaEscuro() {
    document.body.classList.remove('tema-escuro');
    navbar.classList.remove('navbar-dark');
    if(mensagemSemTarefas != null){
        mensagemSemTarefas.classList.remove('mesagemSemTarefas-dark');
    }
    dashboardTitulo.forEach(function(list) {
        list.classList.remove('dark');
    });
    dashboardValor.forEach(function(list) {
        list.classList.remove('dark');
    });
    if (tituloHistorico != null){
        tituloHistorico.classList.remove('dark');
    }
    if (pagina != null && setaNavegacao != null){
        pagina.classList.remove('dark');
        setaNavegacao.forEach(function(seta) {
            seta.classList.remove('dark');
        });
    }
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