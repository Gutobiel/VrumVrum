// Validação dos campos
const form   = document.getElementById('form');
const campos = document.querySelectorAll('.required');
const spans  = document.querySelectorAll('.span-required');
const emailRegex = /^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/;
const telefoneRegex = /^(\d{2})(\d{5})(\d{4})$/; // Expressão para validar o telefone no formato 99 92922-9292
const cpfRegex = /^(\d{3})(\d{3})(\d{3})(\d{2})$/;  // Expressão para validar o CPF no formato 111.222.333-44

campos.forEach(function(campo, index) {
    campo.addEventListener("blur", function() {
        removeError(index); // Remove a memsagem de erro quado qualquer campo não estiver selcionado
    });
});

form.addEventListener('submit', (event) => {
    event.preventDefault();
    validarNome();
    validarEmail();
    validarTelefone();
    validarCPF();
    validarSenha();
    compararSenha();
    validarCargo();
});

function setError(index){
    campos[index].style.border = '2px solid #e63636';
    spans[index].style.display = 'block';
}

function removeError(index){
    campos[index].style.border = '';
    spans[index].style.display = 'none';
}


function validarNome(){
    if(campos[0].value.length < 3)
    {
        setError(0);
    }
    else
    {
        removeError(0);

        if (campos[0].value.length >= 3) {
            removeError(0); // Remove o erro se o comprimento for maior ou igual a 3 caracteres
        }
    }
}

function validarEmail(){
    if(!emailRegex.test(campos[1].value))
    {
        setError(1);
    }
    else
    {
        removeError(1);
    }
}

function validarTelefone() {
    const telefoneInput = document.getElementById('telefone');
    let telefoneValue = telefoneInput.value.replace(/\D/g, ''); // Remove todos os caracteres que não são números

    // Limita o valor do telefone a 11 dígitos
    telefoneValue = telefoneValue.slice(0, 11);

    if (telefoneValue.length !== 11) {
        setError(2); // Define um erro se o telefone não tiver 11 dígitos
    } else {
        removeError(2); // Remove qualquer erro anterior se o telefone tiver 11 dígitos
    }

    // Formata o telefone no formato 99 92922-9292
    telefoneInput.value = telefoneValue.replace(telefoneRegex, '($1) $2-$3');
}

function validarCPF() {
    const cpfInput = document.getElementById('cpf');
    let cpfValue = cpfInput.value.replace(/\D/g, ''); // Remove todos os caracteres não numéricos do valor do CPF

    // Limita o valor do CPF a 11 dígitos
    cpfValue = cpfValue.slice(0, 11);

    if (cpfValue.length !== 11) {
        setError(3); // Define um erro se o CPF não tiver 11 dígitos
    } else {
        removeError(3); // Remove qualquer erro anterior se o CPF tiver 11 dígitos
    }

    // Formata o CPF no formato 111.222.333-44
    cpfInput.value = cpfValue.replace(cpfRegex, '$1.$2.$3-$4');
}

function validarCargo() {
    const cargoInput = document.getElementById('cargo');
    const opcoes = document.getElementById('lista__opcoes').getElementsByTagName('option');
    let selecionado = false;

    for (let i = 0; i < opcoes.length; i++) {
        if (cargoInput.value === opcoes[i].value) {
            selecionado = true;
            break;
        }
    }

    if (!selecionado) {
        setError(4); 
    } else {
        removeError(4);
    }
}

function validarSenha(){
    if(campos[5].value.length < 8)
    {
        setError(5);
    }
    else
    {
        removeError(5);
        compararSenha();
    }
}

function compararSenha(){
    if(campos[5].value == campos[6].value && campos[6].value.length >= 8)
    {
        removeError(6);
    }
    else
    {
        setError(6);
    }
}


// Campo select com pesquisa

document.addEventListener("DOMContentLoaded", function() {
    var searchInput = document.getElementById("cargo");
    var optionsList = document.getElementById("lista__opcoes");
    var options = optionsList.getElementsByTagName("option");

    searchInput.addEventListener("input", function() {
        var searchText = searchInput.value.toLowerCase();
        for (var i = 0; i < options.length; i++) {
            var optionText = options[i].value.toLowerCase();
            if (optionText.indexOf(searchText) !== -1) {
                options[i].removeAttribute("hidden");
            } else {
                options[i].setAttribute("hidden", "hidden");
            }
        }
    });

    searchInput.addEventListener("click", function() {
        searchInput.value = "";
        for (var i = 0; i < options.length; i++) {
            options[i].removeAttribute("hidden");
        }
    });
});
