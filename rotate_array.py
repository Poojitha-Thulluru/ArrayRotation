def get_rotated_array(num_array, rotation):
    rotations = rotation % len(num_array)
    if rotations == 0:
        return num_array
    return num_array[-rotations:] + num_array[:-rotations]


try:
    nums_array = list(map(int, input("Enter only Integers separated by space : ").split()))
    number_of_rotations = int(input("Enter number of rotations to be done : "))
    print("The Rotated array is : ", get_rotated_array(nums_array, number_of_rotations))
except ValueError:
    print("Invalid input. Enter Only Integers")