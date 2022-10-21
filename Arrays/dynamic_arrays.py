'''
    Vitor Gomes Ramos(vitorgomesramos@gmail.com)
    https://github.com/Sputn1kz/PythonDataStructuresAlgorithmsCourse
'''
# Dynamic arrays: Don't need to specify array size.
# Lists in python are dynamic.

import ctypes

class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
        
    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if(not (0 <= k < self.n)):
            return IndexError('Index is out of bounds.')
        return self.A[k]
    
    def append(self, element):
        if(self.n == self.capacity):
            self._resize(2*self.capacity)
            
        self.A [self.n] = element
        self.n += 1
    
    def _resize(self, new_capacity):
        B = self.make_array(new_capacity)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = new_capacity
    
    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()
    
def main():
    arr = DynamicArray()
    arr.append(1)
    print(len(arr))#Should be 1
    arr.append(2)
    print(len(arr))#Should be 2
    arr.append(3)
    print(len(arr))#Should be 3
    arr.append(4)
    print(len(arr))#Should be 4
    for ind in range(len(arr)):
        print(arr[ind])#Print all the elements of the dynamic array
    
    

if __name__ == "__main__":
    main()