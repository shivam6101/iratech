series=[2, 3, 10, 15, 26, 35,50,63]
count=0
ans=0
value=0
for i in series:
    count=count+1
ans=series[count-2]-series[count-3]+4
print(series[count-1]+ans)
