import cv2
from tkinter import messagebox, simpledialog
from PIL import Image
from . import settings, utils


def red(cv_array):
    """Возвращает изображение с выделенным красным каналом."""

    if cv_array is None:
        return None

    bgr = cv_array.copy()

    bgr[:, :, 0] = 0
    bgr[:, :, 1] = 0

    image_tk = utils.imagetk_from_bgr(bgr)

    data_dict = {
        'tk_img': image_tk,
        'cv_array': cv_array,
        'tk_st_msg': 'Красный канал.',
    }
    return data_dict


def green(cv_array):
    """Возвращает изображение с выделенным зеленым каналом."""

    if cv_array is None:
        return None

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
        'tk_st_msg': 'Зеленый канал.',
    }
    return data_dict


def blue(cv_array):
    """Возвращает изображение с выделенным синим каналом."""

    if cv_array is None:
        return None

    bgr = cv_array.copy()

    bgr[:, :, 1] = 0
    bgr[:, :, 2] = 0

    image_tk = utils.imagetk_from_bgr(bgr)

    data_dict = {
        'tk_img': image_tk,
        'cv_array': cv_array,
        'tk_st_msg': 'Синий канал.',
    }
    return data_dict


def task1(cv_array):
    """Возвращает изображение с применением негативного фильтра."""

    if cv_array is None:
        return None

    bgr = cv2.bitwise_not(cv_array)

    image_tk = utils.imagetk_from_bgr(bgr)

    data_dict = {
        'tk_img': image_tk,
        'cv_array': bgr,
        'tk_st_msg': 'Негатив.',
    }
    return data_dict


def task2(cv_array, root):
    """Возвращает изображение с повышенной яркостью."""

    brightness_factor = simpledialog.askinteger(
        'Повысить яркость',
        'Введите число:',
        parent=root,
    )

    if cv_array is None or brightness_factor is None:
        return None

    try:
        bgr = cv2.add(cv_array, abs(brightness_factor))
    except Exception:
        messagebox.showerror(
            'Ошибка',
            'Недопустимое значение.',
            parent=root,
        )
        return None

    image_tk = utils.imagetk_from_bgr(bgr)

    data_dict = {
        'tk_img': image_tk,
        'cv_array': bgr,
        'tk_st_msg': f'Повышена яркость на {brightness_factor}.',
    }
    return data_dict


def task3(cv_array, root):
    """Возвращает изображение с нарисованным красным кругом."""

    if cv_array is None:
        return None

    x = simpledialog.askinteger(
        'Круг',
        'Введите X координату центра:',
        parent=root,
    )
    if x is None:
        return None

    y = simpledialog.askinteger(
        'Круг',
        'Введите Y координату центра:',
        parent=root,
    )
    if y is None:
        return None

    r = simpledialog.askinteger(
        'Круг',
        'Введите радиус круга:',
        parent=root,
    )
    if r is None:
        return None

    bgr = cv_array.copy()
    try:
        center = (int(x), int(y))
        radius = int(r)
        cv2.circle(bgr, center, radius, (0, 0, 255), thickness=-1)
    except Exception:
        messagebox.showerror(
            'Ошибка',
            'Недопустимые значения.',
            parent=root,
        )
        return None

    image_tk = utils.imagetk_from_bgr(bgr)

    data_dict = {
        'tk_img': image_tk,
        'cv_array': bgr,
        'tk_st_msg': f'Нарисован красный круг в {center} радиус {radius}.',
    }
    return data_dict
