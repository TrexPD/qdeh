from rich.panel import Panel
from rich.text import Text
from rich.console import Console
from tinydb import TinyDB
from rich.table import Table, box
from datetime import datetime
from pathlib import Path


data_atual: str = datetime.now().strftime(r'%d/%m/%Y %H:%M:%S')
db_key = TinyDB(Path('assets', 'key.json'), encoding="utf-8", ensure_ascii=False)
def pass_key() -> str:
    console = Console()
    console.print(Panel(Text.from_ansi('''
    Para conseguir uma chave key, visite o site \033[1;36mhttps://console.hgbrasil.com/users/sign_in\033[m
    e faça o cadastro (caso já tenha o cadatro faça o seguinte ->), crie uma chave gratuita
    ou paga, \033[1;36mcopie e cole a sua Chave(key) logo abaixo\033[m!
                
    \033[1mObs:\033[m Não se preocupe \033[1;36msua Chave Key está segura\033[m, apenas você terá acesso a ela!
    ''', justify='left'), title='[cyan]Chave Key[/]'))

    while True:
        chave_key = str(console.input('\nDigite sua [u][cyan]Chave Key[/][/] ou [u][cyan]Sair[/][/]: ')).strip()
        if len(chave_key) == 8:
            db_key.default_table_name = 'Acess_key'
            db_key.insert({'Key': [{'Chave(key):': f'{chave_key}'}, {'Adicionada_em:': f'{data_atual}'}]})
            console.print('Sua [cyan]Chave Key[/] foi salva com sucesso!\n')
            return chave_key
        if chave_key.lower() == 'sair':
            return ''
        else:
            console.print('[b]Atenção:[/] Sua [u][red]Chave Key[/][/] tem que ter 8 caracteres!')


# Mostra todas as senhas no arquivo 'key.json'!
def show_keys():
    tabela = Table(f'[blue]|[/] [b]Suas [blue]Chaves Keys[/]!', box=box.SIMPLE, title_justify='center')
    for index, row in enumerate(db_key.table('Acess_key')):
        tabela.add_row(f'[green]{index}[/] [cyan]Chave(key):[/]', row['Key'][0]['Chave(key):'])
        tabela.add_row('[b]  Adicionada em:[/]', row['Key'][1]['Adicionada_em:'])
    return (tabela)


# Pega a ultima senha no arquivo 'key.json'!
def last_key() -> str:
    lista_de_senhas = [row for row in db_key.table('Acess_key')]
    try:
        ultima_senha = lista_de_senhas[-1]['Key'][0]['Chave(key):']
    except IndexError:
        return ''
    else:
        return str(ultima_senha)


if __name__ == '__main__':
    print(pass_key())
    print(show_keys())