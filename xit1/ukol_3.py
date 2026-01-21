import os

import numpy as np
from PIL import Image

from ukol_1 import convert_to_grayscale


def brightness(image, c: int):
    """Úprava jasu obrázku přičtením konstanty c."""
    data = np.array(image).astype(np.int16)
    data += c
    data = np.clip(data, 0, 255).astype(np.uint8)    # zabránění přetečení
    return Image.fromarray(data, mode='L')


def constrast(image, factor: float):
    """Úprava kontrastu obrázku podle zadaného faktoru."""
    data = np.array(image).astype(np.int16)
    data = 128 + factor * (data - 128)    # úprava vzhledem ke středu
    data = np.clip(data, 0, 255).astype(np.uint8)    # zabránění přetečení
    return Image.fromarray(data, mode='L')


def thresholding(image, t: int):
    """Prahování obrázku podle zadané prahové hodnoty t."""
    data = np.array(image).astype(np.uint8)
    data = np.where(data >= t, 255, 0).astype(np.uint8)
    return Image.fromarray(data, mode='L')


def gamma_correction(image, gamma: float):
    """Gamma korekce obrázku podle zadaného gamma faktoru."""
    data = np.array(image).astype(np.float32) / 255.0    # normalizace, abych nepracoval s extrémním exponentem
    data = np.power(data, gamma) * 255.0    # zpětná denormalizace
    data = np.clip(data, 0, 255).astype(np.uint8)
    return Image.fromarray(data, mode='L')

def histogram(image):
    """Vypočítá histogram jasu obrázku."""
    data = np.array(image).astype(np.uint8)
    height, width = data.shape
    hist = np.zeros(256, dtype=int)
    for i in range(height):
        for j in range(width):
            hist[data[i, j]] += 1
    return hist


def cumulative_histogram(image):
    """Vypočítá kumulativní histogram jasu obrázku."""
    hist = histogram(image)
    cum_hist = np.cumsum(hist)
    return cum_hist


def norm_histogram(image):
    """Vypočítá normalizovaný histogram jasu obrázku."""
    hist = histogram(image)
    total_pixels = np.sum(hist)
    norm_hist = hist / total_pixels    # viz přednáška M*N ... dostanu počet pixelů obrazu
    return norm_hist


def norm_cumulative_histogram(image):
    """Vypočítá normalizovaný kumulativní histogram jasu obrázku."""
    norm_hist = norm_histogram(image)
    norm_cum_hist = np.cumsum(norm_hist)
    return norm_cum_hist


def equalization(image):
    """Provede ekvalizaci jasu obrázku."""
    data = np.array(image).astype(np.uint8)
    height, width = data.shape
    norm_cum_hist = norm_cumulative_histogram(image)
    equalized_data = np.zeros((height, width), dtype=np.uint8)
    L = 256

    for i in range(height):
        for j in range(width):
            equalized_data[i, j] = int(norm_cum_hist[data[i, j]] * (L - 1))

    return Image.fromarray(equalized_data, mode='L')


def linear_combination(image1, image2, alpha: float):
    """Lineární kombinace dvou obrázků podle váhy alpha."""
    data1 = np.array(image1).astype(np.float32)
    data2 = np.array(image2).astype(np.float32)

    if data1.shape != data2.shape:
        raise ValueError('Obrázky musí mít stejnou velikost a počet kanálů pro lineární kombinaci.')

    combined_data = alpha * data1 + (1 - alpha) * data2
    combined_data = np.clip(combined_data, 0, 255).astype(np.uint8)

    if len(combined_data.shape) == 2:
        mode = 'L'
    else:
        mode = 'RGB'

    return Image.fromarray(combined_data, mode=mode)


if __name__ == "__main__":
    img = Image.open("./vasik.png").convert("RGB")
    gray = convert_to_grayscale(img, average='weighted')

    kaja = Image.open("kaja.png").convert("RGB")
    kaja_gray = convert_to_grayscale(kaja, average='weighted')

    os.makedirs("output", exist_ok=True)
    brightened = brightness(gray, 30)
    brightened.save("output/brightened.png")

    contrasted = constrast(gray, 1.5)
    contrasted.save("output/contrasted.png")

    thresholded = thresholding(gray, 128)
    thresholded.save("output/thresholded.png")

    gamma_corrected = gamma_correction(gray, 2.2)
    gamma_corrected.save("output/gamma_corrected.png")

    equalized = equalization(gray)
    equalized.save("output/equalized.png")

    combined = linear_combination(gray, kaja_gray, 0.5)
    combined.save("output/linear_combination.png")

