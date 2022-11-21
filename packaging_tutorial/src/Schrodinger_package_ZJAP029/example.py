def run(psi):
    '''
    doc string
    '''
    line.set_data(x_array, np.abs(psi)**2)
    return line,

def play_func():
    '''
    Doc string
    '''
    subprocess.call(["cmd", "/c", "start", "/max", "particle_in_a_well.gif."])
    time.sleep(5)

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
        print ('For the potentials there are a few built in options: 1D_SHO, 0_potential, square_well, potential_step or you can choose to enter a custom potential')
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
    
     def psi(x):
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
        print(' y1) ax + b \n 2) ax**2 + bx + c \n 3) acos(x) + ibsin(x) \n 4) acos(x) + bsin(x) \n 5) ax**b ')
              
        wf_yn = input('would you like to use one of our pre defined wave function formats: yes [y] or no [n] ')
        if wf_yn == 'y' or wf_yn == yes:
            wf= int(input ('number wave function format would you like to use: '))
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
                psi = a*np.cos(x) + b*np.sin(x)
                
            elif wf == 5:
                a = int(input('enter a value: '))
                b = int(input('enter b value: '))
                psi = a*x**(b) 
            
            else: 
                print ('error with selection enter wave function manually')
                psi = input('enter the custom wave function you would like: ')
        
        else:
            psi = input('enter the custom wave function you would like: ')
        
        return psi

    
    def full_schrodinger(x):
            '''    
            function to solve shrodingers equation this function takes in the x defined by the user then uses this to calculate shrodingers equation
        
            '''
            m_value = input('What value would uou like m to be?: ')
            h_bar = 1.05e-34
            psi = psi(x)
            eq = (-1*((h_bar**2)/2*m_value)*(Schrodinger.derivative_2(psi))) + Schrodinger.potential(x)*psi = j*h_bar*Schrodinger.derivative(psi)
            
            return eq
