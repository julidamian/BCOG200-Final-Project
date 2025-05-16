import turtle as t
import os
import tkinter as tk
from tkinter import filedialog, colorchooser
import io
from PIL import Image, ImageTk, ImageFilter, ImageOps


#will make the Display screen for the coloring book page. 
#the bottom of the screen will include the color wheel, the brushes, and an eraser. 

class ImageProcessor: 
    def __init__(self):
        self.original_image = None
        self.processed_image = None

    #getting image that is without user input
    #getting image that is from user input

    def load_image(self, filepath, max_size=(800,600)): #resizing image to fit the screen
        print(f"Loading image from: {filepath}")
        image = Image.open(filepath).convert("L") #turning image into something that can be colored in, monochromatic
        image.thumbnail(max_size)
        self.original_image = image
        self.processed_image = self.outline_image(image)
        return self.processed_image

    def outline_image(self, image):
        edges = image.filter(ImageFilter.FIND_EDGES) #finds boundaries or edges in an image, detects structure of objects in an image
        inverted = ImageOps.invert(edges)
        return inverted

class Display:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Coloring Book :D")
        self.root.geometry("800x700")
        self.root.resizable(True, True)

        self.color = "black"
        self.brush_size = 5
        self.drawing = False
        self.processor = ImageProcessor()
        self.current_image = None

        #creating the frame coloring book will work in 
        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.pack()

        self.image_canvas = tk.Canvas(self.canvas_frame, bg = "white", highlightthickness=0) #trying to not draw directly on the canvas
        self.image_canvas.place(x=0, y=0)

        self.image_canvas.bind("<B1-Motion>", self.paint)
        self.image_canvas.bind("<ButtonRelease-1>", self.stop_draw)

        self.interface_frame = tk.Frame(self.root, height=100)
        self.interface_frame.pack(fill="x") #fill horizontally

        self.image_options = ["bluey.png", "cat.jpg", "dog.jpg", "monkey.png", "penguin.png"]
        self.selected_image = tk.StringVar(self.root)
        self.selected_image.set(self.image_options[0])

        self.image_menu = tk.OptionMenu(self.interface_frame, self.selected_image, *self.image_options)
        self.image_menu.pack(side="left", padx=10)
        
        self.library_button = tk.Button(self.interface_frame, text="Choose This Image to Color", command=self.load_builtin_image)
        self.library_button.pack(side="left", padx=10)

        self.load_button = tk.Button(self.interface_frame, text="Upload Your Image", command=self.upload_image)
        self.load_button.pack(side="left", padx=10)

        self.color_button = tk.Button(self.interface_frame, text = "Pick Any Color!", command=self.choose_color)
        self.color_button.pack(side="left", padx=10)

        self.brush_slider = tk.Scale(self.interface_frame, from_=1, to=20, orient="horizontal", label="Brush Size")
        self.brush_slider.set(self.brush_size)
        self.brush_slider.pack(side="left", padx = 10)
        
        self.eraser_button = tk.Button(self.interface_frame, text="Eraser", command=lambda: self.set_color("white"))
        self.eraser_button.pack(side="left", padx = 10)

        self.save_button = tk.Button(self.interface_frame, text="Save", command=self.save_image)
        self.save_button.pack(side="right", padx=10)


    def load_builtin_image(self):
        filename = self.selected_image.get()
        path = os.path.join("images", filename)
        if os.path.exists(path):
            processed = self.processor.load_image(path)
            print("Image loaded successfully.")
            if processed:
                self.display_image(processed)
     
    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            processed = self.processor.load_image(file_path)
            if processed: 
                self.display_image(processed)

    
    def display_image(self, image):
        self.tk_img = ImageTk.PhotoImage(image)
        self.image_canvas.delete("all")
        self.image_canvas.config(width=image.width, height=image.height)
        self.image_canvas.create_image(0,0, image=self.tk_img, anchor="nw")

        total_height = image.height+100
        total_width = max(image.width, 800)

        self.root.geometry(f"{total_width}x{total_height}")
        self.canvas_frame.config(width=image.width, height=image.height)


    def choose_color(self):
        color_code = tk.colorchooser.askcolor(title="Choose color :)")[1]
        if color_code:
            self.color = color_code

    def set_color(self, new_color):
        self.color = new_color

    def paint(self, event):
        self.brush_size = self.brush_slider.get()
        x,y = event.x, event.y
        if self.drawing:
            self.image_canvas.create_oval(
                x - self.brush_size, y - self.brush_size,
                x + self.brush_size, y + self.brush_size,
                fill = self.color, outline=self.color
            )
        self.drawing = True
    
    def stop_draw(self, event):
        self.drawing = False

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=" .ps", filetypes=[("PostScript Files", "*.ps")])
        if file_path:
            self.image_canvas.postscript(file=file_path, colormode='color')

    
def main():
        app = Display()
        app.root.mainloop()

if __name__ == "__main__":
    main()
