import os

class Application:
    def __init__(self,way,name):
        self.way=way
        self.name=name
        if name in os.listdir(way):
            self.load()
        else:
            self.create()
    def add_import_line(self,file):
        text=0
        with open(self.way+'\\'+self.name+'\\'+file,'r') as f:
            text=f.read()
        with open(self.way+'\\'+self.name+'\\'+file,'w') as f:
            f.write('from '+self.name+'.models import*\n'+text)
    def create(self):
        os.chdir(self.way)
        os.system("cd " + self.way+ " & django-admin startapp " + self.name)
        os.chdir(self.way+'\\'+ self.name)
        os.system("cd " + self.way+'\\'+ self.name +" & mkdir templates" )
        self.add_import_line('views.py')
        self.add_import_line('admin.py')    
        print("Application was created!")
        self.pages=[]
    def load(self):
        self.pages = os.listdir(self.way+'\\'+self.name+'\\templates')
        print("Application was loaded!")

    def add_page(self,name):
        with open(self.way+'\\'+self.name+'\\templates\\'+name+'.html','w') as f:
            f.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

</body>
</html>
""")
        self.pages.append(name)
    def remove_page(self,name):
        self.pages.remove(name)
        os.remove(self.way+'\\templates\\'+name)
