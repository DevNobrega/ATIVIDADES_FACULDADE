let numero = parseInt(prompt('Infome o número desejado:'));

const interval = setInterval(() => {
    if (numero > 0){
        document.getElementById("countdown").innerHTML = numero;
        numero--;
    }else {
        clearInterval(interval);
        document.getElementById("countdown").innerHTML = "Contagem Regressiva!";
    }
}, 1000);