#import os for interacting with os
#define or give path of the directary where are the files that you wanna short(based on extension )
#create folders where you want files folders for each type of extension
#moving the files on desired folders

import os , shutil
from playsound3 import playsound

sound_path = r"C:/Users/acer/Downloads/success Sound Effect.mp3"
path = r"C:/Users/acer/Desktop/Video/2026/rajpal yadav case study/assets/test folder/"

file_names = os.listdir(path)
#print(lists)

# First, ensure the base path itself exists
os.makedirs(path,exist_ok=True)

#name of the folders you want to create
folder_names = ["images","MP4","Word Document","PDF Document"]

# Construct the full path by joining the base path and the folder name
'''for name in folder_names:
    full_path = os.path.join(path,name)
    print(full_path)'''


#creating folder
for i in range(0,4):

    if not os.path.exists(path+folder_names[i]):

      os.makedirs((path + folder_names[i]))

    else:
        print( f"folder {folder_names[i]} already exist")



#moving files into respective folders(removes from old location)
consern = input("do you want to move your files in folders(y/n)").lower()
#playsound(r"C:\Users\acer\Desktop\python projects\project 2 choose your own game\bulk file shortner extension basis\success Sound Effect.mp3")
if consern == "y":
    

   for file in file_names :
       if '.jpg' in file and not os.path.exists(path+ "images/" +file):
          shutil.move(path+ file,path + "images/" + file  )
     
       elif '.pdf' in file and not os.path.exists(path+ "PDF Document/" +file):
          shutil.move(path+ file,path + "PDF Document/" + file  )
          
       elif '.docx' in file and not os.path.exists(path+ "Word Document/" +file):
          shutil.move(path+ file,path + "Word Document/" + file  )
     
       elif '.mp4' in file and not os.path.exists(path+ "MP4/" +file):
          shutil.move(path+ file,path + "MP4/" + file  )
    
   playsound(r"C:\Users\acer\Desktop\python projects\project 2 choose your own game\bulk file shortner extension basis\success Sound Effect.mp3")


  
     
elif consern == "n":
   print("No file is moved as you choose NO")
   playsound(r"C:\Users\acer\Desktop\python projects\project 2 choose your own game\bulk file shortner extension basis\Fail Sound Effect.mp3")


else:
   print("you didn't choose appropriate option")






