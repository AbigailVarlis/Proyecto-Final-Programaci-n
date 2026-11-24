import auxiliar
ruta = auxiliar.seleccionar_archivo()

with open(ruta,"r") as file:
    texto = file.read()

        
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
    palabras = texto.split()
    caracteres = 0
    for palabra in palabras:
        for i in palabra:
            palabra_limpia = palabra
            if i in ".,:,¡!¿?":
                palabra_limpia = palabra_limpia.replace(i,"")
            caracteres += len(palabra_limpia)
    prom_p = caracteres // len(palabras)
    return prom_p

def prom_orac(texto: str) -> int:
    palabras = texto.split()
    oraciones = conteo_oraciones(texto)
    prom_o = len(palabras) // oraciones
    return prom_o
    

print( f"Total de palabras: {conteo_pal(texto)}\n"
    f"Caracteres con espacios: {conteo_char_esp(texto)}\n"
    f"Caracteres sin espacios: {conteo_char_noesp(texto)}\n"
    f"Total de oraciones: {conteo_oraciones(texto)}\n"
    f"Longitud promedio de palabra: {prom_pal(texto)}\n"
    f"Longitud promedio de oración: {prom_orac(texto)}" )
    


    


