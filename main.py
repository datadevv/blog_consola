from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_posts

def main():
    while True:
        opcion = mostrar_menu()

        if opcion is None:
            continue

        if opcion == 1:
            listar_posts(posts)

        elif opcion == 2:
            termino = input("Ingrese el término de búsqueda: ").strip()
            buscar_por_titulo(posts, termino)

        elif opcion == 3:
            tag = input("Ingrese el tag a buscar: ").strip()
            filtrar_por_tag(posts, tag)

        elif opcion == 4:
            validar_posts(posts)

        elif opcion == 5:
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()