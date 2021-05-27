#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Tue/May25/2021
# This program is a calculator for the area of a triangle


def calculate_area(length, height):
    # this function calculates the area of the triangle
    HALF = 0.5
    # process & output

    # process
    area_of_triangle = (length*height)*HALF
    # output
    print("\nThe area of the triangle is {0} cm²".format(area_of_triangle))



def main():
    # this function gets length and width

    # input
    length_from_user = input("Enter the base length of a triangle (cm): ")
    height_from_user = input("Enter the height of a triangle (cm): ")
    try:
        length = int(length_from_user)
        height = int(height_from_user)

        # call functions
        calculate_area(length, height)
    except Exception:
      print("\nInvalid Input!")
    finally:
      print("\nDone.")


if __name__ == "__main__":
    main()
