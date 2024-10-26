import numpy as np;
from navec import Navec;
import skfuzzy as fuzz;
import matplotlib.pyplot as plt;
from skfuzzy import control as ctrl;


def quest_mem_func():
    quest=ctrl.Antecedent(np.arange(0, 101, 1), 'alive')
    quest['горячо'] = fuzz.gaussmf(quest.universe, 100, 10)  # Гауссовская функция с пиком в 100
    quest['тепло'] = fuzz.gaussmf(quest.universe, 50, 15)  # Гауссовская функция с пиком в 50
    quest['прохладно'] = fuzz.gaussmf(quest.universe, 15, 10)  # Гауссовская функция с пиком в 15
    quest['холодно'] = fuzz.gaussmf(quest.universe, 0, 10)  # Гауссовская функция с пиком в 0

    answ=ctrl.Consequent(np.arange(0, 101, 1), 'alive')
    answ['горячо'] = fuzz.gaussmf(answ.universe, 100, 10)  # Гауссовская функция с пиком в 100
    answ['тепло'] = fuzz.gaussmf(answ.universe, 50, 15)  # Гауссовская функция с пиком в 50
    answ['прохладно'] = fuzz.gaussmf(answ.universe, 15, 10)  # Гауссовская функция с пиком в 15
    answ['холодно'] = fuzz.gaussmf(answ.universe, 0, 10)  # Гауссовская функция с пиком в 0
    rule1 = ctrl.Rule((quest['горячо'] | quest['тепло'], answ )
    # Visualize the membership functions
    quest.view(sim=50)


'''
    mem_granules={
        'горячо',
        'тепло',
        'прохладно',
        'холодно',
        }
    #print(navec.vocab['живое'])
'''
    