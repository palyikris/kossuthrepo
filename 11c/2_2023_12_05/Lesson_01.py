# Task 1 - Printing some word, your name
print("Hello XYZ")
# Task 2 - Making a new line
print("")
# Task 3 - Writing multiple things on the screen
print("print multiple things, like:")
print("i like cats!")
print("But also like dogs as well")
print("")
print(
    "printing "
    + "multiple "
    + " things"
    + " with"
    + " only"
    + " one"
    + " print"
    + " command."
)
print("")
# Task 4 - Create a print command with miltiple lines
print(
    """Nature's first green is gold,
Her hardest hue to hold.
Her early leaf's a flower;
But only so an hour.
Then leaf subsides to leaf.
So Eden sank to grief,
So dawn goes down to day.
Nothing gold can stay."""
)
# This is the same without pressing enter
print(
    "Nature's first green is gold,\n Her hardest hue to hold.\n Her early leaf's a flower;\n But only so an hour.\n Then leaf subsides to leaf.\n So Eden sank to grief,\n So dawn goes down to day.\n Nothing gold can stay."
)


# Task 5 - Input data, use it for asking the user
input()
input("Here you can ask from the user in one line and (s)he can answer:")
input("Here you can ask from the user and in the new line (s)he can answer:\n")

input("What is your name?:")
input("How old are you?:")
input("Which of the following pet is your favourite? choose one: dog, cat, hamster:\n")
input("Which country you live in?:\n")
input("")
# Task 6 - comments
# Could be cool to save our answer somehow, does it?
# Oh,yeah... this is how you can write comments on your code
# But be caution, cause it only works with line by line
# After a new line you need to use the '#' sign again like this.

"""
If you want to multiple lines of comment, 
then you should use the 3-3 " sign like on this comment
"""
# Task 7 - Python console

# Task 8-11 - Use input inside the print command.
print(input("Hello World"))
# Replacing the 'a' characters to 'e'
print(input("Give me a poem:\n").replace("a", "e"))
# Make the text uppercase/lowercase
print(input("Give me a poem:\n").upper())
# Change the first letter of the words
print(
    input("Give me a poem:\n").title()
)  # make the first letter in each word upper case
print(
    input("Give me a poem:\n").capitalize()
)  # upper case the first letter in this sentence

# prompt: ide meg aztan gyakorolni kell a valtozoba valo elmenteset az inputnak
myinput = input("Adj meg egy szoveget: \n")
myint = int(input("Adj meg egy egesz szamot"))
# prompt: ezt float-tal is jatsszak el


# task: tipuskonverziok
int()
str()
float()
list()  # prompt: string -> list of characters
bool()

# prompt: kovi ora --> listak es ciklus
