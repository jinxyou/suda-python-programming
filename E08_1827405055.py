i=0
a=100
for i in range(0,5,1):
    a*=1.005
    if i==4:
        print("存款金额为{:>.5f}".format(a))
        break
    a+=100
q=(a-500)/500
print("收益率为{:>.2f}%".format(q*100))