# -*- coding:utf-8 -*-

from tkinter import *

class Calculadora:

	#Método construtor com parâmetros do tkinter
	def __init__(self, master):
		self.frame = Frame(master)
		self.frame.grid()
		self.dados = Entry(master, width=34)
		self.dados.grid(row=1, column=0)

		#botoes utilizados
		# buttons = ['0','1','2','3','4','5','6','7','8','9','.','+','-','*','/','=','C','Bin','Oct','Hex']
		buttons = ['0','1','2','3','Bin','4','5','6','Oct','7','8','9','Hex','+','-','*','/','.','=','C']
		#var controlar as linhas de cada botão
		r = 1
		#cada botao ira ficar nessa coluna
		c = 0
		# Aqui vai criar a interface 
		for btn in buttons:
			comando = lambda x=btn:self.calcular(x)
			self.botao = Button(self.frame, text=btn, width=6, command=comando)
			self.botao.grid(row=r,column=c)
			c += 1
			if c > 3:
				c = 0
				r += 1

	# Lógicas para cacular da calculadora
	def calcular(self, valor):
		# Verificação do sinal de igualdade para obter resultado
		if valor == '=':
			tudo = '0123456789.+-*/'

			#Condição para verificar se existem operadores diferentes na instãncia
			if self.dados.get()[0] not in tudo:
				self.dados.insert(END, "Operação Inválida!")
			try:
				#Metodo para realizar soma, multiplicacao, adicao e subtracao 
				#Retornando uma string
				resultado = eval(self.dados.get())
				self.dados.insert(END,'='+str(resultado))
			except:
				self.dados.insert(END,'Erro!')

		#Condições para conversões da base numerica
		#OBS: O Python já dispõe de métodos para converter: bin() oct() hex()
		#IMPORTANTE: Chamar Matheus para Mostrar o Uso por parte da Google do Python
		elif valor == 'Bin':
			try:
				resultado = bin(int(self.dados.get()))
				#Retorna na tela um array de Strings a partir do 2 index
				#Para não aparecer a identificação do Python de bin, oct e hex presentes na função
				self.dados.insert(END,'='+str(resultado[2:]))
			except:
				self.dados.insert(END,'Erro!')
		
		elif valor == 'Oct':
			try:
				resultado = oct(int(self.dados.get()))
				self.dados.insert(END,'='+str(resultado[2:]))
			except:
				self.dados.insert(END,'Erro!')

		elif valor == 'Hex':
			try:
				resultado = hex(int(self.dados.get()))
				self.dados.insert(END,'='+str(resultado[2:]))
			except:
				self.dados.insert(END,'Erro!')

		#Método para quando clicar em C limar a tela.
		elif valor == 'C':
			self.dados.delete(0,END)

		#Após realizar resultado ao insetir um novo valor ele apaga o antigo.
		else:
			if '=' in self.dados.get():
				self.dados.delete(0,END)
			self.dados.insert(END,valor)

#Padrão tkinter instânciando um objeto em loop
root = Tk()
root.title('Calculadora escrita em Python')
Calculadora(root)
root.mainloop()