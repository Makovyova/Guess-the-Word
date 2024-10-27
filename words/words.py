# -*- coding: utf-8 -*-
import numpy as np;
from navec import Navec;
#import matplotlib.pyplot as plt;
#import skfuzzy as fuzz;
from questions import rules;
from questions import first_question,print_tree,tree;
from context import skip_gram;
#from membership_func import quest_mem_func;

#Большой файл со словами (рус)
path = './navec_hudlit_v1_12B_500K_300d_100q.tar'
navec = Navec.load(path)
#Объявление правил

def Menu():
    while True:
        print(" 1-Правила \n 2-Первый вопрос \n 3-Показать дерево вопросов \n 4-skip-gram \n 0-Выйти \n *-Угадал \n")        
        actions = {
        '1': rules,
        '2': first_question,
        '3': tree,
        '4': skip_gram,
        #'5': quest_mem_func,#Дефаззификация
        '0': exit,
        #'*': exit
        }
        choice=input("Что вы хотите? ")
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Неправильный выбор")


#Вызов меню
if __name__ == "__main__":
    Menu()
