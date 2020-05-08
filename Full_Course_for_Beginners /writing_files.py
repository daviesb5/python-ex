# https://youtu.be/rfscVS0vtbw?t=12087

# Reading Files

# r = read, w = write, a = append, r+ = read & write
immigrant_file = open("immigrants.txt", "a")

# reads entire file
immigrant_file.write("\n\nFICTIONAL IMMIGRANTS\n\nFranz Seraphicus  Meiersieck")

# closes the file
immigrant_file.close()