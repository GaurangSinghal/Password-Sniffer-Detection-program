import os
from fnmatch import fnmatch
import getpass
usr = getpass.getuser()

src = 'C:/Users/' +usr+'/AppData/Local/Google/Chrome/User Data/Default/Extensions'
match = "*.js"

for path, subdirs, files in os.walk(src):
    for name in files:
        if fnmatch(name, match):
            temp_path = os.path.join(path, name)
            data=open(temp_path, 'r').read()
            #print type(data)
            x=data.replace(" ", "")
            s = x.replace('\n','')
            #s = line.replace('\t','')
            #print (line)
            if ((s.find('.type!="password"') != -1)or (s.find(".type=='password'") != -1) or (s.find(".type!='password'") != -1) or (s.find('.type=="password"') != -1)):
                print 'Password Sniffer Found in '+ str(name)
