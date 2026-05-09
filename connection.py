import customtkinter as ctk
import tkinter as tk
import random

 


class Launcher:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.geometry("500x400")
        self.app.title("agario.launcher")
        self.app.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")


        self.username = None
        self.host = None
        self.port = None



        self.bubbles = []

        self.canvas = tk.Canvas(
            self.app,
            width=500,
            height=400,
            bg="#0f0f1a",
            highlightthickness=0
        )
        self.canvas.place(x=0, y=0)

        self.create_bubbles()
        self.animate_bubbles()

        self.create_ui()
        self.fade()

    def create_bubbles(self):
        for _ in range(25):
            x = random.randint(0, 500)
            y = random.randint(0, 400)
            r = random.randint(4, 12)

            bubble = self.canvas.create_oval(
                x, y, x + r, y + r,
                fill="#2a2a55",
                outline=""
            )

            speed = random.uniform(0.3, 1.0)
            self.bubbles.append([bubble, speed])

    def animate_bubbles(self):
        for obj, speed in self.bubbles:
            self.canvas.move(obj, 0, -speed)
            x1, y1, x2, y2 = self.canvas.coords(obj)

            if y2 < 0:
                x = random.randint(0, 500)
                y = 400
                size = random.randint(4, 12)
                self.canvas.coords(obj, x, y, x + size, y + size)

        self.app.after(30, self.animate_bubbles)

    def create_ui(self):
        self.frame = ctk.CTkFrame(self.app, width=320, height=300, corner_radius=20)
        self.frame.place(relx=0.5, rely=0.55, anchor="center")

        self.title = ctk.CTkLabel(
            self.app,
            text="Launcher",
            font=("Arial", 28, "bold"),
            text_color="#7aa2ff"
        )
        self.title.place(relx=0.5, rely=0.08, anchor="center")

        self.subtitle = ctk.CTkLabel(
            self.app,
            text="agario launcher",
            font=("Arial", 12),
            text_color="#aaaaaa"
        )
        self.subtitle.place(relx=0.5, rely=0.14, anchor="center")

        self.entry_name = ctk.CTkEntry(self.frame, placeholder_text="Ваш нік", width=220)
        self.entry_name.pack(pady=10)

        self.entry_ip = ctk.CTkEntry(self.frame, placeholder_text="IP", width=220)
        self.entry_ip.pack(pady=10)

        self.entry_port = ctk.CTkEntry(self.frame, placeholder_text="Порт", width=220)
        self.entry_port.pack(pady=10)

        self.button = ctk.CTkButton(self.frame, text="Увійти", command=self.login, width=200)
        self.button.pack(pady=20)

        self.button.bind("<Enter>", lambda e: self.button.configure(width=210))
        self.button.bind("<Leave>", lambda e: self.button.configure(width=200))

    def login(self):
        self.username = self.entry_name.get()
        self.host = self.entry_ip.get()
        self.port = int(self.entry_port.get())

        self.app.destroy()
        

       

    def fade(self, alpha=0):
        if alpha <= 1:
            self.app.attributes("-alpha", alpha)
            self.app.after(20, self.fade, alpha + 0.05)

    #def run(self):
        #self.app.mainloop()


#Launcher().run()