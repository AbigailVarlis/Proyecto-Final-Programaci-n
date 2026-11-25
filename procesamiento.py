import auxiliar

ruta = auxiliar.seleccionar_archivo()

with open(ruta,"r") as file:
    texto = file.read()

def texto_limpio(texto: str) -> str:
    texto_min = texto.lower()
    texto_limp = texto_min
    for i in texto_min: 
        if i in ",.:;¡!¿?":
            texto_limp = texto_limp.replace(i, "")
    return texto_limp

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

def prom_pal(texto: str) -> int:
    palabras = texto_limpio(texto).split()
    caracteres = 0
    for palabra in palabras:
        caracteres += len(palabra)
    prom_p = caracteres / len(palabras)
    return  round(prom_p,2)

def prom_orac(texto: str) -> int:
    palabras = texto.split()
    oraciones = conteo_oraciones(texto)
    prom_o = len(palabras) / oraciones
    return round(prom_o,2)
    

print( f"Total de palabras: {conteo_pal(texto)}\n"
    f"Caracteres con espacios: {conteo_char_esp(texto)}\n"
    f"Caracteres sin espacios: {conteo_char_noesp(texto)}\n"
    f"Total de oraciones: {conteo_oraciones(texto)}\n"
    f"Longitud promedio de palabra: {prom_pal(texto)}\n"
    f"Longitud promedio de oración: {prom_orac(texto)}" )
    





