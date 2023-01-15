#criado por Lucas gabriel
# github : github.com/Lucas836-hub
# instagram : @lucas_git

from datetime import datetime
import os
import sqlite3

data_e_hora_atuais = datetime.now()
data_atual =data_e_hora_atuais.strftime("%d/%m/%Y")
hora_atual = data_e_hora_atuais.strftime("%H:%M:%S")
bi_ano=int(data_e_hora_atuais.strftime("%Y"))
#print("Agora é : ",data_atual,hora_atual,"\n")

def print_data():
	data_e_hora_atuais = datetime.now()
	data_atual =data_e_hora_atuais.strftime("%d/%m/%Y")
	hora_atual = data_e_hora_atuais.strftime("%H:%M:%S")
	bi_ano=int(data_e_hora_atuais.strftime("%Y"))
	print("Agora é : ",data_atual,hora_atual,"\n")
	

#BD

banco = sqlite3.connect("Dados.bd")
cursor = banco.cursor()
try:
	cursor.execute("CREATE TABLE dados(materia char,assunto text,data vachar(10),hora vachar(5), id char)")
except:
	pass
	
def passagem_tempo(a,b,c):
	data=list(a)
	data_atual=list(b)
	
	num=[int(data[0]+data[1]),int(data[3]+data[4]),int(data[6]+data[7]+data[8]+data[9])]
	
	#print(num)

	num2=[int(data_atual[0]+data_atual[1]),int(data_atual[3]+data_atual[4]),int(data_atual[6]+data_atual[7]+data_atual[8]+data_atual[9])]
	
	#print(num2)
	
	resp=[num[0]-num2[0],num[1]-num2[1],num[2]-num2[2]]
	
	#print(resp)
	
	if(resp[0] <= c or resp[1] < 0 or resp[2] < 0):
		return 'true'
		
	else:
		return 'false'


def excluir():
	global banco , cursor , data_atual
	try:
		cursor.execute("SELECT * FROM dados")
		lista=[]
		ex=""
		id=""
		for c in cursor.fetchall():
			lista.append(c)
			
		for p in range(0,len(lista)):
			ex= passagem_tempo(lista[p][2],data_atual,-7)
			id=lista[p][4]
			if(ex == "true"):
				cursor.execute("DELETE from dados WHERE id == ? ",(lista[p][4],))
				banco.commit()
	except:
		print()	
	
	
def editar():
	limpar()
	global banco , cursor  , data_atual
	print_data()
	traco("EDITAR EVENTOS")
	
	
	listagem=[]
	datas=[]
	o=0
	try:
		cursor.execute("SELECT * FROM dados WHERE data ORDER BY data")
		
		for c in cursor.fetchall():
			listagem.append(c)
		for t in range(len(listagem),0,-1):
			o=positivo(t-1)
			if(listagem[o][2] not in datas):
				datas.append(listagem[o][2])
		passou=""	
		#print(datas)		
		for p in range(len(listagem),0,-1):
			o=positivo(p-1)
			print(f"\nId : {o}\nMatéria : {listagem[o][0]} \nDia : {listagem[o][2]} as {listagem[o][3]}\nAssunto : {listagem[o][1]}")
					
		if(len(listagem) == 0):	
			trac="="*40
			erro="NÃO HÁ NEMHUM REGISTRO"
			print("\n",trac.center(48))
			print(erro.center(50))
			print(trac.center(50),"\n")
			print("Digite 1 - Para voltar")
			opcao(1,1)
			menu()
		
	except:
		trac="="*40
		erro="NÃO HÁ NEMHUM REGISTRO"
		print("\n",trac.center(48))
		print(erro.center(50))
		print(trac.center(50),"\n")
		print("Digite 1 - Para voltar")
		opcao(1,1)
		menu()
	
	else:	
		print("\nDigite : 1 - Para volta\n         2 - Deletar evento\n         3 - Atualizar evento\n         4 - Como usar ?")
		n = opcao(1,4)
		if(n == 1):
			menu()
		if(n == 2):
			traco("DELETAR")
			print("\nOK . Digite o Id para ser excluido")
			ID = opcao(0,len(listagem)-1)
			delete=str(listagem[ID][4])
			cursor.execute("DELETE FROM dados WHERE id = ?",(delete,))
			banco.commit()
			editar()
		if(n == 3):
			traco("UPDATE")
			print("\nOK . Digite o Id para ser atualizado")
			ID = opcao(0,len(listagem)-1)
			up(listagem[ID][4])
			
		if(n == 4):
			help_editar()
			

