import tkinter as tk


class App(tk.Frame):

	def __init__(self, master):
		super().__init__(master)
		self.master = master
		self.pack()
		self.display = []
		self.email = None
		self.password = None
		self.newLogin = None
		self.labels = ['Email: ', 'Password: ']
		self.checkButton()
		#self.getDisplay()
		#self.confirm()
		

	def getDisplay(self):
		for index in range(len(self.labels)):
			self.display.append(self.setText(index))

		for i in range(len(self.display)):
			for j in range(len(self.display[i])):
				self.display[i][j].grid(row=i, column=j, sticky='W')

		
	def setText(self, index):
		# Label
		self.label = tk.Label(self)
		self.label['text'] = self.labels[index]

		# Entry
		self.entry = tk.Entry(self)
		self.entry['textvariable'] = tk.StringVar()
		self.entry['show'] = '*'
		
		return self.label, self.entry

	def getEntry(self):
		self.e = self.display[0][1]
		self.p = self.display[1][1]

		self.email = self.e.get()
		self.password = self.p.get()

	def confirm(self):
		login = tk.Button(self)
		login['text'] = 'Login'
		login['command'] = self.getEntry
		login.grid(row=len(self.display)+1, column=0, sticky='S')


	def checkButton(self):

		self.buttonOne = tk.Checkbutton(self)
		self.buttonOne['text'] = 'Login'
		self.buttonOne['variable'] = tk.IntVar()
		self.buttonOne['onvalue'] = 1
		self.buttonOne.grid(row=0, column=0)


		self.buttonTwo = tk.Checkbutton(self)
		self.buttonTwo['text'] = 'Register'
		self.buttonTwo['variable'] = tk.IntVar()
		self.buttonOne['onvalue'] = 1
		self.buttonTwo.grid(row=1, column=0)

		# ok = tk.Button(self)
		# ok['text'] = 'Ok'
		# ok['command'] = tk.Frame.destroy(tk.Frame)
		# ok.grid(row=2, column=0)



root = tk.Tk()
app = App(root)
app.mainloop()