import tkinter
import tkinter.messagebox
import customtkinter
import tkinter.filedialog as filedialog


customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter")
        self.geometry(f"{720}x{580}")

        # configure grid layout (4x4)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1), weight=1)

        # Object
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=0, column=1, sticky="nsew")

        self.button = customtkinter.CTkButton(self.sidebar_frame, text="Открыть", command=self.choose_file)
        self.button.grid(row=0, column=0, padx=20, pady=20)
        self.button1 = customtkinter.CTkButton(self.sidebar_frame, text="Преобразовать", command=self.read_file)
        self.button1.grid(row=1, column=0, padx=20, pady=40)
        self.entry = customtkinter.CTkEntry(
            self.slider_progressbar_frame,
            placeholder_text="Укажите путь до файла...",
            width=400,
        )
        self.entry.grid(row=0, column=1, padx=20, pady=20)

    def choose_file(self):
        filetypes = (
            ("Файл xml", "*.xml"),
            ("Текстовый файл", "*.txt"),
            ("Любой", "*"),
        )
        filename = filedialog.askopenfilename(
            title="Открыть файл",
            # initialdir="/",
            filetypes=filetypes,
        )
        if filename:
            self.entry.delete(0, tkinter.END)
            self.entry.insert(0, filename)

    def read_file(self):
        file = open(self.entry.get()).read()
        tags = {
            "obyzanosti": 'Обязанности:',
            "trebovaniy": 'Требования:',
            "usloviy": 'Условия:',
        }
        full_text = ""
        for key in tags:
            only_text = file[file.find(tags.get(key)):]
            if only_text.find(tags.get(key)) != -1:
                tags_list = ["Обязанности:", "Требования:", "Условия:"]
                tags_list.remove(tags.get(key))
                for tag in tags_list:
                    only_text = only_text[:only_text.find(tag)]
                if only_text.find("DOPINFORMS") != -1:
                    only_text = only_text.replace("DOPINFORMS", "")
                    text = f'<DOPINFORMS{key.upper()}>' + only_text.replace("\n", "") + f'DOPINFORMS{key.upper()}>'
                else:
                    text = f'<DOPINFORMS{key.upper()}>' + only_text.replace("\n", "") + f'</DOPINFORMS{key.upper()}>'
                full_text += text + "\n"
        print(full_text)


if __name__ == "__main__":
    app = App()
    app.mainloop()
