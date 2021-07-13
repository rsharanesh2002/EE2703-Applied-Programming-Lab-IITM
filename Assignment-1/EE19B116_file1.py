'''
EE2703 Applied Programming Lab
Submission for Tutorial-1
Name: Sharanesh R
Roll Numer: EE19B116
'''

import sys

# List to store all element's object
token_list = {
    'Resistor': [],
    'Inductor': [],
    'Capacitor': [],
    'Voltage_Source': [],
    'Current_Source': [],
    'Voltage_Controlled_Voltage_Source': [],
    'Voltage_Controlled_Current_Source': [],
    'Current_Controlled_Voltage_Source': [],
    'Current_Controlled_Current_Source': []
}

# Definging a function to analyse token
def analyseToken(tokens):
    # Check if the name is alphanumeric
    if tokens[0].isalnum():
        # Parse the values of the element and store as objects in a list
        if tokens[0][0] == 'R':
            name, from_node, to_node, value = tokens
            token_list['Resistor'].append({'name': name, 'from_node': from_node, 'to_node': to_node, 'value': value})
        if tokens[0][0] == 'L':
            name, from_node, to_node, value = tokens
            token_list['Inductor'].append({'name': name, 'from_node': from_node, 'to_node': to_node, 'value': value})
        if tokens[0][0] == 'C':
            name, from_node, to_node, value = tokens
            token_list['Capacitor'].append({'name': name, 'from_node': from_node, 'to_node': to_node, 'value': value})
        elif tokens[0][0] == 'V':
            name, from_node, to_node, value = tokens
            token_list['Voltage_Source'].append({'name': name, 'from_node': from_node, 'to_node': to_node, 'value': value})
        elif tokens[0][0] == 'I':
            name, from_node, to_node, value = tokens
            token_list['Current_Source'].append({'name': name, 'from_node': from_node, 'to_node': to_node, 'value': value})
        elif tokens[0][0] == 'E':
            name, from_node, to_node, control_voltage_from_node, control_voltage_to_node, value = tokens
            token_list['Voltage_Controlled_Voltage_Source'].append({'name': name, 'from_node': from_node, 'to_node': to_node,
                                                                    'control_voltage_from_node': control_voltage_from_node, 'control_voltage_to_node': control_voltage_to_node, 'value': value})
        elif tokens[0][0] == 'G':
            name, from_node, to_node, control_voltage_from_node, control_voltage_to_node, value = tokens
            token_list['Voltage_Controlled_Current_Source'].append({'name': name, 'from_node': from_node, 'to_node': to_node,
                                                                    'control_voltage_from_node': control_voltage_from_node, 'control_voltage_to_node': control_voltage_to_node, 'value': value})
        elif tokens[0][0] == 'H':
            name, from_node, to_node, controlling_voltage, value = tokens
            token_list['Current_Controlled_Voltage_Source'].append({'name': name, 'from_node': from_node, 'to_node': to_node, 'controlling_voltage': controlling_voltage, 'value': value})
        elif tokens[0][0] == 'F':
            name, from_node, to_node, controlling_voltage, value = tokens
            token_list['Current_Controlled_Current_Source'].append({'name': name, 'from_node': from_node, 'to_node': to_node, 'controlling_voltage': controlling_voltage, 'value': value})
    else:
        # Check if the node names are not alpahnumeric.
        sys.exit("Error: Node names should be alphanumeric")

try:
	if(len(sys.argv) != 2): # Check if the file is given as a arguement
		sys.exit('Invalid number of arguments')
			
	name = sys.argv[1] # Get the filename from the arguements given in the command line
		
	f = open(name) # Open the file given
	lines = f.readlines() # Read the content of the file line by line array
	f.close() # Close the file after reading its contents

	for index,line in enumerate(lines): # Enumerate through the lines of the file to find the index of the satrt and end line
		try:
			if line.split()[0] == '.circuit\n' or line.split()[0] == '.circuit': # Checking for the start line
				index_start = index # Saving the index of start line 
				
			elif line.split()[0] == '.end' or line.split()[0]  == '.end\n': # Checking for the end line
				index_end = index # Saving the index of start line
				
		except IndexError: # Except all the index error to continue iterating 
			continue
		            
	netlist = lines[index_start+1:index_end] # Selecting only the valid lines that are having the circuit net's details
	for net in reversed(netlist): # Looping through the nets to get further details
		token = net.split() # Splitting each line into its component tokens based on the spaces 
		index = len(token) # The total tokens in the net
		reversed_net = "" # A string to hold the reversed net value
		
		for i in range(index): # Looping through the tokens of the net, to check if there is any comment  
			if token[i] == "#" or token[i] == "#\n": # Checking for "#" to find out if there is any comments
				index = i # if there is any comments, we print till only those index value
				break # break if we have found the "#" sysmbol
				
		for i in range(index): # Concatenating the tokens to be printed in reverse order
			reverse = token[index-i-1] # Selecting the last correct word of the net
			reversed_net = reversed_net+reverse +" " # concatenating with the existing reversed string
		
		analyseToken(token[:index]) #Analysing the tokens to parse the individual data
		print(reversed_net) # Printing the Reversed net
		
except Exception:
	print("Error: Invalid File")