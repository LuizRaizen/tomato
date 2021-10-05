#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Tomato is a command-line task automation module.

    Specialized in text formatting and editing; with Tomato's text 
    editing tools, you can devote more time to the most important 
    details of your program. Format your output in the terminal with
    just a function call and a few arguments.
    
    I. What can you do with Tomato 'format' tool?
    |
    |___ 1) Change you output color text and background:
    |        - Change your program's output color in the terminal with 
    |          the ANSI escape sequence. Just pass an argument 'color'
    |          with the name of the text color, And with the 'markup'
    |          argument do you can change the background color of your 
    |          text. You can use all colors from the ANSI color table:
    |               
    |             *black
    |             *red
    |             *green
    |             *yellow
    |             *blue
    |             *magenta
    |             *white
    |         
    |         (Use the bright version of all colors by adding "bright_"|
    |         before the color name.)                                  |
    |                                                                  |
    |___ 2) Set a style to you text:                                   |
    |        - 

"""


__author__ = "Luiz R. Dererita"
__credits__ = "Thanks to all free software comunity."
__copyright__ = "Copyright (c) Developed by Luiz R. Dererita, 2021."
__version__ = "0.0.3"
__license__ = "MIT License"
__status__ = "Prototype"
__maintainer__ = "Luiz R. Dererita"
__email__ = "luizdererita02@gmail.com"


import os


def format(text, style=False, color=False, markup=False, align=False):
    """ Returns a custom string based on the arguments received. """
    
    st = _set_style(style)
    fr = _set_color(color)
    mk = _set_markup(markup)
    
    fmt = st, fr, mk
    edit = "\033["
    
    for i in fmt:
        if i:
            edit += f"{i};" if not i == mk else i
        
    edit += "m"
    
    return edit + _set_align(text, align) + "\033[0m"
    

def _set_align(text, align):
    width, height = os.get_terminal_size()
    
    _TEXT_ALIGN = {
        'center':  text.center(width),
        'right':   text.rjust(width),
        'left':    text.ljust(width),
        False:     text
    }

    if align in _TEXT_ALIGN:
        return _TEXT_ALIGN[align]
    
    return text


def _set_style(style):
    _TEXT_STYLES = {
        "bold":      "1",
        "underline": "4",
        "negative":  "7",
        False:       False
    }
    
    return _TEXT_STYLES[style]
    
def _set_color(color):
    _TEXT_COLORS = {
        'black':           "30",
        'red':             "31",
        'green':           "32",
        'yellow':          "33",
        'blue':            "34",
        'magenta':         "35",
        'cyan':            "36",
        'white':           "37",
        "bright_black":    "90",
        "bright_red":      "91",
        "bright_green":    "92",
        "bright_yellow":   "93",
        "bright_blue":     "94",
        "bright_magenta":  "95",
        "bright_cyan":     "96",
        "bright_white":    "97",
        False:             False
    }

    if color in _TEXT_COLORS:
        return _TEXT_COLORS[color]
    
    return text
    
def _set_markup(color):
    _MARKUP_COLORS = {
        "black":           "40",
        "red":             "41",
        "green":           "42",
        "yellow":          "43",
        "blue":            "44",
        "magenta":         "45",
        "cyan":            "46",
        "white":           "47",
        "bright_black":    "100",
        "bright_red":      "101",
        "bright_:green":   "102",
        "bright_yellow":   "103",
        "bright_blue":     "104",
        "bright_magenta":  "105",
        "bright_cyan":     "106",
        "bright_white":    "107",
        False:             False
    }

    if color in _MARKUP_COLORS:
        return _MARKUP_COLORS[color]
    
    return text
