'''
    Vitor Gomes Ramos(vitorgomesramos@gmail.com)
    https://github.com/Sputn1kz/PythonDataStructuresAlgorithmsCourse
'''
# Access to an array element with his index: start array address + (cell size) & (desired cell index) 
ExampleList = [1, 2, 3] # List in python
ExampleTuple = (1, 2, 3) # Tuple in python
ExampleString = "123" # String is also an array

print("[*] Priting an list:", ExampleList)
print("[*] Priting an tuple:", ExampleTuple)
print("[*] Priting an string:", ExampleString)

prime_numbers = [1, 3, 5, 7, 11]
temporary_list = prime_numbers[1:3] # Make a copy from the original prime_numbers array from the index 1 to the index 3.
print("[*] Priting a temporary array:", temporary_list)
temporary_list[0] = 6 # Change the temporary_list reference of the element in index 0 but doesn't change the reference of the original array which is prime_numbers
print("[*] Priting temporary array after change:", temporary_list)
print("[*] Priting prime numbers array after change:", prime_numbers)
counters = [0] * 5 # Same reference for all 5 objects in the array

counters.extend([1] * 5) # Receives the objects references
print("[*] Priting counters with new objects references:", counters)