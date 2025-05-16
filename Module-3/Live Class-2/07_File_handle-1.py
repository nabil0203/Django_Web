# 1:44
# read mode
# here the 3 steps mentioned in 06 no is performed



my_file = open("10_example-1.txt", "r")         # open file
xyz = my_file.read()                            # perform operation (here, read occured)
my_file.close()                                 # close the file


# now we have the content of the File, we can do any thing 
print(xyz)