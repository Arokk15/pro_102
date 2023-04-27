import os 
import shutil

path_a="/Users/arokk/OneDrive/Desktop/New folder/pic_rs"
path_b="/Users/arokk/OneDrive/Desktop/New folder/pic_se"

ch=os.listdir(path_a)

if os.path.exists(path_a) !=True :
    os.mkdir(path_a)

for i in os.listdir(path_b):
    if i in ch :
        os.system("cls")
        print("it allways hear...!")
        
    else:
        print("stil copying.....",i)
        shutil.copy(path_b+"/"+i,path_a)