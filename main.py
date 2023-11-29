import numpy as np
from PIL import Image


def main():
    img_array = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
                 [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
                 [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
                 [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
                 [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
                 [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
                 [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1],
                 [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1],
                 [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
                 [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
                 [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    img = create_img_from_array(img_array)  # tworzy obrazek na podstawie powyższej macierzy
    img.save('img.png')  # zapisuje obrazek
    top_layer_array = create_top_random_layer_array(len(img_array),
                                                    len(img_array[
                                                            0]))  # tworzy losową macierz składającą się z 2 i 3 o wymiarach takich jak macierz obrazka(20 na 20)
    print(f'Top layer array:\n {top_layer_array}')  # wypisuje losową macierz
    top_layer_img = create_img_from_array(top_layer_array)  # tworzy pierwszy obraz z losowej macierzy
    top_layer_img.save('top.png')  # zapisuje obeazek losowej macierzy
    bottom_layer_array = create_bottom_layer_array(img_array,
                                                   top_layer_array)  # tworzy drugą macierz na podstawie macierzy obrazka i macierzy losowej
    print(f'Bottom layer array:\n {bottom_layer_array}')  # wypisuje powyższą macierz
    bottom_layer_img = create_img_from_array(bottom_layer_array)  # tworzy obraz z powyższej macierzy
    bottom_layer_img.save('bottom.png')  # zapisuje powyższy obraz


def create_top_random_layer_array(size_x, size_y):
    '''
    zwraca macierz warstwy górnej wygenerowanej losowo wartościami 2 i 3
    :param size_x:
    :param size_y:
    :return:
    '''
    return np.random.randint(2, high=4, size=[size_x, size_y])


def create_bottom_layer_array(img_array, top_random_layer_array):
    '''
    tworzy macierz dolnej warstwy na podstawie macierzy obrazka i macierzy warstwy górnej losowej, która przyjmuje wartości 2 lub 3
    :param img_array: macierz obrazka
    :param top_random_layer_array: losowa macierz
    :return: macierz zawierająca tylko wartości 2 i 3 wygenerowane na podstawie powyższych macierzy
    '''
    bottom_layer = np.ones((len(img_array), len(img_array[0])),
                           dtype=int)  # inicjuje macierz jedynkową o wymiarach takich, jak macierz obrazka
    for i, line in enumerate(img_array):
        for j, pixel in enumerate(line):  # pętla przechodząca po każdej wartości macierzy
            if pixel == 1 and top_random_layer_array[i][
                j] == 2:  # jeśli pixel jest biały i wartość losowej macierzy w tym miejscu ma wartość 2, to
                bottom_layer[i][j] = 3  # wartość macierzy przyjmuje 3
            elif pixel == 1 and top_random_layer_array[i][
                j] == 3:  # jeśli pixel jest biały i wartość losowej macierzy w tym miejscu ma wartość 3, to
                bottom_layer[i][j] = 2  # wartość macierzy przyjmuje 2
            elif pixel == 0 and top_random_layer_array[i][
                j] == 3:  # jeśli pixel jest czarny i wartość losowej macierzy w tym miejscu ma wartość 2, to
                bottom_layer[i][j] = 3  # wartość macierzy przyjmuje 3
            else:  # jeśli pixel jest czarny i wartość losowej macierzy w tym miejscu ma wartość 2, to
                bottom_layer[i][j] = 2  # wartość macierzy przyjmuje 2
    return bottom_layer


def create_img_from_array(img_array):
    '''
    tworzy i zwraca obrazek na podstawie macierzy
    :param img_array: macierz, na podstawie której zostanie wygenerowany obrazek
    :return: zwraca obrazek
    '''
    zero_image = Image.open("0.png")  # obrazek dla 0
    one_image = Image.open("1.png")  # obrazek dla 1
    two_image = Image.open("2.png")  # obrazek dla 2
    three_image = Image.open("3.png")  # obrazek dla 3
    img_size = len(img_array) * 2, len(
        img_array[0]) * 2  # delkaruje rozmiar obrazka, który jest 2x większy niż wymiary macierzy
    img = Image.new("RGBA", img_size,
                    (0, 0, 0, 0))  # tworzy 'pusty' obrazek, który zostanie wypełniony na podstawie macierzy
    for row in range(len(img_array)):
        for column in range(len(img_array[0])):  # przechodzi po każdym elemencie macierzy i...
            if img_array[row][column] == 0:  # ...jeśli trafi na 0...
                img.paste(zero_image, (column * 2, row * 2))  # ...to w odpowiednie miejsce wklei obrazek dla 0
            elif img_array[row][column] == 1:  # ...jeśli trafi na 1...
                img.paste(one_image, (column * 2, row * 2))  # ...to w odpowiednie miejsce wklei obrazek dla 1
            elif img_array[row][column] == 2:  # ...jeśli trafi na 2...
                img.paste(two_image, (column * 2, row * 2))  # ...to w odpowiednie miejsce wklei obrazek dla 2
            else:  # ...jeśli trafi na 3...
                img.paste(three_image, (column * 2, row * 2))  # ...to w odpowiednie miejsce wklei obrazek dla 3
    return img


if __name__ == '__main__':
    main()
