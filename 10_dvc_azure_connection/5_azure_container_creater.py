import os

# Name of the text file to be taken from outside
txt_file = "folders_new_created.txt"

# Azure CLI command template
command = "az storage container create --name {} --account-name account-name --account-key account-key"

# Open the text file and execute the Azure CLI command with each line by replacing the placeholder
count = 0
with open(txt_file, "r") as file:
    for line in file:
        count = count + 1

        folder_name = line.strip()  # Remove trailing whitespace from each line
        os.system(command.format(folder_name))  # Execute the Azure CLI command
        print("Container Number: ",count)
