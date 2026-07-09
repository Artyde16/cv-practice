import tkinter as tk
from tkinter import ttk, messagebox
from . import settings, utils, processing


class ImageApp:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title(settings.WINDOW_TITLE)
        self.root.geometry(settings.WINDOW_SIZE)
        self.root.resizable(False, False)
        self.root.attributes('-topmost', False)

        self.cv_array = None
        self.default_image = None

        self.create_widgets()

    def create_widgets(self):

        # Верхняя панель (кнопки)

        button_frame = ttk.Frame(self.root, padding=10)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        ttk.Button(
            button_frame,
            text="Загрузить изображение",
            command=lambda: self.set_image(
                source=utils.load_image(), new=True
            ),
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            button_frame,
            text="Сделать фото",
            command=lambda: self.set_image(
                source=utils.capture_image(), new=True
            ),
        ).pack(side=tk.LEFT, padx=5)

        ttk.Separator(
            button_frame,
            orient="vertical",
        ).pack(side=tk.LEFT, fill=tk.Y, padx=10)

        ttk.Button(
            button_frame,
            text="Красный канал",
            command=lambda: self.set_image(
                source=processing.red(self.cv_array)
            ),
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            button_frame,
            text="Зеленый канал",
            command=lambda: self.set_image(
                source=processing.green(self.cv_array)
            ),
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            button_frame,
            text="Синий канал",
            command=lambda: self.set_image(
                source=processing.blue(self.cv_array)
            ),
        ).pack(side=tk.LEFT, padx=5)

        ttk.Separator(
            button_frame,
            orient="vertical",
        ).pack(side=tk.LEFT, fill=tk.Y, padx=10)

        # Кнопки для вариативного задания

        # 3
        ttk.Button(
            button_frame,
            text="Негатив",
            command=lambda: self.set_image(
                source=processing.task1(self.cv_array)
            ),
        ).pack(side=tk.LEFT, padx=5)

        # 7
        ttk.Button(
            button_frame,
            text="Повысить яркость",
            command=lambda: self.set_image(
                source=processing.task2(self.cv_array, self.root)
            ),
        ).pack(side=tk.LEFT, padx=5)

        # 13
        ttk.Button(
            button_frame,
            text="Круг",
            command=lambda: self.set_image(
                source=processing.task3(self.cv_array, self.root)
            ),
        ).pack(side=tk.LEFT, padx=5)

        ttk.Separator(
            button_frame,
            orient="vertical",
        ).pack(side=tk.LEFT, fill=tk.Y, padx=10)

        # Кнопка для возвращения исходного изображения
        ttk.Button(
            button_frame,
            text="Вернуть исходное",
            command=lambda: self.set_image(source=None, default=True),
        ).pack(side=tk.LEFT, padx=5)

        # Область с изображением

        self.image_label = ttk.Label(
            self.root,
            text="Изображение не загружено",
            anchor="center",
        )

        self.image_label.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Строка состояния

        self.status = tk.StringVar()
        self.status.set("Готов к работе")

        ttk.Label(
            self.root,
            textvariable=self.status,
            relief=tk.SUNKEN,
            anchor="w",
        ).pack(side=tk.BOTTOM, fill=tk.X)

    def set_image(self, source, default=False, new=False):
        if source:
            self.tk_image = source['tk_img']
            self.cv_array = source['cv_array']

            if new:
                self.default_image = [self.tk_image, self.cv_array]

            self.image_label.configure(image=self.tk_image, text="")
            self.status.set(source['tk_st_msg'])
        else:
            if default and self.default_image:
                self.cv_array = self.default_image[1]
                self.image_label.configure(
                    image=self.default_image[0], text=""
                )
                self.status.set('Изображение восстановлено.')
            else:
                if self.default_image:
                    messagebox.showwarning(
                        'Внимание',
                        'Изображение не изменено.',
                        parent=self.root,
                    )
                else:
                    messagebox.showwarning(
                        'Внимание',
                        'Изображение не загружено.',
                        parent=self.root,
                    )

    def run(self):
        self.root.mainloop()
