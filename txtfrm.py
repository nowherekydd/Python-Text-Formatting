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

# Last tested: 7/14/2024 @ 1955 on ARCH

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
## Basic rainbow
red = rgb(255, 0, 0)
orange = rgb(255, 128, 0)
yellow = rgb(255, 255, 0)
green = rgb(0, 255, 0)
ltblue = rgb(0, 255, 255)
blue = rgb(0, 0, 255)
purple = rgb(125, 0, 255)
magenta = rgb(255, 0, 255)

## Advanced colors
### Black/White/Grey
silver = rgb(192, 192, 192)
grey = rgb(128, 128, 128)
### Red
### Orange
coral = rgb(240, 128, 128) #
### Yellow
gold = rgb(255, 215, 0) #
### Green
olive = rgb(128, 128, 0) #
chartreuse = rgb(127, 255, 0) #
### Blue
navy = rgb(0, 0, 128) #
royalblue = rgb(65, 105, 225) #
### Purple
indigo = rgb(75, 0, 130) #
orchid = rgb(186, 85, 211) #
### Brown
brown = rgb(165, 42, 42) #
khaki = rgb(240, 230, 140) #

# Final formatting.
## Basic
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

## Advanced
### Black/White
def csilver(text):
    return silver + text + reset
def cgrey(text):
    return grey + text + reset
### Red
### Orange
def ccoral(text):
    return coral + text + reset
### Yellow
def cgold(text):
    return gold + text + reset
### Green
def colive(text):
    return olive + text + reset
def cchartreuse(text):
    return chartreuse + text + reset
### Blue
def cnavy(text):
    return navy + text + reset
def croyalblue(text):
    return royalblue + text + reset
### Purple
def cindigo(text):
    return indigo + text + reset
def corchid(text):
    return orchid + text + reset
### Brown
def cbrown(text):
    return brown + text + reset
def ckhaki(text):
    return khaki + text + reset

### Demo ###
# I recommend you to delete anything beyond this comment if you're using this .py script in another project by importing it.
print(bold("Python Formatting Helper by nowherekydd"))
print(italic("This helper includes a linebreak function (linebreak())"))
linebreak()
print(boldtal("Formatting"))
print(bold("This text is bold."))
print(italic("This text is italicized."))
print(underl("This text is underlined."))
print(boldtal("This text is bold and italicized."))
linebreak()
print(boldtal("Colors"))
print(italic("Basic Colors"))
print(cred("This text is red."))
print(corange("This text is orange."))
print(cyellow("This text is yellow."))
print(cgreen("This text is green."))
print(cltblue("This text is light blue."))
print(cblue("This text is blue."))
print(cpurple("This text is purple."))
print(cmagenta("This text is magenta."))
print(italic("Advanced Colors"))
print(csilver("This text is silver."))
print(cgrey("This text is grey."))
print(ccoral("This text is coral."))
print(cgold("This text is gold."))
print(colive("This text is olive."))
print(cchartreuse("This text is chartreuse."))
print(cnavy("This text is navy."))
print(croyalblue("This text is royal blue."))
print(cindigo("This text is indigo."))
print(corchid("This text is orchid."))
print(cbrown("This text is brown."))
print(ckhaki("This text is khaki."))
linebreak()

# You can combine different formats by doing something similar to this.
# For common combos, I'll be making their own functions.
# print(bold(italic("This text is bold and italicized in nested functions.")))