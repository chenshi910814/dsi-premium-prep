"""un/comment to de/activate ###########################

print("hello")

#######################################################"""
"""un/comment to de/activate ###########################

'''
Write a while loop to print a menu out of this list with their number options starting at 1? Store the choices (as the item names, not the numbers) in a list. Print out the list containing the food ordered.
'''

food_lst = ['Pancakes', 'Omelet', 'Toast', 'Waffles', 'Bacon', 'Sausage', 'Orange Juice']

#######################################################"""
"""un/comment to de/activate ###########################

food_lst = ['Pancakes', 'Omelet', 'Toast', 'Waffles', 'Bacon', 'Sausage', 'Orange Juice']

order = []
while True:
    print('Make a selection from this list: ')
    for idx, item in enumerate(food_lst, 1):
        print(f'{idx}: {item}')

    order.append(food_lst[int(input('Choose an item by number: ')) - 1])

    if input('Choose another item? (Y/N) ') in "nNqQ":
        break

print(order)

#######################################################"""
"""un/comment to de/activate ###########################

txt = "I love to look at the moon"
print( txt )                    # I love to look at the moon
txt = txt.replace("o", "U")
print( txt.replace("o", "U") )  # I lUve tU lUUk at the mUUn
print( txt )                    # I love to look at the moon

#######################################################"""
"""un/comment to de/activate ###########################

food_lst = ['Pancakes', 'Omelet', 'Toast', 'Waffles', 'Bacon', 'Sausage', 'Orange Juice']

for idx, ele in enumerate('Pancakes are good', 1):
    print(f"{idx}: {ele}")

#######################################################"""
"""un/comment to de/activate ###########################

'''
Write a function that takes a list like the following list of column names and change any spaces in the column names to underscores. Return a modified list with the updated names.
'''
def snake_caser(in_lst):
    out_lst = []
    for txt in in_lst:
        out_lst.append(txt.replace(" ", "_"))

    return out_lst


column_names = ['gender', 'longest absence from school', 'is enrolled', 'enlist', 'unemployed', 'filed for bankruptcy', 'school', 'peace corps']
print( snake_caser(column_names) )

#######################################################"""
"""un/comment to de/activate ###########################

txt = "hello"
print( list('longest absence from school') )

print( 'longest absence from school'.split() )

#######################################################"""
"""un/comment to de/activate ###########################

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

print(text.replace("?", ".").replace("!", ".").split("."))

#######################################################"""
"""un/comment to de/activate ###########################

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

txt = 'And miles to go before I sleep. hello'
print( txt )
print( txt.lower() )
print( txt.upper() )
print( txt.title() )
print( txt.capitalize() ) # And miles to go before i sleep. hello

# for ch in txt:
#     if ch.lower() in "aeiou":
#         print(ch)

#######################################################"""
"""un/comment to de/activate ###########################

# enforce capitalization at the beginning and after a "."

def better_capitalize(txt):
    acc = ""
    flag = False
    for idx, ch in enumerate(txt):
        if (idx == 0 or flag) and ch not in " \n\t":
            flag = False
            acc += ch.upper()
        else:
            acc += ch
        if ch == ".":
            flag = True

    return acc


text = '''Whose woods these are? I think I know.
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
'''.lower()

print(better_capitalize(text))

#######################################################"""
"""un/comment to de/activate ###########################

'''
Write a function that takes in a string.
Return two parallel lists: one that contains the unique characters in the string and another that has the number of times that character appears in the original string.
'''
def chars_counter(txt):
    unique_chars = []
    char_counts = []
    for ch in txt:
        if ch not in unique_chars:
            unique_chars.append(ch)
            char_counts.append( txt.count(ch) )

    return unique_chars, char_counts


s = 'This is a string, we want you to count how many times each unique character appears in this string!'

print( chars_counter(s) )

#######################################################"""
"""un/comment to de/activate ###########################
'''
Create a function that takes in a string.

This function should split the string into a list of lowercase words that make up that string.

Return a list of unique ‘cleaned’ words.

Challenge: strip any punctuation (for now, strip commas and periods)
Challenge: remove the common english words from the list below you are returning
'''
def string_cleaner(txt):
    txt = txt.lower()

    remove_punct_lst =  [",", ".", ";", ":", "!", "?", "'", '"']
    for punct in remove_punct_lst:
        txt = txt.replace(punct, "")

    remove_word_lst = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "can", "will", "just", "don", "should", "now"]

    lst = []
    for word in txt.split():
        if word not in lst and word not in remove_word_lst:
            lst.append(word)

    return lst


inp = "Hello there! How are you? Why don’t you take a seat over there? Once we went to the store and we found ourselves in a strange place. We ran into two people. They were very interesting to talk to. Each of them had an interesting accent and we wondered where they were from."

print( " ".join(string_cleaner(inp)) )

#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
