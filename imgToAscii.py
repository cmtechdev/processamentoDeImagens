'''
ATENCAO: Antes de executar o codigo, garantir que o modulo 'cv2' esta devidamente instalado.
Recomendacoes:
	pip3 install cv2
'''
import cv2

# sua lista de caracteres pode variar de acordo com a sua finalidade. Altere se necessarios os aqui presentes.
simbols = '█▓▒░≡=-:. ' # simbolos que ira compor o conteudo ASCII resultante
l = [0 for x in range(0, 256)] # numeros e seus respectivos intervalos relacionados aos simbolos

# calcula os intervalos precisos para cada valor possivel
def calcDelt():
	global l
	
	ind, delt = 0, (256 // (len(simbols) - 1) )
	
	for i in range(1, 256):
		if (i%(delt)) == 0:
			ind += 1
		
		l[i] = ind

def main():
	global simbols, l
	img, out, dimension, filename = None, None, 0, ""
	
	calcDelt() # calcula os intervalos
	
	# obtem as informacoes do usuario
	filename = input("Digite o caminho do arquivo: ") # Ex.: mario.jpg
	dimension = int( input("Propocao do quadro resultante: ") ) # Ex.: 8
	
	# prepara o ambiente para manipulacao dos arquivos
	img = cv2.imread(filename, 0) # o '0' converte a imagem em questao para escala de cinza
	out = open("saida.txt", "w")  # arquivo que sera criado com o conteudo ASCII
	
	#Um quadro com dimensao fixa calcula a media dos valores em pixels que compoe a imagem 
	for col in range(0, len(img), dimension):
		for row in range(0, len(img[col]), dimension):
			m, cont = 0, 0
			for i in range(col, col + dimension):
				if ( i < len(img) ): # se a coluna estiver na proporcao da imagem...
					for j in range(row, row + dimension):
						if (j < len(img[col])): # se a linha estiver na proporcao da imagem...
							m += img[i][j]
							cont += 1
			
			# calcula a media
			if cont > 0:
				m //= cont
			
			out.write( simbols[ l[m] ] )
			
		out.write("\n")
	
main()
