from time import sleep
from tqdm import tqdm

print('\033[1:32m=-\033[m'*59)
print(' '*42,'\033[7:30:42m$$$   SISTEMA DE BANCO PY-LZ   $$$\033[m')
print('\033[1:32m-=\033[m'*59)

usuario = str('luiz')
senha = int(123456)
saldo = float(1800)
contador = int(1)

while contador <= 3:
    logar = str(input('\n\033[1:40mDigite seu login: \033[m')).strip().upper().lower()
    acesso = int(input('\033[1:40mDigite a senha: \033[m'))
    contador += 1

    if usuario == logar and senha == acesso:
        print('\n\n\n\033[1:36:40mAguarde...\033[m')
        for i in tqdm(range(2)):
            sleep(1)
        print('\n\n\n',' '*42,'\033[1:32:40m ACESSO PERMITIDO \033[m')
        sleep(1)
        print('\n\n\n\n',' '*29,'\033[1:40m{} seja bem-vindo, como posso ajudar hoje?\033[m'.format(usuario).upper())
        sleep(1)
        print('''\033[1:40mMENU:\033[m
        \033[1:33m  [1]\033[m \033[1:40m  SALDO  \033[m
        \033[1:33m  [2]\033[m \033[1:40m  SAQUE  \033[m
        \033[1:33m  [3]\033[m \033[1:40m  DEPÓSITO  \033[m
        \033[1:33m  [4]\033[m \033[1:40m  CÂMBIO  \033[m
        \033[1:33m  [5]\033[m \033[1:40m  EMPRÉSTIMO  \033[m
        ''')
        opcoes = int(input('\n\033[1:40mEscolha uma opção: \033[m'))
        if opcoes == 1:
            print('\n\n\033[1:36:40mAguarde...\033[m')
            for i in tqdm(range(2)):
                sleep(1)
            print('\n\n\n\033[1:40mSaldo atual é de \033[m\033[1:32:40mR${:.2f}\033[m'.format(saldo))
            print('\n\n\033[1:40mSujeito a alteração até o final do dia.\033[m')
        elif opcoes == 2:
            saque = float(input('\n\033[1:40mDigite o valor do saque\033[m\033[1:32:40m(R$)\033[m: '))
            sacado = saldo - saque
            print('\n\n\033[1:36:40mAguarde...\033[m')
            for i in tqdm(range(3)):
                sleep(1)
            if saque > saldo:
                print('\n\n\033[1:31:40mVOCÊ NÃO TEM SALDO SUFICIENTE PARA ESSE SAQUE.\033[m')
            else:
                print('\n\n\n\033[1:40mO valor sacado foi de \033[m\033[1:32:40mR${:.2f}\033[m'.format(saque))
                print('\033[1:40mSaldo atual é de \033[m\033[1:32:40mR${:.2f}\033[m'.format(sacado))
                print('\n\033[1:40mSujeito a alteração até o final do dia.\033[m')

        elif opcoes == 3:
            deposito = float(input('\n\033[1:40mDigite o valor do depósito\033[m\033[1:32:40m(R$)\033[m: '))
            depositado = float(saldo + deposito)
            print('\n\n\033[1:36:40mAguarde...\033[m')
            for i in tqdm(range(2)):
                sleep(1)
            print('\n\n\n\033[1:40mO valor depositado é de \033[m\033[1:32:40mR${:.2f}\033[m'.format(deposito))
            print('\033[1:40mSaldo atual é de \033[m\033[1:32:40mR${:.2f}\033[m'.format(depositado))
            print('\n\n\033[1:40mSujeito a alteração até o final do dia.\033[m')
        elif opcoes == 4:
            sleep(1)
            print('''\n\n\033[1:40mCÂMBIO:\033[m
            \033[1:33m  [1]\033[m \033[1:40m  DOLAR  \033[m
            \033[1:33m  [2]\033[m \033[1:40m  EURO  \033[m
            ''')
            real = float(input('\n\033[1:40mDigite o valor em reais que vai converter \033[m\033[1:32:40m(R$)\033[m:'))
            sleep(1)
            cambio = int(input('\n\033[1:40mEscolha uma moeda: \033[m'))
            print('\n\n\n\033[1:36:40mAguarde...\033[m')
            for i in tqdm(range(2)):
                sleep(1)
            print('\n\n\n\033[1:40mvalor de \033[m\033[1:32:40mR${:.2f}\033[m'.format(real))
            if cambio == 1:
                dolar = real/4.99
                print('\033[1:40mconvertido é de \033[1:32:40mUS${:.2f}\033[m'.format(dolar))
            elif cambio == 2:
                euro = real/5.28
                print('\033[1:40mconvertido é de \033[1:32:40mEUR{:.2f}\033[m'.format(euro))
        elif opcoes == 5:
            emprestimo = float(input('\033[1:40mDigite o valor de empréstimo que deseja \033[m\033[1:32:40m(R$)\033[m: '))
            sleep(1)
            parcelamento = int(input('\033[1:40mDeseja parcelar em quantas vezes \033[m\033[1:33:40m(limite de parcelas 64x)\033[m:'))
            parcelas = float(emprestimo / parcelamento)
            juros = float(parcelas * 0.15) + parcelas
            total = float(juros * parcelamento)
            print('\n\n\n\033[1:36:40mAguarde...\033[m')
            for i in tqdm(range(2)):
                sleep(1)
            print('''\033[1:40mDetalhes do empréstimo:\033[m\n
                \033[1:40mValor solicitado: \033[m\033[1:32:40mR${:.2f}\033[m
                \033[1:40mQuantidade de parcelas: \033[m\033[1:32:40m{}x\033[m
                \033[1:40mValor das Parcelas: \033[m\033[1:32:40mR${:.2f}\033[m
                \033[1:40mTotal: \033[m\033[1:32:40mR${:.2f}\033[m 
            '''.format(emprestimo,parcelamento,juros,total))

        else:
            sleep(1)
            print('\n','\033[1:33:40mOPÇÃO INVÁLIDA\033[m')

    else:
        print('\n\n\033[1:36:40mAguarde...\033[m')
        for i in tqdm(range(2)):
            sleep(1.5)
        print('\n\n\n',' '*44,'\033[1:31:40mACESSO NEGADO\033[m')

        #print('\n\033[1:31mErro, digite as informações de forma correta!\033[m')
