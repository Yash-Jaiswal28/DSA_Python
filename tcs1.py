def find_possible_digits(valid_digits, faulty_digit):   
    possible_digits = []
    for digit, valid in valid_digits.items():     
        # Calculate the difference between faulty and valid digits
        diff = sum(1 for a, b in zip(faulty_digit, valid) if a != b)
        if diff <= 1:  # Allow exact match and single character difference
            possible_digits.append(digit)
    return possible_digits

def solve():    
    # Read the standard digits (3 lines)
    standard_digits = [input().strip() for _ in range(3)]  

    # Read the faulty digits (3 lines)
    faulty_digits = [input().strip() for _ in range(3)]   
   
    # Construct valid digits for each digit position
    valid_digits = {}
    for i in range(10):
        valid_digits[i] = ''.join(standard_digits[j][i*3:(i+1)*3] for j in range(3))   
   
    # Find possible digits for each faulty digit
    faulty_number = []
    for i in range(len(faulty_digits[0]) // 3):
        faulty_digit = ''.join(faulty_digits[j][i*3:(i+1)*3] for j in range(3))
        possible_digits = find_possible_digits(valid_digits, faulty_digit)
        
        # If no possible digits, exit with "Invalid"
        if not possible_digits:
            print("Invalid", end='')
            return
        
        faulty_number.append(possible_digits) 

    # Calculate total sum of all possible combinations
    from itertools import product
    total_sum = 0
    for possible in product(*faulty_number):
        # Ensure no empty combinations
        if not possible:
            print("Invalid", end='')
            return
        
        # Convert each digit to string before joining
        number_str = ''.join(str(digit) for digit in possible)
        total_sum += int(number_str)
    
    print(total_sum, end='')

solve()
