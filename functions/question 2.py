#program to reverse a string

def reverse_string(output):

    reverse_string = 'output'
    index = len(output)
    while index > 0:
        reverse_string += output[ index - 1 ]
        index = index - 1
    return reverse_string
print(reverse_string('1234abcd'))