def minimum_cost_transformation(string_mappings, target_string):
    str_length = len(target_string)
    
    # Initialize dynamic programming array
    transformation_costs = [float('inf')] * (str_length + 1)
    transformation_costs[str_length] = 0
    
    # Iterate from the end of the string
    for start_index in range(str_length - 1, -1, -1):
        current_substring = ""
        
        # Generate all possible substrings
        for end_index in range(start_index, str_length):
            current_substring += target_string[end_index]
            
            # Check against all string mappings
            for mapping_string, mapping_cost in string_mappings:
                # Skip if mapping is longer than current substring
                if len(mapping_string) > len(current_substring):
                    continue
                
                # Check substring match from the beginning
                if current_substring.startswith(mapping_string):
                    # Try different split points and update minimum cost
                    for split_point in range(len(mapping_string)):
                        next_index = start_index + split_point + 1
                        candidate_cost = mapping_cost + transformation_costs[next_index]
                        transformation_costs[start_index] = min(
                            transformation_costs[start_index], 
                            candidate_cost
                        )
    
    # Return result
    return transformation_costs[0] if transformation_costs[0] != float('inf') else -1

def main():
    # Input parsing
    mapping_count = int(input())
    string_mappings = []
    
    # Read string mappings
    for _ in range(mapping_count):
        mapping_string, mapping_cost = input().split()
        string_mappings.append((mapping_string, int(mapping_cost)))
    
    # Read target string
    target_string = input().strip()
    
    # Compute and print result
    result = minimum_cost_transformation(string_mappings, target_string)
    
    if result != -1:
        print(result)
    else:
        print("Impossible")

# Standard boilerplate to run the main function
if __name__ == "__main__":
    main()