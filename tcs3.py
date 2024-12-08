def segment_intersection_validator(wire_segment_a, wire_segment_b):
    x1, y1, x2, y2 = wire_segment_a
    x3, y3, x4, y4 = wire_segment_b
    
    # Vertical segment intersection check
    if x1 == x2 and x3 == x4:
        if x1 == x3 and max(min(y1, y2), min(y3, y4)) <= min(max(y1, y2), max(y3, y4)):
            return x1, max(min(y1, y2), min(y3, y4))
    
    # Horizontal segment intersection check
    if y1 == y2 and y3 == y4:
        if y1 == y3 and max(min(x1, x2), min(x3, x4)) <= min(max(x1, x2), max(x3, x4)):
            return max(min(x1, x2), min(x3, x4)), y1
    
    return None

def voltage_computation_matrix(wire_configurations):
    connection_matrix = {}
    
    # Intersection discovery phase
    for idx_primary in range(len(wire_configurations)):
        for idx_secondary in range(idx_primary + 1, len(wire_configurations)):
            intersection_coordinate = segment_intersection_validator(
                wire_configurations[idx_primary], 
                wire_configurations[idx_secondary]
            )
            if intersection_coordinate:
                if intersection_coordinate not in connection_matrix:
                    connection_matrix[intersection_coordinate] = set()
                connection_matrix[intersection_coordinate].update([idx_primary, idx_secondary])
    
    cumulative_electrical_potential = 0
    
    # Potential calculation phase
    for coordinate, interconnected_segments in connection_matrix.items():
        connection_count = len(interconnected_segments)
        minimal_segment_length = min(
            abs(wire_configurations[i][1] - wire_configurations[i][3]) 
            for i in interconnected_segments
        )
        cumulative_electrical_potential += connection_count * minimal_segment_length
    
    return cumulative_electrical_potential

def system_risk_assessment():
    # Input parsing with enhanced error handling
    try:
        wire_segment_quantity = int(input())
        wire_segment_collection = []
        
        for _ in range(wire_segment_quantity):
            wire_segment_collection.append(list(map(int, input().split())))
        
        # Species vulnerability mapping
        species_threshold_map = {}
        species_input = input().split()
        
        for species_entry in species_input:
            species, resistance_threshold = species_entry.split(":")
            species_threshold_map[species] = int(resistance_threshold)
        
        # Specific species interaction identification
        species_fence_contact = input().strip()
        
        # Electrical potential computation
        total_system_voltage = voltage_computation_matrix(wire_segment_collection)
        
        # Risk evaluation logic
        if species_threshold_map[species_fence_contact] < total_system_voltage:
            print("Yes")
        else:
            print("No")
        
        # Population impact analysis
        vulnerable_species_count = sum(
            1 for threshold in species_threshold_map.values() 
            if threshold < total_system_voltage
        )
        total_species_population = len(species_threshold_map)
        population_risk_factor = vulnerable_species_count / total_species_population
        
        print(f"{population_risk_factor:.2f}")
    
    except (ValueError, KeyError) as processing_error:
        print("System error: Invalid input configuration")
        raise processing_error

def main_execution_handler():
    system_risk_assessment()

if __name__ == "__main__":
    main_execution_handler()