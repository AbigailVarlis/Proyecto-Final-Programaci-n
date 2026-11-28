   
stop_words = {"el","la","y","en","a","de","ni","o","u","los","las","sino",
              "que","pero","más","muy","es","un","para","con","sin","son","una",
              "uno","por","al","del","se","su","sus","lo","embargo","hay","cada"}

def texto_limpio(texto: str) :
    texto_min = texto.lower()
    texto_limp = texto_min
    for i in texto_min: 
        if i in ",.:;¡!¿?()":
            texto_limp = texto_limp.replace(i, "")
    return texto_limp


def filtrado_stopwords(texto: str) :
    tokens = texto_limpio(texto).split()
    filtrado = []
    for token in tokens:
        if token not in stop_words:
            filtrado.append(token)
    return filtrado



def frec_pal(texto: str) :
    pal_frec = {}
    for palabra in filtrado_stopwords(texto):
        if palabra in pal_frec:
            pal_frec[palabra] += 1
        else:
            pal_frec[palabra] = 1
    return pal_frec

def ttr(texto: str) :
    total_pal = len(filtrado_stopwords(texto))
    TTR = len(frec_pal(texto)) / total_pal 
    return round(TTR,2)
    

def top5_pal(texto: str) :
    frecuencias = frec_pal(texto)
    frecuencias_orden = sorted(frecuencias,key=frecuencias.get,reverse=True)
    texto_final = "Top 5 de palabras más frecuentes:\n"
    for palabra in frecuencias_orden[:5]:
        texto_final += "\t" + str(palabra) + " -> " + str(frecuencias[palabra]) + "\n"
    
    return texto_final

