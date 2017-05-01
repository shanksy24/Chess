for x in xrange(64):
 	print "self.g" + str(x) + " = Tkinter.Button(self,highlightbackground='#ffffff').grid(column=" + str(x%8) + ",row=" + str(x/8) + ",sticky=\"EW\")"