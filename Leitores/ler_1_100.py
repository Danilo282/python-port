"""
Loop For

"""
print('Loop For')

for i in range(1, 101, 1):
    if i <= 100:
        print(i)

print("-------------------------------------------------------")

"""

Loop While
 
"""
print('Loop While')
c = 1
while c <= 100:
    print(c)
    c = c + 1

print("-------------------------------------------------------")
"""
Loop do while 

"""
print('Loop do while')
c = 1
while True:
    print(c)
    c = c + 1
    if c > 100:
        break
