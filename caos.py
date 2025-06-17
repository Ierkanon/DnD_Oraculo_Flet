'''tabla_caos = {
    "Imposible": {1: -10, 2: -10, 3: -10, 4: -10, 5: -10, 6: -8, 7: -7, 8: -5, 9: 0},
    "Casi Imposible": {1: -10, 2: -9, 3: -9, 4: -8, 5: -8, 6: -5, 7: -3, 8: 0, 9: 5},
    "Muy Improbable": {1: -9, 2: -8, 3: -7, 4: -6, 5: -5, 6: -3, 7: 0, 8: 3, 9: 7},
    "Improbable": {1: -9, 2: -8, 3: -7, 4: -6, 5: -3, 6: 0, 7: 1, 8: 5, 9: 8},
    "50/50": {1: -8, 2: -7, 3: -5, 4: -3, 5: 0, 6: 3, 7: 5, 8: 7, 9: 9},
    "Probable": {1: -6, 2: -5, 3: -3, 4: 0, 5: 3, 6: 6, 7: 7, 8: 8, 9: 9},
    "Muy Probable": {1: -5, 2: -3, 3: 0, 4: 1, 5: 5, 6: 7, 7: 8, 8: 9, 9: 10},
    "Esperado": {1: -1, 2: 0, 3: 1, 4: 3, 5: 5, 6: 8, 7: 9, 8: 10, 9: 10},
    "Seguro": {1: 0, 2: 1, 3: 3, 4: 5, 5: 6, 6: 8, 7: 10, 8: 10, 9: 10},
    "Dado de Caos": {1: "d4", 2: "d4", 3: "d6", 4: "d6", 5: "d8", 6: "d8", 7: "d10", 8: 'd12', 9: "d20"},
    "Nivel de Caos": {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
}
'''

import os
import random

from modules.data_management import load_data

'''#The directory path (relative to main.py)
path_data = os.path.join(os.path.dirname(__file__), 'data') #'..' go back one level
datos = load_data(path_data)  # Load the data when de app is iniciated
'''

class Caos:
    '''
    This class is a Caos Oracule for a DnD 5
    
    Attributes:
        ncaos = is the level of caos in that moment, the first caos level is 5
        clave1 = is the level of probability
        clave2 = is the level of caos
        [description]: [description]
    ''' 
    def __init__(self, clave1, ncaos, datos, tipevento):
        self.clave1 = ''
        self.ncaos = ''
        self.datos = datos
        self.tipevento = tipevento


    def oraculo_bonus(self, clave1, ncaos, datos):
        '''Give the bonus value
        
        Search in a dictionary the bonus for a especific level of caos
        
        Args:
            clave1 (string): the probability of al action
            ncaos (string): level of caos 
            datos ([dictionary]): dictionary with all the Key-value data
        
        Returns:
            [int]: a especific bonus value for a level of caos and probability.
        '''
        self.dcaos = self.datos ['Dado de Caos'][ncaos]
        self.bonus = self.datos [clave1][ncaos]
        return self.bonus

    def caos_dice(self, ncaos):
        '''[summary]
        
        [description]
        
        Args:
            ncaos (string): level of caos

        Returns:
            [int]: return a int, it is the dice for a specific caos level
        '''
        self.dcaos = self.datos ['Dado de Caos'][ncaos]
        self.dcaos = self.dcaos.replace('d','')
        self.dcaos = int(self.dcaos)
        return self.dcaos

    def evento(self, tipevento):
        '''[summary]
        
        [description]
        
        Args:
            datos (dict): the data of the dict evento_negativo or evento_neutral_positivo
            tipoevento (str): evento_negativo or evento_neutral_positivo

        Returns:
            [str]
        '''
        self.num = random.randint(1,20)
        self.event = tipevento[str(self.num)]
        return self.event


if __name__ == '__main__':
    #The directory path (relative to main.py)
    path_data = os.path.join(os.path.dirname(__file__), 'data') #'..' go back one level
    datos = load_data(path_data)  # Load the data when de app is iniciatedn
    oraculo_caos = datos['oraculo_caos'] #Dictionary what contains the oracle data
    evento_negativo = datos['evento_negativo'] #Dictionary what contains the negative_events
    evento_neutral_positivo = datos ['evento_neutral_positivo'] #Dictionary what contains the neutral_positive_events
    tirada_de_caos = datos['tirada_de_caos'] #Dictionary what contains the caos_roll
    nivelcaos = str(7)
    prob = Caos('50/50',nivelcaos, oraculo_caos, tirada_de_caos)
    resultado = prob.evento(evento_neutral_positivo)

