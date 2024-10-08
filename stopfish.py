'''
todo:
- functions

'''
import time
import os
import re
import subprocess
import socket
import sys
import platform
import base64
import datetime
import random
import shutil
vars={'stopfish':":)",'defaultint':50,"deflist":["hi",56,True],"deflist2":['john','doe','man','hi']}
ip1 = socket.gethostbyname(socket.gethostname())
pkgrandom=False
pkgdatetime=False
pkgos=False
pkgbase= True
def line():
    global command
    command= input(">>>")
    if command=="log":
        log()
    elif command =="strvar":
        strvar()

    elif command =="showvars":
        showvars()
    elif command == "intvar":
        intvar()
    elif command =='showvar':
        showvar()
    elif command=="calc":
        calc()
    elif command=="showfunc":
        showfunc()
    elif command=="delvar":
        delvar()
    elif command =="devlog":
        devlog()
    elif command =="arrcount":
        arrcount()
    elif command =="arrsort":
        arrsort()
    elif command=="logloop":
        logloop()
    elif command=="clearvars":
        clearvars()
    elif command =="updvar":
        updvar()
    elif command =="pkgs":
        pkgs()
    elif command =="arrindex":
        arrindex()
    elif command == "getpkg":
        getpkg()
    elif command == "ip":
        ip()
    elif command =="cutvar":
        cutvar()
    elif command =="encbase":
        if pkgbase == True:
            encbase()
        else:
            
            print("***ERR function not listed***")
            line()
    elif command =="decbase":
        if pkgbase == True:
            decbase()
        else:
            
            print("***ERR function not listed***")
            line()

    elif command =="rand":
        if pkgrandom == True:
            rand()
        else:
            
            print("***ERR function not listed***")
            line()

            

    elif command =="cwd":
        if pkgos == True:
            cwd()
        else:
            print("ERR: pkg not installed")
            line()
    elif command =="shell":
        if pkgos == True:
            shell()
        else:
            print("ERR: pkg not installed")
            line()
    elif command =="sysos":
        
        
        if pkgos == True:
            sysos()
        else:
            print("ERR: pkg not installed")
            line()
    elif command =="dirsize":
        
        
        if pkgos == True:
            dirsize()
        else:
            print("ERR: pkg not installed")
            line()
    elif command =="pyv":
        
        
        if pkgos == True:
            pyv()
        else:
            print("ERR: pkg not installed")
            line()
    elif command =="sysinfo":
        
        
        if pkgos == True:
            sysinfo()
        else:
            print("ERR: pkg not installed")
            line()

            
    elif command =="syspro":
        
        
        if pkgos == True:
            syspro()
        else:
            print("ERR: pkg not installed")
            line()
    elif command =="sysarch":
        
        
        if pkgos == True:
            sysarch()
        else:
            print("ERR: pkg not installed")
            line()


            

    elif command =="makedir":
        
        if pkgos == True:
            makedir()
        else:
            print("ERR: pkg not installed")
            line()
            
        
    elif command =="deldir":
        
        if pkgos == True:
            deldir()
        else:
            print("ERR: pkg not installed")
            line()
        
    elif command =="showdir":
        
        if pkgos == True:
            showdir()

        else:
            print("ERR: pkg not installed")
            line()
        

            



    
    elif command =="exdatetime":
        if pkgdatetime == True:
            exdatetime()
        else:
            
            print("***ERR function not listed***")
            line()
    elif command =="exdate":
        if pkgdatetime == True:
            exdate()
        else:
            
            print("***ERR function not listed***")
            line()
    elif command =="extime":
        if pkgdatetime == True:
            extime()
        else:
            
            print("***ERR function not listed***")
            line()
    elif command =="exutc":
        if pkgdatetime == True:
            exutc()
        else:
            
            print("***ERR function not listed***")
            line()
    elif command =="exit":
        exit()
    elif command== "stopfish":
        print(":)")
    elif command== "arr":
        arr()
    elif command =="arradd":
        arradd()
    elif command =="arrinc":
        arrinc()
    elif command =="arrdel":
        arrdel()
    elif command =="cleararr":
        cleararr()
    elif command =="arrlen":
        
        arrlen()
    elif command =="vlen":
        vlen()
    elif command=="arrmix":
        arrmix()
    elif command =="arrpop":
        arrpop()

    elif command =="help":
        print('''
* Stopfish is a python-based command line interface which can handle quite a lot of functions.
* Use '='or '-' before and after the str if your input is non-variable. It depends on the function if it is necessary.
* Use '`' or '!' bfore and after a list if you want an item from the list through an ID (except logloop).
* Array values are seperated by commas (,).
* Packages are set of commands which are out of context for this program or unable to provide features other functions have. For example variable inputting.
* Array declaration only accepts strings, integers and '/' as correct values. Any values other than that have to be arradd to  the list.
* Use '//' to get random values in some functions.
* Use '/' to use your IP in vars, lists and logloops.
* Functions are typed word by word (except for expressions and list declaration.).
For example- 
>>>strvar  (assigns string value)
strvar>>>name  (name for variable)
value>>>-john doe-  (value)
>>>log (print function)
>>>name (variable)

''')
        line()
    elif command =="":
        print("empty value")
        line()
    elif command ==" ":
        print("empty value")
        line()

    else:
        print("***ERR function not listed***")
        line()
        
        
