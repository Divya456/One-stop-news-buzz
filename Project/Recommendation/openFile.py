import os, sys
import webbrowser
titleDict=dict()
def getTitles():
	path="I:\\6th semester\\Projects and Lab\\Projects\\IR\\Project\\sentimental_analysis\\docs\\"
	
	titles=""
	for fname in os.listdir(path):
		f=open(os.path.join(path, fname),"r")
		line=f.readline()
		
		line=line.replace("\n","")
		#print("line:",line)
		titleDict[line]=int(fname.split(".")[0])
		titles+=line+"~~ "
		f.close()
	titles=titles[:len(titles)-3]
	print(titleDict)



def func(number):
	# global titleDict
	#f=open(titleDict[title]+".txt","r")
	webbrowser.open("I:\\6th semester\\Projects and Lab\\Projects\\IR\\Project\\Recommendation\\"+str(number)+".txt")
	

# getTitles()
func(sys.argv[1])