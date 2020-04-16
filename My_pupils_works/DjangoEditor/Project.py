import os
from Application import *
class Project:
    def __init__(self,way,name):
        self.way=way
        self.name=name
        if name in os.listdir(way):
            self.load()
        else:
            self.create()
    def create(self):
        os.chdir(self.way)
        os.system("cd " + self.way+ " & django-admin startproject " + self.name)
        print("Project was created!")
        self.apps=[]
    def load(self):
        print("Project was loaded!")
    def add_app(self,name):
        self.apps.append(Application(self.way+'\\'+self.name,name))
        text=0
        with open(self.way+'\\'+self.name+'\\'+self.name+'\\urls.py','r') as f:
            text=f.read()
        with open(self.way+'\\'+self.name+'\\'+self.name+'\\urls.py','w') as f:
            f.write('import '+name+'.views \n'+text)
q = Project(r'C:\Users\Python\Desktop','test_proj8')
q.add_app('webapp')