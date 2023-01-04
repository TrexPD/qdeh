import pandas as pd
from datetime import date
from rich.table import Table, box
from rich.text import Text
from rich import print
from json import load


# Cria um novo arquivo csv, de acordo com o ano vigente! 
def new_file():
    ano_atual = date.today().year
    tabela = pd.read_html('https://www.ponteiro.com.br/todas_datas.php')[0][3:].drop(columns=[1, 3]).dropna(how='all')
    tabela.to_csv(f'cal_{ano_atual}.csv', index=False, encoding='utf-8-sig', header=['Dia/Mês', 'Data Sazonal'])


# Ler o arquivo 'calendário 2022' dentro da pasta files!
def ler_arquivo_csv(data_escolhida: str):
    ano_atual = date.today().year # Retorna o ano vigente!
    tabela = Table(f'[blue]|[/] [b]Todas as datas comemorativas em [blue]{data_escolhida}/{ano_atual}![/][/b]',
    box=box.SIMPLE)
    arquivo_csv = pd.read_csv(f'.\\assets\\cal_{ano_atual}.csv')
    localizar = arquivo_csv.loc[arquivo_csv['Dia/Mês'] == f'{data_escolhida}']
    if tabela.columns:
        for i in localizar.itertuples():
            tabela.add_row(i[2])
        return tabela
    else:
        return ('[red]Formato de data válida, [b]porém a data é inexistente, tente outra![/b][/red]')


def arquivo_cache_json():
    with open('.\\assets\\clima_atual.json', mode='rt', encoding='utf-8') as arquivo:
        arquivo_json = load(arquivo)
        titulo = Text(f"[black on white]Previsão do tempo para a cidade de [blue]{arquivo_json['results']['city']}, {arquivo_json['more_info']['country']}[/blue][/]\n", no_wrap=True, justify='left')
        temperatura = arquivo_json['results']['temp']
        humidade = arquivo_json['results']['humidity']
        estado_atual = arquivo_json['results']['description']
        nebulosidade = arquivo_json['results']['cloudiness']
        milimetros_chuva = arquivo_json['results']['rain']
        prob_chuva = arquivo_json['results']['forecast'][0]['rain_probability']
        temp_max = arquivo_json['results']['forecast'][0]['max']
        temp_min = arquivo_json['results']['forecast'][0]['min']                    
        nascer_sol = arquivo_json['results']['sunrise']
        por_sol = arquivo_json['results']['sunset']
        velocidade_vento = arquivo_json['results']['wind_speedy']
        return f"""
    {titulo}
    [b]Temperatura:[/b] {temperatura}°C
    [b]Probabilidade de Chuva:[/b] {prob_chuva}%    :droplet: {float(milimetros_chuva)} mm
    [b]Humidade:[/b] {humidade}%
    [b]Max/Min:[/b] :up_arrow:{temp_max}°C  :down_arrow:{temp_min}°C
    [b]Nebulosidade:[/b] {nebulosidade}%    \U0001f4a8 {velocidade_vento}
    [b]Condições do Tempo:[/b] [cyan]{estado_atual}[/]
    [b]Nascer/Pôr do sol:[/b] :sun_with_face:{nascer_sol, por_sol}:sunrise_over_mountains:
    {arquivo_json['more_info']['last_consultation']}
    """
    

if __name__ == '__main__':
    print(arquivo_cache_json())