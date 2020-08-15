import os
from shutil import copyfile
from getpass import getuser


#Get username for source dir
user = getuser()
srcdir = "C:/Users/" + user + "/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets"


#makes destdir recursively if necessary
destdir = "C:/Users/" + user + "/Documents/Windows 10 Spotlight"
if not os.path.exists(destdir):
    os.makedirs(destdir)


#if new image, copies jpg version into destdir 
filetype = '.jpg'
numcopied = 0

files = os.listdir(srcdir)
for file in files:
    filesrc = srcdir + '/' + file
    filedest = destdir + '/' + file + filetype
    if os.path.getsize(filesrc) > 204800: #200 KB
        if not os.path.exists(filedest):
            copyfile(filesrc,filedest)
            numcopied += 1
print(numcopied, 'files copied')


#set to True to clear files in srcdir
clearsrcdir = False
numdel = 0
if clearsrcdir:
    os.chdir(srcdir) #changes the current working directory
    for file in os.listdir(srcdir):
        os.remove(file) 
        numdel += 1
print(numdel, 'files deleted')