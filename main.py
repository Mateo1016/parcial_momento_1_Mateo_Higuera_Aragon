empleados = []

while True:
    print("\n=== SISTEMA DE NÓMINA ===")
    print("1. Registrar empleado")
    print("2. Calcular nómina")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n--- REGISTRAR EMPLEADO ---")
        nombre = input("Ingrese el nombre: ")
        salario = float(input("Ingrese el salario base: "))
        dias = int(input("Ingrese los días trabajados: "))