import customtkinter as ctk
import tkinter as tk
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("500x400")
app.title("agario.launcher")
app.resizable(False, False)

# --------- АНІМАЦІЯ ФОНУ ----------
canvas = tk.Canvas(app, width=500, height=400, bg="#0f0f1a", highlightthickness=0)
canvas.place(x=0, y=0)

bubbles = []

for _ in range(25):
    x = random.randint(0, 500)
    y = random.randint(0, 400)
    r = random.randint(4, 12)
    bubble = canvas.create_oval(x, y, x + r, y + r, fill="#2a2a55", outline="")
    speed = random.uniform(0.3, 1.0)
    bubbles.append([bubble, speed])


def animate_bubbles():
    for b in bubbles:
        obj, speed = b
        canvas.move(obj, 0, -speed)
        x1, y1, x2, y2 = canvas.coords(obj)

        if y2 < 0:
            new_x = random.randint(0, 500)
            new_y = 400
            canvas.coords(obj, new_x, new_y, new_x + 10, new_y + 10)

    app.after(30, animate_bubbles)


animate_bubbles()

# --------- UI ФРЕЙМ ----------
frame = ctk.CTkFrame(app, width=320, height=300, corner_radius=20)
frame.place(relx=0.5, rely=0.55, anchor="center")

# --------- ЗАГОЛОВОК LAUNCHER ----------
title = ctk.CTkLabel(
    app,
    text="Launcher",
    font=("Arial", 28, "bold"),
    text_color="#7aa2ff"
)
title.place(relx=0.5, rely=0.08, anchor="center")

subtitle = ctk.CTkLabel(
    app,
    text="agario launcher",
    font=("Arial", 12),
    text_color="#aaaaaa"
)
subtitle.place(relx=0.5, rely=0.14, anchor="center")


# --------- ПОЛЯ ----------
entry_name = ctk.CTkEntry(frame, placeholder_text="Ваш нік", width=220)
entry_name.pack(pady=10)

entry_ip = ctk.CTkEntry(frame, placeholder_text="IP", width=220)
entry_ip.pack(pady=10)

entry_port = ctk.CTkEntry(frame, placeholder_text="Порт", width=220)
entry_port.pack(pady=10)


def login():
    print(entry_name.get(), entry_ip.get(), entry_port.get())


button = ctk.CTkButton(frame, text="Увійти", command=login, width=200)
button.pack(pady=20)

# --------- HOVER ----------
button.bind("<Enter>", lambda e: button.configure(width=210))
button.bind("<Leave>", lambda e: button.configure(width=200))

# --------- FADE IN ----------
def fade(alpha=0):
    if alpha <= 1:
        app.attributes("-alpha", alpha)
        app.after(20, fade, alpha + 0.05)

app.attributes("-alpha", 0)
fade()

app.mainloop()