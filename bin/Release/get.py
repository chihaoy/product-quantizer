# Open the file for reading
sum = 0
for a in range(0,100):
    with open('correct.txt', 'r') as file:
    # Initialize a list to store the first vectors
        first_vectors = []
    
    # Loop through each line in the file
        for index, line in enumerate(file):
            if index < 64:
                # Split the line into vectors (assuming they are tab-separated)
                vectors = line.strip().split('\t')
            
            # Get the first vector (or index 'a') and add it to the list
                first_vectors.append(vectors[a])
            else:
                # Stop after processing the first 16 lines
                break
    extracted_values = []
# Open the file
    with open('result.txt', 'r') as file:
    # Loop over the lines in the file
        for i, line in enumerate(file, start=1):
        # Process lines from 101 to 200 only
            if 1+a*64 <= i <= 64+a*64: 
                # Split the line by tabs
                values = line.strip().split('\t')
            # Extract the second value (index 1) and add it to the list
                extracted_values.append(values[1])
        # Stop after reaching the 200th line
            elif i > 64+a*64:
                break

# Output the list to verify the result

##print(extracted_values)
    shared_elements = set(first_vectors) & set(extracted_values)

# Get the number of shared elements
    num_shared_elements = len(shared_elements)

# Output the result
    sum = sum + num_shared_elements
    print("Number of shared elements:", num_shared_elements)
print(sum / 6400)
