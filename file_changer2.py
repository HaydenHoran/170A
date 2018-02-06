def file_changer2(in_file, line_num, iterates, increments,w):
	for j in range(1,iterates+1):#Loop through all the different files you may want
		indata= open(in_file).read()#Have to read in the data
		out_file=open('170Shape'+'%d'%j+'.inp', 'w')#Creating a new file
		out_file.write(indata) #Write all data that was in the original file to this file
		out_file.close() #Close the file
		y=0
		for k in w:
			print(k)
			print(increments[0])
			change_line=indata.splitlines()[line_num[y]]#Read in the specific list
			words=change_line.split(' ')#Divide the line up into an array of words
			words[k]= ("%r" %(float(words[k])+j*increments[y])) ####Pull out the word in the file thats alphanumeric and manipulate it
			output='' #initialize
			for i in range(0, len(words)):#Recombining the array into one string (no array)
				output=output+words[i]+' '
			
			lines = open('170Shape'+'%d'%j+'.inp', 'r').readlines()#Read the lines of this file
			lines[line_num[y]]=output + '\n' #Change the lines you wanted
			out = open('170Shape'+'%d'%j+'.inp', 'w') #Open the file once more for writing purposes
			out.writelines(lines)# write in the lines you wanted to write in
			out.close() #close the file

			print(increments[y], line_num[y])
			y=y+1
			print(y)

file_changer2('170Sphere.inp', [7, 8, 9], 1, [5, 6, 7], [2, 2, 0])


