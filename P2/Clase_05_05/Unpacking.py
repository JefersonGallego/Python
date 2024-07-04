controllers = ('P','PI','PID','PD')
print(type(controllers))
print(controllers)

(control1, control2,control3, control4) =controllers        # Asigne datos a las variables
control1, control2, *controles_restantes =controllers       # Asigne datos, y Almazene los restantes en  un lista
control1, *controles_restantes, control2 =controllers       # Asige el primer y untimo dato a las variables y Almazene los restantes en  un lista
control1, _,control2,_ = controllers                        # Asige el primer y Tercer dato a las variables
control1, *_, control2 = controllers                         # Asige el primer y untimo dato a las variables

print(control1)
print(control2)
print(controles_restantes)
