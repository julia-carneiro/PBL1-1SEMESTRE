"""/*******************************************************************************
Autor: Júlia Carneiro Gonçalves de Souza
Componente Curricular: MI - Algoritmos
Concluido em: 31/08/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum trecho de código de outro colega ou de outro autor,
tais como provindos de livros e apostilas, e páginas ou documentos eletrônicos da Internet.
Qualquer trecho de código de outra autoria que não a minha está destacado com uma citação para o autor e a fonte do código,
e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/"""
fem = masc = idadeTot = idadeSint = atletasTot = 0
maisVelhoSint = 0
maisNovoSint = 999
tempMax = 0
atletasSintoma = femSintoma = mascSintoma = 0
sintomaN = femSintomaN = mascSintomaN = 0
quantMedalha = femMedalha = mascMedalha = bronzeFem = bronzeMasc = prataFem = prataMasc = ouroFem = ouroMasc = 0
femMedalhaSint = mascMedalhaSint = bronzeFemSint = bronzeMascSint = prataFemSint = prataMascSint = ouroFemSint = ouroMascSint =  0
kitCovidS = femKitCovid = mascKitCovid = femKitSintoma = mascKitSintoma = femKitSintomaN = mascKitSintomaN = 0

continuar = 'S'
while (continuar == 'S'):
    #Recolhe dados da idade, idade do mais novo e do mais velho.
    idade = 0
    while idade <= 0 or idade >= 100:
        idade = int(input('Informe sua idade: [Até 99 anos] '))
        idadeTot += idade
        if idade <= 0 or idade >= 100:
            print("Por favor digite uma idade válida")
    ##Recolhe dados de sexo
    sexo = ''
    while sexo != 'F' and sexo != 'M':
        sexo = input('Informe seu sexo [F/M]: ').strip().upper()[0]
        if sexo == 'F':
            fem += 1
        elif sexo == 'M':
            masc += 1
        else:
            print('Por favor digite uma opção válida: F ou M ')

    atletasTot = (fem+masc)

    #Atletas que tiveram febre
    febre = ''
    sintoma = ''
    while febre != 'S' and febre != 'N':
        febre = input('Você apresentou febre depois que retornou das Olimpíadas: [S/N] ').strip().upper()[0]
    #Recebe dados de temperatura e armazena a máxima
        #Teve febre
        if febre == 'S':
            temperatura = float(input('Qual a temperatura corporal máxima em ºC que obteve depois do retorno? '))
            atletasSintoma += 1
            idadeSint += idade #para calcular idade média com sintomas
            #idade do mais velho e mais novo que apresentou sintoma.
            if idade > maisVelhoSint:
                maisVelhoSint = idade
            if idade < maisNovoSint:
                maisNovoSint = idade
            #temperatura maxima
            tempMax = 0 #código feito em conjunto na sessão do dia 12/08/2021
            if temperatura > tempMax:
                tempMax = temperatura

    #Atletas que não tiveram febre, tiveram outro sintoma?
        elif febre == 'N':
            while sintoma != 'S' and sintoma != 'N':
                sintoma = input('Teve algum outro sintoma? ').strip().upper()[0]
                if sintoma == 'S':
                    atletasSintoma += 1
                    idadeSint += idade #para calcular idade média com sintomas
                    # idade do mais velho e mais novo que apresentou sintoma.
                    if idade > maisVelhoSint:
                        maisVelhoSint = idade
                    if idade < maisNovoSint:
                        maisNovoSint = idade
                    #sexo de quem apresentou sintoma
                    if sexo == 'F':
                        femSintoma += 1
                    else:
                        mascSintoma += 1
        #Caso não tenham tido outro sintoma, armazena em atletas assintomáticos
                elif sintoma == 'N':
                    sintomaN += 1
                    if sexo == 'F':
                        femSintomaN += 1
                    else:
                        mascSintomaN += 1
                else:
                    print('Por favor, digite sim ou não: ')
        else:
            print('Por favor, digite sim ou não: ')

    #Recolhe dados do kit covid
    kitCovid = ''
    while kitCovid != 'S' and kitCovid != 'N':
        kitCovid = input('Fez o uso do kit Covid ao voltar? ').strip().upper()[0]
        if kitCovid == 'S':
            kitCovidS += 1
            #mulheres e homens que usaram o kit
            if sexo == 'F':
                femKitCovid += 1
            else:
                mascKitCovid += 1
            if sintoma == 'S' and sexo == 'F':
                femKitSintoma += 1
            elif sintoma == 'S' and sexo == 'M':
                mascKitSintoma += 1
            elif sintoma == 'N' and sexo == 'F':
                femKitSintomaN += 1
            elif sintoma == 'N' and sexo == 'M':
                mascKitSintomaN += 1

        elif kitCovid == 'N':
            print('Que bom! O Kit Covid não tem eficácia comprovada, e pode causar problemas.')

        else:
            print('Por favor, digite sim ou não: ')

    medalha = ''
    while medalha != 'S' and medalha != 'N':
        medalha = input('Você ganhou alguma medalha? ').strip().upper()[0]
        if medalha == 'S':
            quantMedalha == int(input('Quantas? Digite em números: ex: 1,2,3...'))
            quantMedalha += 1
            if sintoma == 'S' or febre == 'S':
                if sexo == 'F':
                    femMedalhaSint += 1
                else:
                    mascMedalhaSint += 1
            else:
                if sexo == 'F':
                    femMedalha += 1
                else:
                    mascMedalha += 1
        #tipos de medalha
        #Bronze:
            bronze = int(input('Quantas de bronze?'))
            if sintoma == 'S' or febre == 'S': #atletas com sintomas
                if sexo == 'F' and bronze > 0:
                    bronzeFemSint += bronze
                elif sexo == 'M' and bronze > 0:
                    bronzeMascSint += bronze
            else:
                if sexo == 'F' and bronze > 0:
                    bronzeFem += bronze
                elif sexo == 'M' and bronze > 0:
                    bronzeMasc += bronze
        #Prata:
            prata = int(input('Quantas de prata?'))
            if sintoma == 'S' or febre == 'S': #atletas com sintomas
                if sexo == 'F' and prata > 0:
                    prataFemSint += prata
                elif sexo == 'M' and prata > 0:
                    prataMascSint += prata
            else:
                if sexo == 'F' and prata > 0:
                    prataFem += prata
                elif sexo == 'M' and prata > 0:
                    prataMasc += prata
        #Ouro:
            ouro = int(input('Quantas de ouro?'))
            if sintoma == 'S' or febre == 'S': #atletas com sintomas
                if sexo == 'F' and ouro > 0:
                    ouroFemSint += ouro
                elif sexo == 'M' and ouro > 0:
                    ouroMascSint += ouro
            else:
                if sexo == 'F' and ouro > 0:
                    ouroFem += ouro
                elif sexo == 'M' and ouro > 0:
                    ouroMasc += ouro
        elif medalha == 'N':
            break

        else:
            print('Por favor, digite sim ou não: ')

    continuar = input('Deseja cadastrar mais um atleta? [S/N]').strip().upper()[0]

