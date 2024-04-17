# input output 
giris_dosyasi = "folders.txt"
cikis_dosyasi = "folders_new_created.txt"

# open file and read
with open(giris_dosyasi, "r") as f:
    satirlar = f.readlines()

# Change all _ character with -
degistirilmis_satirlar = [satir.replace("_", "-") for satir in satirlar]

# Write new text
with open(cikis_dosyasi, "w") as f:
    f.writelines(degistirilmis_satirlar)

print("Changing completed. new folfer created:", cikis_dosyasi)
