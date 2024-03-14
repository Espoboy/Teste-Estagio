'''Você está em uma sala com três interruptores, cada um conectado a uma lâmpada
em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode 
ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir 
qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma 
das salas das lâmpadas, qual interruptor controla cada lâmpada?'''

from emoji import emojize

l = emojize(':light_bulb:')
s = emojize(':stop_button:')

print(f'''                ===========================
                =                         =
    =============      {s}    {s}    {s}        ===================
    =    {l}     =                         =                 =
    =           =            o            =                 =
    =============           /|\           =         {l}      =
                =           / \           =                 =
                =                         ===================
                ===========================
                        =           =
                        =     {l}    =
                        =           =
                        =============''')

'''Partindo do pressuposto de que eu poderia ir em duas salas diferentes:

Primeira visita às salas:

Ligaria o interruptor 1 e deixaria ligado por alguns minutos.
Desligaria o interruptor 1 e ligaria o interruptor 2.
Entraria na primeira sala.

Se a lâmpada estiver acesa, sabemos que o interruptor 2 controla essa lâmpada.
Se a lâmpada estiver apagada, tocaria na lâmpada para sentir se está quente ou fria.
Se estiver quente, sabemos que o interruptor 1 controla essa lâmpada.
Se estiver fria, sabemos que o interruptor 3 controla essa lâmpada.


Ligaria apenas um interruptor que não tenha sido ligado na primeira vez e entraria na sala do meio.

Se a lâmpada estiver acesa, sabemos que o interruptor 2 controla essa lâmpada.
Se a lâmpada estiver apagada, tocaria na lâmpada para sentir se está quente ou fria.
Se estiver quente, sabemos que o interruptor 1 controla essa lâmpada.
Se estiver fria, sabemos que o interruptor 3 controla essa lâmpada.'''