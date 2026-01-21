import os

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def bresenham_circle(x0, y0, radius):
    """Generuje body kružnice pomocí Bresenhamova algoritmu."""
    points = []

    def append_points(x, y):
        """Přidá body pro všechny oktanty."""
        points.append((x0 + x, y0 + y))
        points.append((x0 - x, y0 + y))
        points.append((x0 + x, y0 - y))
        points.append((x0 - x, y0 - y))
        points.append((x0 + y, y0 + x))
        points.append((x0 - y, y0 + x))
        points.append((x0 + y, y0 - x))
        points.append((x0 - y, y0 - x))

    x = 0
    y = radius
    midpoint = (x + 1)**2 + (y - 0.5)**2 - radius**2
    append_points(x, y)
    while x <= y:
        x += 1
        if midpoint <= 0:
            midpoint = midpoint + 2 * x + 3
            y = y
        else:
            midpoint = midpoint + 2 * x + 3 - (2 * y - 2)
            y -= 1
        append_points(x, y)
    return set(points)


def draw_circle_on_image(h, w, points):
    """Nakreslí kružnici na obrázek pomocí Bresenhamova algoritmu."""
    data = np.zeros((h, w)).astype(np.uint8)

    for (x, y) in points:
        if 0 <= x < w and 0 <= y < h:
            data[y, x] = 255

    return Image.fromarray(data, mode='L')


def de_casteljau(control_points: list[list[float]], t: float) -> list[float]:
    """Vypočítá bod na Bézierově křivce pro parametr t."""

    points = np.array(control_points, dtype=float)
    
    for i in range(1, len(points)):
        for j in range(len(points) - i):
            points[j] = (1 - t) * points[j] + t * points[j+1]    # interpolace mezi body

    return points[0].tolist()


def save_bezier(control_points, num_segments=100):
    t_values = np.linspace(0, 1, num_segments)
    curve_points = np.array([de_casteljau(control_points, t) for t in t_values])

    plt.plot(curve_points[:, 0], curve_points[:, 1], 'b-', label='Bézierova křivka')

    cp = np.array(control_points)
    plt.plot(cp[:, 0], cp[:, 1], 'ro--', alpha=0.5, label='Řídicí body')
    
    plt.legend()
    plt.savefig("output/ukol_4_bezier.png")


if __name__ == "__main__":
    points = bresenham_circle(500, 500, 300)
    img = draw_circle_on_image(1000, 1000, points)
    os.makedirs("output", exist_ok=True)
    img.save("output/ukol_4_circle.png")

    control_pts = [[0, 0], [20, 80], [80, 80], [100, 0]]
    save_bezier(control_pts)