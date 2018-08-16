import glob,os

#Caminho para buscar os arquivos
os.chdir("C:/")

#lista que vai receber todos os nomes de arquivos
lista = []

for file in glob.glob("*.jrxml"):
	lista.append(file)

for arquivo in lista:
	aux = ""
	f = open(arquivo, "r")
	linhas = f.readlines()
	for l in linhas:
		aux = aux + l.replace("F9A74E", "0000FF")
		
	f.close()
	f = open(arquivo , "w")
	f.write(aux)
	f.close()
	