def up(id):
	limpar()
	global banco , cursor  , data_atual
	print_data()
	listagem=""
	traco("UPDATE")
	cursor.execute("SELECT * FROM dados WHERE id == ?",(id,))
	listagem=list(cursor.fetchall())
	print()
	print(f"\nMatéria : {listagem[0][0]} \nDia : {listagem[0][2]} as {listagem[0][3]}\nAssunto : {listagem[0][1]}")
	
	print("\nDigite : 1 - Para Cancelar\n         2 - Alterar Materia\n         3 - Alterar Assunto\n         4 - Alterar Data\n         5 - Alterar Hora\n")
	n = opcao(1,5)
	if(n == 1):
		editar()
	if(n == 2):
		print("Materia atual = ",listagem[0][0])
		m = input("Nova materia = ")
		print("\nDigite : 1 - Para cancelar\n         2 - Para Salvar")
		n = opcao(1,2)
		if(n == 1):
			editar()
		else:
			 cursor.execute("UPDATE dados SET materia = ? WHERE id == ?",(m,id))
			 banco.commit()
		
	if(n == 3):
		print("Assunto atual = ",listagem[0][1])
		a = input("Novo Assunto = ")
		print("\nDigite : 1 - Para cancelar\n         2 - Para Salvar")
		n = opcao(1,2)
		if(n == 1):
			editar()
		else:
			 cursor.execute("UPDATE dados SET assunto = ? WHERE id == ?",(a,id))
			 banco.commit()
			 
	if(n == 4):
		print("Data atual = ",listagem[0][2])
		d = input("Nova Data = ")
		print("\nDigite : 1 - Para cancelar\n         2 - Para Salvar")
		n = opcao(1,2)
		if(n == 1):
			editar()
		else:
			 cursor.execute("UPDATE dados SET data = ? WHERE id == ?",(d,id))
			 banco.commit()
			 
	if(n == 5):
		print("Hora atual = ",listagem[0][3])
		h = input("Nova Hora = ")
		print("\nDigite : 1 - Para cancelar\n         2 - Para Salvar")
		n = opcao(1,2)
		if(n == 1):
			editar()
		else:
			 cursor.execute("UPDATE dados SET hora = ? WHERE id == ?",(h,id))
			 banco.commit()
	editar()
	
	
def help_editar():
	limpar()
	print_data()
	traco("COMO EDITAR ?")
	print("\nPara editar selecione uma opção de edição, após digite o Id do registro a ser editado")
	print("\nDigite 1 - Para retorna a edição")
	opcao(1,1)
	limpar()
	editar()
	
							
def positivo(a):
	b=str(a)
	b.replace("-","")
	return int(b)
	
	
def todos():
	limpar()
	global banco , cursor  , data_atual
	print_data()
	
	traco("TODOS OS EVENTOS")
	try:
		cursor.execute("SELECT * FROM dados WHERE data ORDER BY data")
		
		lista=[]
		datas=[]
		o=0
		for c in cursor.fetchall():
			lista.append(c)
		for t in range(len(lista),0,-1):
			o=positivo(t-1)
			if(lista[o][2] not in datas):
				datas.append(lista[o][2])
		passou=""
		passou2=0		
		for p in range(len(lista),0,-1):
			o=positivo(p-1)
			try:
				passou = passagem_tempo(lista[o][2],data_atual,-1)
			except:
				continue
			try:
				if(passou2 == 0 and passou == "true"):
					passou2=1
					traco("EVENTOS ANTIGOS")
			except:
				continue
				
			try:
				if(lista[o][2] == datas[0]):
					trac="="*20
					print("\n",trac.center(48))
					print(datas[0].center(50))
					print(trac.center(50),"\n")
					del datas[0]
			except:
				continue
			print(f"\nMatéria : {lista[o][0]} \nDia : {lista[o][2]} as {lista[o][3]}\nAssunto : {lista[o][1]}\n")
			#print(lista[0])
		if(len(lista) == 0):	
			trac="="*40
			erro="NÃO HÁ NEMHUM REGISTRO"
			print("\n",trac.center(48))
			print(erro.center(50))
			print(trac.center(50),"\n")
		
	except:
		trac="="*40
		erro="NÃO HÁ zzz NEMHUM REGISTRO"
		print("\n",trac.center(48))
		print(erro.center(50))
		print(trac.center(50),"\n")
	
	print("\nDigite : 1 - Para volta\n")
	opcao(1,1)
	menu()

