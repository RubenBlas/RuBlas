"""
Oriol Barba Vázquez
   10/01/2023
   ASIXc M03 UF1 A5

Aleatòriament, el programa ha de triar un dels correus de l'alumnat de classe.
 Que prèviament estaran emmagatzemats "hard code".
"""
import random
LISTACORREOS = ("juan.acosta.7e6@itb.cat","mauro.arena.7e6@itb.cat","onur.aynali.7e6@itb.cat","oriol.barba.7e6@itb.cat",
                "ruben.blas.7e6@itb.cat","juan.canyas.7e6@itb.cat","gerard.cano.7e6@itb.cat","juan.carretero.7e6@itb.cat",
                "claudia.catot.7e6@itb.cat","samir.channagui.7e6@itb.cat","gerardo.chavarry.7e6@itb.cat",
                "pablo.chmyr.7e6@itb.cat","younes.derraz.7e6@itb.cat","soulaimane.elharrak.7e6@itb.cat",
                "hector.escribano.7e6@itb.cat","joel.fernandez.7e6@itb.cat","mario.garcia.7e6@itb.cat",
                "jefrey.hernandez.7e6@itb.cat","kevin.herrera.7e6@itb.cat","denis.jimenez.7e6@itb.cat",
                "erin.lorenzo.7e6@itb.cat","david.martinez.7e6@itb.cat","isaac.menendez.7e6@itb.cat",
                "trishan.mizhquiri.7e6@itb.cat","victor.sempau.7e6@itb.cat","alfredo.sendra.7e3@itb.cat",
                "daniel.shapoval.7e6@itb.cat","bogdan.stefurak.7e6@itb.cat","enric.toll.7e6@itb.cat",
                "joan.villalba.7e6@itb.cat")
numeroAleatori = int(random.randint(0,len(LISTACORREOS)))
print(LISTACORREOS[numeroAleatori])