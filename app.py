from PIL import Image
import os

def compress_image(file_path, output_path, target_size_mb=2, quality_step=5):
    """
    Comprime una imagen para que su tamaño sea menor o igual al tamaño objetivo en MB.
    
    :param file_path: Ruta del archivo de imagen original.
    :param output_path: Ruta para guardar la imagen comprimida.
    :param target_size_mb: Tamaño máximo objetivo en megabytes.
    :param quality_step: Paso de ajuste de calidad.
    """
    target_size_bytes = target_size_mb * 1024 * 1024  # Convertir MB a bytes
    quality = 100  # Calidad inicial
    
    # Abrir la imagen
    with Image.open(file_path) as img:
        while True:
            # Guardar la imagen con la calidad actual
            img.save(output_path, format='JPEG', quality=quality, optimize=True)
            
            # Verificar el tamaño del archivo
            if os.path.getsize(output_path) <= target_size_bytes or quality <= quality_step:
                break
            
            # Reducir la calidad para intentar bajar el tamaño del archivo
            quality -= quality_step

def main(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.jpg'):
            file_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            compress_image(file_path, output_path)

if __name__ == "__main__":
    input_dir = 'input'
    output_dir = 'output'
    main(input_dir, output_dir)
