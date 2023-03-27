import tkinter as tk

class TkGUI:
    def __init__(self,  Video, pic, bg="#F8F8F8", title='Janus AI', geomtry='400x200', ico='janus.ico'):
        self.geomtry = geomtry
        self.Video = Video
        self.pic = pic
        self.bg = bg
        self.ico = ico
        self.title = title

    def run(self) -> None:
        root = tk.Tk()
        root.title(self.title)
        root.geometry(self.geomtry)
        root.configure(bg=self.bg)
        root.iconbitmap(self.ico)
        label = tk.Label(root, text="Video file:", font=('Arial', 14))
        label.pack(pady=10)

        browse_button = tk.Button(root, text="Video File", command=self.Video)
        browse_button.pack()

        label = tk.Label(root, text="Image file:", font=('Arial', 14))
        label.pack(pady=10)


        browse_button2 = tk.Button(root, text="Image File", command=self.pic)
        browse_button2.pack()

        run_btn = tk.Button(root, text='Swap', command=root.quit).pack(pady=10)

        root.mainloop()
