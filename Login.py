import tkinter as tk

class App(tk.Frame):

	def __init__(self, master):
		super().__init__(master)
		self.master = master
		self.pack()
		self.d = []
		self.labels = ['Email: ', 'Password: ']
		self.display()
		self.confirm()
		

	def display(self):
		for index in range(len(self.labels)):
			self.d.append(self.setText(index))

		for i in range(len(self.d)):
			for j in range(len(self.d[i])):
				self.d[i][j].grid(row=i, column=j, sticky='W')

		
	def setText(self, index):
		# Label
		self.label = tk.Label(self)
		self.label['text'] = self.labels[index]

		# Entry
		self.entry = tk.Entry(self)
		self.entry['textvariable'] = tk.StringVar()
		
		return self.label, self.entry

	def getEntry(self):
		self.email = self.d[0][1]
		self.password = self.d[1][1]
		print(self.email.get(), self.password.get())

	def confirm(self):
		login = tk.Button(self)
		login['text'] = 'Login'
		login['command'] = self.getEntry
		login.grid(row=len(self.d)+1, column=0, sticky='S')

root = tk.Tk()
app = App(root)
app.mainloop()