def log():
    command = input(">>>")
    if command.startswith('=') and command.endswith('=') or command.startswith('-') and command.endswith('-'):
        print(command[1:-1])
        print("***successfully compiled 0***")
        line()
    elif command.startswith('`') and command.endswith('`') or command.startswith('!') and command.endswith('!'):
        listname=(command[1:-1])
        if listname in vars and isinstance(vars[listname], list):
            value = int(input("value>>>"))
            print(vars[listname][value])
            print("***successfully compiled 0***")
            line()
    elif command == '/':
        
        print(ip1)
        line()
    elif command == '//':
        value1= int(input('range1>>>'))
        value2= int(input('range2>>>'))
        
        if pkgrandom == True:
            print(random.randint(value1,value2))
            print("***successfully compiled 0***")
            line()
        else:
            print('pkg_random not managed')
            line()
    elif command in vars:
        print(vars[command])
        print("***successfully compiled 0***")
        line()
        

    elif re.match(r'^[-+]?\d*\.?\d+$', command):  
        result = eval(command)
        print(result)
        print("***successfully compiled 0***")
        line()
    elif command == "stopfish":
        print(":)")
    else:
        try:
            
            for var_name, var_value in vars.items():
                command = command.replace(var_name, str(var_value))
            result = eval(command)
            print(result)
            print("***successfully compiled 0***")
            line()
        except Exception as e:
            print("***ERR:", e)
            line()
    time.sleep(0.1)
    

def strvar():
    command= input("strvar>>>")
    value=input("value>>>")
    if value.startswith('=') and value.endswith('=') or value.startswith('-') and value.endswith('-'):
        vars[command]=(value[1:-1])
        print("***successfully compiled 0***")
        line()
    if value.startswith('`') and value.endswith('`') or value.startswith('!') and value.endswith('!'):
        listname=(value[1:-1])
        if listname in vars and isinstance(vars[listname], list):
            
            value1 = int(input("index>>>"))
            vars[command]=(vars[value[1:-1]][value1])
            print("***successfully compiled 0***")
            line()
    if value=='/':
        listname=(value[1:-1])
        ip = socket.gethostbyname(socket.gethostname())    
        
     
        vars[command]=(ip)
        print("***successfully compiled 0***")
        line()
    elif value in vars:
        vars[command]=(vars[value])
        print("***successfully compiled 0***")
        line()

    else:
        print("***ERR invalid log use '='or '-' before and after the str if the input is non-variable***")
        line()

        '''IPAddr = socket.gethostbyname(socket.gethostname())    
    print(IPAddr)
    line()'''

def pkgs():
    print('current packages:\n*random_int_pkg\n*date_time_pkg\n*os_pkg')
    line()
