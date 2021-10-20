import os
import urllib.request

import cv2

from framework.utils.random_generator import RanGen


class ImageUtils:
    @staticmethod
    def download_the_image_from_url(image_source, image_path=None):
        file_name = f'{RanGen.gen_rand_string(10)}.jpg'
        default_image_path = os.path.abspath(f'.pytest_cache\\{file_name}')
        return urllib.request.urlretrieve(image_source, image_path or default_image_path)[0]

    @staticmethod
    def image_comparator(image_1, image_2):
        def calc_image_hash(file_name):
            resized = cv2.resize(file_name, (8, 8), interpolation=cv2.INTER_AREA)  # Уменьшим картинку
            gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)  # Переведем в черно-белый формат
            avg = gray_image.mean()  # Среднее значение пикселя
            ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0)  # Бинаризация по порогу

            _hash = ""
            for x in range(8):
                for y in range(8):
                    val = threshold_image[x, y]
                    if val == 255:
                        _hash = _hash + "1"
                    else:
                        _hash = _hash + "0"
            return _hash

        def compare_hash(hash_1, hash_2):
            l, i, count = len(hash_1), 0, 0
            while i < l:
                if hash_1[i] != hash_2[i]:
                    count = count + 1
                i = i + 1
            return count

        image_1_cv, image_2_cv = map(cv2.imread, (image_1, image_2))
        hash1, hash2 = map(calc_image_hash, (image_1_cv, image_2_cv))
        result = compare_hash(hash1, hash2)
        return result == 0
