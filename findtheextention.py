filename=input('Enter a filename: ')
index=0
for i in range(len(filename)):
    if filename[i]=='.':
       index=i
print(filename[index+1:])



#output screen
#Enter a filename: prabu.py
#py
