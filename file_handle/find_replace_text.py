import os 

texttofind='amit'
texttoreplace='sumit'
sourcepath=os.listdir('inputfiles')
for file in sourcepath:
	inputfile='inputfiles/'+ file
	#inputfiles is a file directory 
	#print(inputfile)
	print('convesetion is going for:'+inputfile)
	with open(inputfile,'r') as inputfile:
		filedata=inputfile.read()
		freq=0
		freq=filedata.count(texttofind)
	destinationpath='outputfiles/'+ file
	filedata=filedata.replace(texttofind,texttoreplace)
	with open(destinationpath,'w') as file:
		file.write(filedata)
	print('total %d record replaced' %freq)






