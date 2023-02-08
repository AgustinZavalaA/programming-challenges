#
# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#

def fizzbuzz(n: int) -> None:
    for i in range(n):
        prompt = ""
        if i % 3 == 0:
            prompt += "fizz"
        if i % 5 == 0:
            prompt += "buzz"
        if prompt == "":
            prompt = i
        print(prompt)


def main():
    print('Hello World!')
    fizzbuzz(100)


if __name__ == '__main__':
    main()
