import re
i = 1
while(i==1):
	#Take statement
	querry = input('Write your querry-\n')
	#Convert to lowercase for matching
	lower = querry.casefold()
	#Find both integar values
	num = re.findall('\d+',lower)
	
	#Logic for calculation
	
	word = lower.split()
	
	for x in word:
		if x in ('add','addition','give','sum','+','plus','increase','adding'):
			r = int(num[1]) + int(num[0])
			print('Result:-', r)
		elif x in ('subtraction','minus','take','-','decrease','subtracting','subtract'):
			r = int(num[1]) - int(num[0])
			print('Result:-', r)
		elif x in ('multiply','manifold','*','multiplication','multiplying'):
			r = int(num[1]) * int(num[0])
			print('Result:-', r)
		elif x in ('divide','division','fraction','part','/','%','dividing'):
			r = int(num[1]) / int(num[0])
			print('Result:-', r)
		elif x in ('end','terminate','finish','close','kill'):
			i = 0
			print('Program terminated')
		