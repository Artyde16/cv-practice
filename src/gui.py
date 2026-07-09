import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from . import settings, utils, processing


class ImageApp:

    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title(settings.WINDOW_TITLE)
        self.root.geometry(settings.WINDOW_SIZE)
        self.root.resizable(False, False)
        self.root.attributes('-topmost', False)

        self.cv_array = None
        self.default_image = None

        self.create_widgets()

    def create_widgets(self):
        # Верхняя панель (кнопки)

        button_frame = ctk.CTkFrame(self.root, corner_radius=8)

        button_frame.pack(side=tk.TOP, padx=10, pady=10)

        def add_button(text, command, width=110):
            ctk.CTkButton(
                button_frame,
                text=text,
                command=command,
                width=width,
                height=28,
                corner_radius=6,
            ).pack(side=tk.LEFT, padx=3)

        def add_separator():
            ctk.CTkFrame(
                button_frame,
                width=2,
                height=25,
                fg_color="gray50",
                corner_radius=0,
            ).pack(side=tk.LEFT, padx=8)

        add_button(
            "Загрузить изображение",
            lambda: self.set_image(source=utils.load_image()),
            width=150,
        )

        add_button(
            "Сделать фото",
            lambda: self.set_image(source=utils.capture_image()),
            width=110,
        )

        add_separator()

        add_button(
            "Красный канал",
            lambda: self.set_image(source=processing.red(self.cv_array)),
        )

        add_button(
            "Зеленый канал",
            lambda: self.set_image(source=processing.green(self.cv_array)),
        )

        add_button(
            "Синий канал",
            lambda: self.set_image(source=processing.blue(self.cv_array)),
        )

        add_separator()

        add_button(
            "Негатив",
            lambda: self.set_image(source=processing.task1(self.cv_array)),
            width=90,
        )

        add_button(
            "Повысить яркость",
            lambda: self.set_image(
                source=processing.task2(self.cv_array, self.root)
            ),
            width=130,
        )

        add_button(
            "Круг",
            lambda: self.set_image(
                source=processing.task3(self.cv_array, self.root)
            ),
            width=80,
        )

        add_separator()

        add_button(
            "Вернуть исходное",
            lambda: self.set_image(source=None, default=True),
            width=130,
        )

        # Область с изображением

        self.image_CTkLabel = ctk.CTkLabel(
            self.root,
            text="Изображение не загружено",
        )

        self.image_CTkLabel.pack(expand=True, fill=tk.BOTH, padx=10, pady=5)

        # Строка состояния

        self.status = tk.StringVar(value="Готов к работе")

        ctk.CTkLabel(
            self.root,
            textvariable=self.status,
            anchor="w",
        ).pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)

    def set_image(self, source, default=False):
        if source:
            self.tk_image = source['tk_img']
            self.cv_array = source['cv_array']

            if not self.default_image:
                self.default_image = [self.tk_image, self.cv_array]

            self.image_CTkLabel.configure(image=self.tk_image, text="")
            self.status.set(source['tk_st_msg'])
        else:
            if default and self.default_image:
                self.cv_array = self.default_image[1]
                self.image_CTkLabel.configure(
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
