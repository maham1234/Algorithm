#srtf
finish=[]
total=0
current=0
m=[]
x=0

num=int(raw_input('Total number of processes: '))

for i in xrange(num):

	m.append([])

	m[i].append(raw_input('enter process name: '))
	m[i].append(int(raw_input('enter arrival time: ')))
	m[i].append(int(raw_input('enter burst time: ')))
	m[i].append(m[i][2]) #remaining burst time
	total+=m[i][2] #total burst time



while total>0:

	flag=0
	y=0
	while y<n and flag==0: #smaller burst time
		if current==a[y][1] and a[y][3]<a[x][3] and a[y][3]!=0:
			flag=1			
			x=y
		y=y+1
	if m[x][3]>0:	#running process
		total=total-1
		m[x][3]=m[x][3]-1
		current=current+1
		if m[x][3]==0:
			m[x][4]=current
	elif (x+1)<num:
		x=x+1
	else:
		m.sort(key=lambda m:a[3]) #x is at n then remaining burst time
		q=0
		flag2=0
		while q<num and flag2==0:
			if mq][3]>0 and m[q][1]<=current:
				flag2=1
				x=q
			q=q+1

m.sort(key=lambda m:m[1])
print 'Process \ Arrival time \ Burst time \waiting time'

for i in xrange(num):
	print m[i][0],',m[i][1],',m[i][2],',m[i][4]-m[i][1]-m[i][2] #finish time -arrival time -burst time
