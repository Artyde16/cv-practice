import cv2
from tkinter import messagebox
from PIL import Image, ImageTk
from . import settings, utils


def red(cv_array):
    """Возвращает изображение с выделенным красным каналом."""

    bgr = cv_array.copy()

    bgr[:, :, 0] = 0
    bgr[:, :, 1] = 0

    image_tk = utils.imagetk_from_bgr(bgr)

    data_dict = {
        'tk_img': image_tk,
        'cv_array': cv_array,
        'tk_st_msg': f'Красный канал.',
    }
    return data_dict


def green(cv_array):
    """Возвращает изображение с выделенным зеленым каналом."""

    bgr = cv_array.copy()

    bgr[:, :, 0] = 0
    bgr[:, :, 2] = 0

    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(rgb)

    preview = image.copy()
    preview.thumbnail(settings.MAX_IMAGE_SIZE)

    image_tk = utils.imagetk_from_bgr(bgr)

    data_dict = {
        'tk_img': image_tk,
        'cv_array': cv_array,
        'tk_st_msg': f'Зеленый канал.',
    }
    return data_dict


def blue(cv_array):
    """Возвращает изображение с выделенным синим каналом."""

    bgr = cv_array.copy()

    bgr[:, :, 1] = 0
    bgr[:, :, 2] = 0

    image_tk = utils.imagetk_from_bgr(bgr)

    data_dict = {
        'tk_img': image_tk,
        'cv_array': cv_array,
        'tk_st_msg': f'Синий канал.',
    }
    return data_dict


def task1(cv_array):
    """Возвращает изображение с применением негативного фильтра."""

    bgr = cv2.bitwise_not(cv_array)

    image_tk = utils.imagetk_from_bgr(bgr)

    data_dict = {
        'tk_img': image_tk,
        'cv_array': cv_array,
        'tk_st_msg': f'Негатив.',
    }
    return data_dict


def task2(cv_array, brightness_up=52):
    """Возвращает изображение с повышенной яркостью."""

    bgr = cv2.convertScaleAbs(cv_array, alpha=1, beta=brightness_up)

    image_tk = utils.imagetk_from_bgr(bgr)

    data_dict = {
        'tk_img': image_tk,
        'cv_array': cv_array,
        'tk_st_msg': f'Повышена яркость на {brightness_up}.',
    }
    return data_dict


def task3():
    messagebox.showinfo("Задание 3", "Еще не реализовано.")
