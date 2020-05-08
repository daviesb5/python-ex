# https://youtu.be/rfscVS0vtbw?t=12087

# Reading Files

# r = read, w = write, a = append, r+ = read & write
immigrant_file = open("ext_files/index.html", "w")

# adds new lines
immigrant_file.write("<h1>Welcome to My Website</h1><p>This is HTML</p>")

# closes the file
immigrant_file.close()