import unicodedata

class IdentificarIntenciones:

  def __init__(self, intenciones, procesador):
      self.intenciones = intenciones
      self.procesador = procesador

  def identificar(self, mensaje):
      tokens_usuario = self.procesador.tokenizar(mensaje)
      tokens_usuario = self.procesador.filtrar_sw(tokens_usuario)

      mejor_intencion = None
      mejor_puntaje = 0

      for intencion in self.intenciones:
          puntaje = 0

          for ejemplo in intencion.ejemplo:
              tokens_ejemplo = self.procesador.tokenizar(ejemplo)
              tokens_ejemplo = self.procesador.filtrar_sw(tokens_ejemplo)

              coincidencias = set(tokens_usuario) & set(tokens_ejemplo)
              puntaje_actual = len(coincidencias)
              
              if puntaje_actual > puntaje:
                  puntaje = puntaje_actual
             

          if puntaje > mejor_puntaje:
             mejor_puntaje = puntaje
             mejor_intencion = intencion

      if mejor_puntaje <2:
          return None
    
      return mejor_intencion