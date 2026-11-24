def leer_texto():
    with open("prueba.txt","r", encoding="UTF-8") as archivo:
        texto = archivo.read()
        return texto
        
def conteo_pal_char(texto):
    palabras = len(texto.split())
    char_esp = len(texto)
    char_sinesp = len(texto.replace(" ",""))
    
    return ( f"Palabras: {palabras} | "
            f"Caracteres (con espacios): {char_esp} | "
            f"Caracteres (sin espacios): {char_sinesp}"
            )

print(conteo_pal_char(leer_texto()))
    