def adicionar():
	limpar()
	global banco , cursor
	print_data()

	traco("NOVO CADASTRO")
	m=input("materia : ")
	a =input("assunto : ")
	d=input("data : ")
	h=input("hora : ")
	id =data_atual +" " + hora_atual

	print("\nDigite : 1 - Para cancelar\n         2 -  Para salvar\n")
	n =opcao(1,2)
	if(n == 1):
		menu()
	else:
		cursor.execute("INSERT INTO dados VALUES(?,?,?,?,?)",(m,a,d,h,id))
		banco.commit()
		menu()
		
		
def duvida():
	limpar()
	print_data()

	traco("COMO USAR ?")
	print("\nVocê deverá colocar as informacoes nesse padrão\n\nmateria : matematica\nassunto : video aula <- Não é obrigatorio\ndata : dia/mês/ano ex 31/07/2020\nhora : hora:minuto\n\nDigite 1 para voltar ao menu\n")
	opcao(1,1)
	menu()
	

def limpar():
	try:
		tes = os.system("clear")
	except:
		os.system("cls")
				
				
def info():
	limpar()
	print_data()
	traco("MAIS INFORMAÇÕES !")
	print("Este é um algoritmo em python com o intuito de auxiliar na organização pessoal nesse tempo de quarentena.\n\nO mesmo possui uma ligação com SQLITE para salvar as informações , naqual a cada 7 dias são excluidas automaticamente para poupar mémoria e para o seu perfeito funcionamento o mesmo terá que estar salvo em uma pasta em seu aparelho.")
	
	print("\nDigite : 1 - Para volta\n")
	opcao(1,1)
	menu()
		
				
def compromico():
	limpar()
	try:
		global cursor,data_atual
		print_data()
	
		traco("COMPROMISSOS DE HOJE")
		print("\n")
		cursor.execute("SELECT * FROM dados WHERE hora ORDER BY hora")
	
		
		lista=[]
		elementos=0
		for c in cursor.fetchall():
			lista.append(c)
		for p in range(0,len(lista)):
			if(lista[p][2] == data_atual):
				elementos+=1
				print(f"Matéria : {lista[p][0]} \nHoje as : {lista[p][2]} {lista[p][3]}\nAssunto : {lista[p][1]}")
				print()
		if(elementos == 0):
			trac="="*40
			erro="NÃO HÁ COMPROMISSOS PARA HOJE"
			print(trac.center(49))
			print(erro.center(50))
			print(trac.center(50),"\n")
	except:
		trac="="*40
		erro="AINDA NÃO HÁ NEMHUM REGISTRO"
		print(trac.center(48))
		print(erro.center(50))
		print(trac.center(50),"\n")
	print("\nDigite : 1 - Para volta\n")
	opcao(1,1)
	menu()
	
def opcao(m,M):
	while True:
		n = input("Digite sua resposta : ")
		try:
			if(int(n) >= m and int(n) <= M):
				break
			else:
				print("\033[31mERRO RESPOSTA INVÁLIDA\033[m")
		except:
			print("\033[31mERRO CARACTERE INVÁLIDO\033[m")
	return int(n)


def menu():
	limpar()
	global banco,data_atual,hora_atual
	print_data()
	
	excluir()
	traco("MENU")
	print("\n0 - Para infomaçoes do código\n1 - Como usar ?\n2 - Adicionar novo evento\n3 - Ver os eventos de hoje\n4 - Ver todos os eventos\n5 - Editar os eventos\n6 - Sair")
	n=opcao(0,6)
	if(n == 0):
		info()
	if(n == 1):
		duvida()
	if(n == 2):
		adicionar()
	if(n == 3):
		compromico()
	if(n == 4):
		todos()
	if(n == 5):
		editar()
	else:
		banco.close()


def traco(a):
	print("~" * 50)
	print(a.center(50))
	print("~" * 50)

	
menu()
