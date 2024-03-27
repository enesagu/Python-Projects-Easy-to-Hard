import os 


with open("result.txt","r") as file1:
    file_stuff = file1.readlines()
    print(file_stuff)
    print(file1.closed) # file didnt closed


print(file1.closed) #after with Exited from the file
print(file_stuff)