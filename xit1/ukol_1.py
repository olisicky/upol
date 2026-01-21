import os

from PIL import Image
import numpy as np


IMG_PATH = "./vasik.png"


def convert_to_grayscale(image, average=None):
    """Určení šedého obrazu z barevného obrázku."""
    data = np.array(image)
    r, g, b = data[:, :, 0], data[:, :, 1], data[:, :, 2]


    if not average:
        weights = random_weights()
        gray = (weights[0] * r + weights[1] * g + weights[2] * b).astype(np.uint8)
    else:
        if average == 'simple':
            gray = (r + g + b) // 3
        elif average == 'weighted':
            gray = (0.299 * r + 0.587 * g + 0.114 * b).astype(np.uint8)
        else:
            raise ValueError("average must be 'simple' or 'weighted'")

    return Image.fromarray(gray, mode='L')


def random_weights():
    """Určení náhodných vah pro jednotlivé kanály."""
    random_nums = np.random.rand(3)
    return random_nums / random_nums.sum()


def desaturate(image, s, average='weighted'):
    """Desaturace obrázku podle faktoru s. Pro výpočet šedého obrazu se používá zvolená metoda."""
    data = np.array(image).astype(np.float32)
    r, g, b = data[:, :, 0], data[:, :, 1], data[:, :, 2]
    gray = np.array(convert_to_grayscale(image, average=average)).astype(np.float32)    # kvůli přetečení ve float
    rd = gray + s * (r - gray)
    gd = gray + s * (g - gray)
    bd = gray + s * (b - gray)
    desat_data = np.stack([rd, gd, bd], axis=-1).astype(np.uint8)
    return Image.fromarray(desat_data, mode='RGB')


def normalization(image, target_dist=50):
    """Provede saturační vyrovnání obrázku, aby byl každý barevný pixel ve vzdálenosti target_dist od šedé hodnoty."""
    data = np.array(image).astype(np.float32)
    weights = np.array([0.299, 0.587, 0.114])
    y = np.sum(data * weights, axis=2, keepdims=True)
    vectors = data - y    # vektory od šedé hodnoty
    distance = np.linalg.norm(vectors, axis=-1, keepdims=True)    # Eukleidovská vzdálenost
    mask = distance > 0.001    # pro ne-achromatické pixely
    res = np.copy(data)
    res[mask.squeeze()] = y[mask.squeeze()] + vectors[mask.squeeze()] * (target_dist / distance[mask.squeeze()])

    return Image.fromarray(np.clip(res, 0, 255).astype(np.uint8))


if __name__ == "__main__":
    img = Image.open(IMG_PATH)

    rgb_image = img.convert("RGB")
    gray_weighted = convert_to_grayscale(rgb_image, average='weighted')
    gray_simple = convert_to_grayscale(rgb_image, average='simple')
    gray_random = convert_to_grayscale(rgb_image)
    desaturated = desaturate(rgb_image, s=0.5, average='weighted')

    os.makedirs("output", exist_ok=True)
    gray_weighted.save("output/gray_weighted.png")
    gray_simple.save("output/gray_simple.png")
    gray_random.save("output/gray_random.png")
    desaturated.save("output/desaturated.png")
    normalized = normalization(rgb_image, target_dist=50)
    normalized.save("output/normalized.png")