class Employee():

    Manager=[]

    def __init__(self,name,age,position,exp=None):
        self.name=name
        self.age=age
        self.position=position
        self.exp=exp


    def __str__(self):
        return self.name
    
    def show__experience(self):
        if self.age >28:
            print('{} is an senior employee in this company'.format(self.name))
        else:
            print('{} is newly joined in our company'.format(self.name))


    def add_manager(self):
        if self.exp == None:
            print('{} cannot be added as an manager'.format(self.name))
        elif self.exp >7:
            self.Manager.append({'name':self.name,'position':self.position,'experience':self.exp})
            print('{} has been successfully added to our manager list'.format(self.name))