def getpkg():
    pkg= input("pkg>>>")
    if pkg == 'random_int_pkg':
        time.sleep(1)
        print("random_int_pkg - 1 function available >>>rand")
        global pkgrandom
        pkgrandom=True
        print("***successfully compiled 0***")
        line()
    elif pkg== 'date_time_pkg':
        time.sleep(1)
        print("date_time_pkg - 4 function available >>>exdate, extime, exdatetime,exutc")
        global pkgdatetime
        pkgdatetime=True
        print("***successfully compiled 0***")
        line()
    elif pkg== 'os_pkg':
        time.sleep(1)
        print("os_pkg - 11 function available >>>cwd, deldir, makedir,showdir,sysinfo,sysarch,syspro,sysos,pyv,dirsize,shell")
        global pkgos
        pkgos=True
        print("***successfully compiled 0***")
        line()
    elif pkg== 'encode_base_pkgsawsssss':
        time.sleep(1)
        print("encode_base_pkg - 2 function available >>>encbase,decbase")
        global pkgbase
        pkgbase=True
        print("***successfully compiled 0***")
        line()
def exdate():
    try:
        print(datetime.date.today())
        line()
    except Exception as e:
        print(e)
def extime():
    try:
        print(datetime.datetime.now().time())
        line()
    except Exception as e:
        print(e)
def exdatetime():
    try:
        print(datetime.datetime.now())
        line()
    except Exception as e:
        print(e)
def exutc():
    try:
        print(datetime.datetime.now(datetime.UTC))
        line()
    except Exception as e:
        print(e)
def sysarch():
    try:
        print(platform.architecture())
        line()
    except Exception as e:
        print(e)
def syspro():
    try:
        print(platform.processor())
        line()
    except Exception as e:
        print(e)
def sysos():
    try:
        print(platform.platform())
        line()
    except Exception as e:
        print(e)
def shell():
    value = input('shellcmd>>>')
    try:
        result = subprocess.run(['powershell', '-Command', value], shell=True, capture_output=True, text=True)
        print(result.stdout)
        line()
    except Exception as e:
        print(e)
        line()
def pyv():
    try:
        print(sys.version)
        line()
    except Exception as e:
        print(e)

def cwd():
    try:
        print(os.getcwd())
        line()
    except Exception as e:
        print(e)

def sysinfo():
    try:
        print(platform.uname())
        line()
    except Exception as e:
        print(e)

def deldir():

    value=input("value>>>")
    
    if value.startswith('=') and value.endswith('=') or value.startswith('-') and value.endswith('-'):
        os.rmdir(value[1:-1])
        print("***successfully compiled 0***")
        line()
    elif value.startswith('`') and value.endswith('`') or value.startswith('!') and value.endswith('!'):
        listname=(value[1:-1])
        if listname in vars and isinstance(vars[listname], list):
            value = int(input("value>>>"))
            os.rmdir(vars[listname][value])
            print("***successfully compiled 0***")
            line()
    elif value in vars:
        os.rmdir(vars[value])
        print("***successfully compiled 0***")
        line()
    else:
        print("***ERR variable not found***")
        line()
def dirsize():

    value=input("value>>>")
    
    if value.startswith('=') and value.endswith('=') or value.startswith('-') and value.endswith('-'):
        os.path.getsize(value[1:-1])
        print("***successfully compiled 0***")
        line()
    elif value.startswith('`') and value.endswith('`') or value.startswith('!') and value.endswith('!'):
        listname=(value[1:-1])
        if listname in vars and isinstance(vars[listname], list):
            value = int(input("value>>>"))
            os.path.getsize(vars[listname][value])
            print("***successfully compiled 0***")
            line()
    elif value in vars:
        
        os.path.getsize(vars[value])
        print("***successfully compiled 0***")
        line()
    else:
        print("failed")
        line()
    

