from rich.panel import Panel
from datetime import datetime


def menu_main():
    data_atual: str = datetime.now().strftime(r'%d/%m/%Y')
    dia_semana_atual: int = datetime.now().isoweekday()
    hora_atual: int = datetime.now().hour
    semanas: dict = {
        1: 'Segunda-Feira',
        2: 'Terça-Feira',
        3: 'Quarta-Feira',
        4: 'Quinta-Feira',
        5: 'Sexta-Feira',
        6: 'Sábado',
        7: 'Domigo',
    }

    if hora_atual >= 5 and hora_atual < 12:
        cumprimento: str = 'Bom dia!'
    elif hora_atual >= 12 and hora_atual < 18:
        cumprimento: str = 'Boa tarde!'
    elif hora_atual >= 18 and hora_atual < 25:
        cumprimento: str = 'Boa noite!'
    else:
        cumprimento: str = 'Boa madrugada!'
    return (Panel(f"""
    [b]Olá, [cyan]{cumprimento}[/][/]
    [b]Hoje é [cyan]{semanas[dia_semana_atual]}[/], dia {data_atual}[/]!
    
    [b]Escolha uma opção abaixo, digitando o seu número correspondente![/b]

    1 -> Ver o [b]clima[/] e datas de hoje
    2 -> Digitar uma data especifica
    3 -> Adicionar minha própria Chave(Key)
    4 -> Mostrar todas as Chaves(keys)
    0 -> Sair do programa
""", title='[blue]Menu de opções[/]', height=13, highlight=True))


if __name__ == '__main__':
    print(menu_main())