#RELATÓRIO:
#Primeira questão
print('\nRELATÓRIO FINAL:')
print('----------------------------------------------------------------------------------------------')
print(f'1) Atletas monitorados: {atletasTot}')
#Segunda questão
print('----------------------------------------------------------------------------------------------')
if atletasSintoma>0:
    print(f'2) Quantidade de atletas com sintomas: {atletasSintoma},'
        f'cerca de {((atletasSintoma*100)/atletasTot):.2f}% do total.')
else:
    print('2) Nenhum atleta apresentou sintomas.')
#Terceira questão
print('----------------------------------------------------------------------------------------------')
if atletasSintoma > 0 and sintomaN > 0:
    print(f'3) A idade média de todos os atletas foi {idadeTot/atletasTot:.2f},'
          f' a idade média dos atletas com sintomas foi {idadeSint/atletasSintoma:.2f}'
          f' e a idade média dos atletas sem sintomas foi {((idadeTot-idadeSint)/sintomaN):.2f}')
else:
    if atletasSintoma > 0 and sintomaN == 0:
        print(f'3) A idade média de todos os atletas foi {idadeTot/atletasTot:.2f}, todos os atletas apresentaram sintomas.')
    elif sintomaN > 0 and atletasSintoma == 0:
        print(f'3) A idade média de todos os atletas foi {idadeTot/atletasTot:.2f}, nenhum atleta apresentou sintomas.')
#Quarta questão
print('----------------------------------------------------------------------------------------------')
if tempMax > 0:
    print(f'4) A temperatura mais alta relatada foi {tempMax}ºC.')
else:
    print('4) Nenhum atleta apresentou febre.')
#Quinta questão
print('----------------------------------------------------------------------------------------------')
if maisNovoSint != 999 and maisVelhoSint > 0:
    print(f'5) A idade do atleta mais novo que apresentou sintomas foi {maisNovoSint} e a do mais velho foi {maisVelhoSint}.')
else:
    print('5) Nenhum atleta apresentou sintomas.')
#Sexta questão
print('----------------------------------------------------------------------------------------------')
if kitCovidS > 0:
    print(f'6) {kitCovidS} atletas fizeram o uso do Kit Covid, dentre eles {femKitCovid} mulheres e {mascKitCovid} homens.\n'
      f'Das mulheres que usaram, {femKitSintoma} apresentaram sintomas e {femKitSintomaN} não. Já os homens, {mascKitSintoma} apresentaram sintomas e {mascKitSintomaN} não.')
else:
    print('6) Nenhum atleta fez uso do Kit Covid.')
#Sétima questão
print('----------------------------------------------------------------------------------------------')
if quantMedalha > 0:
    print(f'7) Dos atletas SEM sintomas:\n{femMedalha} mulheres ganharam medalha, sendo {bronzeFem} de bronze, {prataFem} de prata e {ouroFem} de ouro.\n'
        f'{mascMedalha} homens ganharam medalha, sendo {bronzeMasc} de bronze, {prataMasc} de prata e {ouroMasc} de ouro.\n'
        f'Dos atletas COM sintomas:\n{femMedalhaSint} mulheres com sintomas trouxeram medalha, sendo {bronzeFemSint} de bronze, {prataFemSint} de prata e {ouroFemSint} de ouro.\n'
        f'{mascMedalhaSint} homens com sintomas trouxeram medalha, sendo {bronzeMascSint} de bronze, {prataMascSint} de prata e {ouroMascSint} de ouro.')
else:
    print('7) Nenhum atleta ganhou medalhas.')
#tentei executar o programa no prompt de comando do python e ele rodou mas não mostrou os prints.
#decidi adicionar esse input para garantir que todos os passos vão ser executados, mesmo tendo rodado normal ao ser executado direto pelo cmd do windows.
#ele impede que o programa encerre imediatamente após os prints.
print(input('Aperte "Enter" para encerrar o programa.'))
