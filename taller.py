# Sistema de registro de estudiantes

# Lista para almacenar los estudiantes
estudiantes = []

# Bucle para registrar 5 estudiantes
for i in range(5):
    print(f"\nRegistro del estudiante {i+1}:")

    # Pedir nombre
    nombre = input("Ingrese el nombre del estudiante: ")

    # Pedir y validar edad
    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante (5-100): "))
            if 5 <= edad <= 100:
                break
            else:
                print("Edad inválida. Debe estar entre 5 y 100.")
        except ValueError:
            print("Por favor, ingrese un número entero para la edad.")

    # Pedir y validar calificación
    while True:
        try:
            calificacion = float(input("Ingrese la calificación del estudiante (0-5): "))
            if 0 <= calificacion <= 5:
                break
            else:
                print("Calificación inválida. Debe estar entre 0 y 5.")
        except ValueError:
            print("Por favor, ingrese un número decimal para la calificación.")

    # Agregar estudiante a la lista
    estudiantes.append({
        'nombre': nombre,
        'edad': edad,
        'calificacion': calificacion
    })

# Calcular calificación más alta, más baja y promedio
if estudiantes:
    max_calif = max(estudiantes, key=lambda x: x['calificacion'])
    min_calif = min(estudiantes, key=lambda x: x['calificacion'])
    promedio = sum(e['calificacion'] for e in estudiantes) / len(estudiantes)

    # Mostrar resultados
    print("\nResultados:")
    print(f"Estudiante con la calificación más alta: {max_calif['nombre']} con {max_calif['calificacion']}")
    print(f"Estudiante con la calificación más baja: {min_calif['nombre']} con {min_calif['calificacion']}")
    print(f"Calificación promedio: {promedio:.2f}")
else:git