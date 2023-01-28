from tkinter import *
import random

diccionario_preguntas = {"uno": ["pregunta 1","hint 1", "Respuesta 1"], "dos": ["pregunta 2","hint 2", "Respuesta 2"], "tres": "pregunta 3", "cuatro": "pregunta 4",
                         "cinco": "pregunta 5"}
lista_preguntas = []
raiz = Tk()
raiz.title("preguntas")


def seleccion_preguntas():
    for numero in diccionario_preguntas:
        lista_preguntas.append(numero)
    random_index = random.randint(0, len(lista_preguntas) - 1)
    # print("dentro de seleccion de preguntas")
    # print(lista_preguntas[random_index])


def preguntas():
    for numero in diccionario_preguntas:
        lista_preguntas.append(numero)
    random_index = random.randint(0, len(lista_preguntas) - 1)
    # print(lista_preguntas[random_index])
    random_index = random.randint(0, len(lista_preguntas) - 1)
    # print(diccionario_preguntas[lista_preguntas[random_index]])
    return diccionario_preguntas[lista_preguntas[random_index]]


def click_boton_pregunta():
    texto = Label(raiz, text= preguntas()).grid()

def click_boton_hint():
    texto = Label(raiz, text= preguntas()).grid()


boton_pregunta = Button(raiz, text="pregunta", padx=50, pady=25, command=click_boton_pregunta).grid(row=1, column=1)

boton_hint = Button(raiz, text="hint!", padx=50, pady=25, command=click_boton_hint).grid(row=1, column=4)

preguntas()

raiz.mainloop()