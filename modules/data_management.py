'''
This module load all the data.json from the data directory
'''

import flet
import json
import os


def load_data(directory):
    '''
    Load the data from all JSON archives finded in the especificated directory

    Args:
        directory(str): the directory where the JSON archives are

    Returns:
        dict: a dictionary where the keys are the name of the archive (without extension)
            and the value are the load data of each archive
    '''
    print(directory)
    load_data = {}
    try:
        for filename in os.listdir(directory):
            if filename.endswith('.json'):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                        key = os.path.splitext(filename)[0]
                        load_data[key] = data
                    except json.JSONDecodeError:
                        print (f'Error al decodificar JSON en : {filename}')
    except FileNotFoundError:
        print(f'Error: El directorio "{directory}" no se ha encontrado')
    except Exception as e:
        print(f"Un error inesperado a ocurrido: {e}") # catch other errors
        #Important:  Log unexpected errors.
        return {} #Return empty dict on error
    return load_data


if __name__ == '__main__':
    os_data = os.path.join('..', 'data') #Access to 'data' directory from 'module' directory
    data = load_data(os_data)