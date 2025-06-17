import os
import random

from modules.data_management import load_data

#The directory path (relative to main.py)
path_data = os.path.join(os.path.dirname(__file__),'..', 'data') #'..' go back one level
datos = load_data(path_data) #Load the data when de app is iniciated

#List with variable name
'''valoresencuentros = [airelibre, pesos_airelibre, mazmorra, pesos_mazmorra, urbanos, pesos_urbanos,
misiones, origenmision]
valoresacciones = [verbos]
valoresnpc = [razamundana, pesos_raza, razanomundana, pesos_razanomundana, profesion, pesos_profesion, 
rango, pesos_rango, novato, pesos_novato, medio, pesos_medio, avanzado, pesos_avanzado, 
estatus, pesos_estatus, alineamiento, oficio, clase, actitud, sexo]
valorestaberna = [taberna1, taberna2, taberna, tema_rumor, loc_rumor]'''

airelibre = datos['datos_encuentros']['airelibre']
pesos_airelibre = datos['datos_encuentros']['pesos_airelibre']
mazmorra = datos['datos_encuentros']['mazmorra']
pesos_mazmorra = datos['datos_encuentros']['pesos_mazmorra']
urbanos = datos['datos_encuentros']['urbanos']
pesos_urbanos = datos['datos_encuentros']['pesos_urbanos']
misiones = datos['datos_encuentros']['misiones']
origenmision = datos['datos_encuentros']['origenmision']
acciones = datos['datos_acciones']['verbos']
razamundana = datos['datos_npc']['razamundana']
pesos_raza = datos['datos_npc']['pesos_raza']
razanomundana = datos['datos_npc']['razanomundana']
pesos_razanomundana = datos['datos_npc']['pesos_razanomundana']
profesion = datos['datos_npc']['profesion']
pesos_profesion = datos['datos_npc']['pesos_profesion']
rango = datos['datos_npc']['rango']
pesos_rango = datos['datos_npc']['pesos_rango']
novato = datos['datos_npc']['novato']
pesos_novato = datos['datos_npc']['pesos_novato']
medio = datos['datos_npc']['medio']
pesos_medio = datos['datos_npc']['pesos_medio']
avanzado = datos['datos_npc']['avanzado']
pesos_avanzado = datos['datos_npc']['pesos_avanzado']
estatus = datos['datos_npc']['estatus']
pesos_estatus = datos['datos_npc']['pesos_estatus']
alineamiento = datos['datos_npc']['alineamiento']
oficio = datos['datos_npc']['oficio']
clase = datos['datos_npc']['clase']
actitud = datos['datos_npc']['actitud']
sexo = datos['datos_npc']['sexo']
taberna1 = datos['datos_taberna']['taberna1']
taberna2 = datos['datos_taberna']['taberna2']
taberna = datos['datos_taberna']['taberna']
tema_rumor = datos['datos_taberna']['tema_rumor']
loc_rumor = datos['datos_taberna']['loc_rumor']
npc_razamundana = dict(zip(razamundana, pesos_raza))
npc_razanomundana = dict(zip(razanomundana, pesos_razanomundana))
npc_profesion = dict(zip(profesion, pesos_profesion))
npc_rango = dict (zip(rango, pesos_rango))
npc_novato = dict(zip(novato, pesos_novato))
npc_medio = dict(zip(medio, pesos_medio))
npc_avanzado = dict(zip(avanzado, pesos_avanzado))
npc_estatus = dict(zip(estatus, pesos_estatus))


