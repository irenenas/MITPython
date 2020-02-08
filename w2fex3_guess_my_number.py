#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 13:15:20 2020

@author: irina
"""

secret_number=-1
low = 0
high = 100
guess = (high + low)//2
print("Please think of a number between 0 and 100!")
while guess != secret_number:
    print("Is your secret number " + str(guess) + "?")
    hint=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if hint in ('H','h'):
        high = guess
        guess = (high + low)//2
    elif hint in ('L','l'):
        low = guess
        guess = (high + low)//2
    elif hint in ('C','c'):
        secret_number = guess
    else:
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was:", secret_number)