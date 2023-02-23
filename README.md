## AirBnB clone - The console

## Introduction
This Project is the first step towards building our first full web application: the AirBnB clone. This is to build a comand interpreter that manages the objects of the project.

## Creation Of The Console
* First we create the parent class BaseModel.
* This class do the initialization, serialization and deserialization of the future instances : Instance <-> Dictionary <-> JSON string <-> file
* Then we create the FileStorage class, the first storage engine.
* We create the console, to interpret the args and kwargs.
* We create several classes that inherit from Basemodel, such as City, State, Place, Amenity, and Review.
* We finish by creating the unittests to validate all the class and storage processes.

## Useful Definitions
* A Python Package is a folder that contains modules and other folders. A package folder usually contains a file named __init__.py that tells Python: “This directory is a package.” The init file may be empty, or it may contain code to be executed upon package initialization.
* The Cmd instance or subclass instance is a line-oriented interpreter framework. It’s useful as a superclass of an interpreter class defined by the coder to inherit Cmd’s methods and encapsulate action methods.
* To manage datetime in Python, the module named Datetime must be imported. This model allows the code to deal with hours and or dates.
* UUIDs (Universally Unique Identifier) are used to identify information that needs to be unique within a system.
* The special syntax ```*args``` is used to pass a variable number of arguments to a function.
* The special syntax ```**kwargs``` allow the user to pass keyword arguments to a function. They are used when one isn’t sure the number of keyword arguments that will be passed to the function.
* Keyword arguments are values that, when passed into a function, are identifiable by specific parameter names. A keyword argument is preceded by a parameter and the assignment operator.

## Using the Console
The console runs with ./console.py

When used, the console creates a BaseModel instance. The BaseModel assigns the attributes and calls the new method in storage. FileStorage saves the class and id in a dictionary.
newinstance.save goes to BaseModel and saves the date of modification. It calls on storage.save, and the save function in FileStorage goes through the dictionary with the name and id. The object is serialized to JSON.

## Main Commands
| COMMAND | DESCRIPTION |
| ----------------------- | ------------ |
| quit | quit the console |
| EOF | To quit the console by EOF |
| help + command | Display the help for the command ask |
| create + class | Creates an object and prints the ID |
| show + class + id | Displays the information of the object |
| destroy + class + id | Removes an object |
| all + class | Shows all the instances of a class |
| update + class + id + attribute name + "attribute value" | Updates the attribute of a class |
| count + class	To count | Counts the number of instance by class |

## BaseModel
The BaseModel class is the parent of all the classes :
* The init method defines the common attributes for all the class that inherit from that one.
* The str method is the method that defines the good output format as a string.
* The save method is useful to updates the public instance attribute 'updated_at' with the current time and date.
* The to_dict method returns a dictionary containing all the keys and values of the instance.

## Additional Classes
#### User
Attributes: email + password + first_name + last_name
Class about the user information.
#### State
Attributes: name
Class about the future state of the future location.
#### City
Attributes: state_id + name
Class for more precise information about the geographic position of future location.
#### Place
Attributes: city_id + user_id + name + description number_rooms + number_bathrooms + max_guest price_by_night + latitude + longitude + amenity_ids
Class about the future location, all important information like the number of room and the equipment inside the location.
#### Review
Attributes: place_id + user_id + text
Class for a review of the future place with information of the user that post the review.
#### Amenity
Attributes: name
Class about the future amenity.

## FileStorage
* This file contains methods used by the console
* The all method displays the dictionary of the object.
* The new method sets a new instance with the class name and a new id for the object.
* The save method serialize the object in dictionary format to the JSON file.
* The reload method deserialize the JSON file to object.

## Unit Tests
The command to display the results of the tests in interactive mode is:
```
python3 -m unittest discover tests
```
And the command in non-interactive mode is :
```
echo "python3 -m unittest discover tests" | bash
```
