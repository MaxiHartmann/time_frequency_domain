import numpy as np
import math

# Recursive function to return gcd
# of a and b
def gcd(a,b):
    if (a < b):
        return gcd(b, a)
     
    # base case
    if (abs(b) < 0.001):
        # if tolerance is increased -> higher harmonics will be detected
        # BUT: 
        #     higher base frequencies can be diminished, because of very high
        #     harmonics of low base frequencies
        return a
    else:
        return (gcd(b, a - math.floor(a / b) * b))

def numbers_are_related(a, b):
    bool_related = True

    if gcd(a,b) == min(a,b): 
        bool_related = 1
    else: 
        bool_related = 0

    return bool_related

def find_base_freqs(freqs):
    """
        docstring: TODO
    """

    freqs.sort()

    dim = len(freqs)
    matrix = np.zeros((dim, dim))

    for row in range(dim):
        for col in range(dim):
            # if 2 freqs are related, entry will be set to 1
            matrix[row, col] = numbers_are_related(freqs[row], freqs[col])

    upper_triangle_matrix = np.triu(matrix, 0)
    # print(upper_triangle_matrix)

    # freq is basefrequency when sum of column is 1 and freq is unique
    sum_columns = upper_triangle_matrix.sum(axis=0)

    base_freqs = []
    for i, col in enumerate(sum_columns):
        if col == 1:
            base_freqs.append(freqs[i])

    # counter = len(base_freqs)

    base_freqs_dict = {}

    ## Frequency and which harmonics ...
    for bf in base_freqs:
        list_of_harmonics = []
        row = freqs.index(bf)
        indices = matrix[row,:]
        for j, i in enumerate(indices):
            if i==1:
                list_of_harmonics.append(int(freqs[j]/bf))

        base_freqs_dict[bf] = list_of_harmonics
        # counter += len(list_of_harmonics)

    # print("### Check ###")
    # print(f"Number of input frequencies:  {dim}")
    # print(f"Number of output frequencies: {counter}")

    return base_freqs_dict

def print_pretty(input_dict):
    print(" Fundamental Frequency   Harmonics")
    for key, value in input_dict.items():
        print(f" {key:>21.4f}   {value}")

def main():
    freqs = [1.1, 78, 42398, 94, 22, 44, 66, 72, 11, 90, 180, 270, 270, 270, 10666.66667, 2, 2.2, 4, 4.5, 6, 2.2*4.5, 8, 9, 15, 16, 30, 32, 5333.3333, 16000, 16001]
    base_freqs = find_base_freqs(freqs)
    print_pretty(base_freqs)

    freqs = [4, 8, 12, 16.01, 16]
    base_freqs = find_base_freqs(freqs)
    print(freqs)
    print_pretty(base_freqs)

if __name__ == "__main__":
    main()
