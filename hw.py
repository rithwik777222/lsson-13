x = open('file the iii.txt','r')
print("file is in read mode.")
print(x.read())
x.close()

y = open('file the iii.txt','w')
y.write('file in write mode')
y.write("\n woah the homework is so simple")
y.close()

z = open('file the iii.txt','a')
z.write("\n file in append mode")
z.write("\n like same as the cw?")
z.close()