count=int(input("how many numbers you want to add?"))

nums=[]

for i in range(count):
    n=int(input("enter a number:"))
    nums.append(n)
print("numbers entered:",nums)
print("total:",sum(nums))