def makedir():
    value=input("value>>>")

    if value.startswith('=') and value.endswith('=') or value.startswith('-') and value.endswith('-'):
        os.mkdir(value[1:-1])
        print("***successfully compiled 0***")
        line()
    elif value.startswith('`') and value.endswith('`') or value.startswith('!') and value.endswith('!'):
        listname=(value[1:-1])
        if listname in vars and isinstance(vars[listname], list):
            value = int(input("value>>>"))
            os.mkdir(vars[listname][value])
            print("***successfully compiled 0***")
            line()
    elif value in vars:
        os.mkdir(vars[value])
        print("***successfully compiled 0***")
        line()
    else:
        print("***ERR variable not found***")
        line()



def showdir():
    value=input("value>>>")

    if value.startswith('=') and value.endswith('=') or value.startswith('-') and value.endswith('-'):
        os.listdir(value[1:-1])
        print("***successfully compiled 0***")
        line()
    elif value.startswith('`') and value.endswith('`') or value.startswith('!') and value.endswith('!'):
        listname=(value[1:-1])
        if listname in vars and isinstance(vars[listname], list):
            value = int(input("value>>>"))
            os.listdir(vars[listname][value])
            print("***successfully compiled 0***")
            line()
    elif value in vars:
        os.listdir(vars[value])
        print("***successfully compiled 0***")
        line()
    else:
        print("failed")
        line()

def ip():   
    IPAddr = socket.gethostbyname(socket.gethostname())    
    print(IPAddr)
    line()
    
def rand():
    from1 = input("from>>>")
    to = input("to>>>")
    print(random.randint(int(from1),int(to)))
def showvars():
    print(vars)
    time.sleep(.1)
    
    print("***successfully compiled 0***")
    line()
def varlen():
    command= input(">>>")
    if command.startswith('=') and command.endswith('=') or command.startswith('-') and command.endswith('-'):
        print (len((command[1:-1])))
        print("***successfully compiled 0***")
        line()
    elif command in vars:
        print (len(str(vars[command])))
        print("***successfully compiled 0***")
        line()

    else:
        print("***ERR invalid log use '='or '-' before and after the str if the input is non-variable***")
        line()
def vlen():
    
    list_name = input("arrlen>>>")
    
    if list_name in vars and isinstance(vars[list_name], list):
        length = len(vars[list_name])
        print(length)
        print("***successfully compiled 0***")
        line()
    else:

        print("***ERR invalid input***")
    
    line()
def arrcount():
    list_name = input("arrcount>>>")
    list_value = input("value>>>")
    
    if list_name in vars and isinstance(vars[list_name], list):
        count= vars[list_name].count(list_value)
        
        print(count)
        print("***successfully compiled 0***")
        line()
    else:

        print("***ERR invalid input***")
    
    
def arrpop():
    try:
        e = input("arrpop>>>")
        if e in vars:
            vars[e].pop()
            print("***successfully compiled 0***")
            line()
        else:
            print("Invalid list name")
            line()
    except KeyError:
        print("Invalid list name")
        line()
    
    
    line()
def arrsort():
    try:
        e = input("arrsort>>>")
        if e in vars:
            if all(isinstance(item, str) for item in vars[e]):
                vars[e].sort()  
                print("***successfully compiled 0***")
                print(vars[e])
                line()
            else:
                print("List values are not all strings")
                line()
        else:
            print("Invalid list name")
            line()
    except KeyError:
        print("Invalid list name")
        line()

    
def intvar():
    command = input("intvar>>>")
    if command in vars:
        print("Variable name already exists.")
        line()
        return

    
    value = input("value>>>")
    if value == '//':

        value1= int(input('range1>>>'))
        value2= int(input('range2>>>'))
        
        if pkgrandom == True:
            hi=random.randint(value1,value2)
            vars[command]=hi
            print("***successfully compiled 0***")
            line()
        else:
            print("ERR went wrong or random_int_pkg not imported")
            line()
    if value in vars:
        vars[command] = int(vars[value])
            
        time.sleep(0.1)
        print("***successfully compiled 0***")
        line()
        return
    else:
         print("Invalid expression or variable name.")
         line()
         return

    
    
    try:
        result = eval(value)
        vars[command] = int(result)
        
        time.sleep(0.1)
        print("***successfully compiled 0***")
        line()
        return
    
        
        if value in vars:
            vars[command] = int(vars[value])
            
            time.sleep(0.1)
            print("***successfully compiled 0***")
            line()
            return
        else:
            print("Invalid expression or variable name.")
            line()
            return

    except Exception as e:
        
        print(e)
    
    
