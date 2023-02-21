import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


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

        args = arg.split()[0]

        if not arg:
            print("** class name missing **")

        elif args in self.tab:
            new_instance = eval(arg + '()')
            new_instance.save()
            print(new_instance.id)
    
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """On va recuper le dictionnaire d'une id d'une class"""
        args = arg.split()

        if not arg:
            print("** class name missing **")
            return
        
        class_name = args[0]
        if class_name not in self.tab:
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        id = args[1]
        key = "{}.{}".format(class_name, id)
        obj_all = models.storage.all()
        if key not in obj_all:
            print("** no instance found **")
            return
        print(obj_all[key])

    def do_destroy(self, arg):
        """On va suprimer les instance d'une class et enregister dans le fichier json"""
        args = arg.split()

        if not arg:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.tab:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        id = args[1]
        key = "{}.{}".format(class_name, id)
        obj_all = models.storage.all()
        if key not in obj_all:
            print("** no instance found **")
            return

        del obj_all[key]

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name
        Usage: all [Class Name] or all"""
    
        args = arg.split()
        obj_all = models.storage.all()

        # Si aucun argument n'est fourni, on affiche toutes les instances.
        if not len(args):
            print([str(obj_all[key]) for key in obj_all])
        
        # Si un nom de classe est fourni, on affiche toutes les instances de cette classe.
        elif args[0] in self.tab:
            print([str(obj_all[key]) for key in obj_all if key.startswith(args[0] + ".")])

        else:
            print("** class doesn't exist **")

               
    def do_update(self, arg):
        """met à jour une instance en fonction du nom et de l'identifiant
            en ajoutant ou en mettant à jour l'attribut"""
        pass