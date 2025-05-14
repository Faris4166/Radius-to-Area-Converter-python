from tkinter import *

# สร้างหน้าต่างหลัก
root = Tk()
root.title("หาค่าวงกลม")
root.geometry("450x200")
root.resizable(False, False)

# ฟอนต์หลัก
main_font = ("TH Sarabun New", 18)

# แถวที่ 0: ป้อนรัศมี
Label(root, text="รัศมี (หน่วย)", font=main_font).grid(row=0, column=0, sticky=W, padx=10, pady=10)
radius = IntVar()
et = Entry(root, width=20, textvariable=radius, font=main_font)
et.grid(row=0, column=1, padx=10, pady=10)

# แถวที่ 1: แสดงผลลัพธ์พื้นที่
Label(root, text="พื้นที่วงกลม", font=main_font).grid(row=1, column=0, sticky=W, padx=10, pady=10)
et2 = Entry(root, width=20, font=main_font, state="readonly")
et2.grid(row=1, column=1, padx=10, pady=10)

# ฟังก์ชันคำนวณ
def calculate():
    try:
        r = radius.get()
        area = 3.14 * r**2
        et2.config(state="normal")
        et2.delete(0, END)
        et2.insert(0, f"{area:.2f}")
        et2.config(state="readonly")
    except Exception as e:
        et2.config(state="normal")
        et2.delete(0, END)
        et2.insert(0, "กรุณากรอกตัวเลข")
        et2.config(state="readonly")

# ฟังก์ชันล้างค่า
def deletText():
    et.delete(0, END)
    et2.config(state="normal")
    et2.delete(0, END)
    et2.config(state="readonly")

# แถวที่ 2: ปุ่ม
btn1 = Button(root, text="คำนวณ", command=calculate, font=main_font, bg="#4CAF50", fg="white", width=10)
btn1.grid(row=2, column=0, padx=10, pady=20)

btn2 = Button(root, text="ล้างค่า", command=deletText, font=main_font, bg="#f44336", fg="white", width=10)
btn2.grid(row=2, column=1, padx=10, pady=20)

root.mainloop()
