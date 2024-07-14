#  _ _  _____ __ _| |_  ___ _ _ ___ 
# | ' \/ _ \ V  V / ' \/ -_) '_/ -_)
# |_||_\___/\_/\_/|_||_\___|_| \___|
# | |___  _ __| |__| |        (_) \ 
# | / / || / _` / _` |         _ | |
# |_\_\\_, \__,_\__,_|        (_)| |
#      |__/                     /_/ 
#
# Python Text Formatting Helper
# by nowherekydd :)

# I know this might already exist out there somewhere, but this could be useful for someone out there.

# PLEASE NOTE! Not all of these functions will work with every terminal/console.
# The IDE I use, Thonny, does not support colors in its own shell.

# I usually code on these machines:
# WINDOWS - Windows 11, Thonny IDE, Windows PowerShell
# ARCH - Arch Linux, Thonny IDE, GNOME Terminal

# Last tested: 7/14/2024 @ 1917 on Windows

### Basic formatting ###

def bold(text):
    return "\033[1m" + text + "\033[0m"

def italic(text):
    return "\x1B[3m" + text + "\x1B[0m"

def underl(text):
    return "\033[4m" + text + "\033[0m"

def boldtal(text): 
    return "\033[1m" + "\x1B[3m" + text + "\x1B[0m" + "\033[0m"

def linebreak():
    print("\n")

### Colors ###

reset = "\033[0m"

# Generates code based off RGB.
def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

# RGB codes.
red = rgb(255, 0, 0)
orange = rgb(255, 128, 0)
yellow = rgb(255, 255, 0)
green = rgb(0, 255, 0)
ltblue = rgb(0, 255, 255)
blue = rgb(0, 0, 255)
purple = rgb(125, 0, 255)
magenta = rgb(255, 0, 255)

# Final formatting.
def cred(text):
    return red + text + reset

def corange(text):
    return orange + text + reset

def cyellow(text):
    return yellow + text + reset

def cgreen(text):
    return green + text + reset

def cltblue(text):
    return ltblue + text + reset

def cblue(text):
    return blue + text + reset

def cpurple(text):
    return purple + text + reset

def cmagenta(text):
    return magenta + text + reset

### Debug ###
# I reccommend you to delete anything beyond this comment if you're using this .py script in another project by importing it.
print("Python Formatting Helper by nowherekydd")
linebreak()
print("Formatting")
print(bold("This text is bold."))
print(italic("This text is italicized."))
print(underl("This text is underlined."))
print(boldtal("This text is bold and italicized under one function."))
linebreak()
print("Colors")
print(cred("This text is red."))
print(corange("This text is orange."))
print(cyellow("This text is yellow."))
print(cgreen("This text is green."))
print(cltblue("This text is light blue."))
print(cblue("This text is blue."))
print(cpurple("This text is purple."))
print(cmagenta("This text is magenta."))

# You can combine different formats by doing something similar to this.
# For common combos, I'll be making their own functions.
# print(bold(italic("This text is bold and italicized in nested functions.")))