from PIL import Image


class Filter:
    """Базовый класс для создания фильтров."""

    def apply_to_pixel(self, pixel: tuple) -> tuple:

        raise NotImplementedError()

    def apply_to_image(self, img: Image.Image) -> Image.Image:

        pixels = img.load()
        width, height = img.size

        for x in range(width):
            for y in range(height):
                # получаем цвет пикселя
                r, g, b = pixels[x, y]

                # применяем фильтр к пикселю
                new_r, new_g, new_b = self.apply_to_pixel((r, g, b))

                # сохраняем обновленный пиксель
                pixels[x, y] = (new_r, new_g, new_b)

        return img


class RedFilter(Filter):
    def apply_to_pixel(self, pixel: tuple) -> tuple:
        r, g, b = pixel
        new_r = min(255, r + 30)  # Увеличиваем красный канал на 30, но не больше 255
        return (new_r, g, b)


class GreenFilter(Filter):
    def apply_to_pixel(self, pixel: tuple) -> tuple:
        r, g, b = pixel
        new_g = min(255, g + 30)  # Увеличиваем зеленый канал на 30, но не больше 255
        return (r, new_g, b)


class BlueFilter(Filter):
    def apply_to_pixel(self, pixel: tuple) -> tuple:
        r, g, b = pixel
        new_b = min(255, b + 30)  # Увеличиваем синий канал на 30, но не больше 255
        return (r, g, new_b)


class InvertFilter(Filter):
    def apply_to_pixel(self, pixel: tuple) -> tuple:
        r, g, b = pixel
        new_r = 255 - r  # Инвертируем значение красного канала
        new_g = 255 - g  # Инвертируем значение зеленого канала
        new_b = 255 - b  # Инвертируем значение синего канала
        return (new_r, new_g, new_b)


class BrightenFilter(Filter):
    def apply_to_pixel(self, pixel: tuple) -> tuple:
        r, g, b = pixel
        new_r = min(255, r + 30)  # Увеличиваем красный канал на 30, но не больше 255
        new_g = min(255, g + 30)  # Увеличиваем зеленый канал на 30, но не больше 255
        new_b = min(255, b + 30)  # Увеличиваем синий канал на 30, но не больше 255
        return (new_r, new_g, new_b)


class DarkenFilter(Filter):
    def apply_to_pixel(self, pixel: tuple) -> tuple:
        r, g, b = pixel
        new_r = max(0, r - 30)  # Уменьшаем красный канал на 30, но не меньше 0
        new_g = max(0, g - 30)  # Уменьшаем зеленый канал на 30, но не меньше 0
        new_b = max(0, b - 30)  # Уменьшаем синий канал на 30, но не меньше 0
        return (new_r, new_g, new_b)

