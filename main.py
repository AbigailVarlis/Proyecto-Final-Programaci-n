import auxiliar
import limpieza
import procesamiento
import analisis
ruta = auxiliar.seleccionar_archivo()

if ruta is None:
    print("No se seleccionó ningún archivo.")
else:
    with open(ruta,"r",encoding="utf-8") as file:
        texto = file.read()
    sentimiento, puntaje = analisis.polaridades(texto)  
    print(f"Total de palabras: {procesamiento.conteo_pal(texto)}\n"
              f"Caracteres con espacios: {procesamiento.conteo_char_esp(texto)} | Sin espacios: {procesamiento.conteo_char_noesp(texto)}\n"
              f"Total de oraciones: {procesamiento.conteo_oraciones(texto)}\n"
              f"Longitud promedio de palabra: {procesamiento.prom_pal(texto)}\n"
              f"Longitud promedio de oración: {procesamiento.prom_orac(texto)}\n"
              f"TTR: {limpieza.ttr(texto)}\n"
              f"{limpieza.top5_pal(texto)}"
              f"Sentimiento: {sentimiento} | Puntaje acumulado: {puntaje}")