#!/usr/bin/python3
""" Class square """


class Square():
    """ Contain the definition of a class Square"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
            Constructor that initialize the values

        Args:
            args (int): Variable length argument list.
            kwargs (int): Arbitrary keyword arguments.
        """
        for key, value in kwargs.items():
            if value <= 0:
                value *= -1
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.height * self.width

    def permiter_of_my_square(self):
        """ Perimeter of a square """
        return (self.height * 2) + (self.width * 2)

    def __str__(self):
        """
            Function that friendly
            with the user
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    # Defining class square
    # Print sring, area and perimeter
    s = Square(width=6, height=6)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
