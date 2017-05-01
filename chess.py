import Tkinter
from PIL import Image, ImageTk

class game(Tkinter.Tk):
	def __init__(self, parent):
		Tkinter.Tk.__init__(self, parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.background_image=Tkinter.PhotoImage("board.gif")
		self.background_label = Tkinter.Label(image=self.background_image)
		self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
		self.grid()

		self.pawn_black = Tkinter.PhotoImage(file="resources/p_b.gif")
		self.pawn_white = Tkinter.PhotoImage(file="resources/p_w.gif")
		self.knight_black = Tkinter.PhotoImage(file="resources/n_b.gif")
		self.knight_white = Tkinter.PhotoImage(file="resources/n_w.gif")
		self.bishop_black = Tkinter.PhotoImage(file="resources/b_b.gif")
		self.bishop_white = Tkinter.PhotoImage(file="resources/b_w.gif")
		self.castle_black = Tkinter.PhotoImage(file="resources/c_b.gif")
		self.castle_white = Tkinter.PhotoImage(file="resources/c_w.gif")
		self.king_black = Tkinter.PhotoImage(file="resources/k_b.gif")
		self.king_white = Tkinter.PhotoImage(file="resources/k_w.gif")
		self.queen_black = Tkinter.PhotoImage(file="resources/q_b.gif")
		self.queen_white = Tkinter.PhotoImage(file="resources/q_w.gif")

		self.g0 = Tkinter.Button(self,highlightbackground='#ffffff',image=self.castle_white).grid(column=0,row=0,sticky="EW")
		self.g1 = Tkinter.Button(self,highlightbackground='#000000',image=self.knight_white).grid(column=1,row=0,sticky="EW")
		self.g2 = Tkinter.Button(self,borderwidth=0,bg="#ff0000",fg="#ff0000",highlightthickness=0,text="2").grid(column=2,row=0,sticky="EW")
		#,image=self.bishop_white
		self.g3 = Tkinter.Button(self,highlightbackground='#000000',image=self.queen_white).grid(column=3,row=0,sticky="EW")
		self.g4 = Tkinter.Button(self,highlightbackground='#ffffff',image=self.king_white).grid(column=4,row=0,sticky="EW")
		self.g5 = Tkinter.Button(self,highlightbackground='#000000',image=self.bishop_white).grid(column=5,row=0,sticky="EW")
		self.g6 = Tkinter.Button(self,highlightbackground='#ffffff',image=self.knight_white).grid(column=6,row=0,sticky="EW")
		self.g7 = Tkinter.Button(self,highlightbackground='#000000',image=self.castle_white).grid(column=7,row=0,sticky="EW")
		self.g8 = Tkinter.Button(self,highlightbackground='#000000',image=self.pawn_white).grid(column=0,row=1,sticky="EW")
		self.g9 = Tkinter.Button(self,highlightbackground='#ffffff',image=self.pawn_white).grid(column=1,row=1,sticky="EW")
		self.g10 = Tkinter.Button(self,highlightbackground='#000000',image=self.pawn_white).grid(column=2,row=1,sticky="EW")
		self.g11 = Tkinter.Button(self,highlightbackground='#ffffff',image=self.pawn_white).grid(column=3,row=1,sticky="EW")
		self.g12 = Tkinter.Button(self,highlightbackground='#000000',image=self.pawn_white).grid(column=4,row=1,sticky="EW")
		self.g13 = Tkinter.Button(self,highlightbackground='#ffffff',image=self.pawn_white).grid(column=5,row=1,sticky="EW")
		self.g14 = Tkinter.Button(self,highlightbackground='#000000',image=self.pawn_white).grid(column=6,row=1,sticky="EW")
		self.g15 = Tkinter.Button(self,highlightbackground='#ffffff',image=self.pawn_white).grid(column=7,row=1,sticky="EW")
		self.g16 = Tkinter.Button(self,highlightbackground='#ffffff').grid(column=0,row=2,sticky="EW")
		self.g17 = Tkinter.Button(self,highlightbackground='#000000').grid(column=1,row=2,sticky="EW")
		self.g18 = Tkinter.Button(self,highlightbackground='#ffffff').grid(column=2,row=2,sticky="EW")
		self.g19 = Tkinter.Button(self,highlightbackground='#000000').grid(column=3,row=2,sticky="EW")
		self.g20 = Tkinter.Button(self,highlightbackground='#ffffff').grid(column=4,row=2,sticky="EW")
		self.g21 = Tkinter.Button(self,highlightbackground='#000000').grid(column=5,row=2,sticky="EW")
		self.g22 = Tkinter.Button(self,highlightbackground='#ffffff').grid(column=6,row=2,sticky="EW")
		self.g23 = Tkinter.Button(self,highlightbackground='#000000').grid(column=7,row=2,sticky="EW")
		self.g24 = Tkinter.Button(self,highlightbackground='#ffffff').grid(column=0,row=3,sticky="EW")
		self.g25 = Tkinter.Button(self,highlightbackground='#000000').grid(column=1,row=3,sticky="EW")
		self.g26 = Tkinter.Button(self,highlightbackground='#ffffff').grid(column=2,row=3,sticky="EW")
		self.g27 = Tkinter.Button(self,highlightbackground='#000000').grid(column=3,row=3,sticky="EW")
		self.g28 = Tkinter.Button(self,highlightbackground='#ffffff').grid(column=4,row=3,sticky="EW")
		self.g29 = Tkinter.Button(self,highlightbackground='#000000').grid(column=5,row=3,sticky="EW")
		self.g30 = Tkinter.Button(self,highlightbackground='#ffffff').grid(column=6,row=3,sticky="EW")
		self.g31 = Tkinter.Button(self,highlightbackground='#000000').grid(column=7,row=3,sticky="EW")
		self.g32 = Tkinter.Button(self,highlightbackground='#ffffff').grid(column=0,row=4,sticky="EW")
		self.g33 = Tkinter.Button(self,highlightbackground='#000000').grid(column=1,row=4,sticky="EW")
		self.g34 = Tkinter.Button(self,highlightbackground='#ffffff').grid(column=2,row=4,sticky="EW")
		self.g35 = Tkinter.Button(self,highlightbackground='#000000').grid(column=3,row=4,sticky="EW")
		self.g36 = Tkinter.Button(self,highlightbackground='#ffffff').grid(column=4,row=4,sticky="EW")
		self.g37 = Tkinter.Button(self,highlightbackground='#000000').grid(column=5,row=4,sticky="EW")
		self.g38 = Tkinter.Button(self,highlightbackground='#ffffff').grid(column=6,row=4,sticky="EW")
		self.g39 = Tkinter.Button(self,highlightbackground='#000000').grid(column=7,row=4,sticky="EW")
		self.g40 = Tkinter.Button(self,highlightbackground='#ffffff').grid(column=0,row=5,sticky="EW")
		self.g41 = Tkinter.Button(self,highlightbackground='#000000').grid(column=1,row=5,sticky="EW")
		self.g42 = Tkinter.Button(self,highlightbackground='#ffffff').grid(column=2,row=5,sticky="EW")
		self.g43 = Tkinter.Button(self,highlightbackground='#000000').grid(column=3,row=5,sticky="EW")
		self.g44 = Tkinter.Button(self,highlightbackground='#ffffff').grid(column=4,row=5,sticky="EW")
		self.g45 = Tkinter.Button(self,highlightbackground='#000000').grid(column=5,row=5,sticky="EW")
		self.g46 = Tkinter.Button(self,highlightbackground='#ffffff').grid(column=6,row=5,sticky="EW")
		self.g47 = Tkinter.Button(self,highlightbackground='#000000').grid(column=7,row=5,sticky="EW")
		self.g48 = Tkinter.Button(self,highlightbackground='#ffffff',image=self.pawn_black).grid(column=0,row=6,sticky="EW")
		self.g49 = Tkinter.Button(self,highlightbackground='#000000',image=self.pawn_black).grid(column=1,row=6,sticky="EW")
		self.g50 = Tkinter.Button(self,highlightbackground='#ffffff',image=self.pawn_black).grid(column=2,row=6,sticky="EW")
		self.g51 = Tkinter.Button(self,highlightbackground='#000000',image=self.pawn_black).grid(column=3,row=6,sticky="EW")
		self.g52 = Tkinter.Button(self,highlightbackground='#ffffff',image=self.pawn_black).grid(column=4,row=6,sticky="EW")
		self.g53 = Tkinter.Button(self,highlightbackground='#000000',image=self.pawn_black).grid(column=5,row=6,sticky="EW")
		self.g54 = Tkinter.Button(self,highlightbackground='#ffffff',image=self.pawn_black).grid(column=6,row=6,sticky="EW")
		self.g55 = Tkinter.Button(self,highlightbackground='#000000',image=self.pawn_black).grid(column=7,row=6,sticky="EW")
		self.g56 = Tkinter.Button(self,highlightbackground='#ffffff',image=self.castle_black).grid(column=0,row=7,sticky="EW")
		self.g57 = Tkinter.Button(self,highlightbackground='#000000',image=self.knight_black).grid(column=1,row=7,sticky="EW")
		self.g58 = Tkinter.Button(self,highlightbackground='#ffffff',image=self.bishop_black).grid(column=2,row=7,sticky="EW")
		self.g59 = Tkinter.Button(self,highlightbackground='#000000',image=self.queen_black).grid(column=3,row=7,sticky="EW")
		self.g60 = Tkinter.Button(self,highlightbackground='#ffffff',image=self.king_black).grid(column=4,row=7,sticky="EW")
		self.g61 = Tkinter.Button(self,highlightbackground='#000000',image=self.bishop_black).grid(column=5,row=7,sticky="EW")
		self.g62 = Tkinter.Button(self,highlightbackground='#ffffff',image=self.knight_black).grid(column=6,row=7,sticky="EW")
		self.g63 = Tkinter.Button(self,highlightbackground='#000000',image=self.castle_black).grid(column=7,row=7,sticky="EW")
		
	"""
		#initialise whole board
		for x in xrange(16,48):
			if ((x%8)%2 == 0 and (x/8)%2 == 0) or ((x%8)%2 == 1 and (x/8)%2 == 1):
				self.x = Tkinter.Button(self,highlightbackground='#ffffff', text=str(x)).grid(column=(x%8),row=(x/8),sticky="EW")
			else:
				self.x = Tkinter.Button(self,highlightbackground='#000000', text=str(x)).grid(column=(x%8),row=(x/8),sticky="EW")
				
		#initialise specific pieces
		for x in xrange(8,19):
			if ((x%8)%2 == 0 and (x/8)%2 == 0) or ((x%8)%2 == 1 and (x/8)%2 == 1):
				temp = str(x) + "pawn_white"
				self.temp = Tkinter.PhotoImage(file="resources/p_w.gif")
				self.x = Tkinter.Button(self,highlightbackground='#ffffff', image=self.pawn_white, text=str(x)).grid(column=(x%8),row=(x/8),sticky="EW")
			else:
				temp = str(x) + "pawn_white"
				self.temp = Tkinter.PhotoImage(file="resources/p_w.gif")
				self.x = Tkinter.Button(self,highlightbackground='#000000', image=self.pawn_white, text=str(x)).grid(column=(x%8),row=(x/8),sticky="EW")

		#self.pawn_black = Tkinter.PhotoImage(file="resources/p_b.gif")
		#self.p_b = Tkinter.Button(self, image=self.pawn_black)
		#self.p_b.grid(column=0,row=0,sticky="EW")
"""

if __name__ == "__main__":
	app = game(None)
	app.title("Chess")
	app.mainloop()


"""
, height=3, width=5
, height=3, width=5
"""