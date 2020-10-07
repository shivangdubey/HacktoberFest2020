from tkinter import *
from tkinter import ttk, colorchooser, filedialog
import PIL
from PIL import ImageGrab
from tkinter import ttk, colorchooser, filedialog
from tkinter.colorchooser import askcolor
from tkinter.filedialog import asksaveasfilename, askopenfilename
from PIL import ImageTk
from PIL import Image, ImageEnhance, ImageFilter

class main:

    DEFAULT_COLOR = 'black'

    def __init__(self, master):
       
        self.master = master
        global var1, var2, var3
        var1 = DoubleVar()
        var2 = DoubleVar()
        var3 = DoubleVar()


        self.pen_button = Button(self.master, text='Pen', command=self.use_pen, relief=RIDGE)
        self.pen_button.grid(row=0, column=0)
        
        self.color_button = Button(self.master, text='Color Picker', command=self.choose_color, relief=RIDGE)
        self.color_button.grid(row=0, column=1)

        self.bg_color = Button(self.master, text='Change Background color', command=self.change_bg, relief=RIDGE)
        self.bg_color.grid(row=0, column=2)

        self.eraser_button = Button(self.master, text='Eraser', command=self.use_eraser, relief=RIDGE)
        self.eraser_button.grid(row=0, column=3)

        self.delete_button = Button(self.master, text='Clear Canvas', command=self.clear_all, relief=RIDGE)
        self.delete_button.grid(row=0, column=4)


        self.choose_size_button = Scale(self.master, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=5)


       
        self.choose_sharpness_button = Scale(self.master, from_=1, to=10, variable= var1, orient=HORIZONTAL)
        self.choose_sharpness_button.grid(row=1, column=0)

        self.choose_brightness_button = Scale(self.master, from_=1, to=10, variable= var2, orient=HORIZONTAL)
        self.choose_brightness_button.grid(row=1, column=1)


        self.choose_contrast_button = Scale(self.master, from_=1, to=10, variable= var3, orient=HORIZONTAL)
        self.choose_contrast_button.grid(row=1, column=2)

        Label(self.master, text='Change Sharpness',font=('arial 10')).grid(row=2,column=0)
        Label(self.master, text='Change Brightness',font=('arial 10')).grid(row=2,column=1)
        Label(self.master, text='Change Contrast',font=('arial 10')).grid(row=2,column=2)


        self.c = Canvas(self.master, bg='white', width=1200, height=1000)
        self.c.grid(row=3, columnspan=6)

        self.menubar = Menu(self.master)  
        self.menubar.add_command(label="Load Image", command = self.load_img)  
        self.menubar.add_command(label="Save Image", command = self.save)
        self.menubar.add_command(label="Blur Image", command = self.blur_img)
        self.menubar.add_command(label="Black & White Image", command = self.color_img)
        self.menubar.add_command(label="Sharpen Image", command = self.sharp_img)
        self.menubar.add_command(label="Brighten Image", command = self.bright_img)
        self.menubar.add_command(label="Contrast Image", command = self.contrast_img)
        self.master.config(menu = self.menubar)

        self.setup()

    def setup(self):
        
        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.color_bg = 'white'
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def clear_all(self):
        self.c.delete(ALL)

    def save(self):
        file = filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics','*.png')])
        if file:
            x = self.master.winfo_rootx() + self.c.winfo_x()
            y = self.master.winfo_rooty() + self.c.winfo_y()
            x1 = x + self.c.winfo_width()
            y1 = y + self.c.winfo_height()

            PIL.ImageGrab.grab().crop((x,y,x1,y1)).save(file + '.png')

    #image loading functionality
    def load_img(self):
        global img1
        self.filename = askopenfilename()
        self.img = Image.open(self.filename)
        img1 = self.img
        self.c.image = ImageTk.PhotoImage(self.img)
        self.c.create_image(0,0, image = self.c.image, anchor = 'nw') 

    #Blurring the image
    def blur_img(self):
        enhancer = ImageEnhance.Sharpness(img1)
        # enhancer.enhance(0)
        sharpness = 0.0
        img_blurred = enhancer.enhance(sharpness)
        self.c.image = ImageTk.PhotoImage(img_blurred)
        self.c.create_image(0,0, image = self.c.image, anchor = 'nw')

    #Sharpening the image
    def sharp_img(self):
        enhancer = ImageEnhance.Sharpness(img1)
        sharpness = int(var1.get())
        img_sharpen = enhancer.enhance(sharpness)
        self.c.image = ImageTk.PhotoImage(img_sharpen)
        self.c.create_image(0,0, image = self.c.image, anchor = 'nw')


    #Brightening the image
    def bright_img(self):
        enhancer = ImageEnhance.Brightness(img1)
        # enhancer.enhance(0)
        brightnes = int(var2.get())
        img_brighten = enhancer.enhance(brightnes)
        self.c.image = ImageTk.PhotoImage(img_brighten)
        self.c.create_image(0,0, image = self.c.image, anchor = 'nw')


    #Applying contrast effect
    def contrast_img(self):
        enhancer = ImageEnhance.Contrast(img1)
        # enhancer.enhance(0)
        contrast = int(var3.get())
        img_contrast = enhancer.enhance(contrast)
        self.c.image = ImageTk.PhotoImage(img_contrast)
        self.c.create_image(0,0, image = self.c.image, anchor = 'nw')


    #Black & White Effect
    def color_img(self):
        enhancer = ImageEnhance.Color(img1)
        bw = 0.0
        img_black_white = enhancer.enhance(bw)
        self.c.image = ImageTk.PhotoImage(img_black_white)
        self.c.create_image(0,0, image = self.c.image, anchor = 'nw')

    def choose_color(self):
        self.eraser_on = False
        color = colorchooser.askcolor(color = self.color)[1]
        if color != None:
            self.color = color
        else:
            return None

    def change_bg(self):  #changing the background color canvas
        self.color_bg=colorchooser.askcolor(color=self.color_bg)[1]
        self.c['bg'] = self.color_bg

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.penwidth = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.penwidth, fill=paint_color,
                               capstyle=ROUND, smooth=True, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    root = Tk()
    main(root)
    root.title('Paint & Photo Editor')
    root.mainloop()
