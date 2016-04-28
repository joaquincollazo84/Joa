a = ["0","1","2","3","4","5","6","7","8"]
b = "si"
while b=="si":
	x = int(raw_input(("Ingresar un numero : ")))
	if a[x]!="x":
		a[x]="x"
		print " "
		print "   -----"
		print "  ",a[0],a[1],a[2]
		print "  ",a[3],a[4],a[5]
		print "  ",a[6],a[7],a[8]
		print "   -----"
	else:
		a[x]=="x"
		print "    -----"
		print "   ",a[0],a[1],a[2]
		print "   ",a[3],a[4],a[5]
		print "   ",a[6],a[7],a[8]
		print "    -----"
		
	b = raw_input("quiere segui si o no")


