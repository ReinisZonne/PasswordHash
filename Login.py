import tkinter as tk
import hashlib as hs
from save import Message


class App(tk.Frame):

	def __init__(self, master, ans):
		super().__init__(master)
		self.master = master
		self.ans = ans
		self.pack()
		self.display = []
		# self.email = None
		self.password = None
		self.hashPassword = None
		self.labels = ['Email: ', 'Password: ']
		if self.ans[0] == False:
			self.labels.append('Verify password: ')
		self.getDisplay()


	def getDisplay(self):
		for index in range(len(self.labels)):
			self.display.append(self.setText(index))

		for i in range(len(self.display)):
			for j in range(len(self.display[i])):
				self.display[i][j].grid(row=i, column=j, sticky='W')

		self.confirm()
		self.exitButton()


		
	def setText(self, index):
		# Label
		self.label = tk.Label(self)
		self.label['text'] = self.labels[index]

		# Entry
		self.entry = tk.Entry(self)
		self.entry['textvariable'] = tk.StringVar()
		if index >= 1:		
			self.entry['show'] = '*'
	
		return self.label, self.entry

	def getEntry(self):

		self.hashPassword = hs.sha256(b'self.display[1][1].get()').hexdigest()


		if len(self.labels) == 3: # Registration		
			with open('save.txt', 'w') as save:
				#save.write(email)
				#save.write('\n')
				save.write(self.hashPassword)
			correct = tk.Label(self)
			correct['text'] = 'Signing successful!'
			correct['fg'] = 'green'
			correct.grid(row=len(self.display)+1, column=0, sticky='W')
		else:
			with open('save.txt') as savedFile:
				savedPass = savedFile.readline()
			#print(self.savedPass)
			#print(self.hashPassword)
			if savedPass == self.hashPassword:
				self.correctPass()
			else:
				self.invalidPass()

	def invalidPass(self):
		text = tk.Label(self)
		text['text'] = 'Invalid password!'
		text['fg'] = 'red'
		text.grid(row=len(self.display)+1, column=0, sticky='W')

	def correctPass(self):
		correct = tk.Label(self)
		correct['text'] = 'Signing in!'
		correct['fg'] = 'green'
		correct.grid(row=len(self.display)+1, column=0, sticky='W')


	def confirm(self):
		login = tk.Button(self)
		login['text'] = 'Login'
		login['command'] = self.getEntry
		login.grid(row=len(self.display)+2, column=0, sticky='S')

	def exitButton(self):
		exit = tk.Button(self)
		exit['text'] = 'Quit'
		exit['command'] = self.quit
		exit.grid(row=len(self.display)+2, column=1, sticky='E')


root = tk.Tk()
m = Message(root)
ans = m.ans
m.mainloop()
# print(ans)
root = tk.Tk()
app = App(root, ans)
app.mainloop()