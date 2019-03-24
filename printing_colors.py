# -*- coding: utf-8 -*-

from colors import green, red, reset

def main():
    print(green + 'ça s\'affiche bien en vert' + reset)
    print(red + 'En rouge aussi !' + reset)
    print('ah ben ouais ça change tout !!')


if __name__ == '__main__':
    main()
