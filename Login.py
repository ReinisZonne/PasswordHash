import tkinter as tk

class App(tk.Frame):

	def __init__(self, master):
		super().__init__(master)
		self.master = master
		self.pack()
		self.d = []
		self.labels = ['Email: ', 'Password: ']
		self.display()

	def display(self):
		for index in range(len(self.labels)):
			self.d.append(self.setText(index))

		for i in range(len(self.d)):
			for j in range(len(self.d[i])):
				self.d[i][j].grid(row=i, column=j)

	def setText(self, index):
		# Label
		self.label = tk.Label(self)
		self.label['text'] = self.labels[index]

		# Entry
		self.entry = tk.Entry(self)
		self.entry['textvariable'] = tk.StringVar()
		
		return self.label, self.entry

root = tk.Tk()
app = App(root)
app.mainloop()