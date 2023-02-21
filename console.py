#!/usr/bin/python3
"""CONSOLE DE LA CONSOLE AIRBNB"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand qui herite cmd.Cmd"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass

    tab = ["BaseModel", "ali"]

    def do_create(self, arg):
        """On va cree une nouvelle instance de class en fonction 
        de l'argument """

        if not arg:
            print("** class name missing **")

        elif arg in self.tab:
            new_instance = eval(arg + '()')
            new_instance.save()
            print(new_instance.id)
    
        else:
            print("** class doesn't exist **")

    
    def do_show(self, arg):
        """On va imprimer la representation sous forme de chaine
        on fonction du nom de l'edantifiant mis dans arg"""
        pass

    def do_destroy(self, arg):
        """on va suprimer une instance en fonction du nom et de l'identifiant
        de la class mis dans arg"""
        pass

    def do_all(self, arg):
        """imprimeles représentations sous forme de chaîne de toutes 
        les instances en fonction ou non du nom de la classe"""
        pass

    def do_update(self, arg):
        """met à jour une instance en fonction du nom et de l'identifiant
            en ajoutant ou en mettant à jour l'attribut"""
        pass



if __name__ == '__main__':
    HBNBCommand().cmdloop()