def showvar():
    command= input(">>>")
    print(vars[command])
    line()
def arr():
    
    
    
    arr_name = input("arr>>>")
    arr_input = input("values>>>").split(',')
    arr_elements = []
    for element in arr_input:
        if element.startswith('=') and element.endswith('='):
            arr_elements.append(element[1:-1])
            
        elif element.isdigit(): 
            arr_elements.append(int(element))
            
        elif element=='/':
            
            ip = socket.gethostbyname(socket.gethostname())
            arr_elements.append(ip)

        
        else:
            arr_elements.append(element)
    vars[arr_name] = arr_elements

    
   

    time.sleep(0.1)
    print("***successfully compiled 0***")
    line()
def arradd():
     list= input("arr>>>")
     command= input("value>>>")
     if command.startswith('=') and command.endswith('=') or command.startswith('-') and command.endswith('-'):
         
  
         if list in vars:
             

             vars[list].append(command[1:-1])
             print("***successfully compiled 0***")
             line()
             
     elif command in vars:
         vars[list].append(vars[command])
         print("***successfully compiled 0***")
         line()
     elif re.match(r'^[-+]?\d*\.?\d+$', command):  
         vars[list].append(eval(command))
         
         print("***successfully compiled 0***")
         line()
         
     elif command == '//':

        value1= int(input('range1>>>'))
        value2= int(input('range2>>>'))

        
        if pkgrandom == True:
            hi=random.randint(value1,value2)
            vars[list].append(hi)
            print("***successfully compiled 0***")
            line()
        else:
            print("ERR went wrong or random_int_pkg not imported")
            line()

    
     elif command=='/':
         
        
         ip = socket.gethostbyname(socket.gethostname())    
        
        
      
         vars[list].append(ip)
         print("***successfully compiled 0***")
         line()


     elif command == "stopfish":
         print(":)")

     else:
         print("***ERR invalid log use '='or '-' before and after the str if the input is non-variable***")
         line()
         
def arrmix():
    list1_name = input("arr1>>>")
    list2_name = input("arr2>>>")
    new_list_name = input("name>>>")

    if list1_name in vars and isinstance(vars[list1_name], list) and list2_name in vars and isinstance(vars[list2_name], list):
        combined_list = vars[list1_name] + vars[list2_name]
        vars[new_list_name] = combined_list
        print("***successfully compiled 0***")
    else:
        print("***ERR: Invalid input or list not found***")
    line()
    
def arrinc():
     list= input("arr>>>")
     command= input("value>>>")
     if command.startswith('=') and command.endswith('=') or command.startswith('-') and command.endswith('-'):
         
  
         if list in vars:
             if command[1:-1] in vars[list]:
                 

                 print(True)
                 print("index>>>",vars[list].index(command[1:-1]))
                 print("***successfully compiled 0***")
                 line()
             else:
                 print(False)
     
          
             
             
             print('no list')
     elif command.isdigit()==True:
         if list in vars:
             if int(command) in vars[list]:
                 

                 print(True)
                 print("***successfully compiled 0***")
                 line()
             else:
                 print(False)
         
         
         
             
def arrdel():
     list= input("arr>>>")
     command= input("value>>>")
     if command.startswith('=') and command.endswith('=') or command.startswith('-') and command.endswith('-'):
  
         if list in vars:

             vars[list].remove(command[1:-1])
             print("***successfully compiled 0***")
             line()
     elif command in vars:
         vars[list].remove(vars[command])
         print("***successfully compiled 0***")
         line()
     elif re.match(r'^[-+]?\d*\.?\d+$', command):  
         vars[list].remove(eval(command))
         
         print("***successfully compiled 0***")
         line()
     elif command == "stopfish":
         print(":)")

     else:
         print("***ERR invalid log use '='or '-' before and after the str if the input is non-variable***")
         line()

