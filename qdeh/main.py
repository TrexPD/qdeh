from datetime import date
from rich.text import Text
from rich.panel import Panel
from rich.layout import Layout
from rich.console import Console
from key import pass_key, show_keys, last_key
from clima import clima_agora
from dados import ler_arquivo_csv
from time import sleep
from re import findall
from rich import print
from menu_main import menu_main


# Instanciando classes!
layout = Layout(name='main')
texto = Text()
console = Console()

# Aceita apenas números inteiros!
def leia_inteiros() -> int:
    while True:
        try:
            numero: int = int(console.input('Digite um número para escolher: '))
        except ValueError:
            print('[red]Por favor, digite apenas números inteiros![/red]')
        else:
            return numero



def painel_info(cidade: str, key: str = ''):
    data_atual = date.today().strftime("%d/%m")
    calendario = Panel(ler_arquivo_csv(data_atual), title='[cyan]Calendário Sazonal[/]', highlight=True)
    previsao_tempo = Panel(clima_agora(cidade, key), title=f'[cyan]Previsão do Tempo[/]', highlight=True)
    layout['main'].split_column(Layout(name='cima', minimum_size=13), Layout(name='baixo', minimum_size=10))
    layout['cima'].split_row(Layout(previsao_tempo, name='esquerda'), Layout(calendario, name='direita')) 

    return layout



with console.screen() as screen:
    chave_key: str = last_key()
    while True:
        sair: bool = False
        force_menu: bool = False
        screen.update(menu_main())
        escolha: int = leia_inteiros()
        if escolha == 0:
            with console.status('Obrigado por usar nosso sistema. Volte Sempre! :heart:'):
                sleep(3)
                break
        elif escolha > 4 or escolha < 0:
            print('[red]Alternativa incorreta, digite apenas 0, 1, 2, 3 ou 4![/red]')
            sleep(3)
        else:
            while True:
                if escolha == 1:
                    screen.update('')
                    nome_cidade: str = str(console.input('Digite o nome da sua cidade! [cyan]Ex:"sao paulo":[/] ')).strip().replace(' ', '_').lower()
                    screen.update(painel_info(nome_cidade, chave_key))
                    sleep(5)
                    break
                if escolha == 2:
                    screen.update('')
                    data_escolhida = str(console.input('Digite a data comemorativa você quer ver? [cyan]Ex: [DD/MM]:[/] ')).strip()
                    if findall(r'([0-9]{2}/[0-9]{2})', data_escolhida):
                        dia = int(data_escolhida[0:2])
                        mes = int(data_escolhida[3:5])
                        if dia > 31 or dia < 1 or mes > 12 or mes < 1:
                            print('[red][b]Data inválida[/b], digite outra data![/red]')     
                            sleep(3)
                        else:
                            screen.update(ler_arquivo_csv(data_escolhida))
                            break
                    else:
                        print('[red]A data tem que estar no seguinte formato. Ex: 01/01[/red]')
                        sleep(3)

                if escolha == 3:
                    screen.update('')
                    chave_key = pass_key()
                    force_menu = True
                    break

                if escolha == 4:
                    screen.update(show_keys())
                    break

            while True:
                if force_menu:
                    break
                outra_opcao = str(console.input('Você quer sair do app ou voltar ao menu? [b][Sair | Menu]:[/] ')).strip().lower()
                if outra_opcao == 'menu':
                    break                      
                if outra_opcao == 'sair':   
                    sair = True
                    break
                else:
                    print('[yellow]Alternativa incorreta, digite apenas [b][red]menu[/][/] ou [b][red]sair[/][/]![/]', end='\r')

        if sair:
            with console.status('Obrigado por usar nosso sistema. Volte Sempre! [b]:heart:[/b]'):
                sleep(3)
                break
