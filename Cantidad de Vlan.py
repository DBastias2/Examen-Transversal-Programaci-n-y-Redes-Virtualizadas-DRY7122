vlan_normal=range(1, 1005)
vlan_extendida=range(1006, 4094)
numero_vlan=int(input("Ingresa el numero de vlan:  "))

if numero_vlan in vlan_normal:
    print("El numero de vlan", numero_vlan, "es de rango normal")
elif numero_vlan in vlan_extendida:
    print("El numero de vlan", numero_vlan, "es de rango extendida")
else:
    print("El numero ingresado", numero_vlan, "no pertenece a una normal o una extendida.")

    