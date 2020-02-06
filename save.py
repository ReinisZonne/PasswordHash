import tkinter as tk

class Message(tk.Frame):

	def __init__(self, master):
		super().__init__(master)
		self.master = master
		self.pack()
		self.ans = None  
		self.text = ['Login', 'Register']
		self.buttons = []
		self.display()
	def getInfo(self):
		self.getLogin = self.buttons[0][1]['variable']
		self.getRegister = self.buttons[1][1]['variable']

		if self.getLogin == 1 or self.getRegister == 0:
			self.ans = True
		else:
			self.ans = False

	def getButton(self, index):
		label = tk.Label(self)
		label['text'] = self.text[index]

		button = tk.Checkbutton(self)
		button['variable'] = tk.IntVar()
		button['command'] = self.getInfo

		return label, button


	def display(self):
		for j in range(len(self.text)):
			self.buttons.append(self.getButton(j))

		for i in range(len(self.buttons)):
			for j in range(len(self.buttons[i])):
				self.buttons[i][j].grid(row=i, column=j)
				#print(self.buttons[i][j])

		# Exit
		self.exit = tk.Button(self)
		self.exit['text'] = 'Ok'
		self.exit['command'] = self.quit
		self.exit.grid(row=len(self.buttons)+1, column=0)

if __name__ == '__main__':
	root = tk.Tk()
	m = Message(root)
	m.mainloop()