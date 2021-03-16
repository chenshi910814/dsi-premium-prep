""" un/comment to de/activate ################

var1, var2 = 2, 3

print( '{var1} out of {var2} programmers prefer f-strings' )

print( f'{var1} out of {var2} programmers prefer f-strings' )
print( '{} out of {} programmers prefer f-strings'.format(var1, var2) )

########################################## """
""" un/comment to de/activate ################

lst1 = []
for i in iterable:
    lst2 = []
    for j in iterable:
        pass

########################################## """
""" un/comment to de/activate ################

num = 0
for x in list_of_numbers:
    num += x

sum(list_of_numbers)

########################################## """
""" un/comment to de/activate ################

'''
Write a function called `accum_nums` that takes in an integer `n` as an argument it should perform the tasks below for a range of numbers from `1` through `n` (int accumulator starts at 1)
* If the number is divisible by 3, add 3 to the accumulator
* If the number is divisible by 5, divide accumulator by 5
* If number is divisible by 4, multiply the accumulator by 4
* If number is divisible by 3, 4, and 5 do nothing
* If number is divisible by 3 and 4, subtract 12 from accumulator
* If number is divisible by 3 and 5, floor divide accumulator by 15
* If number is divisible by 4 and 5, modulo accumulator by 20
'''

########################################## """
""" un/comment to de/activate ################

tup = ()
tup += ("hello",)
tup += ("world",)

print( tup )

########################################## """
""" un/comment to de/activate ################

def non_val(s):
    new_s = ''
    for char in s:
        if char.lower() not in 'aeiou':
            new_s += char

    return new_s

########################################## """
""" un/comment to de/activate ################
'''
Write a function called collect_evens() that takes a list of integers. The function should return a string that accumulates the even numbers into a string.
'''
def collect_evens(lst):
    txt = ""
    for num in lst:
        if num % 2 == 0:
            txt += str(num)

    return txt


print( collect_evens([1, 2, 3, 4]) ) # '24'

########################################## """
""" un/comment to de/activate ################

# "a".lower() == "A".lower() # False

########################################## """
""" un/comment to de/activate ################

text = '''
Whose woods these are? I think I know.
His house is in the village though;
He will not see me stopping here
To watch his woods fill up with snow.
'''
# split
words = text.lower().split()
# print( text.lower().split() )

# join
txt = " ".join(words)
print( txt )

########################################## """
""" un/comment to de/activate ################

def word_freq_dict(txt):
    d = {}
    words_lst = txt.split()
    for word in words_lst:
        d[word] = words_lst.count(word)

    return d


def freq_word_dict(txt):
    wf_dict = word_freq_dict(txt)
    d = {} # target
    for word, freq in wf_dict.items():
        if freq not in d.keys():
            d[freq] = [] # add new key val pair
        d[freq].append(word)

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
'''.lower()

print( freq_word_dict(text) )


########################################## """
""" un/comment to de/activate ################

d = { "a" : 0
, "b" : 0
, "c" : 0
}

print(d)
d["a"] += 1
print(d)
# {'a': 0, 'b': 0, 'c': 0}
# {'a': 1, 'b': 0, 'c': 0}

########################################## """
""" un/comment to de/activate ################

def char_count_d(txt):
    d = { "vowels"     : 0
        , "non vowels" : 0
        , "non alpha"  : 0
        }
    for ch in txt:
        if ch.lower() in "aeiou":
            d["vowels"] += 1
        else:
            d["non vowels"] += 1
        if not ch.isalpha():
            d["non alpha"] += 1

    return d


#####################
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
'''.lower()

print( char_count_d(text) )
# {}

########################################## """
# """ un/comment to de/activate ################



########################################## """
