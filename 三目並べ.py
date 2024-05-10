from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# 先行Aが〇、後攻Bが✕になるように定義
def clicked(btn):
    global player
    if player == "A":
        btn.config(text="〇", state=DISABLED)
        btn = "〇"
        player = "B"
    else:
        btn.config(text="✕", state=DISABLED)
        btn = "✕"
        player = "A"
    
    # メッセージボックスで勝敗判定
    if ((b1["text"]==b2["text"]==b3["text"]=="〇")
        or(b4["text"]==b5["text"]==b6["text"]=="〇")
        or(b7["text"]==b8["text"]==b9["text"]=="〇")
        or(b1["text"]==b4["text"]==b7["text"]=="〇")
        or(b2["text"]==b5["text"]==b8["text"]=="〇")
        or(b3["text"]==b6["text"]==b9["text"]=="〇")
        or(b1["text"]==b5["text"]==b9["text"]=="〇")
        or(b3["text"]==b5["text"]==b7["text"]=="〇")):
        messagebox.showinfo("ゲーム終了", "〇の勝ち！")
        root.destroy()
    elif ((b1["text"]==b2["text"]==b3["text"]=="✕")
        or(b4["text"]==b5["text"]==b6["text"]=="✕")
        or(b7["text"]==b8["text"]==b9["text"]=="✕")
        or(b1["text"]==b4["text"]==b7["text"]=="✕")
        or(b2["text"]==b5["text"]==b8["text"]=="✕")
        or(b3["text"]==b6["text"]==b9["text"]=="✕")
        or(b1["text"]==b5["text"]==b9["text"]=="✕")
        or(b3["text"]==b5["text"]==b7["text"]=="✕")):
        messagebox.showinfo("ゲーム終了", "✕の勝ち！")
        root.destroy()
    elif all(button["text"] in ["〇","✕"] for button in [b1, b2, b3, b4, b5, b6, b7, b8, b9]):
        messagebox.showinfo("ゲーム終了", "引き分け")
        root.destroy()

root = Tk()
root.title("三目並べ")

player = "A"

# ボタンの定義（幅、高さ、座標）
b1 = Button(root, width=13, height=6, command=lambda: clicked(b1))
b1.grid(row=0,column=0)
b2 = Button(root, width=13, height=6, command=lambda: clicked(b2))
b2.grid(row=0,column=1)
b3 = Button(root, width=13, height=6, command=lambda: clicked(b3))
b3.grid(row=0,column=2)
b4 = Button(root, width=13, height=6, command=lambda: clicked(b4))
b4.grid(row=1,column=0)
b5 = Button(root, width=13, height=6, command=lambda: clicked(b5))
b5.grid(row=1,column=1)
b6 = Button(root, width=13, height=6, command=lambda: clicked(b6))
b6.grid(row=1,column=2)
b7 = Button(root, width=13, height=6, command=lambda: clicked(b7))
b7.grid(row=2,column=0)
b8 = Button(root, width=13, height=6, command=lambda: clicked(b8))
b8.grid(row=2,column=1)
b9 = Button(root, width=13, height=6, command=lambda: clicked(b9))
b9.grid(row=2,column=2)

root.mainloop()