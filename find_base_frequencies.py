import numpy as np
import math

# Recursive function to return gcd
# of a and b
def gcd(a,b):
    if (a < b):
        return gcd(b, a)
     
    # base case
    if (abs(b) < 0.001):
        return a
    else:
        return (gcd(b, a - math.floor(a / b) * b))

def numbers_are_related(a, b):
    bool_related = True

    if gcd(a,b) == min(a,b): 
        bool_related = True
    else: 
        bool_related = False

    return bool_related

def main():
    freqs = [2, 2.2, 4, 4.5, 6, 2.2*4.5, 8, 9, 15, 16, 30, 32, 5333.3333, 16000, 16001]

    print("INPUT")
    print("Frequencies: {}".format(freqs))

    dim = len(freqs)
    matrix = np.zeros((dim, dim))

    for row in range(dim):
        for col in range(dim):
            matrix[row, col] = numbers_are_related(freqs[row], freqs[col])


    upper_triangle_matrix = np.triu(matrix, 0)
    print(upper_triangle_matrix)

    # freq is basefrequency when sum of column is 1 and freq is unique
    sum_columns = upper_triangle_matrix.sum(axis=0)


    base_freqs = []
    for i, col in enumerate(sum_columns):
        if col == 1:
            base_freqs.append(freqs[i])

    

    print(" Fundamental Frequency   Harmonics")
    ## Frequency and which harmonics ...
    for bf in base_freqs:
        list_of_harmonics = []
        row = freqs.index(bf)
        indices = matrix[row,:]
        # print(indices)
        for j, i in enumerate(indices):
            if i==1:
                list_of_harmonics.append(int(freqs[j]/bf))

        print(f"   {bf:>14.4f}        {list_of_harmonics}")

if __name__ == "__main__":
    main()
