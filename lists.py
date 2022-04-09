#list = [1, 5, 7, 11, 15]

#for counter in list [ : len(list) // 2]:
#    print(counter)

#list1 = ['hello', 'python', 'pem', 'world of coding']
#for counter in list1 :
#    print(counter.upper())

#for word in list1:
#    if len(word) < 4 :
#        break
#    else:
#        print(word.upper())

#myName = ('Donald Trump')
#splitName = myName.split()
#splitName[1]

#print(myName[:len(myName) // 3])

#dim = ('Hello World')
#print(dim.upper().find('o'))\

"""
string="hello world"
l=list(string)
s="o"
for x in l:
    if x==s:
        print("index "+str(l.index(x)) + " and symbol "+x)
        l.remove(x)
"""







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