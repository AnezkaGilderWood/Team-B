# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 14:51:54 2022

@author: mattb
"""
import numpy as np
import sympy as sym
from findiff import FinDiff

"""
This is essentially combining the equations previously made into one dingle Schrodinger equation
"""
class Schrodinger:
    
    def derivative(psi):
        term_to_derive_by = input('enter the term in which you would like to derive by: ')
        x_1 = sym.Symbol(term_to_derive_by)
        first = sym.diff(psi)
        return first
    
    def derivative_2(psi):
        term_to_derive_by = input('enter the term in which you would like to derive by: ')
        x_2 = sym.Symbol(term_to_derive_by)
        first = sym.diff(psi)
        second = sym.diff(first)
        return second
        
        
    def potential(x):
        print (
            'For the potentials there are a few built in options: 1D_SHO, 0_potential, square_well, potential_step or you can choose to enter a custom potential')
        v_x_selected = input('enter potential V(x): ')
        if v_x_selected == '1D_SHO':
            k = int(input('What is your spring constant k: '))
            v_x = 0.5 * k * x * x
        elif v_x_selected == '0_potential':
            v_x = 0
        elif v_x_selected == 'square_well':
            a = int(input('enter the size of your well: '))
            if x <= a or x <= -1 * a:
                v_x = 0
            else:
                v_x = np.inf
        elif v_x_selected == 'potential_step':
            v_0 = input('enter the v(x) value at the potential step: ')
            b = input('enter x value in which the potential steps: ')
            if b < x:
                v_x = v_0
            else:
                v_x = 0
        else:
            v_x = input('enter your custom potential equation: ')
        return v_x
    
    def full_schrodinger(x,psi):
            '''    
            Parameters
            ----------
            x : Values of x that will go into the potential
                
            psi : Function
        
            Returns
            -------
            Should give back a value/form for the Schrodinger equation
        
            '''
            m_value = input('What value would uou like m to be?: ')
            h_bar = 1.05e-34
            x_min = input('enter the min x value:')
            x_max = input('enter the max x value:')
            x = np.linspace(x_min,x_max, 100)
            psi = psi(x)
            eq = (-1*((h_bar**2)/2*m_value)*(derivative_2(psi))) + potential(x)*psi = j*h_bar*derivative(psi)
            
            return eq
            #return -1 * (0.5 * 1/ m_value * derivative_2() + v_x())
        
        
            