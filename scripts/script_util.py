# Script útil - Conversión de grados Celsius a Fahrenheit

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Ejemplo de uso
if __name__ == "__main__":
    c = 25
    f = celsius_a_fahrenheit(c)
    print(f"{c}°C equivalen a {f}°F")
