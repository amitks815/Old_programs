import os 

#print(dir(os))

print(os.getcwd())

print('lis.py',os.F_OK)

os.chdir('C:\\Users\\kumaami3\\Desktop\\DOCUMENTS\python_files')


print(os.getcwd())

path='C:\\Users\\kumaami3\\Desktop\\DOCUMENTS\python_files'
path='C:\\Users\\kumaami3\\Desktop\\DOCUMENTS\python_files\\tuple'
# file=os.listdir(path)
# for i in file :
# 	print(i)
#os.makedirs(path1)


# fd=os.open('C:\\Users\\kumaami3\\Desktop\\DOCUMENTS\python_files\\variable\\test.txt',os.O_RDWR)

# os.write(fd, "This is test")
# os.close( fd )
print(os.getcwd())
os.chdir('C:\\Users\\kumaami3\\Desktop\\DOCUMENTS\python_files')
for root, dirs, files in os.walk(path):
	print(root)
	print(dirs)
	print(files)


a=os.path.join('C:\\Users\\kumaami3\\Desktop\\DOCUMENTS\python_files\\tuple',tuplevar.py)

print(a)