"""
    TREND MAYA TOOLS UI

    AUTHOR : Mahmoud Kamal

    DATE : 8-4-2018






"""

import os

import sys


import platform

import random

import webbrowser

from functools import partial

from ix import *




# ===================================================================================


windows_main_path = "Y:/Assets/Scripts/ClarisseTools/Scripts"  


path_name = windows_main_path

dirs = os.listdir(path_name)





def is_item_exists(slot, category_name, item_title):

    items = shelf.get_items(slot, category_name)

    if items == None:

        return False

    for j in range(items.get_count()):

        item = items[j]

        if item_title == item.get_title():

            return True

    return False





for folder in dirs:



    sub_folder = path_name + "/" + folder

    shelf = ix.application.get_shelf()


    for file_ in os.listdir(sub_folder):



        after_split = file_.split(".")  



        if after_split[1] == 'py':  

            script_full_path = sub_folder + "/" + file_

            icon_path = sub_folder + "/" + after_split[0] + ".png"

            hint_file_path = sub_folder + "/" + after_split[0] + ".txt"

            hint_html_path = sub_folder + "/" + after_split[0] + ".html"

            if os.path.isfile(hint_file_path):

                hint_file = open(hint_file_path, 'r')

                help_file_name = hint_file_path

                hint = str(hint_file.readlines())

            elif os.path.isfile(hint_html_path):

                hint_file = open(hint_html_path, 'r')

                help_file_name = hint_html_path

                hint = str(hint_file.readlines())

            else:

                help_file_name = ''

                hint = ""

            if os.path.isfile(icon_path):


                icon_style = "iconAndTextHorizontal"

            else:

                icon_style = "textOnly"


            print script_full_path , icon_path

            extract_title_description = open(script_full_path,'r')


            lines = extract_title_description.readlines()

            if is_item_exists(0, folder, after_split[0]) == False:

                shelf.add_item(0,folder ,after_split[0],lines[0],script_full_path,icon_path)

            else:

                print ""

            extract_title_description.close()
