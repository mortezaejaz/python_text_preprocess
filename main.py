import tkinter as tk
import tkinter.ttk as ttk

def start_process():
    print('start process')

window = tk.Tk()
inner_frame = tk.Frame(window)
inner_frame.pack(ipadx=15, ipady=15, fill="both", expand=True)
tk.Label(inner_frame, text="متن ورودی", foreground="blue").pack()
textEntry = tk.StringVar()
txt_sentence = tk.Entry(inner_frame, width=150, justify='right', textvariable = textEntry).pack()
remove_other_char = tk.IntVar()
remove_emoji = tk.IntVar()
convert_informal = tk.IntVar()
remove_stopwords = tk.IntVar()
C1 = tk.Checkbutton(inner_frame, text = "حذف کاراکتر ها اضافه مانند (-, :, #, ...)", variable = remove_other_char).pack()
C2 = tk.Checkbutton(inner_frame, text = "حذف ایموجی ها", variable = remove_emoji,).pack()
C3 = tk.Checkbutton(inner_frame, text = "تبدیل متن به حالت نوشتار رسمی", variable = convert_informal,).pack()
C4 = tk.Checkbutton(inner_frame, text = "حذف کلمات اضافه", variable = remove_stopwords,).pack()
tk.Label(inner_frame, text="").pack()
btn_start = tk.Button(inner_frame, text="پردازش متن", command=start_process, background="yellow").pack()
ttk.Label(inner_frame, text="نتیجه", foreground="blue").pack()
txt_result = tk.Entry(inner_frame, width=150, justify='right').pack()
tk.Label(inner_frame, text="کلمات", foreground="blue").pack()
txt_words = tk.Text(inner_frame).pack()

window.mainloop()
