import tkinter as tk
from tkinter import filedialog


def seleccionar_archivo(titulo: str = "Seleccionar un archivo", tipos: list[tuple[str, str]] | None = None) -> str | None:
    """
    Abre el explorador de archivos para seleccionar un único archivo.
    Devuelve la ruta como str o None si el usuario cancela.
    """
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal vacía de Tkinter
    root.attributes("-topmost", True)  # Trae el diálogo al frente

    if tipos is None:
        tipos = [("Todos los archivos", "*.*")]

    ruta = filedialog.askopenfilename(
        title=titulo,
        filetypes=tipos,
        multiple=False,  # Asegura que solo se seleccione un archivo, no carpeta ni varios
    )

    root.destroy()
    return ruta if ruta else None


# Ejemplo de uso
if __name__ == "__main__":
    archivo = seleccionar_archivo(
        titulo="Elige un documento o imagen",
        tipos=[
            ("Imágenes", "*.png *.jpg *.jpeg *.webp"),
            ("PDF", "*.pdf"),
            ("Todos los archivos", "*.*"),
        ],
    )

    if archivo:
        print("Archivo seleccionado:", archivo)
    else:
        print("No se seleccionó ningún archivo.")