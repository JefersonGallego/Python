

from mailbox import NoSuchMailboxError


class Usuario:

    def __init__(self,nombre,id):
        self.nombre=nombre
        self.__user=nombre+str(id) 
        
    def print_user(self):
        print(f'El Usuario es {self.__user}')

if __name__=='__main__':
    user1= Usuario('Sergio',123456)
    print(user1.nombre)
    print(user1.__user)
