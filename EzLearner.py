# coding: utf8
from __future__ import unicode_literals
import os
import random
import sys
import time
import pickle
import math

import io

# EzLearner 0.2

#TODO:
# 1) Main menu - Modes: Version / Thème
# 2) gestion des parenthèses / des slashs


'''
n = number of words
Every word start with weight 16.
Iitial capacity = 16 x number of words.
Upon failing on a word, its weight is doubled, up to 256. Update capacity by the difference.
Upon succeeding on a word, its weight is halved, up to 1. Update capacity by the difference.
Randomly choose a number r between 0 and capacity - 1.
Use dichotomy search to get the word in the weighted dictionary.
The weighted dictionary is represented as a binary tree, where at each node in the tree is stored the sum of the weights of the nodes that are under it. (ABR)
The leaves in the tree are the actual words. At each level in the tree, the sum of weights equal to the total capacity.
An update on the weight of the word is performed by changing the weight of the leaf, and by propagating to his fathers the update.
Finding the word corresponding to the random number r is performed in O(log(n)).
Updating a weight of word is performed in O(log(n)).
Building the binary tree is performed recursively in O(nlog(n)). ?

'''

from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.label = Label(self, text="", font=('Arial', 20))
        self.label.place(x=200,y=120)
        self.update("EzLearner")

    def update(self, st):
        self.label.configure(text=st)

root = Tk()
app = Window(root)
root.wm_title("EzLearner")
root.geometry("600x300")
root.update()

class TreeDict():  # ToDo: Update, parenthesis handling
    def __init__(self, list_of_lines, delimiter, meaning_delimiter, father=None, depth=0):
        n = len(list_of_lines)
        self.length = n
        self.father = father
        self.left = []
        self.right = []
        self.translations = []
        self.depth = depth
        if n > 1:
            self.native_word = ""
            self.weight = 16*len(list_of_lines)
            self.left.append(TreeDict(list_of_lines[:n//2], delimiter, meaning_delimiter, father=[self], depth=self.depth + 1))
            self.right.append(TreeDict(list_of_lines[n//2:], delimiter, meaning_delimiter, father=[self], depth=self.depth + 1))
            return
        elif n == 1:
            self.weight = 16
            line = list_of_lines[-1].split(delimiter)
            self.native_word = line[0]
            self.translations = line[-1].split(meaning_delimiter)
            return
        else:
            self.native_word = ""
            self.weight = 0
            return

    def update(success=True):
        if success:
            if self.weight > 1:
                pass

            return
        else:
            if self.weight < 256:
                pass
            return

    def __len__(self):
        return self.length

    def copy(self):
        # DFS
        pass

    def print(self):
        if self.length <= 1:
            #print(self.native_word + " -> " + self.translations[0])
            #print(self.native_word)
            app.update(self.native_word)
            root.update()
        else:
            self.left[0].print()
            self.right[0].print()
        return

def clean_words(word_path="./words/jap_raw", output_path="./words/clean_jap"):
    # Check for spaces with arrow & comas
    # Clean unicode emojis
    pass



def setup(words_path="./words/jap_raw", config_path="./config_jap.cfg", dict_save_path="./weighted_dict.pckl"):
    translate_delimiter = ' → ' # Please include spaces if necessary
    meaning_delimiter = ', '     # Please include spaces if necessary
    with open(words_path, mode='r', encoding='utf-8') as word_file:
        lines = word_file.readlines()
        n = len(lines)
        tree_height = math.floor(math.log2(n)) + 1
        dictionary = TreeDict(lines, translate_delimiter, meaning_delimiter)

        with open(dict_save_path, 'wb') as save_file:
            pickle.dump(dictionary, save_file)


def load(dict_save_path="./weighted_dict.pckl"):
    with open(dict_save_path, 'rb') as save_file:
        dictionary = pickle.load(save_file)

    #dictionary.print()
    return dictionary

## MENU
def menu():
    print(" ______     ______     __         ______     ______     ______     __   __     ______     ______    ")
    print('/\  ___\   /\___  \   /\ \       /\  ___\   /\  __ \   /\  == \   /\ "-.\ \   /\  ___\   /\  == \   ')
    print("\ \  __\   \/_/  /__  \ \ \____  \ \  __\   \ \  __ \  \ \  __<   \ \ \-.  \  \ \  __\   \ \  __<   ")
    print(' \ \_____\   /\_____\  \ \_____\  \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_\\\ \_\  \ \_____\  \ \_\ \_\ ')
    print("  \/_____/   \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_/ /_/   \/_/ \/_/   \/_____/   \/_/ /_/ ")
    print("                                                                                                    ")

    print("1. Play with existing config")
    print("2. Reset - New config")
    print(" ")
    tmp = input()
    if tmp == '1':
        dico = load()
        play(dico)
        save(dico)
    elif tmp == '2':
        setup()
        print("Setup successful.")
        load()
        exit()
    else:
        print("Invalid menu choice. Exiting program.")
        exit()

def save(dic): # Saves config file
    try:
        new_config = open(config_path, 'w', encoding='utf8')
        for key in dic.keys():
            new_config.write(key + ":" + str(dico[key][1]) + "\n")
    except Exception as e:
        print(e)
    finally:
        new_config.close()

## MAIN

def play(dic): # Fontion comprenant la boucle principale de jeu
    done = False
    while not done:
        weight = dic.weight
        r  = random.randint(weight)
        word = # TODO: Get Word inFo in by coding method in BTS class



menu()
