"""
YAKISOBA RECEPTA
"""
#region 1_descomposició
def recopilar_informacio():
    print("Comprar al supermercat")
    print("Disposar-los sobre el marbre")
def cuinar_tallarines():
    preparar_aigua()
    print("Bullir Tallarines")
    print("Escorrer tallarines")
    print("Deixar-les preparades")
def cuinar_pastanagues():
    print("Tallar pastanaguea")
    fregir_pastanagues()
    print("Deixar pastanagues preparades")
def cuinar_cebes():
    print("Tallar cebes")
    fregir_cebes()
    print("Deixar cebes preparades")
def preparacio_final():
    print("Barrejar ingredients amb salsa yakitori")
    print("Deixar llest per servir")
#endregion

#region 2_descomposició
def saltar_ingredients():
    print("Preparar paella per saltar")
    print("Cuinar remenant ingredients")
def fregir_cebes():
    print("preparar paella per fregir")
    print("Rossejar cebes")
    print("Netejar oli de paella")
def preparar_aigua():
    print("Escalfar aigua")
    print("Posar-hi sal")
def fregir_pastanagues():
    print("Preparar paella per fregir")
    print("Rossejar pastanagues")
    print("Netejar oli de paella")
#endregion

recopilar_informacio()
cuinar_tallarines()
cuinar_pastanagues()
cuinar_cebes()
preparacio_final()
