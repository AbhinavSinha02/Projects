N=int(input("Enter the number of subjects: "))
sum=0
for i in range(1,N+1):
    m=int(input("enter mark: "))
    sum=sum+m
print("Total: ",sum)
average=sum/N
print("Average:",average)
if average>=90:
    print("Grade:S")
elif average>=80 and average<89:
    print("Grade:A")
elif average>=70 and average<79:
    print("Grade:B")
elif average>=60 and average<69:
    print("Grade:C")
elif average>=50 and average<59:
    print("Grade:D")
elif average<50:
    print("Grade:Fail")

