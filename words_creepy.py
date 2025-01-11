meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "OMG": "Expresión de asombro",
            "NASHE": "Algo asombroso o divertido está pasando",
            "WTF": "¿Qué carajos?",
            "Aesthetic": "Expresión usada para definir cierto estilo",
            "GRWM": "Expresión usada para: Alistate conmigo",
            "NEA": "Persona con corte de cabello el 7",
            "BRUH": "Expresión usada para cualquier cosa",
            "GG": "Great Game",
            "SHIPPEAR": "Juntar a dos personas o personajes en un romance",
            "PRIME": "Persona que se encuentra en el mejor punto de su carrera o existencia",
            "HYPE": "Es la emoción que se siente ante algo",
            "F": "Indicar penas en una situación lamentable"
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print("Aquí tienes el significado de tu palabra", meme_dict[word])
else:
    print("No se encuentra esa palabra")
