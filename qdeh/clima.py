from requests.sessions import Session
from rich.text import Text
from rich import print
from datetime import datetime



headers: dict = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',  # Do Not Track Request Header
    'Connection': 'close'}


def clima_agora(nome_cidade: str, key: str = '') -> str:
    data_atual = datetime.now().strftime(r'%d/%m/%Y %H:%M:%S')
    if len(key) == 8:
        key = f'key={key}'
    busca_por_woeid: str = f'https://api.hgbrasil.com/stats/find_woeid?{key}&format=json-cors&sdk_version=console&city_name={nome_cidade}'
    try:
        with Session().get(busca_por_woeid, headers=headers) as sessao1:
            if 'error' in sessao1.json():
                return (f'{sessao1.json()}\n\nCadastre sua chave de acesso (key) no [b]"menu de opcões"[/] para fazer novas consultas!')
            else:
                city_name = sessao1.json()['name']
                region = sessao1.json()['region']
                country = sessao1.json()['country']
                woeid = sessao1.json()['woeid']
    except:
        return f'Cidade não encontrada em nossos servidores ou não existe!'


    busca_por_cidade: str = f'https://api.hgbrasil.com/weather?{key}&woeid={woeid}'
    with Session().get(busca_por_cidade, headers=headers) as sessao2:
        try:
            data_atual_dict = {'more_info': {'city': city_name, 'region': region, 'country': country, 'woeid': woeid, 'last_consultation': data_atual}}
            juntar_dict = {**sessao2.json(), **data_atual_dict}
            arquivo_json = str(juntar_dict).replace("'", '"').replace('True', 'true').replace('False', 'false')
            with open('.\\files\\clima_atual.json', mode='wt', encoding='utf-8') as arquivo:
                arquivo.write(arquivo_json)
                titulo = Text(f"[black on white]Previsão do tempo para a cidade de [blue]{city_name}, {region}, {country}[/blue][/]\n", no_wrap=True, justify='left')
                temperatura = sessao2.json()['results']['temp']
                humidade = sessao2.json()['results']['humidity']
                estado_atual = sessao2.json()['results']['description']
                nebulosidade = sessao2.json()['results']['cloudiness']
                milimetros_chuva = sessao2.json()['results']['rain']
                prob_chuva = sessao2.json()['results']['forecast'][0]['rain_probability']
                temp_max = sessao2.json()['results']['forecast'][0]['max']
                temp_min = sessao2.json()['results']['forecast'][0]['min']                    
                nascer_sol = sessao2.json()['results']['sunrise']
                por_sol = sessao2.json()['results']['sunset']
                velocidade_vento = sessao2.json()['results']['wind_speedy']
        
                return f"""
    {titulo}
    [b]Temperatura:[/b] {temperatura}°C
    [b]Probabilidade de Chuva:[/b] {prob_chuva}%    :droplet: {float(milimetros_chuva)} mm
    [b]Humidade:[/b] {humidade}%
    [b]Max/Min:[/b] :up_arrow:{temp_max}°C  :down_arrow:{temp_min}°C
    [b]Nebulosidade:[/b] {nebulosidade}%    \U0001f4a8 {velocidade_vento}
    [b]Condições do Tempo:[/b] [cyan]{estado_atual}[/]
    [b]Nascer/Pôr do sol:[/b] :sun_with_face:{nascer_sol, por_sol}:sunrise_over_mountains:
    """
        except Exception as error:
            return f'{error}'



if __name__ in '__main__':
    print(clima_agora('sao paulo', 'sua_chave_aqui'))
