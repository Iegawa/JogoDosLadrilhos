# JogoDosLadrilhos
Trabalho1 - Curso de Verão Tópicos de Programação
No jogo dos ladrilhos, uma matriz nxn possui os elementos de 1 a n-1 e um espaço em branco, aqui representado pelo 0. Este espaço indica que há uma posição livre, podendo ser ocupada por outro elemento. O jogo consiste em partir de uma configuração inicial para uma configuração final em que os movimentos permitidos ocorrem apenas com o espaço em branco (0). 

## Regras
Não usar nenhuma biblioteca.

Movimentos:
 _c_: mover o espaço em branco (0) para cima
 _d_: mover o 0 para a direita
 _e_: mover o 0 para a esquerda
 _b_: mover o 0 para baixo


## Opções de jogo:
Opção 0:

Leia a opção de jogo (supor digitado 0);
Leia um inteiro n>=2 (dimensão do tabuleiro);
Leia uma configuração inicial qualquer de uma matriz n x n contendo os números de 0 a n2 -1;
Leia uma configuração final qualquer de uma matriz n x n contendo os números de 0 a n2 -1;
Imprima SIM se ambas as matrizes forem idênticas, caso contrário imprima NAO.

Opção 1: 

Leia a opção de jogo (supor digitado 1);
Leia um inteiro n>=2 (dimensão do tabuleiro);
Leia uma configuração inicial qualquer de uma matriz n x n contendo os números de 0 a n2 -1
Leia uma "string" com uma sequência de movimentos (dentre {'c', 'd', 'b', 'e'}) a serem tentados (supor m>=1 movimentos);
Realize os m movimentos (se todos forem válidos) e ao final imprima a matriz resultante.
Se o movimento i (1<=i<=m) for o primeiro movimento inválido, deve-se imprimir NAO: i.


