import os

import numpy as np
from PIL import Image

from ukol_1 import convert_to_grayscale


def matrix_dithering(n):
    """Rekurzivní generování ditheringové matice velikosti n x n."""
    if n == 1:
        return np.array([[0]])
    
    n_half = n // 2
    small = matrix_dithering(n_half)

    J = np.ones((n_half, n_half), dtype=int)

    return np.block([
        [4 * small, 4 * small + 2 * J],
        [4 * small + 3 * J, 4 * small + 1 * J]
    ])


def apply_dithering(image, matrix):
    """Aplikace ditheringu na obrázek pomocí dané prahovací matice. Kompenzace na hodnoty 256 pomocí posunu o 0.5."""
    data = convert_to_grayscale(image, average='weighted')
    data = np.array(data).astype(np.uint8)
    n = matrix.shape[0]
    height, width = data.shape
    dithered = np.zeros((height, width), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            threshold = ((matrix[i % n, j % n] + 0.5) / (n*n))  * 255    # kompenzace prahu pro střední hodnotu
            dithered[i, j] = 255 if data[i, j] >= threshold else 0

    return Image.fromarray(dithered, mode='L')


def apply_dithering_fast(image, matrix):
    """Rychlá verze ditheringu využívající NumPy vektorové operace."""
    data = convert_to_grayscale(image, average='weighted')
    data = np.array(data).astype(np.uint8)
    n = matrix.shape[0]
    height, width = data.shape
    # pokrytí celé velikosti obrazu
    tiled_matrix = np.tile(matrix, (height // n + 1, width // n + 1))
    tiled_matrix = tiled_matrix[:height, :width]
    threshold = ((tiled_matrix + 0.5) / (n*n)) * 255
    dithered = np.where(data >= threshold, 255, 0).astype(np.uint8)

    return Image.fromarray(dithered, mode='L')


if __name__ == "__main__":
    img = Image.open("./vasik.png")

    matrix = matrix_dithering(16)

    dithered_img = apply_dithering_fast(img, matrix)

    os.makedirs("output", exist_ok=True)
    dithered_img.save("output/ukol_2_2_dithered.png")