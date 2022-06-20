# Module creation training
# Never import all objects in a program. It may be the chance that after importing you overwrite
# modules in your current file.
#  Path looking

import sys
# sys.path gives you access to all the paths to packages in your program
# To turn a folder in a package add a file called __init__.py to said folder
# python will recognize it as a package.
# After the folder has been turned into a package the import process changes to
# package.module (import Python_Training_2022.modules)

print(sys.path)

class UIControl():
    def draw(self):
        print("Draw")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


def draw(controls):
    for control in controls:
        control.draw()


# dir function.
# Can check all the methods and attributes in an object



