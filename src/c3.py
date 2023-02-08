# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
# - Longitud: Entre 8 y 16.
# - Con o sin letras mayúsculas.
# - Con o sin números.
# - Con o sin símbolos.
# (Pudiendo combinar todos estos parámetros entre ellos)
import random
import string


def generate_password(p_length: int, with_upper: bool, with_number: bool, with_symbol: bool) -> str:
    password_pool = [
        string.ascii_lowercase
    ]
    if with_upper:
        password_pool.append(string.ascii_lowercase)
    if with_number:
        password_pool.append(string.digits)
    if with_symbol:
        password_pool.append(string.punctuation)

    password_text = ""
    for i in range(p_length):
        password_text += random.choice(random.choice(password_pool))

    return password_text


def main() -> None:
    print(generate_password(p_length=8, with_upper=True, with_number=True, with_symbol=True))
    print(generate_password(p_length=10, with_upper=True, with_number=True, with_symbol=False))
    print(generate_password(p_length=12, with_upper=True, with_number=False, with_symbol=True))
    print(generate_password(p_length=14, with_upper=False, with_number=False, with_symbol=False))


if __name__ == '__main__':
    main()
