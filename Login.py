import tkinter as tk
import hashlib as hs
from save import Message


class App(tk.Frame):

	def __init__(self, master):
		super().__init__(master)
		self.master = master
		self.ans = 0
		self.pack()
		self.display = []
		self.email = None
		self.password = None
		self.labels = ['Email: ', 'Password: ']
		self.getDisplay()
		self.confirm()
		

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
		if index == 1:		
			self.entry['show'] = '*'
	
		return self.label, self.entry

	def getEntry(self):
		self.e = self.display[0][1]
		self.p = self.display[1][1]

		self.email = self.e.get()
		self.password = self.p.get()
		self.hashPassword = hs.sha256(b'self.password')
		#self.hashPassword = hs.name(self.hashPassword)

		with open('save.txt', 'w') as save:
			save.write(self.email)
			save.write('\n')
			save.write(self.hashPassword.hexdigest())

	def confirm(self):
		login = tk.Button(self)
		login['text'] = 'Login'
		login['command'] = self.getEntry
		login.grid(row=len(self.display)+1, column=0, sticky='S')


if __name__ == '__main__':
	root = tk.Tk()
	app = App(root)
	app.mainloop()