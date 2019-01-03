
apetece_helado_input = input("¿Te apetece un helado? (Si / No): ").upper()

if apetece_helado_input == "Si":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("Te he dicho que me digas si o no, no se que has dicho pero cuento como que no")
    apetece_helado = False

tiene_dinero_input = input("¿tienes dinero para un helado? (Si / No): ").upper()
esta_tu_tia_input = input("¿Estás con tu tía? (Si / No): ").upper()


apetece_helado = apetece_helado_input == "SI"
puede_permitirselo = tiene_dinero_input == "SI" or esta_tu_tia_input == "SI"


if apetece_helado and puede_permitirselo:
    print("Pues comete un helado")
else:
    print("Pues nada")