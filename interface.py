import os
from tkinter import ttk, Tk, Frame, StringVar
import sv_ttk
from constants import AUDIO_FORMATS


class Interface:
    def __init__(self):
        self.root = Tk()
        sv_ttk.set_theme("light")
        self.setup_variables()

    def setup_variables(self):
        self.file_path_var = StringVar()
        self.file_name_var = StringVar()
        self.format_var = StringVar(value=AUDIO_FORMATS[0])

    def setup(self, controller):
        self.root.title("Video to Audio Converter")
        frame = Frame(self.root)
        frame.grid(padx=10, pady=10, sticky='nsew')

        ttk.Label(frame, text="Choose a file to convert").grid(row=0, column=0, sticky='w')
        ttk.Entry(frame, textvariable=self.file_path_var).grid(row=1, column=0, sticky='ew')
        ttk.Button(frame, text="Browse", command=controller.on_browse_btn).grid(row=1, column=1)

        ttk.Label(frame, text="Enter File Name").grid(row=2, column=0, sticky='w')
        ttk.Entry(frame, textvariable=self.file_name_var).grid(row=3, column=0, sticky='ew')

        ttk.Label(frame, text="Choose Format").grid(row=4, column=0, sticky='w')
        ttk.OptionMenu(frame, self.format_var, *AUDIO_FORMATS).grid(row=5, column=0, sticky='ew')

        ttk.Button(frame, text="Convert", command=controller.on_convert_btn).grid(row=6, column=0, columnspan=2,
                                                                                  sticky='ew')

        frame.columnconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

    def set_file_path(self, path):
        self.file_path_var.set(path)

    def get_output_file_path(self, original_path):
        file_name = self.file_name_var.get() or os.path.splitext(os.path.basename(original_path))[0]
        return os.path.join(os.path.dirname(original_path), f"{file_name}.{self.format_var.get()}")

    def start_mainloop(self):
        self.root.mainloop()
