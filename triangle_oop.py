import math as m

# Get coordinates

a = [0, 0]
b = [0, 3]
c = [4, 0]

# Get sides lengths 

ab = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5
bc = ((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2) ** 0.5
ac = ((c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2) ** 0.5

class Triangle:

    def __init__(self, a, b, c, ab, bc, ac):
        self.a = a
        self.b = b
        self.c = c

        self.ab = ab
        self.bc = bc
        self.ac = ac

        self.sides = sorted([self.ab, self.bc, self.ac])

    def coordinate_check(self):
        if self.a[0] != self.b[0] and self.a[1] != self.b[1]:
            return (self.c[0] - self.a[0])/(self.b[0] - self.a[0]) != (self.c[1] - self.a[1])/(self.b[1] - self.a[1])
        elif self.a == self.b or self.a[0] == self.b[0] == self.c[0] or self.a[1] == self.b[1] == self.c[1]:
            return False
        else:
            return True

    def get_side(self, side_name):
        if side_name.lower() == 'ab':
            return self.ab
        elif side_name.lower() == 'bc':
            return self.bc
        elif side_name.lower() == 'ac':
            return self.ac
        elif side_name.lower() == 'all':
            return self.ab, self.bc, self.ac 
        else:
            return 'Wrong value'

    def border_length(self):
        return sum(self.sides)

    def square(self):
        half_border_length = self.border_length() / 2

        return (half_border_length * (half_border_length - self.ab) * (half_border_length - self.bc) * (half_border_length - self.ac)) ** 0.5

    def around_radius(self):
        return (self.ab * self.bc * self.ac) / (4 * self.square())

    def inside_radius(self):
        return (2 * self.square()) / (self.ab + self.bc + self.ac)


    def angle(self):
        cos_cab = (self.ab ** 2 + self.ac ** 2 - self.bc ** 2) / (2 * self.ab * self.ac)
        cos_abc = (self.ab ** 2 + self.bc ** 2 - self.ac ** 2) / (2 * self.ab * self.bc)
        cos_bca = (self.bc ** 2 + self.ac ** 2 - self.ab ** 2) / (2 * self.bc * self.ac)

        return 'Угол А = ' + str((m.acos(cos_cab) * 180) / m.pi) + '\nУгол B = ' + str((m.acos(cos_abc) * 180) / m.pi) + '\nУгол C = ' + str((m.acos(cos_bca) * 180) / m.pi)

    def scale(self, scale_percent, action):
        if action == 'up':
            self.ab += (self.ab * scale_percent) / 100
            self.bc += (self.bc * scale_percent) / 100
            self.ac += (self.ac * scale_percent) / 100

        elif action == 'down':
            self.ab -= (self.ab * scale_percent) / 100
            self.bc -= (self.bc * scale_percent) / 100
            self.ac -= (self.ac * scale_percent) / 100

        return self.ab, self.bc, self.ac

class RectangularTriangle(Triangle):

    def __init__(self):
        super().__init__(a, b, c, ab, bc, ac)

    def check_rectangular(self):
        if super().coordinate_check():
            if self.sides[2] ** 2 == (self.sides[0] ** 2 + self.sides[1] ** 2):
                return True
            else:
                return False
        else:
            return False

    def border_length(self):
        return super().border_length()

    def around_radius(self):
        return max(self.sides) / 2

    def inside_radius(self):
        return (self.sides[0] + self.sides[0] - max(self.sides)) / 2

    def angle(self):
        if self.bc == max(self.sides):
            a_angle = 90
            b_angle = ((m.atan(self.ac / self.ab) * 180) / m.pi)
            c_angle = 180 - a_angle - b_angle

            return 'Угол А: ' + str(a_angle) + '\nУгол B: ' + str(b_angle) + '\nУгол C: ' + str(c_angle)

        elif self.ac == max(self.sides):
            b_angle = 90
            c_angle = ((m.atan(self.ab / self.bc)) / m.pi)
            a_angle = 180 - b_angle - c_angle

            return 'Угол А: ' + str(a_angle) + '\nУгол B: ' + str(b_angle) + '\nУгол C: ' + str(c_angle)
        else:
            c_angle = 90
            a_angle = ((m.atan(self.bc / self.ac)) / m.pi)
            b_angle = 180 - c_angle - a_angle

            return 'Угол А: ' + str(a_angle) + '\nУгол B: ' + str(b_angle) + '\nУгол C: ' + str(c_angle)

    def square(self):
        return (self.sides[0] * self.sides[1]) / 2
    
    def scale(self, scale_percent, action):
        return super().scale(scale_percent, action)
    

if __name__ == '__main__':
    triangle = Triangle(a, b, c, ab, bc, ac)
    rectangular_triangle = RectangularTriangle()

    # Checking if these coordinates make a triangle and do operations: 

    if triangle.coordinate_check():
        print('Usual triangle')

        print(triangle.get_side('all'))
        print(triangle.border_length())
        print(triangle.around_radius())
        print(triangle.inside_radius())
        print(triangle.angle())
        print(triangle.square())
        print(triangle.scale(50, 'up'))

        print('Rectangular triangle')

        if rectangular_triangle.check_rectangular():
            print(rectangular_triangle.check_rectangular())
            print(rectangular_triangle.border_length())
            print(rectangular_triangle.around_radius())
            print(rectangular_triangle.inside_radius())
            print(rectangular_triangle.angle())
            print(rectangular_triangle.square())
            print(rectangular_triangle.scale(50, 'up'))

    else:

        print("These coordinates can't be triangle")
