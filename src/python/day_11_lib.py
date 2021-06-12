# """un/comment to de/activate ###########################

# data types
    # int, float
    # bool
    # None
    # str
    # * tuple

    # list
    # * dict
    # * set

# abstractions
# control flow
# iteration

#######################################################"""
"""un/comment to de/activate ###########################

car_d = {
    "make" : "toyota" ,
    "model": "highlander" ,
    "year" : 2011 ,
}


car_l = [
    "toyota" ,
    "highlander" ,
    2011 ,
]


print( id(car_l[ 1 ]) )

print( id(car_d[ "model" ]) )


#######################################################"""
"""un/comment to de/activate ###########################

car_d = {
    "make" : "toyota" ,
    "model": "highlander" ,
    "model": "civic" ,
    "year" : 2011 ,
}

print( car_d[ "model" ] )

#######################################################"""
"""un/comment to de/activate ###########################

lst = []
print(lst)

lst.append("hello")
print(lst)

lst[0] = "foo"
print(lst)

lst[1] = "bar"
print(lst)

#######################################################"""
"""un/comment to de/activate ###########################
# CRUD

car_d = {
    "make" : "toyota" ,
    "model": "highlander" ,
}

# read
print( car_d )

# read
print( car_d["model"] )

# create
car_d["year"] = 2011
print( car_d )

# update
car_d["model"] = "civic"
print( car_d )

# delet
del car_d["model"]
print( car_d )

# del car_d
# print( car_d ) # NameError: name 'car_d' is not defined

#######################################################"""
"""un/comment to de/activate ###########################

def word_frequency_d( txt ):
    d = {}
    for word in txt.split():
        if word not in d.keys():
            d[word] = 0
        d[word] += 1

    return d


text = '''
Whose woods these are I think I know
His house is in the village though
He will not see me stopping here
To watch his woods fill up with snow

My little horse must think it queer
To stop without a farmhouse near
Between the woods and frozen lake
The darkest evening of the year

He gives his harness bells a shake
To ask if there is some mistake
The only other sound's the sweep
Of easy wind and downy flake

The woods are lovely dark and deep
But I have promises to keep
And miles to go before I sleep
And miles to go before I sleep
'''

for the_key, the_value in sorted(word_frequency_d(text).items()):
    print(the_key, the_value)
# { "word": <int>(frequency) }


#######################################################"""
"""un/comment to de/activate ###########################

car_d = {
    "make" : "toyota" ,
    "model": "highlander" ,
    "year" : 2011 ,
}


print("car_d:   ", car_d )
print("as list: ", list( car_d ) )
print("items:   ", list( car_d.items() ) )
print("keys:    ", list( car_d.keys() ) )
print("values:  ", list( car_d.values() ) )

# [('make', 'toyota'), ('model', 'highlander'), ('year', 2011)]

#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
