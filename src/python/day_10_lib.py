# """un/comment to de/activate ###########################

# types
    # int float
    # bool
    # None
    # str
    # tuple

    # list
    # dict
    # set

# abstractions
    # variables
    # functions
# control flow / conditions
# iteration
    # while
        # for
            # list comprehensions
            # dict comprehensions

# comprehensions

#######################################################"""
"""un/comment to de/activate ###########################

def factorial(n):
    prod = 1
    for i in range(2, n+1):
        prod *= i

    return prod


# i**2 if (i > lim) else i**3
def squares_lst(lst, lim):
    other_lst = []
    return [ other_lst.append(i**2) for i in lst ]

# [<some_expression> for some_val in some_collection]
some_lst = [33, 66, 2, 88, 43, 6, 33, 4, 9, 3, 442, 9]
print( squares_lst(some_lst, 50) )
# [None, None, None, None, None, None, None, None, None, None, None, None]

print({i%5: i for i in range(10, 20)})

#######################################################"""
"""un/comment to de/activate ###########################

person = ["Jessie", 52]
print( f"{person[0]} is {person[1]} years old" ) # Jessie is 52 years old
print( "{} is {} years old".format(person[0], person[1]) ) # Jessie is 52 years old

#######################################################"""
"""un/comment to de/activate ###########################


some_string = "hello "
print(some_string)
some_string += "w"
some_string += "o"
some_string += "r"
some_string += "l"
some_string += "d"
print(some_string)

#######################################################"""
"""un/comment to de/activate ###########################

def build_non_vowel_str(txt):
    s = ""
    for c in txt:
        if c.lower() not in "aeiouy":
            s += c
    return s


string = "It’s a beautiful day in the neighborhood, A beautiful day for a neighbor, could you be mine? Would you be mine?"
print( build_non_vowel_str(string) )

#######################################################"""
"""un/comment to de/activate ###########################
'''
Write a function called collect_evens() that takes a list of integers.
The function should return a string that accumulates the even numbers into a string.
'''
def collect_evens(lst):
    s = ""
    for num in lst:
        if num % 2 == 0:
            s += str(num)
    return s


some_lst = [1, 2, 3, 4]
print(collect_evens(some_lst)) # '24'

#######################################################"""
"""un/comment to de/activate ###########################

'''
Write a function called words_start_with() with two parameters, a list of letters and a string.
The function should return a new list filled with words from the string that start with the letters in the list of letters. Test with this string:
'''

def words_start_with(let_lst, txt):
    lst = []
    for word in txt.split():
        if word[0].lower() in let_lst:
            lst.append(word)

    return lst

str1 = "It's a beautiful day in the neighborhood, A beautiful day for a neighbor, could you be mine? Would you be mine?"
print(words_start_with(["b", "c", "w"], str1))

#######################################################"""
"""un/comment to de/activate ###########################

# catagorical
def words_start_with_abc_dct(txt):
    d = { "a": []
        , "b": []
        , "c": [] }

    for word in txt.split():
        first_letter = word[0].lower()
        if first_letter in d.keys():
            d[first_letter].append(word)

    return d


# pure
def word_freq_dict(txt):
    word_lst = txt.split()
    d = {}
    for word in word_lst:
        if word not in d.keys():
            d[word] = word_lst.count(word)

    return d
# {"word": <int> of count}


# hybrid
def word_idxs_dict(txt):
    word_lst = txt.split()
    d = {}
    for idx, word in enumerate(word_lst):
        if word not in d.keys():
            d[word] = []
        d[word].append(idx)

    return d
# {"word": [<int> of idxs]}


text = '''
Whose woods these are? I think I know.
His house is in the village though;
He will not see me stopping here
To watch his woods fill up with snow.

My little horse must think it queer
To stop without a farmhouse near
Between the woods and frozen lake
The darkest evening of the year.

He gives his harness bells a shake
To ask if there is some mistake.
The only other sound's the sweep
Of easy wind and downy flake.

The woods are lovely, dark and deep,
But I have promises to keep,
And miles to go before I sleep,
And miles to go before I sleep.
'''

for k, v in word_idxs_dict(text).items():
    print(f"{k}: {v}")

#######################################################"""
"""un/comment to de/activate ###########################
'''
For any given string, return a dictionary that gives us the number of vowels, the number of non vowels, the number of non-alpha characters.
'''
def string_data_dict(txt):
    d = {
        "vowels"     : 0,
        "vowel_idx"  : [],
        "consonants" : 0,
        "nonalpha"   : 0,
        }
    for idx, c in enumerate(txt):
        if not c.isalpha():
            d["nonalpha"] += 1
        elif c.lower() in "aeiouy":
            d["vowels"] += 1
            d["vowel_idx"].append(idx)
        else:
            d["consonants"] += 1

    return d


text = '''
Whose woods these are? I think I know.
His house is in the village though;
He will not see me stopping here
To watch his woods fill up with snow.

My little horse must think it queer
To stop without a farmhouse near
Between the woods and frozen lake
The darkest evening of the year.

He gives his harness bells a shake
To ask if there is some mistake.
The only other sound's the sweep
Of easy wind and downy flake.

The woods are lovely, dark and deep,
But I have promises to keep,
And miles to go before I sleep,
And miles to go before I sleep.
'''

print( sum(string_data_dict(text).values()), len(text) )

#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
