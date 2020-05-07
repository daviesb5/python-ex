# https://youtu.be/rfscVS0vtbw?t=11562

# Reading Files

# r = read, w = write, a = append, r+ = read & write
immigrant_file = open("ext_files/immigrants.txt", "r")

# for loop
for immigrant in immigrant_file.readlines():
    print(immigrant)

# can this file be read?
# print(immigrant_file.readable())

# reads entire file
# print(immigrant_file.read())

# reads file line
# print(immigrant_file.readline())

# reads file lines (plural)
# print(immigrant_file.readlines())


# closes the file
immigrant_file.close()