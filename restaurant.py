sorvetes =['baunilha','chocolate','morango']
lista_string=["can add post","can delete post","can ban user"]

class User():

    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
        self.number_served = 0
        self.login_attempts = 0
    
    def increment_number_served(self,b):
        self.number_served += b

    def restaurant(self,a):
        self.number_served = a
    
    def just_readbro(self):
        print("clientes sevidos " + str(self.number_served) + ".")

    def describe_restaurant(self):
        print(self.name.title() + " " + self.lastname.title())
        print(self.name.title() + " CPF:087.577.221.88")
        print(self.name.title() + " CEP:79074100")
    
    def open_restaurant(self):
        print("Ta aberto rapeize")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        a = self.login_attempts
        print("Tentativa " + str(a))
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Voce foi resetado, tentativa " + str(self.login_attempts) +"\n\n")

class Privileges():

    def __init__(self):
        self.privileges = lista_string

    def describe_listastring(self):
        print("\n\nO admin pode: \n")
        for i in self.privileges:
            print(i)

class Admin(User):

    def __init__(self, name, lastname):
        super().__init__(name, lastname)
        self.privileges_admin = Privileges()

class IceCreamStand(User):

    def __init__(self, name, lastname):
        super().__init__(name, lastname)
        self.flavors = sorvetes
    
    def describe_sorvetes(self):
        for i in self.flavors:
            print(i)


