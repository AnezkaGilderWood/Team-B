# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:35:30 2022

@author: zjap015
"""

import numpy as np
class Schrodinger:
    
    def psi:
        """
        function to return a wave function
        this function has some built in formats for the wave function these include:
            1) ax + b
            2) ax**2 + bx + c
            3) acos(x) + ibsin(x)
            4) acos(x) + bsin(x)
            5) ax**b
        alternatively a custom function can be written as long as it follows python format using numpy where needed
        
        """
        
        print('In this function we have some pre-defined wavefunction formats available to use: ')
        print('1) ax + b /n * 2) ax**2 + bx + c /n * 3) acos(x) + ibsin(x) /n * 4) acos(x) + bsin(x) /n * 5) ax**b ')
              
        wf_yn = input('would you like to use one of our pre defined wave function formats: yes [y] or no [n] ')
        if wf_yn == 'y' or wf_yn == yes:
            wf= input ('number wave function format would you like to use: ')
            if wf == 1:
                a = int(input('enter a value: '))
                b = int(input('enter b value: '))
                psi = a*x + b
                
            elif wf == 2:
                a = int(input('enter a value: '))
                b = int(input('enter b value: '))
                c = int(input('enter c value: '))
                psi = a*x + b + c
                
            
            elif wf == 3:
                a = int(input('enter a value: '))
                b = int(input('enter b value: '))
                psi = a*np.cos(x) + j*b*np.sin(x)
            
            elif wf == 4:
                a = int(input('enter a value: '))
                b = int(input('enter b value: '))
                psi =a*np.cos(x) + b*np.sin(x)
                
            elif wf == 5:
                a = int(input('enter a value: '))
                b = int(input('enter b value: '))
                psi =a*x**b 
            
            else: 
                print ('error with selection enter wave function manually')
                psi = input('enter the custom wave function you would like: ')
        
        else:
            psi = input('enter the custom wave function you would like: ')
        
       return psi