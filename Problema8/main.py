import generador_numeros

def main():
    lista = generador_numeros.generar_numeros()
    generador_numeros.mostrar_lista(lista)
    generador_numeros.ordenar_lista(lista)

if __name__ == "__main__":
    main()