list=[1,2,3,4,5,6,7,8,9,10]
num=1
num2=10
#1
for i in list:
    print(i)
while num <=10:
    print(num)
    num+=1

#2
for j in list[::-1]:
    print(j)
while num2>=1:
    print(num2)
    num2-=1
#3
triangle=['      *      ','     ***     ','    *****    ','   *******   ','  *********  ',' *********** ','*************']
for k in triangle:
    print(k)
for l in range(1,11):
    consequence= i*i
    print('{}*{}={}'.format(l,l,consequence))

#exercise 2
list3=['Python', 'Numpy','Pandas','Scikit', 'Pytorch']
for i in list3:
    print(list3)
#2
sum=0
for m in range(1,101):
    sum+=m
    print(sum)
sumeven=0
sumodd=0
for n in range(1,101):
    if n%2==0:
        sumeven+=n
    print(sumeven)
for o in range(1,101):
    if o%2==1:
        sumodd+=o
    print(sumodd)
#  i v extract the data in corresponding document ,name the nested list as country
from countries_details_data import country
for indice in range(1,len(country)):
    name=country[indice]['name']
    if "land" in name:
        print(name)
fruit= ['banana', 'orange', 'mango', 'lemon']
reversedlist=[]
for indice2 in fruit[::-1]:
    reversedlist.append(indice2)
    print(reversedlist)
#question a and b
languageset=set()
languagelist=[]
languagenum=[]
num=[]
for indice3 in range(1,len(country)):
    for indice4 in range(1,len(country[indice3]['languages'])):
       language=country[indice3]['languages'][indice4]
       languageset.add(language)
       languagelist.append(language)
s=len(languageset)
for indice5 in languagelist:
    count=languagelist.count(indice5)
    num.append(count)
    num.sort()
    list3=num[-10:-1]
    if count in list3:
        print("top10 language include{},num is {} ".format(indice5,count))
#questionC
poplist=[]
for indice6 in range(1,len(country)):
    population=country[indice6]["population"]
    countryname=country[indice6]["name"]
    poplist.append(population)
    poplist.sort()
    top10pop=poplist[-10:-1]
    if population in top10pop:
        print("top10 population include{},num is {} ".format(countryname,population))












