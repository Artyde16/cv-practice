import cv2
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox
from . import settings


def imagetk_from_bgr(bgr):
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(rgb)

    preview = image.copy()
    preview.thumbnail(settings.MAX_IMAGE_SIZE)

    return ImageTk.PhotoImage(preview)


def load_image():
    """
    Загружает изображение.
    """

    filename = filedialog.askopenfilename(
        title="Выберите изображение",
        filetypes=settings.SUPPORTED_FORMATS,
    )

    if not filename:
        return None

    try:
        bgr = cv2.imread(filename)
        image_tk = imagetk_from_bgr(bgr)

    except Exception as e:
        messagebox.showerror("Ошибка", str(e))
        return None

    data_dict = {
        'tk_img': image_tk,
        'cv_array': bgr,
        'tk_st_msg': f'Открыт файл: {filename}',
    }

    return data_dict


def capture_image():
    """
    Захватывает изображение с камеры.
    """

    messagebox.showinfo(
        "Информация", "Нажмите Enter для захвата изображения, Esc для выхода."
    )

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        messagebox.showerror(
            message='Ошибка, не удалось подключиться к веб-камере.'
        )
        return None

    while True:

        ret, bgr = cap.read()

        if not ret:
            break

        cv2.imshow("Камера", bgr)

        key = cv2.waitKey(1)

        if key == 13:

            image_tk = imagetk_from_bgr(bgr)

            cap.release()
            cv2.destroyAllWindows()

            data_dict = {
                'tk_img': image_tk,
                'cv_array': bgr,
                'tk_st_msg': 'Открыто изображение с веб-камеры.',
            }

            return data_dict

        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    return None
