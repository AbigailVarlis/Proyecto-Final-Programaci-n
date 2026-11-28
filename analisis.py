


polaridad = { # Positivas
    "excelente": 3, "increíble": 3, "fantástico": 3, "maravilloso": 3,
    "perfecto": 3, "genial": 3, "fascinante": 3, "gratificante": 3,
    "amo": 3, "encanta": 3,"bueno": 2, "bonito": 2, "feliz": 2, "útil": 2, 
    "agradable": 2, "claro": 2, "versátil": 2, "poderoso": 2, "gran": 2, "mejor": 2,
    "disfrutar": 2, "gracias": 2, "recomiendo": 2, "éxito": 2,
    "bien": 1, "fácil": 1, "interesante": 1, "correcto": 1, "seguro": 1,

    # Negativas
    "horrible": -3, "terrible": -3, "pésimo": -3, "asqueroso": -3,
    "desastre": -3, "fracaso": -3, "detesto": -3, "basura": -3,
    "malo": -2, "feo": -2, "triste": -2, "molesto": -2, "frustrante": -2,
    "decepcionante": -2, "error": -2, "fallo": -2, "peor": -2, "odio": -2,
    "inútil": -2, "miedo": -2, "difícil": -1, "problema": -1, "lento": -1, "caro": -1,
    "aburrido": -1, "confuso": -1, "complicado": -1,
    }

def polaridad(texto: str) -> str :
    puntaje = 0
    if palabra in 