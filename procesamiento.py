from limpieza import texto_limpio


def conteo_pal(texto: str) -> int:
    no_palabras = len(texto.split())
    return no_palabras

def conteo_char_esp(texto: str) -> int:
    char_esp = len(texto)
    return char_esp

def conteo_char_noesp(texto: str) -> int:
    char_sinesp = len(texto.replace(" ",""))
    return char_sinesp
    
def conteo_oraciones(texto: str) -> int:
    oraciones = 0
    for char in texto:
        if char in "!.?":
            oraciones += 1
    return oraciones

def prom_pal(texto: str) -> float:
    palabras = texto_limpio(texto).split()
    caracteres = 0
    for palabra in palabras:
        caracteres += len(palabra)
    prom_p = caracteres / len(palabras)
    return  round(prom_p,2)

def prom_orac(texto: str) -> float:
    palabras = texto.split()
    oraciones = conteo_oraciones(texto)
    prom_o = len(palabras) / oraciones
    return round(prom_o,2)
    





