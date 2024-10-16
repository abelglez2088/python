"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, 
el descuento que se le hace por no ser fresca y el coste final total."""

## Variables 

costoPan=3.49
VentaPan=0
ganancia=0
descuento=0
VentaGral=0


VentaPan=int(input("elige el número de panes viejos vendidos"))

VentaGral=costoPan*VentaPan
descuento=VentaGral*.60
ganancia=VentaGral-descuento

print("################## venta de pan Frio######################")
print(f"la venta Total de panes fue: {VentaPan}")
print(f"Tu descuento total fue: {descuento}")
print(f"venta general $: {ganancia}")