class Generator:
    '''
    

    Args:

    Return:
    '''
    def __init__(self, elementos=None, pesos=None, claves=None, valores=None, diccionario=None, lista=None):
        self.elementos = elementos if elementos is not None else []
        self.pesos = pesos if pesos is not None else []
        self.claves = claves if claves is not None else []
        self.valores = valores if valores is not None else []
        self.diccionario = diccionario if diccionario is not None else {}
        self.lista = lista if lista is not None else []


    def elegir_clave_ponderada(self, diccionario):
        # Creamos una lista de tuplas (clave, peso)
        pesos = [(clave, valor) for clave, valor in diccionario.items()]

        # Extraemos solo los pesos (valores numéricos)
        solo_pesos = [peso for _, peso in pesos]

        # Elegimos una clave al azar, ponderando por los pesos
        if solo_pesos:  # Check if solo_pesos is not empty
          clave_elegida = random.choices(pesos, weights=solo_pesos)[0]
          clave_elegida = clave_elegida[0]
          return clave_elegida
        else:
          return None  # Or raise an exception, or handle the empty case differently

    def elegir_lista (self, lista):
        return random.choice(lista)

    def generar_npc (self):
        npc=[]
        global npc_razamundana,sexo, npc_razanomundana
        global alineamiento
        global oficio
        global npc_profesion
        global clase
        global npc_rango
        global npc_novato
        global npc_medio
        global npc_avanzado
        global actitud
        global npc_estatus
        #Escogemos la raza del PNJ
        raza=self.elegir_clave_ponderada(npc_razamundana)
        if raza == 'Otra raza':
          raza=self.elegir_clave_ponderada(npc_razanomundana)
        npc.append(raza)
        #Escogemos el sexo del PNJ
        sex=self.elegir_lista(sexo)
        npc.append(sex)
        #Excogemos el nombre en función de la raza
        va1='nombres_'+raza.lower()+'s_'+sex.lower()+'s'
        va2='apellidos_'+raza.lower()+'s'
        try:
          names = datos['nombres'][va1]
          surname = datos['nombres'][va2]
          nombre = self.elegir_lista(names)
          apellido = self.elegir_lista(surname)
          name = f'{nombre} {apellido}'
        except:
          name ='None'
        
        #Escogemos el alineamiento
        alin=self.elegir_lista(alineamiento)
        npc.append(alin)
        #Escogemos la actitud hacia los personajes
        actit = self.elegir_lista(actitud)
        npc.append(actit)
        #Escogemos el estatus de ese PNJ
        estatus=self.elegir_clave_ponderada(npc_estatus)
        npc.append(estatus)
        #Escogemos la profesión y el nivel si fuera de una clase
        prof=self.elegir_clave_ponderada(npc_profesion)
        prof=prof
        if prof == 'Plebeyo (sin empleo)':
          npc.append(prof)
        elif prof == 'Artesano / comerciante / profesional (tira en la tabla de oficios)':
          prof=self.elegir_lista(oficio)
          npc.append(prof)
        elif prof == 'Aventurero (Tira en la tabla de clases y niveles)':
          prof=self.elegir_lista(clase)
          npc.append(prof)
          rango=self.elegir_clave_ponderada(npc_rango)
          rango=rango
          if rango == 'Novato 1-5':
            rango = self.elegir_clave_ponderada(npc_novato)
          elif rango == 'Medio 6-15':
            rango = self.elegir_clave_ponderada(npc_medio)
          else:
            rango = self.elegir_clave_ponderada (npc_avanzado)
          npc.append(rango)
        # Convertir la lista a una cadena con formato
        #npc_str = f'Raza: {npc[0]}\nSexo: {npc[1]}\nAlineamiento: {npc[2]}\nActitud: {npc[3]} (Agregue el modificador de Carisma / Persuasión / Engaño / Intimidación / Actuación correspondiente según la situación).\nEstatus: {npc[4]}\nProfesión: {npc[5]}'
        npc_str = f"""
Nombre: {name}
Raza: {npc[0]}
Sexo: {npc[1]}
Alineamiento: {npc[2]}
Actitud: {npc[3]} (Agregue el modificador de Carisma / Persuasión / Engaño / Intimidación / Actuación correspondiente según la situación).
Estatus: {npc[4]}
Profesión: {npc[5]}
"""
        if len(npc) > 6: # Verifica si hay un rango
          npc_str += f"Nivel: {npc[-1]}"

        return npc_str

    def taberna(self):
        taberna01=[]
        for clave in taberna: #Por cada clave del diccionario taberna
          #Escogemos un elemento de la lista de cada uno de los elementos del diccionario
          valores=taberna.get(clave)  #Seleccionamos los valores perteneciente a la clave del diccionario taberna
          valor= self.elegir_lista(valores) #Se escoge un elemento de la lista de valores
          taberna01.append(valor)
        print (taberna01)
        rumor1=[]
        rumor01=[]
        if taberna01[3] != '0':
          for i in range(0,eval(taberna01[3])):
            rumor1.append(self.elegir_lista(tema_rumor))
            rumor01.append(self.elegir_lista(loc_rumor))

        posada = f'''
Número de habitaciones: {taberna01[0]}
Calidad del alojamiento: {taberna01[1]}
Raza del Tabernero: {taberna01[2]}
Nº Rumores: {taberna01[3]}
Calidad del servicio: {taberna01[4]}
Tema del rumor: {rumor1}
Localización del rumor:  {rumor01}
        '''
        #Imprimimos un tema y una localización por cada uno de los posibles rumores que haya en la taberna.
        for i in range(0,len(rumor1)):
          posada += f'''
Tema del rumor: {rumor1[i]}
Localización del rumor:  {rumor01[i]}
          '''
        return posada