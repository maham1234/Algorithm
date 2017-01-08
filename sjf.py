
total_w=[]
num=int(raw_input('Total number of processes: '))
total=0
m=[]

for i in xrange(num):
	m.append([])
	m[i].append(raw_input('enter process name: '))
	m[i].append(int(raw_input('enter arrival time: ')))
	m[i].append(int(raw_input('enter burst time: ')))
#selection sort
for i in xrange (num):
	pos=i
	j=i+1
	while j<num:
		if m[j][2] < m[pos][2]:
			pos=j
		j=j+1
	temp=m[i][2]
	m[i][2]=m[pos][2]
	m[pos][2]=temp
	
	temp=m[i][0]
	m[i][0]=m[pos][0]
	m[pos][0]=temp

	temp=m[i][1]
	m[i][1]=m[pos][1]
	m[pos][1]=temp

start_time=0
for i in xrange(num):
	total_w.append([])
	total_w[i].append(int(start_time-m[i][1]))
	start_time=start_time+m[i][2]


print 'Process \ Arrival time \ Burst time \ waiting time'

for i in xrange(num):
	print a[i][0],',a[i][1],',a[i][2],',total_w[i]
