# -*- coding: utf-8 -*-
from navec import Navec;
from graphviz import Digraph;
def rules():
    print(" Правила : \n 1)Придумайте слово, но не называйте его.\n 2)Слово должно быть существительным в И.П. и реально существовать.\n 3)Ответами могут быть только горячо/тепло/нейтрально/прохладно/холодно \n");

def first_question():
    print("Оно живое?")
    first_question=input()
    return first_question


def add_node(tree, parent, child, label):
    """
    Adds a new node to the tree.

    Args:
        tree: The tree dictionary.
        parent: The parent node.
        child: The child node.
        label: The label for the edge between parent and child.
    """
    if parent not in tree:
        tree[parent] = {}
    tree[parent][child] = label
def tree():
    # Create an empty tree dictionary
    tree = {}

    # Add nodes to the tree
    add_node(tree, 'живое', 'человек', ('горячо' or 'тепло'))
    add_node(tree, 'живое', 'животное', ('горячо' or 'тепло'))
    add_node(tree, 'живое', 'растение', ('горячо' or 'тепло'))

    return tree

def print_tree(tree):
    # Print the tree
    print(tree)

     

data = {
    'живое': 
    {
        'человек': 
        {
            'профессия': 
            {
                'весёлая': 'клоун',
                'тяжёлая': 'врач'
            }
        },
        'животное': 
        {
           'большой': 'слон',
           'маленький': 'хомяк'
        },
        'растение': 
        {
            'размер': 
            {
                'средний': 'яблоко',
                'маленький': 'вишня'
            }
        }
 }
 }


'''
mem_granules={
        'горячо',
        'тепло',
        'нейтрально',
        'прохладно',
        'холодно',
        }

def questions_ask():
    print("Оно живое?")
    first_question=input()


    print("Оно материальное(можно пощупать)?")
    second_question=input()

    print("Это абстрактное понятие?")
    third_question=input()

    print("Оно большое?")
    fourth_question=input()


def answer_print():
    print("Введите ваше слово для проверки")
    answer=input()
    print(navec.vocab[answer])
'''
    
    