This code helps us automate the MCNP5 simulation procress
The python file, "file_changer2" takes in four inputs: A document, a line number, the number of iterations, an incremental increase in value, and a word number. The line numbers, the incremental increase in values, and the word numbers should are all arrays. The number of iterations is any arbitrary integer and the document can have any extension. 
The file works like this: Say you want to change a number on line 2 (remembering of course the python 0 indexes) in "word number" 5 (call this element a). That is, it is the FIFTH word (but its actually a number) (remembering the 0 index!) in the line. Elements are delimited by spaces. Further, say you want to increase the fifth element by a value of .2, in .1 intervals. The call function would be: file_changer2=('mytext.inp',[2], 2, [.1], [5]).
The output would be two text files, named 'mytext1.inp' and 'mytext2.inp' with the the desired numerical value changed. Now, say you ALSO want to change a number in word number position 6 (call this element b), line 5, by an increment of 10. 
The input would be: file_changer2=('mytext.inp',[2 5], 2, [.1 10], [5 6]). The output would be:
1. 'mytext.inp1' with a=a+.1 and b=b+10
2.'mytext.inp2' with a=a+2*.1 and b=b+2*10
This code is meant to populate files for serial input into MCNP. ALl initial files are preserved!

The .awk file, "myAWK.awk", is a useful file for stripping results. It is a simple one-liner piece of code. For the project right now, its set to pluck out the keff, keff standard deviations, and keff confidence interval values from the ouput files of MCNP. You call it with the following command:

awk -f myAWK.awk myoutput>>keff.txt
The code is acting on the file "myouput" and putting the results into keff.txt by appending the values to the keff.txt file.

Say we have a lot of files with names: outp outq outr outs outt.... (General output from MCNP). We can then call the awk functions on all the files in one line: awk -f myAWK. awk outp outq outr ....>>keff.txt or we can say m awk -f myAWK.awk out*>>keff.txt. This is a neat little shortcut.
