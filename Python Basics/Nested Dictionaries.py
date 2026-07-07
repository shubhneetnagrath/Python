car = {
   "Mustang":{ "brand": "Ford",
       "Year": 1964
   },
   "Urus":{
       "brand":"Lambo",
       "Year":"1982"
   }
}
for x, obj in car.items():
    print(x)

    for y in obj:
        print(y + ':',obj[y])

'''
Firstly X and Obj two variables are defined. Both of them go under a for loop.
x goes under turn by turn iteration, and values of inner dictions with refrence 
to the outer ones are stored in obj.Now Aonther for loop is implied on the obj
variable and the values of inner dictionaries go under turn by turn iterations. 
'''