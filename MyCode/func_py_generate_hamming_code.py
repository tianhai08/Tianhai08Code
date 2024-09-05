# func_py_generate_hamming_code.py
def func_py_generate_hamming_code(bits):
    n = len(bits)
    parity_count = 0
    
    while (2**parity_count) < (n + parity_count + 1):
        parity_count += 1
    
    hamming_code = []
    j = 0
    k = 0
    for i in range(1, n + parity_count + 1):
        if i == 2**j:
            hamming_code.append(0)
            j += 1
        else:
            hamming_code.append(int(bits[k]))
            k += 1
    
    for i in range(parity_count):
        position = 2**i
        value = 0
        for j in range(1, len(hamming_code) + 1):
            if j & position:
                value = value ^ hamming_code[j - 1]
        hamming_code[position - 1] = value
    
    return ''.join(map(str, hamming_code))

bits = "1011"
print(func_py_generate_hamming_code(bits))
