# here we are importing the package '5.05_package'
# this 5.05.1 file is created to show how to import a package into a file
# '5.05_package' - folder is imported here as a Package

# rename--> '5.05_package' folder into 'package'



import package.my_package                        # package import style-1
package.my_package.pack()                               



from package import my_package                   # package import style-2
my_package.pack()



from package.my_package import pack              # package import style-3
pack()
