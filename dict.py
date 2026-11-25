
def texto_limpio(texto: str) -> str:
    texto_min = texto.lower()
    texto_limp = texto_min
    for i in texto_min: 
        if i in ",.:;¡!¿?":
            texto_limp = texto_limp.replace(i, "")
    return texto_limp


stop_words = 