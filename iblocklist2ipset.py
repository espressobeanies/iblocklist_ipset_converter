#!/usr/bin/env python3
import os

# Function to convert the input file into an ipset ruleset
def convert_to_ipset(input_file, output_file):
    # Open the input file for reading
    with open(input_file, 'r') as f:
        # Read the contents of the file into a list
        lines = f.readlines()
    
    ipset_list = []
    # Iterate over each line in the input file
    for line in lines:
        # Split the line into name and IP range
        name, ip_range = line.rsplit(':',1)
        ipset_list.append((name,ip_range))

    # Open the output file for writing
    with open(output_file, 'w') as f:
        # Write the ipset create command to the output file
        f.write("create myset hash:net\n")

        for ipset in ipset_list:
            # Write the ipset add command to the output file
            f.write(f"add myset {ipset[1]} name {ipset[0]}\n")

    # Write the ipset list command to the output file
    with open(output_file, 'a') as f:
        f.write("list myset\n")

# Example usage
convert_to_ipset('input.txt', 'output.ipset')

