class Tarea:
    def __init__(self, descripcion):
        """
        Inicializa una nueva tarea con una descripción y la marca como pendiente.
        """
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        """
        Marca la tarea como completada.
        """
        self.completada = True

    def __str__(self):
        """
        Devuelve una cadena que representa la tarea con su estado.
        """
        estado = "\033[92mCompletada\033[0m" if self.completada else "\033[91mPendiente\033[0m"
        return f"{self.descripcion} - {estado}"

class ListaDeTareas:
    def __init__(self):
        """
        Inicializa una lista vacía de tareas.
        """
        self.tareas = []

    def agregar_tarea(self, descripcion):
        """
        Agrega una nueva tarea a la lista de tareas pendientes.
        """
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)
        print(f"Tarea '{descripcion}' agregada.")

    def marcar_completada(self, indice):
        """
        Marca una tarea como completada dado su índice en la lista.
        """
        try:
            self.tareas[indice].marcar_completada()
            print(f"Tarea '{self.tareas[indice].descripcion}' marcada como completada.")
        except IndexError:
            print("Índice de tarea inválido. Por favor, intenta nuevamente.")

    def mostrar_tareas(self):
        """
        Muestra todas las tareas pendientes y completadas con su estado.
        """
        print("\033[96m\n=== Lista de Tareas Pendientes ===\033[0m")
        if not self.tareas:
            print("\033[93mNo hay tareas en la lista.\033[0m")
        else:
            for i, tarea in enumerate(self.tareas, start=1):
                print(f"{i}. {tarea}")

    def eliminar_tarea(self, indice):
        """
        Elimina una tarea de la lista dado su índice.
        """
        try:
            tarea = self.tareas.pop(indice)
            print(f"Tarea '{tarea.descripcion}' eliminada.")
        except IndexError:
            print("Índice de tarea inválido. Por favor, intenta nuevamente.")

def main():
    """
    Función principal que controla el flujo del programa.
    """
    lista_de_tareas = ListaDeTareas()
    print("=========================")
    print(" ==   Lista de Tareas  == ")
    print("=========================\n")

    while True:
        print("---------Opciones:--------\n")
        print("1. Agregar una nueva tarea")
        print("2. Marcar una tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar una tarea")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            descripcion = input("Descripción de la nueva tarea: ")
            lista_de_tareas.agregar_tarea(descripcion)
        elif opcion == "2":
            try:
                indice = int(input("Índice de la tarea a marcar como completada: ")) - 1
                lista_de_tareas.marcar_completada(indice)
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número entero.")
        elif opcion == "3":
            lista_de_tareas.mostrar_tareas()
        elif opcion == "4":
            try:
                indice = int(input("Índice de la tarea a eliminar: ")) - 1
                lista_de_tareas.eliminar_tarea(indice)
            except ValueError:
                print("\033[91mEntrada no válida. Por favor, introduce un número entero.\033[0m")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("\033[91mOpción inválida, por favor elige nuevamente.\033[0m")

if __name__ == "__main__":
    main()

