# numero aleatorios mediante el ingreso de letras
def NumAleatorio(a,b):
	letra = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	aleatorio=0
	i=0
	while i<26:
		if (a==letra[i]):
			aleatorio+=i
			i+=1
		elif(b==letra[i]):
			aleatorio+=i
		i+=1
	print aleatorio
letra1 = str(raw_input(" ingrese una letra :"))
letra2 = str(raw_input(" ingrese una letra :"))
NumAleatorio(letra1,letra2)
