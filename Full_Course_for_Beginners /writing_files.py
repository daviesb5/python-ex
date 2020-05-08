# https://youtu.be/rfscVS0vtbw?t=12087

# Reading Files

# r = read, w = write, a = append, r+ = read & write
immigrant_file = open("ext_files/immigrants.txt", "w")

# adds new lines
immigrant_file.write("FICTIONAL IMMIGRANTS\n\nFranz Seraphicus  Meiersieck")

# closes the file
immigrant_file.close()