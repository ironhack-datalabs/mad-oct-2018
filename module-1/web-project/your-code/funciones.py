import requests
import pandas as pd
import json
from collections import Counter

dominio_api = 'https://rickandmortyapi.com/'
fuentes = {"characters": "https://rickandmortyapi.com/api/character", 
           "locations": "https://rickandmortyapi.com/api/location", 
           "episodes": "https://rickandmortyapi.com/api/episode"
          }
episodes = requests.get(fuentes["episodes"])
max_ord_episodios = episodes.json()['info']['count']

def save_df(data, path='./output/', fname='output.csv', l_epi={}): 
    episodios = '-'.join([str(e) for e in l_epi])
    data.to_csv(path+episodios+fname)

def get_num_episodios(mini=1, maxi=max_ord_episodios, res=None): 
    ''' Programación defensiva para obtener un entero y un episodio que exista '''
    print('Introduce números enteros entre {} y {} separados por coma: '.format(mini, maxi))
    while True: 
        episodios = input('Numeros: ')
        try: 
            res = set([int(e.strip()) for e in episodios.split(',')] )
            # cambiar el if
            if not res.issubset(set([x for x in range(mini, maxi+1)])): 
                raise Exception('Episodios no validos')
        except Exception as e: 
            print('Esos espisodios no valen')
        else: 
            break
    return set(res)

def get_episode_n(n=1): 
    ''' Obtenemos el episodio en cuestión '''
    url = 'https://rickandmortyapi.com/api/episode/' + str(n)
    res = requests.get(url)
    return res 

def get_char_names_episode(episode=1): 
    ''' Obtenemos todos los nombres de los personajes que aparecen en el episodio '''
    res = []
    epi = get_episode_n(episode)
    urls = epi.json()['characters']
    for u in urls: 
        charac = requests.get(u).json()['name']
        res.append(charac)
    return res

def get_stats(set_epi={}): 
    ''' Dado un conjunto de episodios, genera una lista con la lista de personajes '''
    res = []
    for i in set_epi: 
        res.append(get_char_names_episode(i))
    return res

def flatten_list(list_of_lists): 
    return [val for sublist in list_of_lists for val in sublist]

def create_df(personajes_episodios): 
    flat = flatten_list(personajes_episodios)
    df_res = pd.DataFrame.from_dict(Counter(flat), orient='index', columns=['Appereances'])
    # Nombramos el índice
    df_res.index.name = 'Characters'
    # Creamos nueva columna
    df_res['Appereances (%)'] = 100 * (df_res['Appereances']/len(personajes_episodios))
    # Ordenamos por número de apariciones
    df_res = df_res.sort_values(by=['Appereances'], ascending=False)
    return df_res 

if __name__ == '__main__': 
    pass