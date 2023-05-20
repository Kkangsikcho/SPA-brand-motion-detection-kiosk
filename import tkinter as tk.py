import tkinter as tk

def show_image():
    if var.get() == 1:
        image_label.config(image=tsimage)
    else:
        image_label.config(image="")

root2 = tk.Tk()

# 체크 버튼을 위한 변수
var = tk.IntVar()

# 체크 버튼 생성
check_button = tk.Checkbutton(root2, text="이미지 표시", variable=var, command=show_image)
check_button.pack()

# 이미지 표시를 위한 라벨
tsimage = tk.PhotoImage(file="C:\\Users\\cho11\\Desktop\\화이팅\\ts.png")
image_label = tk.Label(root2, image="") 
image_label.pack()

root2.mainloop()
