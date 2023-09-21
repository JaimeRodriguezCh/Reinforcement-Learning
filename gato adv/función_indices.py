class f_ind():
    def parse_input(input_str):
        try:
            row, col = map(int, input_str.split(','))
            return (row, col)
        except ValueError:
            print("Error: Entrada inválida. Ingrese dos números separados por coma.")
            return None
'''
input_str = input("Ingrese las coordenadas (fila,columna): ")
coordinates = parse_input(input_str)

if coordinates is not None:
    print("Tupla de coordenadas:", coordinates)'''