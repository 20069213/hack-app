import tkinter as tk
from tkinter import messagebox
import time

# إعداد النافذة الرئيسية للتطبيق
app = tk.Tk()
app.title("تطبيق الهكر الأخلاقي المتطور")
app.geometry("400x550")
app.config(bg="#0b0f19") # خلفية داكنة احترافية

# عنوان التطبيق
title_label = tk.Label(
    app, 
    text=" نظام اختراق الهواتف المتطور ", 
    fg="#00ffcc", 
    bg="#0b0f19", 
    font=("Arial", 14, "bold")
)
title_label.pack(pady=20)

# حقل إدخال رقم الهاتف
phone_label = tk.Label(
    app, 
    text="أدخل رقم الهاتف المستهدف:", 
    fg="#ffffff", 
    bg="#0b0f19", 
    font=("Arial", 10, "bold")
)
phone_label.pack(anchor="w", padx=30)

phone_entry = tk.Entry(
    app, 
    width=28, 
    font=("Arial", 14), 
    bg="#1a2238", 
    fg="#00ffcc", 
    insertbackground="white"
)
phone_entry.pack(pady=10, padx=30)

# صندوق عرض الحالة أو السجل
status_box = tk.Text(
    app, 
    height=8, 
    width=32, 
    bg="#121826", 
    fg="#00ffcc", 
    font=("Courier", 10)
)
status_box.pack(pady=10)
status_box.insert(tk.END, "[ النظام جاهز في انتظار الهدف... ]\n")

# الدالة اللي بتشتغل لما ندوس على زر الاختراق
def run_hack():
    target = phone_entry.get()
    if target == "":
        messagebox.showerror("خطأ", "برجاء كتابة رقم الهاتف أولاً!")
    else:
        status_box.delete("1.0", tk.END)
        status_box.insert(tk.END, f"[*] جاري الاتصال بالرقم: {target}\n")
        app.update()
        
        time.sleep(0.5)
        status_box.insert(tk.END, "[+] يتم تجاوز جدار الحماية...\n")
        app.update()
        
        time.sleep(0.5)
        status_box.insert(tk.END, "[+] تم سحب الثغرات بنجاح!\n")
        app.update()
        
        time.sleep(0.5)
        status_box.insert(tk.END, "[✔] الحالة: تم الاختراق بنجاح! 😎\n")
        messagebox.showinfo("نجاح العملية", f"تم اختراق الجهاز {target} بنجاح تام!")

# زر بدء الاختراق الرئيسي
hack_button = tk.Button(
    app, 
    text="بدء عملية الاختراق ⚡", 
    bg="#ff0055", 
    fg="white", 
    font=("Arial", 12, "bold"),
    width=24,
    command=run_hack
)
hack_button.pack(pady=20)

# تشغيل التطبيق
app.mainloop()