def cleararr():
    command= input("arr>>>")
    if command in vars:
        
        while len(vars[command]):
            
            vars[command].clear()
            print("***successfully compiled 0***")
            line()
    else:
         print("***ERR invalid arr***")
         line()
def arrindex():
    m= input("arr>>>")
    v= input("item>>>")
    if m in vars:
        print(vars[m].index(v))
    else:
         print("***ERR invalid arr or item***")
         line()
    
def encbase():
    value = input("value>>>")
    base= input("base>>>")
    if base=='base64':
        basee=base64.b64encode(value.encode('utf-8'))
        print(basee)
    if base=='base32':
        basee=base64.b32encode(value.encode('utf-8'))
        print(basee)
    if base=='base16':
        basee=base64.b16encode(value.encode('utf-8'))
        print(basee)
    if base=='base84':
        basee=base64.b84encode(value.encode('utf-8'))
        print(basee)
def decbase():
    value = input("value>>>")
    base= input("base>>>")
    
    if base=='base64':
        basee=base64.b64decode(value).decode('utf-8')
        print(basee)
    if base=='base32':
        basee=base64.b32decode(value).decode('utf-8')
        print(basee)
    if base=='base16':
        basee=base64.b16decode(value).decode('utf-8')
        print(basee)
    if base=='base84':
        basee=base64.b84decode(value).decode('utf-8')
        print(basee)

    
    
def logloop():

    
    list_name = input("value>>>")
    value = (input("steps>>>"))
    timebw = float(input("timer>>>"))
    

    if list_name in vars:
        e = vars[list_name]
        if isinstance(e, list):  
            for item in e:
                print(item)
                time.sleep(timebw)
            line()
        else:
            if list_name in vars:
                for x in range(int(value)):
                    
                    print(vars[list_name])
                    time.sleep(timebw)
                line()
    elif list_name.startswith('=') and list_name.endswith('=') or list_name.startswith('-') and list_name.endswith('-'):
        
        for x in range(int(value)):
            print(list_name[1:-1])
            time.sleep(timebw)
        line()
    elif list_name=='/':
        ip = socket.gethostbyname(socket.gethostname())
        for x in range(int(value)):
            print(ip)
            time.sleep(timebw)
        line()
    elif value == '//':

        value1= int(input('range1>>>'))
        value2= int(input('range2>>>'))
        
        if pkgrandom == True:
            hi=random.randint(value1,value2)
            for x in range(hi):
                
                    
                print(list_name)
                time.sleep(timebw)
            line()
            
           
        else:
            print("ERR went wrong or random_int_pkg not imported")
            line()
    else:
        print("***ERR variable not found***")
        line()
    


    
    
def showfunc():
    print('''
log- prints input
strvar- assigns a str value
intvar- assigns an int value
showvars- shows all variables and values
showvar- shows value for a value
calc- calculate an expression
showfunc- shows listed functions
delvar- remove a single var
clearvars- remove all vars
updvar- reassign value to a var
cutvar- cut letters from a string
exit- exit program
stopfish- prints a ':)'
arr- assigns an array
arradd- append a value to an array
arrdel- removes a value from an array
arrindex- prints the index of a value in an array
cleararr- remove all values from an array
vlen- prints amount of letters 
arrlen- prints amount of items in array
arrpop- removed the last item inside an array
arrsort- sorts the array alphabetically
arrinc- checks if a value is in an array
arrmix- mixes two arrays into one
arrcount- counts the amount of times a value repeated in an array
logloop- prints a value for given time
pkgs- show available packages
getpkgs- get available packages
ip- gets user ip
devlog- show devlog
help- help
-------------------------
Pkg commands
rand- prints a random number from user input
exdate- prints date
extime- prints time
exdatetime- prints date and time
exutc- prints date, time and utc
cwd- shows the current working directory
showdir- shows all items in a directory
deldir- removes a directory in the specified location
makedir- makes a directory in the specified location
dirsize- shows the size of a path
sysinfo- gives total system info
sysarch- gives pc architecture
syspro- gives system processor
sysos- gives os info
pyv- gives python info
shell- run all shell commands
-------------------------
Calc operators
+ add
- subtract
* multiply
/ divide
// floor divide
** exponents
> greater than
< smaller than
% remainder
>= equal to or greater than
<= equal to or smaller than
!= not equal to
== equal to
''')
    line()
