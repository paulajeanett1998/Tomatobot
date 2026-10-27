#En esta clase se utiliza NLTK la cual es una librería que se utiliza para el
#preprocesamiento del lenguaje natural

#Unicode data proporciona acceso a la base de datos de caracteres unicode
#wordpunct es una función de la biblioteca NLTK que separa un texto en palabras-
#y signos de puntuación
import unicodedata
from nltk.tokenize import wordpunct_tokenize

class ProcesadorTexto:

 #Se convierte la cadena de caracteres a minúscula para que todos los caracteres-
#tengan el mismo formato

    def normalizar(self, cadena):
        cadena = cadena.lower()
        cadena = unicodedata.normalize("NFD", cadena)

        cadena = "".join(
            caracter
            for caracter in cadena
            if unicodedata.category(caracter)!="Mn"
        )

        return cadena

#Se utiliza el método de wordpunct_tokenize para extrar los tokens de una cade-
#na de strings en forma de caracteres
    def tokenizar(self, cadena):
        cadena = self.normalizar(cadena)
        tokens = wordpunct_tokenize(cadena)
        return tokens

    def filtrar_sw(self, token):
        stopwords = [
            "el", "la", "los", "las",
            "un", "una", "unos, unas",
            "a", "al", "de", "del", "te",
            "y", "en", "por", "para",
            "como", "hago", "mi", "que",
            "cuales", "cual", "es", "son",
            "estas", "este", "esto", "esta",
            "estoy", "tu", "tus", "yo", "me"
        ]
        
        tokens_filtrados = [
           palabra
           for palabra in token
           if palabra not in stopwords
        ]

        return tokens_filtrados