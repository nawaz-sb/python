f1 =open("f1.txt","r")
f2 =open("f2.txt","r")
a= f1.read()
b= f2.read()
f1.close()
f2.close()


s1 =open("f1.txt","w")
s2 =open("f2.txt","w")

s1.write(b)
s2.write(a)
s1.close()
s2.close()