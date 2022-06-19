from time import sleep
from tqdm import tqdm


azul = '\033[1:36:40m'
amarelo = '\033[1:33:40m'
preto = '\033[1:40m'
verde = '\033[1:32:40m'
vermelho = '\033[1:31:40m'
fim = '\033[m'

try:
    print(f'{verde}=-{fim}'*57)
    print(' '*37,f'{verde}$$$   SISTEMA DE BANCO PY-LZ   $$${fim}')
    print(f'{verde}-={fim}'*57)

    senha = int(123456)
    saldo = float(1800)
    contador = int(1)
    tentativas = int(3)

    while contador < 4:
        usuario = str(input(f'\n{preto}Digite seu login: {fim}')).strip().upper().lower()
        acesso = int(input(f'{preto}Digite a senha: {fim}'))
        contador += 1
        tentativas -= 1
        if senha == acesso:
            print(f'\n\n\n{azul}Aguarde...{fim}')
            for i in tqdm(range(2)):
                sleep(1)
            print('\n\n\n',' '*42,f'{verde} ACESSO PERMITIDO {fim}')
            sleep(1)
            print('\n\n\n\n',' '*29,f'{usuario} seja bem-vindo, como posso ajudar hoje?'.upper())
            sleep(1)
            print(f'''{preto}MENU:{fim})
                {amarelo}[1]{fim} {preto}  SALDO  {fim}
                {amarelo}[2]{fim} {preto}  SAQUE  {fim}
                {amarelo}[3]{fim} {preto}  DEPÓSITO  {fim}
                {amarelo}[4]{fim} {preto}  CÂMBIO  {fim}
                {amarelo}[5]{fim} {preto}  EMPRÉSTIMO  {fim}
                ''')

            opcoes = int(input(f'\n{preto}Escolha uma opção: {fim}'))
            if opcoes == 1:
                print(f'\n\n{azul}Aguarde...{fim}')
                for i in tqdm(range(2)):
                    sleep(1)
                print(f'\n\n\n{preto}Saldo atual é de {fim}{verde}R${saldo:.2f}{fim}')
                print(f'\n\n{preto}Sujeito a alteração até o final do dia.{fim}')
                break
            elif opcoes == 2:
                saque = float(input(f'\n{preto}Digite o valor do saque{fim}{verde}(R$){fim}: '))
                sacado = saldo - saque
                print(f'\n\n{azul}Aguarde...{fim}')
                for i in tqdm(range(3)):
                    sleep(1)
                if saque > saldo:
                    print(f'\n\n{vermelho}VOCÊ NÃO TEM SALDO SUFICIENTE PARA ESSE SAQUE.{fim}')
                else:
                    print(f'\n\n\n{preto}O valor sacado foi de {fim}{verde}R${saque:.2f}{fim}')
                    print(f'{preto}Saldo atual é de {fim}{verde}R${sacado:.2f}{fim}')
                    print(f'\n{preto}Sujeito a alteração até o final do dia.{fim}')
                break
            elif opcoes == 3:
                deposito = float(input(f'\n{preto}Digite o valor do depósito{fim}{verde}(R$){fim}: '))
                depositado = float(saldo + deposito)
                print(f'\n\n{azul}Aguarde...{fim}')
                for i in tqdm(range(2)):
                    sleep(1)
                print(f'\n\n\n{preto}O valor depositado é de {fim}{verde}R${deposito:.2f}{fim}')
                print(f'{preto}Saldo atual é de {fim}{verde}R${depositado:.2f}{fim}')
                print(f'\n\n{preto}Sujeito a alteração até o final do dia.{fim}')
                break
            elif opcoes == 4:
                sleep(1)
                print(f'''\n\n{preto}CÂMBIO:{fim}
                {amarelo}  [1]{fim}{preto}  DOLAR  {fim}
                {amarelo}  [2]{fim}{preto}  EURO  {fim}
                ''')
                real = float(input(f'\n{preto}Digite o valor em reais que vai converter {fim}{verde}(R$){fim}:'))
                sleep(1)
                cambio = int(input(f'\n{preto}Escolha uma moeda: {fim}'))
                print(f'\n\n\n{azul}Aguarde...{fim}')
                for i in tqdm(range(2)):
                    sleep(1)
                print(f'\n\n\n{preto}Valor de {fim}{verde}R${real:.2f}{fim}')
                if cambio == 1:
                    dolar = real/4.99
                    print(f'{preto}convertido é de {verde}US${dolar:.2f}{fim}')
                elif cambio == 2:
                    euro = real/5.28
                    print(f'{preto}convertido é de {verde}EUR{euro:.2f}{fim}')
                break
            elif opcoes == 5:
                emprestimo = float(input(f'{preto}Digite o valor de empréstimo que deseja {fim}{verde}(R$){fim}: '))
                sleep(1)
                parcelamento = int(input(f'''{preto}Deseja parcelar em quantas vezes {fim}
{amarelo}(limite de parcelas 48x){fim}:'''))
                parcelas = float(emprestimo / parcelamento)
                juros = float(parcelas * 0.15) + parcelas
                total = float(juros * parcelamento)
                print(f'\n\n\n{azul}Aguarde...{fim}')
                for i in tqdm(range(2)):
                    sleep(1)
                if parcelamento <= 48:
                    print(f'''{preto}Detalhes do empréstimo:{fim}\n
                        {preto}Valor solicitado: {fim}{verde}R${emprestimo:.2f}{fim}
                        {preto}Quantidade de parcelas: {fim}{amarelo}{parcelamento}x{fim}
                        {preto}Valor das Parcelas: {fim}{verde}R${juros:.2f}{fim}
                        {preto}Total: {fim}{verde}R${total:.2f}{fim}
                    ''')
                    break
                else:
                    print(f'{preto}Erro! O limite de parcelas é 48x{fim}')
                    break
        elif contador < 4:
            print(f'\n\n{amarelo}Senha ou login inválidos.{fim}')
            sleep(0.5)
            print(f'{amarelo}Você pode tentar mais {tentativas} veze(s).{fim}')

    else:
        sleep(0.5)
        print('\n\n\n',' '* 44,f'{vermelho}ACESSO NEGADO{fim}')
        sleep(0.3)
        print(' '* 25,f'{vermelho}SEU ACESSO FOI BLOQUEADO, TENTE NOVAMENTE MAIS TARDE.{fim}')

    while True:
            if contador <= 3:
                novaConsulta = int(input(f'''\n\n\n{preto} Deseja fazer outra operação{amarelo}SIM[1]{fim} 
{preto}ou {fim}{amarelo}NÃO[0]{fim} {preto}para sair:{fim} '''))
                if novaConsulta == 1:
                    print(f'''{preto}MENU:{fim}
                          {amarelo}[1]{fim} {preto}  SALDO  {fim}
                          {amarelo}[2]{fim} {preto}  SAQUE  {fim}
                          {amarelo}[3]{fim} {preto}  DEPÓSITO  {fim}
                          {amarelo}[4]{fim} {preto}  CÂMBIO  {fim}
                          {amarelo}[5]{fim} {preto}  EMPRÉSTIMO  {fim}
                        ''')

                    opcoes = int(input(f'\n{preto}Escolha uma opção: {fim}'))
                    if opcoes == 1:
                        print(f'\n\n{azul}Aguarde...{fim}')
                        for i in tqdm(range(2)):
                            sleep(1)
                        print(f'\n\n\n{preto}Saldo atual é de {fim}{verde}R${saldo:.2f}{fim}')
                        print(f'\n\n{preto}Sujeito a alteração até o final do dia.{fim}')
                        continue
                    elif opcoes == 2:
                        saque = float(input(f'\n{preto}Digite o valor do saque{fim}{verde}(R$){fim}: '))
                        sacado = saldo - saque
                        print(f'\n\n{azul}Aguarde...{fim}')
                        for i in tqdm(range(3)):
                            sleep(1)
                        if saque > saldo:
                            print(f'\n\n{vermelho}VOCÊ NÃO TEM SALDO SUFICIENTE PARA ESSE SAQUE.{fim}')
                        else:
                            print(f'\n\n\n{preto}O valor sacado foi de {fim}{verde}R${saque:.2f}{fim}')
                            print(f'{preto}Saldo atual é de {fim}{verde}R${sacado:.2f}{fim}')
                            print(f'\n{preto}Sujeito a alteração até o final do dia.{fim}')

                    elif opcoes == 3:
                        deposito = float(input(f'\n{preto}Digite o valor do depósito{fim}{verde}(R$){fim}: '))
                        depositado = float(saldo + deposito)
                        print(f'\n\n{azul}Aguarde...{fim}')
                        for i in tqdm(range(2)):
                            sleep(1)
                        print(f'\n\n\n{preto}O valor depositado é de {fim}{verde}R${deposito:.2f}{fim}')
                        print(f'{preto}Saldo atual é de {fim}{verde}R${depositado:.2f}{fim}')
                        print(f'\n\n{preto}Sujeito a alteração até o final do dia.{fim}')
                    elif opcoes == 4:
                        sleep(1)
                        print(f'''\n\n{preto}CÂMBIO:{fim}
                        {amarelo}  [1]{fim}{preto}  DOLAR  {fim}
                        {amarelo}  [2]{fim}{preto}  EURO  {fim}
                        ''')
                        real = float(input(f'''\n{preto}Digite o valor em reais que vai 
                        converter {fim}{verde}(R$){fim}: '''))
                        sleep(1)
                        cambio = int(input(f'\n{preto}Escolha uma moeda: {fim}'))
                        print(f'\n\n\n{azul}Aguarde...{fim}')
                        for i in tqdm(range(2)):
                            sleep(1)
                        print(f'\n\n\n{preto}Valor de {fim}{verde}R${real:.2f}{fim}')
                        if cambio == 1:
                            dolar = real/4.99
                            print(f'{preto}convertido é de {verde}US${dolar:.2f}{fim}')
                        elif cambio == 2:
                            euro = real/5.28
                            print(f'{preto}convertido é de {verde}EUR{euro:.2f}{fim}')
                    elif opcoes == 5:
                        emprestimo = float(input(f'''{preto}Digite o valor de empréstimo que deseja {fim}
{verde}(R$){fim}: '''))
                        sleep(1)
                        parcelamento = int(input(f'''{preto}Deseja parcelar em quantas vezes {fim}
{amarelo}(limite de parcelas 48x){fim}: '''))
                        parcelas = float(emprestimo / parcelamento)
                        juros = float(parcelas * 0.15) + parcelas
                        total = float(juros * parcelamento)
                        print(f'\n\n\n{azul}Aguarde...{fim}')
                        for i in tqdm(range(2)):
                            sleep(1)
                        if parcelamento <= 48:
                            print(f'''{preto}Detalhes do empréstimo:{fim}\n
                                {preto}Valor solicitado: {fim}{verde}R${emprestimo:.2f}{fim}
                                {preto}Quantidade de parcelas: {fim}{amarelo}{parcelamento}x{fim}
                                {preto}Valor das Parcelas: {fim}{verde}R${juros:.2f}{fim}
                                {preto}Total: {fim}{verde}R${total:.2f}{fim}
                            ''')
                        else:
                            print(f'{preto}Erro! O limite de parcelas é 48x{fim}')
                    continue
                elif novaConsulta == 0:
                    print('\n\n\n',' '*40,f'{preto}Até Logo!{fim}')
                    break
                else:
                    sleep(1)
                    print('\n',f'{vermelho}OPÇÃO INVÁLIDA{fim}')

except:
    print(f'\n{vermelho}Erro, digite as informações de forma correta!{fim}')
