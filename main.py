from tkinter import *
import random

diccionario_preguntas = {"uno": "pregunta 1", "dos": "pregunta 2", "tres": "pregunta 3", "cuatro": "pregunta 4",
                         "cinco": "pregunta 5"}
lista_preguntas = []
raiz = Tk()
raiz.title("preguntas")


def seleccion_preguntas():
    for numero in diccionario_preguntas:
        lista_preguntas.append(numero)
    random_index = random.randint(0, len(lista_preguntas) - 1)
    print("dentro de seleccion de preguntas")
    print(lista_preguntas[random_index])


def preguntas():
    for numero in diccionario_preguntas:
        lista_preguntas.append(numero)
    random_index = random.randint(0, len(lista_preguntas) - 1)
    print(lista_preguntas[random_index])
    random_index = random.randint(0, len(lista_preguntas) - 1)
    print(diccionario_preguntas[lista_preguntas[random_index]])
    return diccionario_preguntas[lista_preguntas[random_index]]


def click_boton():
    texto = Label(raiz, text= preguntas()).grid()


boton1 = Button(raiz, text="aqui esta el boton", padx=100, pady=25, command=click_boton).grid(row=1, column=2)

preguntas()

raiz.mainloop()