import os
import moviepy.editor as mp
from tkinter import filedialog as fd
from tkinter import messagebox
from constants import VIDEO_FORMATS


class Controller:
    def __init__(self, interface):
        self.file_path = ""
        self.interface = interface

    def start(self):
        self.interface.setup(self)
        self.interface.start_mainloop()

    def on_browse_btn(self):
        file = fd.askopenfilename(title="Choose A File", filetypes=[("Video files", VIDEO_FORMATS)])
        self.file_path = os.path.abspath(file)
        self.interface.set_file_path(self.file_path)
        print(self.file_path)

    @staticmethod
    def convert_to_audio(video_path, audio_path):
        try:
            video_clip = mp.VideoFileClip(video_path)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(audio_path)
            audio_clip.close()
            video_clip.close()
            messagebox.showinfo("Success!", "Conversion successfully completed!")
        except Exception as e:
            messagebox.showinfo("Error", str(e))

    def on_convert_btn(self):
        if self.file_path:
            new_path = self.interface.get_output_file_path(self.file_path)
            Controller.convert_to_audio(self.file_path, new_path)
