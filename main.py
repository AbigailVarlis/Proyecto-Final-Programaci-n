import limpieza
import procesamiento
import auxiliar
ruta = auxiliar.seleccionar_archivo()

with open(ruta,"r") as file:
    texto = file.read() 
    
    print
    