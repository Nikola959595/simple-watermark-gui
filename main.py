from tkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw
from tkinter import filedialog


root = Tk()

root.title("Image Watermarking")
root.config(padx=50, pady=25)
root.geometry("400x400")


IMAGE_PATH = ""
ORIGINAL_IMAGE = None
WATERMARK_IMAGE = None


def upload():
    global IMAGE_PATH, ORIGINAL_IMAGE
    file_path = filedialog.askopenfilename(filetypes=[('.jpg', '*.jpg')])
    if file_path:
        IMAGE_PATH = file_path
        ORIGINAL_IMAGE = Image.open(IMAGE_PATH)
        display_image= ORIGINAL_IMAGE.copy()
        display_image.thumbnail((200, 200))
        img = ImageTk.PhotoImage(display_image)
        canvas.create_image(100, 100, image= img)
        canvas.image = img
        watermark_btn.place(x= 125, y= 325)


def watermark():
    global WATERMARK_IMAGE
    if ORIGINAL_IMAGE:
        watermark_image = ORIGINAL_IMAGE.copy()
        draw = ImageDraw.Draw(watermark_image)

        w, h = watermark_image.size
        x, y = int(w / 2), int(h / 2)
        if x > y:
            font_size = y
        elif y > x:
            font_size = x
        else:
            font_size = x
        font = ImageFont.truetype('arial.ttf', int(font_size/6))

        draw.text((x,y), "NIKOLA WATERMARK", fill=(255,255,255), font=font, anchor='ms')
        WATERMARK_IMAGE = watermark_image
        display_image = watermark_image.copy()
        display_image.thumbnail((200,200))
        img = ImageTk.PhotoImage(display_image)
        canvas.create_image(100,100, image = img)
        canvas.image = img
        download_btn.place(x= 125, y= 350)   

   


def download():
    global WATERMARK_IMAGE
    if WATERMARK_IMAGE:
        save_path = filedialog.asksaveasfilename(defaultextension='.jpg',filetypes=[("JPG files", "*.jpg")])
        if save_path:
            WATERMARK_IMAGE.save(save_path)




welcome_txt = Label(text="Image Watermarking App", font=("Arial", 20))
welcome_txt.grid(row=1, column=1)
canvas = Canvas(width=200, height = 200, highlightthickness=0)
canvas.grid(row=2,column=1)

watermark_btn = Button(text ='Watermark', command=watermark)
upload_btn = Button(text = "Upload", command=upload)
download_btn = Button(text = "Download", command = download)
upload_btn.place(x= 125, y=300)


root.mainloop()