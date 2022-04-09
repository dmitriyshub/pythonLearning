

# creating list
a = [1, 2, 3, 4,"Hello", "World"] # list can be made by variable = list() or variable = []
print(a)
b = a[::-1] # reverse slicing
a.reverse() # reverse method

print(a)
print(b)

#remove elements
a.remove(3) # remove elements by value
del a[2] # remove by index [0]
print(a)

#adding, changing and concatenate different lists
a.append("Add me")  # adding new element to end of the list
print(a)
a[0] = 200 # change the value by the index
print(a)
#more
a = [1,2,3]
b = [4,5,6]
a.extend(b)  # concatenate lists!
a.insert(0,99) #(insert new elements to index) 0 is the index of the element and 99 new value
print(a)
print(a.pop(2)) # remove 2 by value from list
print(a)
a.clear() # delete all elements from lists
print(a)
a.append(99)
print("The index of the element is: ", a.index(99)) # show the index of elements with 99 value
a.clear()
a = [76,23,45,121,54,11,3]
print("list a: ", a)
a.sort() # sort the list method
print("sorted list a: ", a)
a = [76,23,45,121,54,11,3]
a.sort(reverse=True) # reverse
print("reversed and sorted list: ", a)

"""
n = int(input("insert a number: "))
a = [i for i in range(n)]
print(a)
"""

comp = ["Apple", "Facebook", "Google"]

for i in comp:
    print(i)
i = 0
while i < len(comp):
    print(comp[i])
    i += 1

list = [1, 5, 7, 11, 15]

for i in list [ : len(list) // 2]:
    print(i)

list1 = ['hello', 'python', 'pem', 'world of coding']
for counter in list1 :
    print(counter.upper())

for word in list1:
    if len(word) < 4 :
        break
    else:
        print(word.upper())