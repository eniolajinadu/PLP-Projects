handler = open("my_file.txt", "w")
print(handler.write("There's me writing some lines of stuff\n"))
print(handler.write("Here's a number 69.\n"))
print(handler.write("Help rewrite this code.\n"))
print(handler.close())

try:
    handler = open('my_file.txt', 'r')
    with open('my_file.txt', 'r') as file:
        print(handler.readlines())
        print(handler.close())
except FileNotFoundError:
    print ("File not found.")


handler = open("my_file.txt", "a+")
with open('my_file.txt', 'a') as file:
    print(handler.write("Mansa Musa is a king and more.\n"))
    print(handler.write("Power Learn Project is an amazing innovation.\n"))
    print(handler.write("©Abdulrasaq Eniola Jinadu.\n"))
    print(handler.readlines())