import tkinter as tk

class Message(tk.Frame):

	def __init__(self, master):
		super().__init__(master)
		self.master = master
		self.pack()  
		self.text = ['Login', 'Register']
		self.buttons = []
		self.ans = [0]
		self.d = {0: tk.BooleanVar(), 1: tk.BooleanVar()}
		self.display()


	def getInfo(self):
		self.getLogin = self.d[0].get()
		self.getRegister = self.d[1].get()
		#print(self.getLogin, self.getRegister)

		if self.getLogin == True:
			self.ans[0] = True
		elif self.getRegister == True:
			self.ans[0] = False
		# else:
		# 	self.ans = False
		#print(self.ans)

	def getButton(self, index):
		label = tk.Label(self)
		label['text'] = self.text[index]

		button = tk.Checkbutton(self)
		button['variable'] = self.d[index]
		button['command'] = self.getInfo

		return label, button


	def display(self):
		for j in range(len(self.text)):
			self.buttons.append(self.getButton(j))

		for i in range(len(self.buttons)):
			for j in range(len(self.buttons[i])):
				self.buttons[i][j].grid(row=i, column=j)
				#print(self.buttons[i][j])

		self.getInfo()

		# Exit
		self.exit = tk.Button(self)
		self.exit['text'] = 'Ok'
		self.exit['command'] = self.quit
		self.exit.grid(row=len(self.buttons)+1, column=0)

if __name__ == '__main__':
	root = tk.Tk()
	m = Message(root)
	m.mainloop()