from tkinter import Tk, Canvas, PhotoImage, mainloop

WIDTH = 640
HEIGHT = 480
window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
canvas.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")


img.put("#ffffff", (100, 100))
img.put("#ffffff", (101, 100))
img.put("#ffffff", (102, 100))
img.put("#ffffff", (103, 100))

# x = 100
# y = 100
# while y < 480:
#     img.put("#ffffff", (x, y))
#     y += 1


mainloop()
