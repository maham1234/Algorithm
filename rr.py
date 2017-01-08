
total_w=[]
r_burst=[]
finish=[]
total=0
m=[]


num=int(raw_input('Total processes: '))

quantum=int (raw_input('Enter time quantum: '))



for i in xrange(num):
	
	m[i].append(raw_input('enter process name: '))
	m[i].append(int(raw_input('enter arrival time: ')))
	m[i].append(int(raw_input('enter burst time: ')))
	m[i].append(a[i][2]) #remaining burst time
	total+=m[i][2] #total burst time
	m[i].append(0) #finish time

m.sort(key=lambda m:m[1])

x=0

current=m[x][1]

while total>0:

	if m[x][3]<quantum and m[x][3]!=0 and m[x][1]<=current:
		total=total-m[x][3]
		current=current+m[x][3]
		m[x][4]=current
		m[x][3]=0
	elif m[x][3]>=qtm and m[x][1]<=current:
		a[x][3]=a[x][3]-qtm
	
		if a[x][3]==0:
			a[x][4]=current
	

print 'Process \Arrival time \Burst time \waiting time'

for i in xrange(num):
	print a[i][0],',a[i][1],',a[i][2],',a[i][4]-a[i][1]-a[i][2]
