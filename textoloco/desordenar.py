# desordenar.py
import random
def desordenar_palabra(alfabeticos, inicio, fin):
    alfabeticos_a_desordenar = alfabeticos[inicio + 1 : fin - 1]
    random.shuffle(alfabeticos_a_desordenar)
    alfabeticos[inicio + 1 : fin - 1] = alfabeticos_a_desordenar