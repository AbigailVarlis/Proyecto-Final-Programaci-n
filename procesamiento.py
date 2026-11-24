with open("prueba.txt","r") as archivo:
    texto = archivo.read()
        
def conteo_pal_char(texto):
    palabras = len(texto.split())
    char_esp = len(texto)
    char_sinesp = len(texto.replace(" ",""))
    
    return ( f"Palabras: {palabras} | "
            f"Caracteres (con espacios): {char_esp} | "
            f"Caracteres (sin espacios): {char_sinesp}" )

def conteo_oraciones(texto):
    oraciones = 0
    for char in texto:
        if char in "!.?":
            oraciones += 1
    return f"Oraciones: {oraciones}"

    

print(conteo_oraciones(texto))
    


