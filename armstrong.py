number = input("enter number: ")
n = len(number)
list_ = []
for i in number:
    m = int(i) ** int(n)
    list_.append(m)
sum= 0

for t in list_:
    sum += int(t)

print(sum)