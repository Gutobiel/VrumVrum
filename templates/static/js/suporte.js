function submitForm(event) {
    // Tentativa de impedir o envio do formulário de maneira tradicional
    event.preventDefault(); 

    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const regiao = document.getElementById('regiao').value;
    const mensagem = document.getElementById('mensagem').value;

    // Variaveis da mensagem
    const formData = {
        nome: nome,
        email: email,
        regiao: regiao,
        mensagem: mensagem
    };

    // Tentando enviar por um fetch
    fetch('http://127.0.0.1:8000/api/suporte', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Mensagem enviada com sucesso!');
        } else {
            alert('Ocorreu um erro ao enviar a mensagem.');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Ocorreu um erro ao enviar a mensagem.');
    });
}