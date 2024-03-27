import os 
import colorama

# reading files with open
def read_file():
    with open("result.txt","r") as file1:
        file_stuff = file1.read()
        print(file_stuff)
        print(file1.closed) # file didnt closed


    print(file1.closed) #after with Exited from the file
    print(file_stuff)
print(colorama.Fore.GREEN+"------------------READ PAGE------------------")

read_file()



## writing files with open
def writing_files():
    lines = ["Merhaba Kainat\n", "mortal\n","life\n"]

    with open("result.txt","w") as file1:
        file1.write("This is line A\n")
        file1.write("Thih is line B\n")
        
        for line in lines:
            file1.write(line)
print(colorama.Fore.GREEN+"------------------WRITE PAGE------------------")

writing_files()



print(colorama.Fore.GREEN+"------------------READ AGAIN PAGE------------------")
read_file()        





### file copy


def copy_files():
    # Open the source file for reading

    with open("result.txt","r") as readFile:
        # Open the destination file for writing

        with open("result_copy.txt","w") as writeFile:
            
            # Read lines from the source file and copy them to the destination file

            for line in writeFile:
                writeFile.write(line)
            # Destination file is automatically closed when the 'with' block exits

                
# Source file is automatically closed when the 'with' block exits

            
    