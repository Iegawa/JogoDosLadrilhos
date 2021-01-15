#OPCAO DO JOGO
opcao = input('Opcao de jogo: \n')
while opcao < 0 or opcao > 2:
    opcao = input('Opcao invalida! Digite novamente: \n')

#Dimensao 
n = input('Tamanho do tabuleiro: \n')
while n < 2:
    n = input('Erro! Digite novamente: \n')

#configuracao inicial
tabuleiro_inicial = []
linha = []
print 'Tabuleiro inicial: '
for i in range(0,n):
    inicial = raw_input()
    conf_inicial = inicial.split(' ')
    for j in range(len(conf_inicial)):
        if conf_inicial[j] == '':
            linha.append(int(conf_inicial[j+1]))
        else:
            linha.append(int(conf_inicial[j]))
    tabuleiro_inicial.append(linha)
    linha = []


if opcao == 0:
    #configuracao final
    tabuleiro_final = []
    print 'Tabuleiro final: \n'
    for i in range(0,n):
        final = raw_input()
        conf_final = final.split(' ')
        for j in range(len(conf_final)):
            if conf_final[j] == '':
                linha.append(int(conf_final[j+1]))
            else:
                linha.append(int(conf_final[j]))
        tabuleiro_final.append(linha)
        linha = []

    #comparacao
    a = 0
    for i in range(0,n):
        for j in range(0,n):
            if tabuleiro_inicial[i][j] == tabuleiro_final[i][j]:
                a = a + 1
    if a == n*n:
        print 'SIM\n'
    else:
        print 'NAO\n'

if opcao == 1:
    erro = 0

    #informa sequencia
    m = raw_input("Digite seq mov: \n")
    for k in range(len(m)):
        if m[k] != 'c' and m[k] != 'b' and m[k] != 'd' and m[k] != 'e':
            erro = m[k]

    #verifica se eh possivel e realiza os movimentos
    k = 0
    for i in range(0,n):
        for j in range(0,n):
            if erro != 0:
                pass
            elif tabuleiro_inicial[i][j] == 0:
                for k in range(len(m)):
                    if m[k] == 'e' and erro == 0:
                        j = j - 1
                        if j >= 0:
                            aux = tabuleiro_inicial[i][j+1]
                            tabuleiro_inicial[i][j+1] = tabuleiro_inicial[i][j]
                            tabuleiro_inicial[i][j] = aux
                        else:
                            erro = k + 1
                            print 'NAO:',erro
                    elif m[k] == 'd' and erro == 0:
                        j = j + 1
                        if j < n:
                            aux = tabuleiro_inicial[i][j]
                            tabuleiro_inicial[i][j] = tabuleiro_inicial[i][j-1]
                            tabuleiro_inicial[i][j-1] = aux
                        else:
                            erro = k + 1
                            print 'NAO:',erro 
                    
                    elif m[k] == 'c' and erro == 0:
                        i = i - 1
                        if i >= 0:
                            aux = tabuleiro_inicial[i][j]
                            tabuleiro_inicial[i][j] = tabuleiro_inicial[i+1][j]
                            tabuleiro_inicial[i+1][j] = aux
                        else:
                            erro = k + 1
                            print 'NAO:',erro
                    elif m[k] == 'b' and erro == 0:
                        i = i + 1
                        if i < n:
                            aux = tabuleiro_inicial[i][j]
                            tabuleiro_inicial[i][j] = tabuleiro_inicial[i-1][j]
                            tabuleiro_inicial[i-1][j] = aux
                        else:
                            erro = k + 1
                            print 'NAO:',erro
    if erro == 0:
        print("Tabuleiro final: ")
        for i in range(n):
            print(str(tabuleiro_inicial[i][0])+ ' '+str(tabuleiro_inicial[i][1])+ ' '+str(tabuleiro_inicial[i][2])+ ' ')