import tkinter as tk


price_bottomw = {"여성 청바지": 30000, "반바지": 35000, "운동복 바지": 50000, "면바지": 50000, "치마": 70000}
price_topw = {"긴팔티": 30000, "반팔티": 35000, "셔츠": 40000, "재킷": 45000, "가죽 재킷": 50000}

order_bottomw = {}
order_topw = {}

total_pricew = 0


def show_bottomw():
    btn_bottomw.configure(bg="yellow")
    btn_topw.configure(bg="white")
    frame8.pack_forget()
    frame7.pack_forget()
    frame6.pack(fill="both", expand=True)
    frame8.pack(fill="both", expand=True)


def show_topw():
    btn_bottomw.configure(bg="white")
    btn_topw.configure(bg="yellow")
    frame8.pack_forget()
    frame6.pack_forget()
    frame7.pack(fill="both", expand=True)
    frame8.pack(fill="both", expand=True)


def bottom_addw(m):
    global price_bottomw, order_bottomw, total_pricew
    if m not in price_bottomw:
        print("입력한 메뉴가 존재하지 않습니다.")
    this_pricew = price_bottomw.get(m)
    total_pricew += this_pricew

    if m in order_bottomw:
        order_bottomw[m] = order_bottomw.get(m) + 1
    else:
        order_bottomw[m] = 1
    print_orderw()
    price_pricew()


def top_addw(m):
    global price_bottomw, order_bottomw, total_pricew
    if m not in price_topw:
        print("입력한 메뉴가 존재하지 않습니다.")
    this_pricew = price_topw.get(m)
    total_pricew += this_pricew

    if m in order_topw:
        order_topw[m] = order_topw.get(m) + 1
    else:
        order_topw[m] = 1
    print_orderw()
    price_pricew()


def print_orderw():
    global order_bottomw, order_topw

    tmp = ""
    price_tmp = 0
    for i in order_bottomw:
        price_tmp = price_bottomw[i] * order_bottomw.get(i)
        tmp = tmp + i + " X " + str(order_bottomw.get(i)) +  " = " + str(price_tmp)+"\n"
    for i in order_topw:
        price_tmp = price_topw[i] * order_topw.get(i)
        tmp = tmp + i + " X " + str(order_topw.get(i)) +  " = " + str(price_tmp)+"\n"

    text_1.delete('1.0', tk.END)
    text_1.insert(tk.INSERT, tmp)


def order_end():
    global total_pricew, order_bottomw, order_topw
    total_pricew = 0
    del order_bottomw
    del order_topw

    order_bottomw = {}
    order_topw = {}
    price_pricew()
    print_orderw()
    show_bottomw()


def price_pricew():
    global total_pricew
    label_price.configure(text=str(total_pricew)+" 원")


window = tk.Tk()
window.title("주문 프로그램")
window.geometry("600x400+500+300")
window.resizable(False, False)

frame1 = tk.Frame(window, width="600", height="10")
frame1.pack(fill="both")

frame6 = tk.Frame(window, width="600")
frame6.pack(fill="both", expand=True)

frame7 = tk.Frame(window, width="600")
# frame7.pack(fill="both", expand=True)

frame8 = tk.Frame(window, width="600", height="10")
frame8.pack(fill="both", expand=True)

btn_bottomw = tk.Button(frame1, text="하의", padx="10", pady="10", bg="yellow", command=show_bottomw)
btn_bottomw.grid(row=0, column=0, padx=10, pady=10)

btn_topw = tk.Button(frame1, text="상의", padx="10", pady="10", bg="white", command=show_topw)
btn_topw.grid(row=0, column=1, padx=10, pady=10)

btn_end = tk.Button(frame1, text="주문종료", padx="10", pady="10", command=order_end)
btn_end.grid(row=0, column=2, padx=10, pady=10)

label_price = tk.Label(frame1, text="0 원", width="20", padx=10, pady="10", fg="blue", font='Arial 15')
label_price.grid(row=0, column="3", padx="10", pady="10")

# 바지
btn_bottomw_1 = tk.Button(frame6, text="여성 청바지\n(30000원)", padx="10", pady="10", width="10", command=lambda: bottom_addw('여성 청바지'))
btn_bottomw_1.grid(row=0, column=0, padx=10, pady=10)

btn_bottomw_2 = tk.Button(frame6, text="반바지\n(35000원)", padx="10", pady="10", width="10", command=lambda: bottom_addw('반바지'))
btn_bottomw_2.grid(row=0, column=1, padx=10, pady=10)

btn_bottomw_3 = tk.Button(frame6, text="운동복 바지\n(50000원)", padx="10", pady="10", width="10", command=lambda: bottom_addw('운동복 바지'))
btn_bottomw_3.grid(row=0, column=2, padx=10, pady=10)

btn_bottomw_4 = tk.Button(frame6, text="면바지\n(50000원)", padx="10", pady="10", width="10", command=lambda: bottom_addw('면바지'))
btn_bottomw_4.grid(row=0, column=3, padx=10, pady=10)

btn_bottomw_5 = tk.Button(frame6, text="치마\n(70000원)", padx="10", pady="10", width="10", command=lambda: bottom_addw('치마'))
btn_bottomw_5.grid(row=0, column=4, padx=10, pady=10)


# 음료
btn_topw_1 = tk.Button(frame7, text="긴팔티\n(30000원)", padx="10", pady="10", width="10", command=lambda: top_addw('긴팔티'))
btn_topw_1.grid(row=0, column=0, padx=10, pady=10)

btn_topw_2 = tk.Button(frame7, text="반팔티\n(35000원)", padx="10", pady="10", width="10", command=lambda: top_addw('반팔티'))
btn_topw_2.grid(row=0, column=1, padx=10, pady=10)

btn_topw_3 = tk.Button(frame7, text="셔츠\n(40000원)", padx="10", pady="10", width="10", command=lambda: top_addw('셔츠'))
btn_topw_3.grid(row=0, column=2, padx=10, pady=10)

btn_topw_4 = tk.Button(frame7, text="재킷\n(45000원)", padx="10", pady="10", width="10", command=lambda: top_addw('재킷'))
btn_topw_4.grid(row=0, column=3, padx=10, pady=10)

btn_topw_5 = tk.Button(frame7, text="가죽 재킷\n(50000원)", padx="10", pady="10", width="10", command=lambda: top_addw('가죽 재킷'))
btn_topw_5.grid(row=0, column=4, padx=10, pady=10)


# 주문 리스트
text_1 = tk.Text(frame8, height="10")
text_1.pack()

window.mainloop()