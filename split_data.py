# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 10:39:13 2020

@author: shanthakumar
"""


import os
import random
from shutil import copyfile 

def split_data(SOURCE, TRAINING, TESTING, SPLIT_SIZE):
    files = []
    for filename in os.listdir(SOURCE):         
         file = SOURCE + filename
         
         if os.path.getsize(file) > 0:             
             files.append(filename)
             
         else:
             print(filename + " is zero length, so ignoring.")

    training_length = int(len(files) * SPLIT_SIZE)
    testing_length = int(len(files) - training_length)
    
    shuffled_set = random.sample(files, len(files))
    training_set = shuffled_set[0:training_length]
    testing_set = shuffled_set[-testing_length:]
    for filenames in training_set:
        move_file = SOURCE + filenames
        designation = TRAINING+filenames
        copyfile(move_file, designation)
    for filenames in testing_set:
        move_file = SOURCE + filenames
        designation = TESTING+filenames
        copyfile(move_file, designation)
        
Dorsch_SOURCE_DIR = "conference_dataset/herring_train/"
TRAINING_Dorsch_DIR = "conference_dataset/her_conf_tran/"
TESTING_Dorsch_DIR = "conference_dataset/her_conf_test/"

#Herring_SOURCE_DIR = "test_images/herring/"
#TRAINING_Herring_DIR = "Trainexample1/herring/"
#TESTING_herring_DIR = "Validation-Example1/herring/"

# Kliesche_SOURCE_DIR = "test_images/kliesche/"
# TRAINING_kliesche_DIR = "Trainexample1/kliesche/"
# TESTING_kliesche_DIR = "Validation-Example1/kliesche/"

# steinbutt_SOURCE_DIR = "test_images/steinbutt/"
# TRAINING_steinbutt_DIR = "Trainexample1/steinbutt/"
# TESTING_steinbutt_DIR = "Validation-Example1/steinbutt/"




split_size = .12
split_data(Dorsch_SOURCE_DIR, TESTING_Dorsch_DIR, TRAINING_Dorsch_DIR, split_size)

# split_data(Herring_SOURCE_DIR, TRAINING_Herring_DIR, TESTING_herring_DIR, split_size)


# split_data(Kliesche_SOURCE_DIR, TRAINING_kliesche_DIR, TESTING_kliesche_DIR, split_size)


# split_data(steinbutt_SOURCE_DIR, TRAINING_steinbutt_DIR, TESTING_steinbutt_DIR, split_size)

