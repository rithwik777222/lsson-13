x = open('text.txt','r')
print("file is in read mode.")
print(x.read())
x.close()

y = open('text.txt','w')
y.write('file in write mode')
y.write("\n hiiii,i am ba penguin(i wish)")
y.close()

z = open('text.txt','a')
z.write("\n file in append mode")
z.write(" still wish i were a penguin:(")
z.close()