mix_fruits = {'Guava', 'Pear', 'Mango', 'Apple', 'Fig', 'Orange', 'Banana'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
num = [22, 19, 24, 25, 26, 24, 25, 24]
a=len(mix_fruits)
print(a)
print(mix_fruits)
mix_fruits.add("Kiwi")
print(mix_fruits)
fruits_set={'passionfruit','tangerine'}
mix_fruits.update(['passionfruit','tangerine'])
mix_fruits=mix_fruits.discard('Apple')
#when remove a element from a set, use remove to eliminate a element which does not exist will cause error,while discard wont be
A = {1,2,3,4,5}
B = {4,5,6,7,8}
#join A and B,B and A
print(A|B)
print(B|A)
#intersection of a and b
print(A&B)
#judge wether subset
print(A.issubset(B))
print(B.issubset(A))
#judge wether a disjoint set  nb
print(A.isdisjoint(B))
#sysmetric difference
print(A^B)
#convert num to set
num=set(num)
print(num)

#Explain the difference between the following data types: string, list, tuple and set
#string means merely text which only represent some letter that have no any functional use on python ,stringed num is unable
# to calculate, the element of list is convenient to change,also have index to extract designated element,the order of list is stable
#while tuple has index either but it cant be duplicated,what s more the element of tuple is not mutable. the element of set cant be duplicate either ,what s more it has no index.


string="I am a researcher cum teacher and I love to inspire and teach people."
a=string.split()
print(set(a))


