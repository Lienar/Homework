import random
import sys
import webcolors
import math

color_list = []
this_color = [1, 1, 1]
k = 0




class Figure:

    def __init__(self, sides_count):
        self.sides_count = sides_count
        self.current_color = []
        self.valide_color = False
        self.valide_sides_count = False
        self.__sides = []
        self.__colors = [255, 255, 255]
        #self.sides_equal_cheak_need = False

    def get_color(self):
        for i in range(0, 256):
            for j in range(0, 256):
                for x in range(0, 256):
                    try:
                        this_color = webcolors.rgb_to_hex([i, j, x])
                        color_list.append(webcolors.hex_to_name(this_color))
                    except:
                        return

    def set_color(self):

        #self.valide_color = False

        while self.valide_color == False:
            try:
                print()
                r = int(input('введите степень красного (0; 255): '))

            except:
                r = 1000
                print('введите не корректное значение красного (0; 255): ')

            try:
                print()
                g = int(input('введите степень зеленого (0; 255): '))

            except:
                g = 1000
                print('введите не корректное значение зеленого (0; 255): ')

            try:
                print()
                b = int(input('введите степень синего (0; 255): '))

            except:
                b = 1000
                print('введите не корректное значение синего (0; 255): ')

            current_color = [r, b, g]

            self.__is_valid_color(current_color)

            if self.valide_color == True:
                self.__colors = current_color
                print('Ваш цвет корректен')
            else:
                print('Параметры цвета не верны')





    def __is_valid_color(self, current_color):

        valide_color_rgb = []
        valide_color_rgb.clear()

        for i in range(len(current_color)):
            if current_color[i] > 0 and current_color[i] < 255:
                valide_color_rgb.append(True)

        if valide_color_rgb[0] == True and valide_color_rgb[1] == True and valide_color_rgb[2] == True:
            self.valide_color = True

    def set_sides(self, sides):
        sides = []
        side_end = ' '
        side_number = 1

        while side_end != 'end':
            try:
                side_end = input('Введите длину стороны ', side_number, ': ' )
                sides.append(int(side_end))
                side_number += 1
            except:
                if len(sides) > 0:
                    side_end = 'end'


        self.__is_valid_sides(sides)

        if self.valide_sides_count == True:
            self.__sides = sides
            print (sides)
            print('Данные по кол-ву сторон верные')
            return (sides)
        else:
            print('Параметры сторон не верны')

    def __is_valid_sides(self, sides_count_in):
        if self.sides_count == len(sides_count_in):
            self.valide_sides_count = True
        #if sides_equal_cheak_need == True:
        #    for i in range (1,len(sides_count_in)):
        #        if (self.__sides[i]) != (self.__sides[i-1]):
        #            self.valide_sides_count = False
        #            i = len(sides_count_in) + 1


    def __len__ (self):
        P = 0
        for i in range(len(self.__sides)):
            P += self.__sides[i]
        #print ('Периметр = ', P)
        return (P)

class Circle(Figure):
    __radius = 0
    __sides = 0
    S = 0

    def __init__(self, sides_count,):
        super().__init__(sides_count=sides_count)
        self.__sides = self.set_sides(self.__sides)[0]
        self.__radius = self.__sides/(2*3.14)
        self.S = 0


    def get_square(self):
        self.S = 3.14*self.__radius*self.__radius

    def print_in(self):
        print (self.S)
        print (self.__len__())


class Triangle(Figure):
    __height = []
    __sides = []
    P = 0
    S = 0


    def __init__(self, sides_count):
        hp = 0
        super().__init__(sides_count=sides_count)
        self.__sides = self.set_sides(self.__sides)
        self.P += (self.__len__())/2
        self.S = 0

        hp = 2*math.sqrt(self.P*(self.P - self.__sides[0])*(self.P - self.__sides[1])*(self.P - self.__sides[2]))

        for i in range(3):
            self.__height.append(hp/self.__sides[i])

    def print_in(self):
        print (self.__height)
        print (self.S)
        print (self.__len__())

    def get_square(self):
        self.S = math.sqrt(self.P*(self.P - self.__sides[0])*(self.P - self.__sides[1])*(self.P - self.__sides[2]))


class Cube(Figure):
    __sides = []
    V = 0
    sides_equal_cheak_need = True

    def __init__(self, sides_count):
        super().__init__(sides_count = sides_count)
        print (self.sides_count)
        self.__sides = self.set_sides(self.__sides)
        self.V = 0
        self.sides_equal_cheak_need = True

    def set_sides(self, sides):
        sides = []
        side_end = ' '

        while side_end != 'end':
            try:
                side_end = input('Введите длину стороны: ' )
                for i in range(0, 12):
                    sides.append(int(side_end))
                print (sides)
                side_end = 'end'

            except:
                if len(sides) > 0:
                    side_end = 'end'
        print (len(sides))
        self.__is_valid_sides(sides, self.sides_equal_cheak_need)

        if self.valide_sides_count == True:
            self.__sides = sides
            print('Данные по кол-ву сторон верные')
            return (sides)
        else:
            print('Параметры сторон не верны')

    def __is_valid_sides(self, sides_count_in, sides_equal_cheak_need):
        if self.sides_count == len(sides_count_in):
            self.valide_sides_count = True
        if sides_equal_cheak_need == True:
            for i in range (1,len(sides_count_in)):
                if (sides_count_in[i]) != (sides_count_in[i-1]):
                    self.valide_sides_count = False
                    i = len(sides_count_in) + 1

    def get_volume(self):
        self.V = self.__sides[0]*self.__sides[0]*self.__sides[0]

    def print_in(self):
        print (self.V)
        print (self.__len__())

Forms = Cube(sides_count = 12)
Forms.get_volume()
Forms.print_in()