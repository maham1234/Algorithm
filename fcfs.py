#fcfs
total_w=[]
num=int(raw_input('Total number of processes: '))
start_time=0
total=0
m=[]

for i in xrange(num):

	
	m[i].append(raw_input('enter process name: '))
	
	m[i].append(int(raw_input('enter burst time: ')))

        m[i].append(int(raw_input('enter arrival time: ')))

	total_w.append([])

	total_w[i].append(int(start_time-m[i][1]))


	start_time=start_time+m[i][2]

a.sort(key=lambda a:a[1])

print 'Process \ Arrival time \ Burst time \waiting time'

for i in xrange(n):

	print a[i][0],',a[i][1],',a[i][2]
