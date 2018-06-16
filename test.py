#题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

count=0
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if i != j and i != k and j != k:
				print(i*100+j*10+k)
			count +=1

print("共有不重复的3位数"+str(count)+"个")

###题目：输出9*9口诀。

for i in range(1,10):
	for j in range(1,i+1):
		print(str(i)+"*"+str(j)+"="+str(i*j))
	print()

