# formulas
# criado por: julio
from time import sleep
import sympy
from sympy.abc import x

#  menu prin
#------------------------------------------------------------------------------------------------------------------------------#
sleep(0.3)
print('\n\033[1;31m{: ^100}\033[m\n'.format('FORMULAS'))
sleep(0.3)
print('{: ^100}\n'.format('escolha sua formula:'))
print('{: ^135}'.format('\033[34mq\033[muadrado   \033[31mt\033[mriangulo   t\033[32mr\033[mapezio  \033[35ml\033[mozango  r\033[33me\033[mtangulo'))
esc = str(input('\033[36m: \033[m'))
#------------------------------------------------------------------------------------------------------------------------------#

#  triangulo
#-----------------------------------------------------------------------------------------------------------------------#
if esc == 't':    
    sleep(0.6)    
    print('{: ^135}'.format('\033[31me\033[mquacao \033[31mr\033[metas \033[31mp\033[masso a passo \033[31ma\033[mrea'))
    est = str(input(': '))

    if est == 'a':
        sleep(0.5)
        bas = float(input('digite o valor da base: '))
        sleep(0.3)
        alt = float(input('digite o valor da altura: '))    
        print('a area desse triangulo e de: \033[1;31m{:.2f}'.format(bas*alt/2))    
        print()
        sleep(0.4)
        esc = str(input(': '))
        
    
    if est == 'p':
        sleep(0.5)
        print('a formula da area do triangulo e de: A = b x h : 2 aonde b e a base e h e altura')
        sleep(3)
        print('entao transformando isso em conta ficaria: {}x{}:2'.format(bas,alt))
        sleep(3)
        print('depois: {}:2'.format(bas*alt))
        sleep(3)
        print('e para finalizar: {}'.format(bas*alt/2))  
        sleep(0.4)
        esc = str(input(': '))      
    
    if est == 'r':
        sleep(0.5)
        re1 = float(input('digite o valor da primeira reta: '))
        re2 = float(input('digite o valor da segunda reta: '))
        re3 = float(input('digite o valor da terceira reta: '))
        
        if re1 + re2 > re3:
            print('pode formar um triangulo')
        else: 
            print('nao pode formar um triangulo') 
        sleep(0.4)
        esc = str(input(': '))   
    
    if est == 'e':
        sleep(0.5)
        bae = float(input('digite o valor da altura ou base: '))
        fin = float(input('digite o valor do resultado final: '))
        
        eq = sympy.Eq(fin,bae*x/2 )
        print(sympy.solve(eq))
        sleep(0.4)
        esc = str(input(': '))
#----------------------------------------------------------------------------------------------------------------------#

#  quadrado
#-------------------------------------------------------------------------------------------------#
if esc == 'q':
    sleep(0.6)
    print('{: ^135}'.format('\033[34mr\033[metas \033[34ma\033[mreas \033[34mp\033[masso a passo'))
    esq = str(input(': '))
    
    if esq == 'a':
        sleep(0.5)
        la1 = float(input('digite o valor do primeiro lado: '))        
        
        print('a area desse quadrado e de: {}'.format(la1**2))
        sleep(0.4)
        esc = str(input(': '))
    
    if esq == 'p':
        sleep(0.5)
        print('e so elevar ao quadrado como: {}**2'.format(la1))
        sleep(3)
        print('que da: {}'.format(la1**2))
        sleep(0.4)
        esc = str(input(': '))
    
    if esq == 'r':
        sleep(0.5)
        rc1 = float(input('digite o valor da primeira reta de cima: '))
        rc2 = float(input('digite o valor da segunda reta de cima: '))
        rb1 = float(input('digite o valor da primeira reta de baixo: '))
        rb2 = float(input('digite o valor da segunda reta de baixo: '))

        if (rc1-rc2) == (rb1-rb2):
            print('pode formar um quadrado')
        else:
            print('nao pode formar um quadrado')
        sleep(0.4)
        esc = str(input(': '))
#-------------------------------------------------------------------------------------------------#

#  trapezio
#-----------------------------------------------------------------------------------------------#
if esc == 'r':
    sleep(0.6)

    print('{: ^135}'.format('area passo a passo equacao'))
    esr = str(input(': '))

    if esr == 'a':
        sleep(0.5)
        bme = float(input('digite o valor da base menor: '))
        bma = float(input('digite o valor da base maior: '))
        alr = float(input('digite o valor da altura: '))

        print('a area desse trapezio e: {}'.format((bme+bma)*alr/2))
        esr = str(input(': '))
        sleep(0.4)
        esc = str(input(': '))
    
    if esr == 'p':
        sleep(0.5)
        print('a formula para saber a area do trapezio e base maior + base menor x altura : 2')
        sleep(4)
        print('transformando na conta fica: {}+{}x{}:2'.format(bma,bme,alr))
        sleep(3)
        print('entao: {}x{}:2'.format(bma+bme,alr))
        sleep(3)
        print('e: {}:2'.format((bma+bme)*alr))
        sleep(3)
        print('por fim: {}'.format((bma+bme)*alr/2))
        sleep(0.4)
        esc = str(input(': '))
        

    if esr == 'e':          
        bme = float(input('digite o valor da base menor: '))
        ale = float(input('digite o valor da altura: '))
        fme = float(input('digite o valor final: '))

        eeq = sympy.Eq(fme,(bme+x)*ale/2)
        print(sympy.solve(eeq))
        sleep(0.4)
        esc = str(input(': '))
#----------------------------------------------------------------------------------------------#

#  retangulo
#------------------------------------------------------------#
if esc == 'e':
    sleep(0.6)
    alre = float(input('digite o valor da altura: '))
    bare = float(input('digite o valor da base: '))
    print('a area desse retangulo e de: {}'.format(alre*bare))
    sleep(0.4)
    esc = str(input(': '))
#------------------------------------------------------------#

#  losango
#-------------------------------------------------------------------------------------------#
if esc == 'l':
    sleep(0.6)
    print('{}'.format('area equacao passo a passo'))
    esl = str(input(': '))

    if esl == 'a':
        dma = float(input('digite o valor da diagonal maior: '))
        dme = float(input('digite o valor da diagonal menor: '))

        print('a area desse lozango e de: {}'.format(dma*dme/2))
        sleep(0.4)
        esc = str(input(': '))

    if esl == 'p':
        sleep(0.6)
        print('a formula para a area do lozango e de: diagonal maior x diagonal menor : 2')
        sleep(3)
        print('transformando isso em conta fica: {}x{}:2'.format(dma,dme))
        sleep(3)
        print('e entao: {}:2'.format(dma*dme))
        sleep(0.4)
        esc = str(input(': '))

    if esl == 'e':
        dia = float(input('digite o valor da diagonal menor/maior: '))
        fil = float(input('digite o valor do resultado da conta: '))
        
        eql = sympy.Eq(fil,dia*x/2)
        print(sympy.solve(eql))
        sleep(0.4)
        esc = str(input(': '))
#-------------------------------------------------------------------------------------------#
            