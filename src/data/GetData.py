import os
import zipfile

def __init__():
    pass

def get_data(name,path = '../src/data'):
    '''
    Importa e descompacta Datasets do Kaggle.

    Parametros:
    -----------
    name: string
        nome da competição de acordo com a api do kaggle

    path: string
        caminho da pasta para salvar os dados

    '''

    os.system(f'kaggle competitions download -c {name}')
    os.system(f'move {name}.zip {path}')
    with zipfile.ZipFile(f'{path}/{name}.zip','r') as zipref:
        zipref.extractall(f'{path}/')

