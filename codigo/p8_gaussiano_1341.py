import cv2
import os

# Obtener la carpeta donde está este archivo Python
carpeta_proyecto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Rutas
ruta_imagen = os.path.join(carpeta_proyecto, "imagenes", "alcon.jpg")
carpeta_resultados = os.path.join(carpeta_proyecto, "resultados")

# Crear carpeta resultados si no existe
os.makedirs(carpeta_resultados, exist_ok=True)

# Cargar imagen
imagen = cv2.imread(ruta_imagen)

# Verificar imagen
if imagen is None:
    print("ERROR: No se pudo cargar la imagen.")
    print("La ruta que Python está buscando es:")
    print(ruta_imagen)
    exit()

# Aplicar filtro Gaussiano
imagen_suavizada = cv2.GaussianBlur(
    imagen,
    (7, 7),
    0
)

# Mostrar imágenes
cv2.imshow("Imagen original - Alcon", imagen)
cv2.imshow("Imagen suavizada - Filtro Gaussiano", imagen_suavizada)

# Guardar resultado
ruta_salida = os.path.join(
    carpeta_resultados,
    "alcon_gaussiano.jpg"
)

cv2.imwrite(ruta_salida, imagen_suavizada)

print("Filtro Gaussiano aplicado correctamente.")
print("Imagen original:", ruta_imagen)
print("Resultado guardado en:", ruta_salida)

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()