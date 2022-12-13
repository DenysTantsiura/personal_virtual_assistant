""" 
-описати абстрактний базовий клас для представлень користувача і конкретні реалізації, які наслідують базовий клас і
реалізують консольний інтерфейс.
"""
# import sys
from typing import NoReturn

from system.pva import PVA


def main() -> NoReturn:
    pva_start = PVA()
    pva_start.start()


if __name__ == '__main__':
    main()
 