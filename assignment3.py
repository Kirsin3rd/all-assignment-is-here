vegetables='lettuce','broccoli','spinach','shallot'
fruits='avocado','passion fruit','tangerine','kiwi'
fruit_vegetable=vegetables+fruits
print(fruit_vegetable)
num=len(fruit_vegetable)
print(num)
food_tuple=fruit_vegetable+('needle murshroom',"yoghourt",)
print(food_tuple)
(a,b,c,d,e,f,g,h,i,j)=food_tuple
print(i,j)
food_list=list(food_tuple)
i=food_tuple[4:6]
print(i)
j=food_list[1:8:3]
print(j)
k=food_list[:4]
l=food_list[-4:-1]
print(k)
print(l)
del food_tuple

asian_countries = 'India','China','Singapore','Thailand','Indonesia'
m='Finland'in asian_countries
n='India'in asian_countries
print(m)
print(n)
