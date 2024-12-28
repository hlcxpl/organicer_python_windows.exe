import sys
from pathlib import Path


def organizar_archivos(directorio):
    for archivo_path in Path(directorio).glob("*"):
        if archivo_path.is_file() and not archivo_path.name.startswith(
            "organizar_archivos"
        ):
            organizar_archivo(archivo_path)


def organizar_archivo(archivo_path):
    extension = archivo_path.suffix[1:]  # Obtener la extensión sin el punto inicial
    carpeta_destino = Path(archivo_path.parent, extension)
    carpeta_destino.mkdir(exist_ok=True)
    archivo_path.rename(Path(carpeta_destino, archivo_path.name))
    print(f"Archivo {archivo_path.name} movido a carpeta {extension}/")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: organizar_archivos.py <directorio_a_organizar>")
        sys.exit(1)

    directorio_a_organizar = Path(sys.argv[1])
    organizar_archivos(directorio_a_organizar)
