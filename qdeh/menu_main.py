from rich.panel import Panel
from datetime import datetime


def menu_main():
    data_atual = datetime.now().strftime(r'%d/%m/%Y')
    dia_semana_atual = datetime.now().isoweekday()
    semanas: dict = {
        1: 'Segunda-Feira',
        2: 'Terça-Feira',
        3: 'Quarta-Feira',
        4: 'Quinta-Feira',
        5: 'Sexta-Feira',
        6: 'Sábado',
        7: 'Domigo',
    }
    
    if (datetime.now().hour) >= 5 and (datetime.now().hour) < 12:
        cumprimento = 'Bom dia!'
    if (datetime.now().hour) >= 12 and (datetime.now().hour) < 18:
        cumprimento = 'Boa tarde!'
    if (datetime.now().hour) >= 18 and (datetime.now().hour) < 23:
        cumprimento = 'Boa noite!'
    else:
        cumprimento = 'Boa madrugada!'
    return (Panel(f"""
    [b]Olá, [cyan]{cumprimento}[/][/]
    [b]Hoje é [cyan]{semanas[dia_semana_atual]}[/], dia {data_atual}[/]!
    
    [b]Escolha uma opção abaixo, digitando o seu número correspondente![/b]

    1 -> Clima e data de hoje
    2 -> Digitar uma data especifica
    3 -> Adicionar minha própria Chave(Key)
    4 -> Mostrar todas as Chaves(keys)
    0 -> Sair do programa
""", title='[blue]Menu de opções[/]', height=13, highlight=True))


# print(menu_main())
