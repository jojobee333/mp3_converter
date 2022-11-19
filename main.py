import os
import moviepy.editor as mp
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox


# logic
class Controller:
    def __init__(self, interface):
        self.file_path = ""
        self.interface = interface
        self.start()

    def start(self):
        self.interface.set_up(self)
        self.interface.start_mainloop(self)

    def on_browse_btn(self):
        vid_formats = ('video files', '*.webm*', '*.mpg*', '*.mp2*', '*.mpeg*', '*.mpe*', '*.mpv*', '*.mp4*', '*.m4p*', '*.m4v*', '*.avi*', '*.wmv*', '*.mov*')
        file = fd.askopenfilename(title="Choose A File", filetypes=[("Video files", vid_formats)])
        self.file_path = os.path.abspath(file)
        self.interface.varntry_0.set(self.file_path)
        print(self.file_path)

    def on_convert_btn(self):
        if len(self.file_path) > 0:
            old_path = self.file_path
            n_list = self.file_path.split("\\")
            if len(self.interface.varntry_1.get()) > 0:
                file_name = self.interface.varntry_1.get()
                print(file_name)
            else:
                split_suffix = n_list[-1].split(".")
                file_name = split_suffix[0]
                print(file_name)
            file_suffix = "." + self.interface.frmt_var.get()
            new_path = '\\'.join(n_list[:-1]) + "\\" + file_name + file_suffix
            videoclip = mp.VideoFileClip(old_path)
            audioclip = videoclip.audio
            audioclip.write_audiofile(new_path)
            audioclip.close()
            videoclip.close()
            if os.path.exists(new_path):
                msg = messagebox.showinfo("Success!", "Conversion successfully completed!")
        print(self.file_path)



# interface

class Interface:
    root = Tk()
    lbl_0 = lbl_1 = lbl_2 = varlbl_0 = varlbl_1 = varntry_0 = None
    brwse_btn = frmt_btn = file_ntry = nme_ntry = None
    frame = None

    def set_up(self, controller):
        self.root.title("Video --> Audio")
        self.frame = Frame(self.root)
        self.lbl_0, self.lbl_1, self.lbl_2 = (Label(self.frame) for _ in range(3))
        self.varlbl_0, self.varlbl_1, self.varlbl_2, self.varntry_0, self.varntry_1 = (StringVar() for _ in range(5))
        self.brwse_btn, self. frmt_btn = Button(self.frame, text="Browse", command=controller.on_browse_btn), Button(self.frame, text="Convert", command=controller.on_convert_btn)
        self.file_ntry, self.nme_ntry = Entry(self.frame, textvariable=self.varntry_0), Entry(self.frame, textvariable=self.varntry_1)
        # --- Drop Down ----
        self.audio_options = ["mp3", "ogg", "wav"]
        self.frmt_var = StringVar()
        self.frmt_var.set(self.audio_options[0])
        self.frmt_menu = OptionMenu(self.frame, self.frmt_var, *self.audio_options)
        self.create_interface()
        self.start_mainloop()

    def create_interface(self):
        self.varlbl_0.set("Choose a file to convert."), self.varlbl_1.set("Enter File Name"), self.varlbl_2.set("Choose Format")
        self.lbl_0.config(textvariable=self.varlbl_0), self.lbl_1.config(textvariable=self.varlbl_1), self.lbl_2.config(textvariable=self.varlbl_2)
        # It is recommended to assign a non-zero weight to whatever
        # column and row that you would like to allocate extra space.
        self.frame.grid(column=0, row=0, padx=5, pady=10)
        self.root.grid_columnconfigure(0, weight=1), self.root.grid_columnconfigure(3, weight=1)
        self.lbl_0.grid(row=0, column=1, columnspan=2)
        self.file_ntry.grid(row=1, column=0, columnspan=3, sticky='WE'), self.brwse_btn.grid(row=1, column=3, sticky='WE')
        self.lbl_1.grid(row=2, column=0, sticky='WE'), self.nme_ntry.grid(row=2, column=1, sticky='WE', columnspan=3)
        self.lbl_2.grid(row=3, column=0, sticky='WE'), self.frmt_menu.grid(row=3, column=3, sticky='WE')
        self.frmt_btn.grid(row=4, column=0, columnspan=4, sticky='WE')

    def modify_var(self, str_var, txt_str):
        str_var.set(txt_str)

    def start_mainloop(self):
        self.root.mainloop()



a = Controller(Interface())
a.start()