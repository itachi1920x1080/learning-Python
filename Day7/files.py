#opening file in python ​use open() function
#syntax: open(filename, mode)
#mode: 'r' - read (default), 'w' - write, 'a' - append, 'b' - binary, 't' - text, '+' - read and write
with open('sample.txt','r') as file:
    content = file.read()
    print(content)
    # content = file.readline()
    # print(content)

