empleados = []

SALARIO_MINIMO = 1300000
AUXILIO_TRANSPORTE = 160000
TOPE_AUXILIO = SALARIO_MINIMO * 2
DESCUENTO = 0.08

def registrar_empleado():
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

        empleado = {
            "nombre": nombre,
            "salario_base": salario,
            "dias_trabajados": dias
        }

        empleados.append(empleado)
        print("✅ Empleado registrado con éxito\n")


def calcular_nomina():
    print("\n--- CÁLCULO DE NÓMINA ---")

    if len(empleados) == 0:
        print("⚠️ No hay empleados registrados\n")
        return

    for emp in empleados:
        salario_proporcional = (emp["salario_base"] / 30) * emp["dias_trabajados"]

        auxilio = 0
        if emp["salario_base"] < TOPE_AUXILIO:
            auxilio = AUXILIO_TRANSPORTE

        descuento = salario_proporcional * DESCUENTO
        total_pagar = salario_proporcional + auxilio - descuento

        print("\nEmpleado:", emp["nombre"])
        print("Salario base:", emp["salario_base"])
        print("Días trabajados:", emp["dias_trabajados"])
        print("Salario proporcional:", salario_proporcional)
        print("Auxilio transporte:", auxilio)
        print("Descuento (8%):", descuento)
        print("💰 Total a pagar:", total_pagar)


def menu():
    while True:
        print("\n=== SISTEMA DE NÓMINA ===")
        print("1. Registrar empleado")
        print("2. Calcular nómina")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_empleado()
        elif opcion == "2":
            calcular_nomina()
        elif opcion == "3":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida")


# Ejecutar programa
menu()
    