import numpy as np
from PIL import Image


def get_array_from_bitmap(name):
    bmp_image = Image.open(name)
    image_array = np.array(bmp_image)
    binary_array = (image_array != 0).astype(int)
    new_array = np.ones((len(binary_array), len(binary_array[0])), dtype=int)
    for i in range(len(binary_array)):
        for j in range(len(binary_array[i])):
            new_array[i][j] = binary_array[i][j][0]
    return new_array


if __name__ == "__main__":
    array = get_array_from_bitmap("A.bmp")
    print(array)
