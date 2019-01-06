# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 11:13:44 2018

@author: Siew Ling
for Data Quest Guided Project #5: Visualizing The Gender Gap in College Degree
"""


import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
cb_dark_blue = (0/255,107/255,164/255)
cb_orange = (255/255, 128/255, 14/255)
stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']
fig = plt.figure(figsize=(18, 9))

for sp in range(0,6):
    ax1 = fig.add_subplot(6,3,sp*3+1)
    ax3 = fig.add_subplot(6,3,sp*3+3)
    ax1.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax1.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    ax3.plot(women_degrees['Year'], women_degrees[other_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax3.plot(women_degrees['Year'], 100-women_degrees[other_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    ax1.spines["right"].set_visible(False)    
    ax1.spines["left"].set_visible(False)
    ax1.spines["top"].set_visible(False)    
    ax1.spines["bottom"].set_visible(False)
    ax3.spines["right"].set_visible(False)    
    ax3.spines["left"].set_visible(False)
    ax3.spines["top"].set_visible(False)    
    ax3.spines["bottom"].set_visible(False)
    ax1.set_xlim(1968, 2011)
    ax1.set_ylim(0,100)
    ax3.set_xlim(1968, 2011)
    ax3.set_ylim(0,100)
    ax1.set_title(stem_cats[sp])
    ax3.set_title(other_cats[sp])
    ax1.tick_params(bottom="off", top="off", left="off", right="off",labelbottom="off")
    ax3.tick_params(bottom="off", top="off", left="off", right="off",labelbottom="off")
    ax1.set_yticks([0,100])
    ax3.set_yticks([0,100])
    ax1.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
    ax3.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
    if sp == 0:
        ax1.text(2005, 89, 'Men')
        ax1.text(2002, 6, 'Women')
        ax3.text(2005, 5, 'Men')
        ax3.text(2002, 90, 'Women')
    elif sp == 5:
        ax1.text(2005, 62, 'Men')
        ax1.text(2001, 30, 'Women')
        ax3.text(2005, 62, 'Men')
        ax3.text(2001, 30, 'Women')
        ax1.tick_params(labelbottom="on")
        ax3.tick_params(labelbottom="on")
for sp in range(0,5):
    ax2 = fig.add_subplot(6,3,sp*3+2)
    ax2.plot(women_degrees['Year'], women_degrees[lib_arts_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax2.plot(women_degrees['Year'], 100-women_degrees[lib_arts_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    ax2.spines["right"].set_visible(False)    
    ax2.spines["left"].set_visible(False)
    ax2.spines["top"].set_visible(False)    
    ax2.spines["bottom"].set_visible(False)
    ax2.set_xlim(1968, 2011)
    ax2.set_ylim(0,100)
    ax2.set_title(lib_arts_cats[sp])
    ax2.tick_params(bottom="off", top="off", left="off", right="off",labelbottom="off")    
    ax2.set_yticks([0,100])
    ax2.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
    if sp == 0:
        ax2.text(1970, 8, 'Men')
        ax2.text(1970, 87, 'Women')
    elif sp == 4:
        ax2.text(1970, 68, 'Men')
        ax2.text(1970, 24, 'Women')
        ax2.tick_params(labelbottom="on")
plt.savefig("gender_degrees.png")
plt.show()