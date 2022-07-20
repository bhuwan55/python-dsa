"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""



"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""

locations = {'North America': {'USA': ['Mountain View','Atlanta']},
             'Asia': {'India':['Bangalore'],'China':['Shangai']},
             'Africa': {'Egypt':['Cairo']}
}

american_cities = locations['North America']['USA']
american_cities.sort()
print(1)
for city in american_cities:
    print(city)

print(2)
asian_cntries = locations['Asia']
lis = []
for cntry, cities in asian_cntries.items():
    for city in cities:
        st = city + ' - '+ cntry
        lis.append(st)
lis.sort()
for item in lis:
    print(item)