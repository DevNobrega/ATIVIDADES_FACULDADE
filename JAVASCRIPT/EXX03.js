let n1 = parseFloat(prompt('Informe o 1° número:'));
let opcoes = prompt('Escolha a operação que deseja:\n 1 = Adição\n 2 = Subtração\n 3 = Multiplicação\n 4 = Divisão\n ');
let n2 = parseFloat(prompt('Informe o 2° número:'));
let resultado;
if (opcoes == 1){
    resultado = n1+n2;
    alert(resultado);
}else if(opcoes == 2){
    resultado = n1-n2;
    alert(resultado);
}else if(opcoes == 3){
    resultado = n1 * n2;
    alert(resultado);
}else if(opcoes == 4){
      if(n2 == 0){
        alert('ERRO');
      }
      else{
        resultado = n1/n2;
        alert(resultado);
      }
}