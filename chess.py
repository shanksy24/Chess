import Tkinter
from PIL import Image, ImageTk

class game(Tkinter.Tk):
	def __init__(self, parent):
		Tkinter.Tk.__init__(self, parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.grid()
		image = Image.open("png/pawn_black.png")
		photo = ImageTk.PhotoImage(image)
		label = Tkinter.Label(image=photo)
		label.image = photo
		label.pack()

if __name__ == "__main__":
	app = game(None)
	app.title("Chess")
	app.mainloop()
		