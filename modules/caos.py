import random
from random import randint

probabilidades_caos = {
    "Imposible": {"d4": -10, "d6": -10, "d8": -8, "d10": -7, "d12": -5, "d20": 0},
    "Casi Imposible": {"d4": -9, "d6": -8, "d8": -5, "d10": -3, "d12": 0, "d20": 5},
    "Muy Improbable": {"d4": -8, "d6": -6, "d8": -3, "d10": 0, "d12": 3, "d20": 7},
    "Improbable": {"d4": -8, "d6": -6, "d8": -3, "d10": 1, "d12": 5, "d20": 8},
    "50/50": {"d4": -7, "d6": -3, "d8": 0, "d10": 5, "d12": 7, "d20": 9},
    "Probable": {"d4": -5, "d6": 0, "d8": 3, "d10": 7, "d12": 8, "d20": 9},
    "Muy Probable": {"d4": -3, "d6": 1, "d8": 5, "d10": 8, "d12": 9, "d20": 10},
    "Esperado": {"d4": 0, "d6": 3, "d8": 5, "d10": 9, "d12": 10, "d20": 10},
    "Seguro": {"d4": 1, "d6": 5, "d8": 6, "d10": 10, "d12": 10, "d20": 10},
    "Dado de Caos": {"1": "d4", "2": "d4", "3": "d6", "4": "d6", "5": "d8", "6": "d8", "7": "d10", "8": "d12", "9": "d20"},
    "Nivel de Caos": {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
}

niveles_caos = {
    1: 4,
    2: 4, 
    3: 6,
    4: 6,
    5: 8, 
    6: 8,
    7: 10,
    8: 12,
    9: 20
}

efectos_caos = {
    1: "La escena sucede como estaba planeada",
    2: "La escena sucede como estaba planeada", 
    3: "La escena sucede como estaba planeada",
    4: "Pequeño cambio en la escena",
    5: "Quita algo de la escena",
    6: "Crea algo en la escena",
    7: "Evento negativo",
    8: "Evento neutral/positivo",
    9: "Evento negativo antes de la escena planeada",
    10: "Evento neutral/positivo antes de la escena planeada",
    11: "Algo no era lo que se imaginaba o no será como se esperaba",
    12: "Cambio en el comportamiento de PNJ o sentimiento de PJ",
    13: "Pequeño cambio en la escena",
    14: "Quitar algo de la escena",
    15: "Crear algo en la escena",
    16: "Evento negativo",
    17: "Evento neutral/positivo",
    18: "Algo no era lo que se imaginaba o no será como se esperaba",
    19: "Evento negativo antes de la escena planeada",
    20: "Evento neutral/positivo antes de la escena planeada"
}

# Diccionario que mapea resultados de d20 con enfoques de eventos negativos
evento_negativo = {
    1: "Combate. Haz un encuentro de combate. Puede ser balanceado o no balanceado, o incluso un encuentro aleatorio.",
    2: "Combate. Haz un encuentro de combate. Puede ser balanceado o no balanceado, o incluso un encuentro aleatorio.",
    3: "Combate. Haz un encuentro de combate. Puede ser balanceado o no balanceado, o incluso un encuentro aleatorio.",
    4: "Combate. Haz un encuentro de combate. Puede ser balanceado o no balanceado, o incluso un encuentro aleatorio.",
    5: "Combate. Haz un encuentro de combate. Puede ser balanceado o no balanceado, o incluso un encuentro aleatorio.",
    6: "Combate. Haz un encuentro de combate. Puede ser balanceado o no balanceado, o incluso un encuentro aleatorio.",
    7: "Combate. Haz un encuentro de combate. Puede ser balanceado o no balanceado, o incluso un encuentro aleatorio.",
    8: "Objetivo negativo. Elige o determina aleatoriamente un objetivo, tira una Idea e interpreta.",
    9: "Objetivo negativo. Elige o determina aleatoriamente un objetivo, tira una Idea e interpreta.",
    10: "Objetivo negativo. Elige o determina aleatoriamente un objetivo, tira una Idea e interpreta.",
    11: "PNJ negativo. Elige o determina aleatoriamente un PNJ negativo, tira una Idea e interpreta.",
    12: "PNJ negativo. Elige o determina aleatoriamente un PNJ negativo, tira una Idea e interpreta.",
    13: "PNJ negativo. Elige o determina aleatoriamente un PNJ negativo, tira una Idea e interpreta.",
    14: "PNJ negativo. Elige o determina aleatoriamente un PNJ negativo, tira una Idea e interpreta.",
    15: "PJ negativo. Elige o determina aleatoriamente un PJ negativo, tira una Idea e interpreta.",
    16: "PJ negativo. Elige o determina aleatoriamente un PJ negativo, tira una Idea e interpreta.",
    17: "PJ negativo. Elige o determina aleatoriamente un PJ negativo, tira una Idea e interpreta.",
    18: "Instigar. Elige o determina aleatoriamente un PJ, analiza vínculos, defectos y alineamiento, tira una idea (opcional) e interpreta. Tirada de salvación SAB, INT o CAR CD 20 para no ceder.",
    19: "Transfondo negativo. Elige o determina aleatoriamente un PNJ, analiza su trasfondo, tira una Idea e interpreta.",
    20: "Objeto mágico negativo. Inventa, elige o determina aleatoriamente un objeto mágico, tira una Idea e interpreta."
}

# Diccionario que mapea resultados de d20 con enfoques de eventos neutrales/positivos
evento_positivo = {
    1: "Evento remoto. Tira una Idea e interpreta.",
    2: "Evento remoto. Tira una Idea e interpreta.",
    3: "Evento ambiguo. Tira una Idea e interpreta.",
    4: "Evento ambiguo. Tira una Idea e interpreta.",
    5: "Nuevo PNJ. Introduce un nuevo PNJ",
    6: "Nuevo PNJ. Introduce un nuevo PNJ",
    7: "Acción de PNJ. Elige o determina aleatoriamente un PNJ, tira una Idea e interpreta.",
    8: "Acción de PNJ. Elige o determina aleatoriamente un PNJ, tira una Idea e interpreta.",
    9: "Acción de PNJ. Elige o determina aleatoriamente un PNJ, tira una Idea e interpreta.",
    10: "Acción de PNJ. Elige o determina aleatoriamente un PNJ, tira una Idea e interpreta.",
    11: "Acción de PNJ. Elige o determina aleatoriamente un PNJ, tira una Idea e interpreta.",
    12: "Acción de PNJ. Elige o determina aleatoriamente un PNJ, tira una Idea e interpreta.",
    13: "Acción de PNJ. Elige o determina aleatoriamente un PNJ, tira una Idea e interpreta.",
    14: "Acción de PNJ. Elige o determina aleatoriamente un PNJ, tira una Idea e interpreta.",
    15: "PNJ positivo. Elige o determina aleatoriamente un PNJ, tira una Idea e interpreta.",
    16: "PJ positivo. Elige o determina aleatoriamente un PJ, tira una Idea e interpreta.",
    17: "Transfondo positivo. Elige o determina aleatoriamente un PNJ, analiza su trasfondo, tira una Idea e interpreta.",
    18: "Objeto mágico positivo. Inventa, elige o determina aleatoriamente un objeto mágico, tira una Idea e interpreta.",
    19: "Objetivo positivo. Elige o determina aleatoriamente un objetivo, tira una Idea e interpreta.",
    20: "Objetivo positivo. Elige o determina aleatoriamente un objetivo, tira una Idea e interpreta."
}

chequeo_destino = {
    1: "No crítico",
    2: "No",
    3: "No",
    4: "No",
    5: "No",
    6: "No",
    7: "Evento neutral/positivo",
    8: "No",
    9: "No",
    10: "No débil",
    11: "Sí débil",
    12: "Sí",
    13: "Evento negativo",
    14: "Sí",
    15: "Sí",
    16: "Sí",
    17: "Sí",
    18: "Sí",
    19: "Sí",
    20: "Sí crítico"
}

'''class Caos:
    def __init__(self, dado, cl):
        self.dado_de_caos = 4
        self.nivel_caos = cl
        self.dado = 20
        self.tirada = 0

    #Method to obtain the level and dice caos
    def dado_caos(self, self.nivel_caos):
        global niveles_caos
        self.dado_de_caos = self.niveles_caos.get(nivel_caos)

    #Function to obtain the caos effect    
    def obtener_efectos_caos (self, self.dado_de_caos):
        global efectos_caos
        self.roll(self.dado_de_caos)
        return efectos_caos.get(self.tirada)

    #Function to obtain a negative event
    def obtener_evento_negativo (self):
        global evento_negativo
        self.roll(20)
        return evento_negativo.get(self.tirada)

    #Function to obtain a possitive event
    def obtener_evento_positivo (self):
        global evento_positivo
        self.roll(20)
        return evento_positivo.get(self.tirada)

    def roll (self, self.dado):
        self.tirada = randint(1,self.dado)
        return self.tirada

    #Oracle with d20 caos
    def oracle(self):
        global chequeo_destino
        self.roll(20)
        self.chequeo = chequeo_destino.get(self.tirada)
        if self.dado == 7:
            evento = self.obtener_evento_positivo()
        elif self.dado == 13:
            evento = self.obtener_evento_negativo()'''

class Caos:
    def __init__(self, nivel_caos, probabilidad):
        """
        Inicializa la clase Caos con un nivel específico.
        
        Args:
            nivel_caos (int): Nivel de caos entre 1 y 9
        """
        if not isinstance(nivel_caos, int) or nivel_caos < 1 or nivel_caos > 9:
            raise ValueError("El nivel de caos debe ser un entero entre 1 y 9")
            
        self.nivel_caos = nivel_caos
        self.probabilidad = probabilidad
        self.dado_de_caos = self._obtener_dado_caos()
        self.tirada = 0
        self.ultima_tirada = None
        self.bonificador = self.probabilidad_caos(dado_de_caos, probabilidad)

    def _obtener_dado_caos(self):
        """Obtiene el tipo de dado correspondiente al nivel de caos"""
        return niveles_caos.get(self.nivel_caos, 4)

    def roll(self, dado):
        """
        Realiza una tirada de dado
        
        Args:
            dado (int): Número de caras del dado
            
        Returns:
            int: Resultado de la tirada
        """
        if dado < 1:
            raise ValueError("El dado debe ser mayor a 0")
            
        self.tirada = randint(1, dado)
        self.ultima_tirada = {"dado": dado, "resultado": self.tirada}
        return self.tirada

    def probabilidad_caos (self, dado_de_caos, probabilidad):
        """
        Obtiene según la probabilidad y el dado de caos un bonificador para las tiradas de dificultad
         de los eventos

        Returns:
            int: bonificador a la dificultad de los eventos
        """
        self.bonificador = probabilidades_caos[self.probabilidad][self.dado_de_caos]
        return self.bonificador

    def obtener_efecto_caos(self):
        """
        Obtiene el efecto de caos basado en el nivel actual
        
        Returns:
            dict: Diccionario con el efecto y detalles de la tirada
        """
        resultado = self.roll(self.dado_de_caos)
        efecto = efectos_caos.get(resultado, "Efecto desconocido")
        
        return {
            "tirada": resultado,
            "dado_usado": f"d{self.dado_de_caos}",
            "nivel_caos": self.nivel_caos,
            "efecto": efecto
        }

    def obtener_evento_negativo(self):
        """
        Obtiene un evento negativo aleatorio
        
        Returns:
            dict: Diccionario con el evento negativo y detalles
        """
        resultado = self.roll(20)
        evento = evento_negativo.get(resultado, "Evento desconocido")
        
        return {
            "tirada": resultado,
            "tipo": "Evento Negativo",
            "descripcion": evento
        }

    def obtener_evento_positivo(self):
        """
        Obtiene un evento positivo aleatorio
        
        Returns:
            dict: Diccionario con el evento positivo y detalles
        """
        resultado = self.roll(20)
        evento = evento_positivo.get(resultado, "Evento desconocido")
        
        return {
            "tirada": resultado,
            "tipo": "Evento Positivo",
            "descripcion": evento
        }

    def oracle(self):
        """
        Realiza una consulta al oráculo del destino
        
        Returns:
            dict: Resultado del oráculo con posibles eventos adicionales
        """
        resultado = self.roll(20)
        chequeo = chequeo_destino.get(resultado, "Resultado desconocido")
        
        respuesta = {
            "tirada": resultado,
            "resultado oráculo": chequeo,
            "evento adicional": None
        }
        
        # Verificar si se activan eventos especiales
        if resultado == 7:  # Evento neutral/positivo
            respuesta["evento_adicional"] = self.obtener_evento_positivo()
        elif resultado == 13:  # Evento negativo
            respuesta["evento_adicional"] = self.obtener_evento_negativo()
            
        return respuesta

    def cambiar_nivel_caos(self, nuevo_nivel):
        """
        Cambia el nivel de caos actual
        
        Args:
            nuevo_nivel (int): Nuevo nivel de caos entre 1 y 9
        """
        if not isinstance(nuevo_nivel, int) or nuevo_nivel < 1 or nuevo_nivel > 9:
            raise ValueError("El nivel de caos debe ser un entero entre 1 y 9")
            
        self.nivel_caos = nuevo_nivel
        self.dado_de_caos = self._obtener_dado_caos()

    def obtener_info_nivel(self):
        """
        Obtiene información sobre el nivel actual de caos
        
        Returns:
            dict: Información del nivel actual
        """
        return {
            "nivel": self.nivel_caos,
            "dado": f"d{self.dado_de_caos}",
            "descripcion": f"Nivel {self.nivel_caos} usa un d{self.dado_de_caos}"
        }

    def __str__(self):
        return f"Caos(nivel={self.nivel_caos}, dado=d{self.dado_de_caos})"

    def __repr__(self):
        return self.__str__()


# Ejemplo de uso
'''if __name__ == "__main__":
    # Crear instancia de caos
    caos = Caos(6)
    print(f"Sistema de caos iniciado: {caos}")
    print(f"Info del nivel: {caos.obtener_info_nivel()}")
    
    # Probar efecto de caos
    print("\n--- Efecto de Caos ---")
    efecto = caos.obtener_efecto_caos()
    print(f"Resultado: {efecto}")
    
    # Probar oráculo
    print("\n--- Oráculo ---")
    oracle_result = caos.oracle()
    print(f"Oráculo: {oracle_result}")
    
    # Cambiar nivel y probar de nuevo
    print("\n--- Cambio de Nivel ---")
    caos.cambiar_nivel_caos(9)
    print(f"Nuevo nivel: {caos.obtener_info_nivel()}")
    efecto2 = caos.obtener_efecto_caos()
    print(f"Nuevo efecto: {efecto2}")'''