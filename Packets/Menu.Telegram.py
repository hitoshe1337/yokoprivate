import tkinter as tk
import webbrowser

def open_telegram():
    webbrowser.open("https://t.me/Puvay_Servers")

root = tk.Tk()
root.title("Telegram Yönlendirme")

root.geometry("400x200")

label = tk.Label(root, text="Telegram kanalımıza katılmak için aşağıdaki butona tıklayın!")
label.pack(pady=20)

telegram_button = tk.Button(root, text="Telegram'a Katıl", command=open_telegram, bg="blue", fg="white")
telegram_button.pack(pady=10)

root.mainloop()