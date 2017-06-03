#@author Josue Ruiz CS 431
import os.path
import time
import queue
from itertools import cycle
from pnode import pnode

CPU_TIME = 500
SJF_list = {}
q = queue.Queue()
execution_time = []
result = []

def load_list(num, filename):
	temp_p = pnode(num)
	counter = 0
	for line in open(filename):
		li=line.strip()
		if not li.startswith("#"):

			counter = counter + int(li.split()[1])
			temp_p.add(int(li))
	q.put(temp_p)
	execution_time.append(counter)


def prep():
	state = True
	num =  0
	while(state):
		filename = "p"+ str(num)+".txt"
		if os.path.exists(filename) and int(num) < 100:
			print("File: "+str(num))
			load_list(int(num), filename)
		elif(int(num) >= 100 and os.path.exists(filename)):
			print("Max files read reached computing the rest")
			state = False
		else:
			state = False
		num = num + 1
	for x in range(q.qsize()):
		result.append(CPU_TIME)


# def move_forward(pid):
# 	result[pid] = CPU_TIME
# 	temp = q.get()
# 	q.put(temp)
# 	return None

# def calculate(pid):
# 	temp = result[pid] - q.queue[0].current()
# 	if temp <= 0:
# 		temp = abs(temp)
# 		q.queue[0].set(temp)
# 		move_forward(pid)
# 	elif temp > 0:
# 		result[pid] = temp
# 		q.queue[0].next()
# 	else:
# 		print("error!")
# 	return None





def main():
	#prepares the data structures an necessary information
	prep()
	FCFS()
	SJF()
	RR()

	

if __name__== "__main__":
	main()