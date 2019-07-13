from django.shortcuts import render
import operator


def homepage(request):
	return render (request,'home.html')

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()
	wordcount = {}
	for word in wordlist:
		if word in wordcount:
			#increase
			wordcount[word] += 1
		else:
			#add to the dictonary
			wordcount[word] = 1
	
	sortedwords = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)

	return render (request,'count.html',{'fulltext':fulltext, 'count':len(wordlist),'wordcount':sortedwords})

def about(request):
	return render (request,'about.html')