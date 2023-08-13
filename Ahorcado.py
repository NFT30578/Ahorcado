import random

def seleccionar_palabra(lista_de_palabras):
  """Selecciona una palabra al azar de la lista de palabras"""
  return random.choice(lista_de_palabras)

def mostrar_estado(palabra_seleccionada, letras_acertadas, intentos_jugador):
  """Muestra el estado actual del juego"""
  print("+--"*8 + "+")
  print("Intentos restantes: ", intentos_jugador)
  print("Letras acertadas: ", letras_acertadas)
  print()
  palabra_mostrada = ""
  for letra in palabra_seleccionada:
      if letra in letras_acertadas:
          palabra_mostrada += letra
      else:
          palabra_mostrada += "_"
  print("Palabra: ", palabra_mostrada)
  print("+--"*8 + "+\n")
  print()
  return palabra_mostrada

def pedir_letra():
  """Pide al jugador que ingrese una letra"""
  return input("Ingresa una letra:\n")

def verificar_letra(letra_ingresada, palabra_seleccionada, letras_acertadas, intentos_jugador):
  """Verifica si la letra ingresada está en la palabra seleccionada"""
  if letra_ingresada in palabra_seleccionada:
      letras_acertadas.append(letra_ingresada)
      print("¡Correcto!\n")
  else:
      intentos_jugador -= 1
      print("¡Incorrecto!")
  return letras_acertadas, intentos_jugador

def volver_a_jugar():
  """Pregunta al jugador si quiere volver a jugar"""
  print("¿Quieres volver a jugar?:")
  print()
  respuesta = input("1.- Si  2.- No\n")
  return respuesta == "1"

def jugar_ahorcado(lista_de_palabras):
  """Ejecuta el juego del ahorcado"""
  palabra_seleccionada = seleccionar_palabra(lista_de_palabras)
  intentos_jugador = len(palabra_seleccionada)
  letras_acertadas = []
  while True:
    # Mostrar el estado actual del juego
    palabra_mostrada = mostrar_estado(palabra_seleccionada, letras_acertadas, intentos_jugador)
    # Pedir al jugador que ingrese una letra
    letra_ingresada = pedir_letra()
    # Verificar si la letra está en la palabra
    letras_acertadas, intentos_jugador = verificar_letra(letra_ingresada, palabra_seleccionada, letras_acertadas, intentos_jugador)
    # Verificar si el jugador ha ganado o perdido
    if "_" not in palabra_mostrada:
      print("¡FELICIDADES! Has ganado\n")
      if volver_a_jugar():
          jugar_ahorcado(lista_de_palabras)
      break
    elif intentos_jugador == 0:
      print("¡HAS PERDIDO!. La palabra era:", palabra_seleccionada)
      if volver_a_jugar():
          jugar_ahorcado(lista_de_palabras)
      break

# Lista de palabras
lista_de_palabras = ["elefante","jirafa","hipopotamo","serpiente","cocodrilo","avestruz","rinoceronte","ballena","tiburon","caracol","pajaro","murcielago","pantera","jaguar","termita","escarabajo","escorpion","alacran","mantarraya","anguila","halcon","hormiga","saltamontes","grillo","avispa","mariposa","marmota","nutria"]

# Iniciar el juego
jugar_ahorcado(lista_de_palabras)