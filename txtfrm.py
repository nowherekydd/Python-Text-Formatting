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
# I mainly code on my Win11 laptop using Thonny [aka Windows], but I will test on my Arch Linux machine [using GNOME, irrc] [aka Arch] when I am able to.
# Last tested: 7/14/2024 on Windows

# Basic formatting

def bold(text):
    return "\033[1m" + text + "\033[0m"

def italic(text):
    return "\x1B[3m" + text + "\x1B[0m"

def underl(text):
    return "\033[4m" + text + "\033[0m"

def boldtal(text): 
    return "\033[1m" + "\x1B[3m" + text + "\x1B[0m" + "\033[0m"

# Debug/test. I reccommend you to delete anything beyond this comment if you're using this .py script in another project by importing it.
print(bold("This text is bold."))
print(italic("This text is italicized."))
print(underl("This text is underlined."))
print(boldtal("This text is bold and italicized under one function."))

# You can combine different formats by doing something similar to this.
# For common combos, I'll be making their own functions.

print(bold(italic("This text is bold and italicized in nested functions.")))