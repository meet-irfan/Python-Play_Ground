import tkinter as tk
from tkinter import colorchooser

class DigitalWhiteboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Whiteboard")
        self.root.geometry("800x600")

        # Initializing variables
        self.brush_color = "black"
        self.brush_size = 5
        self.old_x = None
        self.old_y = None

        # Setting up the canvas
        self.canvas = tk.Canvas(root, bg="white", width=800, height=500)
        self.canvas.pack(pady=20)

        # Brush options frame
        brush_options_frame = tk.Frame(root)
        brush_options_frame.pack()

        # Color button
        color_button = tk.Button(brush_options_frame, text="Pick Color", command=self.choose_color)
        color_button.grid(row=0, column=0, padx=10)

        # Brush size label and slider
        size_label = tk.Label(brush_options_frame, text="Brush Size:")
        size_label.grid(row=0, column=1, padx=10)

        self.size_slider = tk.Scale(brush_options_frame, from_=1, to=20, orient=tk.HORIZONTAL)
        self.size_slider.set(self.brush_size)
        self.size_slider.grid(row=0, column=2, padx=10)

        # Clear button
        clear_button = tk.Button(brush_options_frame, text="Clear", command=self.clear_canvas)
        clear_button.grid(row=0, column=3, padx=10)

        # Binding the canvas for drawing
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def choose_color(self):
        """Allows the user to pick a color for the brush."""
        self.brush_color = colorchooser.askcolor(color=self.brush_color)[1]

    def paint(self, event):
        """Draws on the canvas based on mouse movement."""
        self.brush_size = self.size_slider.get()

        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                    width=self.brush_size, fill=self.brush_color,
                                    capstyle=tk.ROUND, smooth=tk.TRUE)

        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        """Resets the coordinates after each stroke."""
        self.old_x = None
        self.old_y = None

    def clear_canvas(self):
        """Clears the canvas."""
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    whiteboard = DigitalWhiteboard(root)
    root.mainloop()
