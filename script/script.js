const temaEscuro = document.getElementById('temaEscuro');
const navbar = document.getElementById('BarraNavegacao');

function abrirCadastro(){
    document.getElementById('telaCadastro').style.display = "block"
}

function fecharCadastro(){
    document.getElementById('telaCadastro').style.display = "none"
}

temaEscuro.addEventListener('change', ()=>{

    document.body.classList.toggle('tema-escuro');
    navbar.classList.toggle('navbar-dark')
})