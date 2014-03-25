import os
import re

numThreads = [1,2,4,6,8,12,16]


fileName = "ThreadPoolSpeedUp.txt"

file = open(fileName,"w+")


#list from 1 to 20
recursionDepth = [x for x in range(15,20,1)]



print ""

#string1 = "results should 23.23 23 25"
#print min(re.findall(r'\d*\.\d+|\d+', string1))

timerList = []
traker = 0



for threadNum in numThreads:
	fileNumString = "LOOKING AT " + str(threadNum)+ " THREAD(S)\n"
	print fileNumString
	file.write(fileNumString)

	threadNumList = range(threadNum,20)

	for x in threadNumList:
		tracker = x
		if len(timerList) > 3 and timerList[-2] < timerList[-1] and timerList[-3] < timerList[-2]  :
			break


		recur = "RECURSIZE DEPTH = " + str(x) + "\n"
		print recur
		file.write(recur)
		a  = os.popen('./quicksort -s 42 -d {0} -n {1} 300000000 -q'.format(x,threadNum)).readlines()
		print a[1]
		timerList.append( float(str(re.findall(r'\d*\.\d+|\d+', a[1])[0])))
		file.write(a[1]+"\n" )

		


	timerList = [float(i) for i in timerList] #convert all strings in list to floats
	print timerList
	minTime = "Fastest time: "+ str(min(timerList))  + "\n"

	foundDepth = str(threadNumList[timerList.index(min(timerList))])
	minrecursionDepth = "recursion depth of: " + foundDepth + " "

	print minTime
	print minrecursionDepth

	file.write(str(timerList) +"\n\n")
	file.write(minTime)
	file.write(minrecursionDepth)

	dataLine = "data points for " + foundDepth+ " at some NUMBER of threads\n"

	print dataLine
	file.write(dataLine)

	for x in range(3):
		a  = os.popen('./quicksort -s 42 -d {0} -n {1} 300000000 -q'.format(foundDepth,threadNum)).readlines()
		datapoint = "DATAPOINT"+" "+str(x) +" "+a[1]
		print datapoint
		file.write(datapoint)

	a  = os.popen('./quicksort -s 42 -d {0} -n 1 300000000 -q'.format(foundDepth)).readlines()
	printOut = "TIME FOR ONE THREAD\n"
	file.write(printOut +a[0]+ a[1] +" \n" )
	print printOut + a[0]+ a[1] +"\n" 



	end =  "=" * 80
	file.write(end)
	print end

	timerList = []



#close the file
file.close()


#qsort serial         took 43.181 sec.
#Using 16 threads, recursive parallel depth=7
#qsort parallel       took 12.451 sec.