def devlog():
    print('''
DAY 1:
------
log
strvar
intvar
showvars
showvar
calc
showfunc
delvar
clearvars
updvar
cutvar
exit

DAY 2:
------
stopfish
arr
arradd
arrdel
cleararr
vlen
arrlen
arrpop
logloop

DAY 3:
------
pkgs
getpkgs
rand
exdate
extime
exdatetime
exutc
arrindex
arrsort
devlog

DAY 4:
------
arrinc
arrmix
arrcount
cwd
deldir
showdir
makedir
ip

DAY 5:
------
sysinfo
syspro
sysarch
sysos
pyv

DAY 6:
------
dirsize
shell

''')
    
    line()
def delvar():
    command = input("delvar>>>")
    if command in vars:
        del vars[command]
        print("Variable", command, "deleted.")
        time.sleep(.1)
        print("***successfully compiled 0***")
        line()
    else:
        print("Variable", command, "not found.")
    line()
    
def cutvar():
    command = input("value>>>")
    val=command
    if command.startswith('=') and command.endswith('=')or command.startswith('-') and command.endswith('-'):
        command = int(input("from>>>"))
        a=command
        command = int(input("to>>>"))
        b=command
        print(val[a:b])
        print("***successfully compiled 0***")
    elif command in vars:
        command = int(input("from>>>"))
        a=command
        command = int(input("to>>>"))
        b=command
        print(vars[val][a:b])
        print("***successfully compiled 0***")
    else:
        print("***ERR invalid log use '='or '-' before and after the str if the input is non-variable***")
    time.sleep(0.1)
    
    line()
    
    
def updvar():
    try:
        
        command = input("updatevar>>>")
        if command in vars:
            
            value = input("new value>>>")
            vars[command] = value
            print("Variable", command, "updated.")
            time.sleep(.1)
            print("***successfully compiled 0***")
            line()
        else:
            
            print("Variable", command, "not found.")
            line()
    except Exception as e:
        print("***ERR:", e,"***")
        line()

        
def clearvars():
    try:
        
        vars.clear()
        time.sleep(.1)
        print("***successfully compiled 0***")
        line()
    except Exception as e:
        print("***ERR:", e)
        line()

def calc():
    command = input(">>>")

    
    if command.startswith('`') and command.endswith('`') or command.startswith('!') and command.endswith('!'):
        listname = command[1:-1]
        if listname in vars and isinstance(vars[listname], list):
            try:
                
                index = int(input("index>>>"))
                
                if 0 <= index < len(vars[listname]):
                    item = vars[listname][index]
                    expression = input("expression (use item for list item)>>>")
                    
                    expression = expression.replace('item', str(item))
                    
                    result = eval(expression)
                    print(result)
                    print("***successfully compiled 0***")
                    line()
                else:
                    print("***ERR: Invalid index")
            except ValueError:
                print("***ERR: Invalid index")
        else:
            print("***ERR: Invalid list variable")
    
    
    elif re.match(r'^[-+]?\d*\.?\d+$', command):  
        result = eval(command)
        print(result)
        print("***successfully compiled 0***")
        line()
    elif command == "stopfish":
        print(":)")
    else:
        try:
            
            for var_name, var_value in vars.items():
                command = command.replace(var_name, str(var_value))
            result = eval(command)
            print(result)
            print("***successfully compiled 0***")
            line()
        except Exception as e:
            print("***ERR:", e)

    time.sleep(0.1)




    
wor=("***STOPFISH***")
print(wor.center(shutil.get_terminal_size().columns))
nor=("***type showfunc for listed functions***")
print(nor.center(shutil.get_terminal_size().columns))
ror=("***type help for help***\n\n")
print(ror.center(shutil.get_terminal_size().columns))

line()
'''THE END'''
