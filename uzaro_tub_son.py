a=int(input("birinchi son= "))
b=int(input("ikkinchi son= "))
s=0
bih=max(a,b)
iih=min(a,b)
while s==0:
	if bih%iih==0:
		programma_ishlasin=0
		print("Bu sonlar o'zaro tub emas!")
		s+=1
	else:
		b2= bih % iih
		a2=iih
		print(b2, a2)
		if b2==1:
			programma_ishlasin=1
			print("Bu sonlar o'zaro tub!")
			s+=1
		else:
			iih=b2
			bih=a2



