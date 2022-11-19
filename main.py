import os
import moviepy.editor as mp
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter import ttk
import sv_ttk


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
            file_suffix = "." + self.interface.var_frmt.get()
            new_path = '\\'.join(n_list[:-1]) + "\\" + file_name + file_suffix
            video_clip = mp.VideoFileClip(old_path)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(new_path)
            audio_clip.close()
            video_clip.close()
            if os.path.exists(new_path):
                msg = messagebox.showinfo("Success!", "Conversion successfully completed!")
        print(self.file_path)



# interface

class Interface:
    root = Tk()
    sv_ttk.set_theme("light")
    lbl_pth = lbl_nter = lbl_frmt = None
    var_lbl_pth = var_lbl_nter = varntry_0 = varntry_1 = var_lbl_frmt = var_frmt = None
    brwse_btn = cnvrt_btn = file_ntry = nme_ntry = None
    frame = None
    audio_options = None


    def set_up(self, controller):
        self.root.title("Video --> Audio")
        self.frame = Frame(self.root)
        self.lbl_pth, self.lbl_nter, self.lbl_frmt = (ttk.Label(self.frame) for _ in range(3))
        self.var_lbl_pth, self.var_lbl_nter, self.var_lbl_frmt, self.varntry_0, self.varntry_1, self.var_frmt = (StringVar() for _ in range(6))
        self.brwse_btn, self. cnvrt_btn = (ttk.Button(self.frame) for _ in range(2))
        self.file_ntry, self.nme_ntry = ttk.Entry(self.frame, textvariable=self.varntry_0), ttk.Entry(self.frame, textvariable=self.varntry_1)
        # --- Drop Down ----
        self.audio_options = ["mp3", "ogg", "wav"]
        self.var_frmt.set(self.audio_options[0])
        self.frmt_menu = ttk.OptionMenu(self.frame, self.var_frmt, *self.audio_options)
        self.config_interface(controller)
        self.start_mainloop()

    def config_interface(self, controller):
        pd = 10
        self.brwse_btn.config(text="Browse", command=controller.on_browse_btn)
        self.cnvrt_btn.config(text="Convert", command=controller.on_convert_btn)
        self.var_lbl_pth.set("Choose a file to convert."), self.var_lbl_nter.set("Enter File Name"), self.var_lbl_frmt.set("Choose Format")
        self.lbl_pth.config(textvariable=self.var_lbl_pth), self.lbl_nter.config(textvariable=self.var_lbl_nter), self.lbl_frmt.config(textvariable=self.var_lbl_frmt)
        # It is recommended to assign a non-zero weight to whatever
        # column and row that you would like to allocate extra space.

        # -- grid --
        self.frame.grid(column=0, row=0, padx=pd, pady=pd)
        self.root.grid_rowconfigure(0, weight=2), self.root.grid_columnconfigure(3, weight=2)
        self.lbl_pth.grid(row=0, column=1, columnspan=2)
        self.file_ntry.grid(row=1, column=0, columnspan=3, sticky='WE'), self.brwse_btn.grid(row=1, column=3, sticky='WE')
        self.lbl_nter.grid(row=2, column=0, sticky='WE'), self.nme_ntry.grid(row=2, column=1, sticky='WE', columnspan=3)
        self.lbl_frmt.grid(row=3, column=0, sticky='WE'), self.frmt_menu.grid(row=3, column=3, sticky='WE')
        self.cnvrt_btn.grid(row=4, column=0, columnspan=4, sticky='WE')

    def modify_var(self, str_var, txt_str):
        str_var.set(txt_str)

    def start_mainloop(self):
        self.root.mainloop()



a = Controller(Interface())
a.start()