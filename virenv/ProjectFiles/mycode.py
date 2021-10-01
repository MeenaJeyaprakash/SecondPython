import os
from os import path
import shutil

static_src = "C:/Jenkins_master/Jenkins_git/Kotak_uat/ApplicationFiles/"
static_dst = "C:/inetpub/wwwroot/"
dynamic_src = ""
dynamic_dest = ""
#shutil.copy("C:\Jenkins_master\Jenkins_git\Kotak_uat\ApplicationFiles\Generic\pc\Desktop\Source_Folder\dirlist.xls","C:/inetpub/wwwroot/")
myfile=open('D:/Temp_Folder/filelist.txt','r')
while myfile:
    contents=myfile.readline()
   # print(contents)
    

#with open('D:/Temp_Folder/list.txt','r') as f:
 #   contents = f.readline()
    #print(contents)
  #  while contents:
    #contents = f.readline()
    contents=contents[:-1] #to get rid of new line character in notepad filelist
    #print(contents)
    dynamic_src = static_src+contents
    #print(dynamic_src)
    dynamic_dest = static_dst+contents
    #print(dynamic_dest)
    #print(dynamic_dest.split('/')[0:-1])
    dynamic_dest1='/'.join(dynamic_dest.split('/')[0:-1])
    #print(dynamic_dest)
    #print(dynamic_dest1)
    #print(contents[-4:])
    if((contents[-4:] == ".htm") or (contents[-4:] == ".css")) :
        #print(contents[-4:])
        if not os.path.exists(dynamic_dest1):
          #print("success")
          os.makedirs(dynamic_dest)
        shutil.copy(dynamic_src,dynamic_dest)
    if contents =="":
        break
myfile.close()