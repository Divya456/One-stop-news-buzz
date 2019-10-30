import os
def sentiment():
	afinn = dict(map(lambda (k,v): (k,int(v)),
		[line.split('\t') for line in open("I:\\6th semester\\Projects and Lab\\Projects\\IR\\Project\\sentimental_analysis\\AFINN-111.txt")]))
	positive=""
	negative=""
	#title=[]
	path="I:\\6th semester\\Projects and Lab\\Projects\\IR\\Project\\sentimental_analysis\\docs\\"
	for fname in os.listdir(path):
		f=open(os.path.join(path, fname),"r")
		lines=f.readlines()
		#print "lines:",lines
		f.seek(0,0)
		tit=f.readline()
		tit=tit.replace("\n","")
		for line in lines:
			line.replace("\n","")
		
		lines="".join(lines)
		score=sum(map(lambda word: afinn.get(word, 0), lines.lower().split()))
		if(score>0):
			#positive.append(lines)
			#positive.append([tit,int(fname.split(".")[0]),score])
			positive+=tit+"~~ "
		elif score<0:
			#negative.append(lines)
			#negative.append([tit,int(fname.split(".")[0]),score])
			negative+=tit+"~~ "
		f.close()
	positive=positive[:len(positive)-3]
	negative=negative[:len(negative)-3]
	print("@@Positive:")
	print(positive)
	print("@@Negative:")
	print(negative)
sentiment()