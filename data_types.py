print("Hi")

integer = 5
number = 5.5
word = "string"

print(integer)
print(number)
print(word)

print("===list===")
list_of_things = [
    integer,
    5,
    number,
    word,
]
print(list_of_things)
print(list_of_things[0])
list_of_things[0] = list_of_things[0] + 1
print(list_of_things[0])

print("===dictionary===")
dictionary_of_things = {
    'integer_key': integer,
    word: integer,
    'list_of_things_key': list_of_things,
}
print(dictionary_of_things)

print("===set===") # sets have distinct items
set_of_things = {
    integer,
    5, # ignored
    number,
    word,
}
print(set_of_things)

print("===tuples===") # tuples can have duplicates
tuple_of_things = (
    integer,
    5, # duplicates are allowed
    number,
    word,
    list_of_things,
)
print(tuple_of_things)
print(tuple_of_things[0])
#tuple_of_things[0] = tuple_of_things[0] + 1 # not allowed

print("bye")