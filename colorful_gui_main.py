
import tkinter as tk
from tkinter import messagebox
from sorular import sorular
from muzikler import muzik_listesi
import random

class RuhHaliUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("🎭 Ruh Hali Müzik Önerici")
        self.root.geometry("600x400")
        self.root.configure(bg="#fce4ec")  # Pembe arka plan

        self.puanlar = {"mutlu": 0, "üzgün": 0, "motivasyon": 0, "yorgun": 0}
        self.soru_index = 0

        self.baslik_label = tk.Label(root, text="Mini Ruh Hali Testi", bg="#fce4ec", fg="#880e4f",
                                     font=("Comic Sans MS", 20, "bold"))
        self.baslik_label.pack(pady=10)

        self.soru_label = tk.Label(root, text="", wraplength=500, bg="#fce4ec", fg="#4a148c",
                                   font=("Arial", 14, "italic"))
        self.soru_label.pack(pady=10)

        self.secenekler_frame = tk.Frame(root, bg="#fce4ec")
        self.secenekler_frame.pack()

        self.goster_soru()

    def goster_soru(self):
        for widget in self.secenekler_frame.winfo_children():
            widget.destroy()

        if self.soru_index < len(sorular):
            soru = sorular[self.soru_index]
            self.soru_label.config(text=f"Soru {self.soru_index + 1}: {soru['soru']}")
            for harf, (metin, duygu) in soru["secenekler"].items():
                b = tk.Button(self.secenekler_frame, text=f"{harf}) {metin}",
                              font=("Arial", 12, "bold"), bg="#ce93d8", fg="white",
                              width=40, height=2, bd=0,
                              activebackground="#ab47bc",
                              command=lambda d=duygu: self.secenek_secildi(d))
                b.pack(pady=5)
        else:
            self.goster_sonuc()

    def secenek_secildi(self, duygu):
        self.puanlar[duygu] += 1
        self.soru_index += 1
        self.goster_soru()

    def goster_sonuc(self):
        ruh_hali = max(self.puanlar, key=self.puanlar.get)
        sarkilar = random.sample(muzik_listesi[ruh_hali], 3)
        mesaj = f"Ruh halin: {ruh_hali.upper()}\n\n🎵 Şarkı Önerileri:\n" + "\n".join(f"- {sarki}" for sarki in sarkilar)
        messagebox.showinfo("Sonuç", mesaj)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RuhHaliUygulamasi(root)
    root.mainloop()
