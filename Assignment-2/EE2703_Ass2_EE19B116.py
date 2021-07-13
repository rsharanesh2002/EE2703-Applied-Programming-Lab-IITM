'''
EE2703 Applied Programming Lab
Submission for Assignment-2
Name: Sharanesh R
Roll Numer: EE19B116
'''

# Importing the required Libraries
import sys
import json
import numpy as np
import math
import cmath

# List to store all element's and its node details
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

# Few auxillary variables to store some True or False values
is_ac = False
frequency = False
is_ground_def = False

# Function to analyse token
def analyseToken(tokens, is_ac):
    # Check if the element name is alphanumeric
    if tokens[0].isalnum():
        # Check the first token and decide on the typeof element
        if tokens[0][0] == 'R':
            try: # Extracting the values from the tokens
                name, from_node, to_node, value = tokens
            except:
                sys.exit('Error: Invalid number of arguments provided while defining the {} Resistor. Correct Format is :- "R... n1 n2 value"'.format(tokens[0]))
            if(from_node.isalnum() and to_node.isalnum() and isinstance(float(value),float) and from_node != to_node):
                # Having a check on the nodes and making sure from and to nodes arent the same
                token_list['Resistor'].append({'name': name, 'from_node': from_node, 'to_node': to_node, 'value': value})
            else:
                sys.exit('Error: Invalid inputs provided while defining the {} Resistor. Correct Format is :- "R... n1 n2 value"'.format(tokens[0]))

        if tokens[0][0] == 'L': # Extracting the values from the tokens
            try:
                name, from_node, to_node, value = tokens
            except:
                sys.exit('Error: Invalid number of arguments provided while defining the {} Inductor. Correct Format is :- "L... n1 n2 value"'.format(tokens[0]))
            if(from_node.isalnum() and to_node.isalnum() and isinstance(float(value),float) and from_node != to_node):
                # Having a check on the nodes and making sure from and to nodes arent the same
                token_list['Inductor'].append({'name': name, 'from_node': from_node, 'to_node': to_node, 'value': value})
            else:
                sys.exit('Error: Invalid inputs provided while defining the {} Inductor. Correct Format is :- "L... n1 n2 value"'.format(tokens[0]))
        
        if tokens[0][0] == 'C': # Extracting the values from the tokens
            try: # Extracting the values from the tokens
                name, from_node, to_node, value = tokens
            except:
                sys.exit('Error: Invalid number of arguments provided while defining the {} Capacitor. Correct Format is :- "C... n1 n2 value"'.format(tokens[0]))
            if(from_node.isalnum() and to_node.isalnum() and isinstance(float(value),float) and from_node != to_node):
                # Having a check on the nodes and making sure from and to nodes arent the same
                token_list['Capacitor'].append({'name': name, 'from_node': from_node, 'to_node': to_node, 'value': value})
            else:
                sys.exit('Error: Invalid inputs provided while defining the {} Capacitor. Correct Format is :- "C... n1 n2 value"'.format(tokens[0]))
        
        if tokens[0][0] == 'V': # Extracting the values from the tokens
            if(is_ac): #Checking if the given source is ac or dc
                if tokens[3] == 'ac':
                    try: # Extracting the values from the tokens
                        name, from_node, to_node, ac_or_dc, mag, phase = tokens
                    except:
                        sys.exit('Error: Invalid number of arguments provided while defining the {} AC Voltage Source. Correct Format is :- "V.. n1 n2 ac mag phase"'.format(tokens[0]))
                    if(from_node.isalnum() and to_node.isalnum() and isinstance(float(mag),float) and isinstance(float(phase),float) and from_node != to_node):
                        # Having a check on the nodes and making sure from and to nodes arent the same
                        token_list['Voltage_Source'].append({'name': name, 'from_node': from_node, 'to_node': to_node, 'ac_or_dc': ac_or_dc, 'mag': mag, 'phase': phase})
                    else:
                        sys.exit('Error: Invalid inputs provided while defining the AC Voltage source. Correct Format is :- "V.. n1 n2 ac mag phase"')
                
                elif tokens[3] == 'dc':
                    try: # Extracting the values from the tokens
                        name, from_node, to_node, ac_or_dc, value = tokens
                    except:
                        sys.exit('Error: Invalid number of arguments provided while defining the {} DC Voltage Source. Correct Format is :- "V.. n1 n2 ac mag phase"'.format(tokens[0]))
                    if(from_node.isalnum() and to_node.isalnum() and isinstance(float(value),float) and from_node != to_node):
                        # Having a check on the nodes and making sure from and to nodes arent the same
                        token_list['Voltage_Source'].append({'name': name, 'from_node': from_node, 'to_node': to_node, 'value': value, 'ac_or_dc': ac_or_dc, 'value': value})
                    else:
                        sys.exit('Error: Invalid inputs provided while defining the DC Voltage source. Correct Format is :- "V.. n1 n2 ac mag phase"')

                else:
                    sys.exit('Error: Invalid type provided for the {} Volatge source. Specify the voltage sources as dc or ac in the declaration. Correct Format is :- "V.. n1 n2 dc value (or) V.. n1 n2 ac mag phase"'.format(tokens[0]))
            
            else:
                try: # Extracting the values from the tokens
                    name, from_node, to_node, value = tokens
                except:
                    sys.exit('Error: Invalid number of arguments provided while defining the {} Voaltge Source. Correct Format is :- "V... n1 n2 value"'.format(tokens[0]))
                if(from_node.isalnum() and to_node.isalnum() and isinstance(float(value),float) and from_node != to_node):
                    # Having a check on the nodes and making sure from and to nodes arent the same
                    token_list['Voltage_Source'].append({'name': name, 'from_node': from_node, 'to_node': to_node, 'value': value, 'value': value})
                else:
                    sys.exit('Error: Invalid inputs provided while defining the {} Volatge Source. Correct Format is :- "V... n1 n2 value"'.format(tokens[0]))

        if tokens[0][0] == 'I':
            if(is_ac): #Checking if the given source is ac or dc
                if tokens[3] == 'ac':
                    try: # Extracting the values from the tokens
                        name, from_node, to_node, ac_or_dc, mag, phase = tokens
                    except:
                        sys.exit('Error: Invalid number of arguments provided while defining the {} AC Current Source. Correct Format is :- "I.. n1 n2 ac mag phase"'.format(tokens[0]))
                    if(from_node.isalnum() and to_node.isalnum() and isinstance(float(mag),mag) and isinstance(float(phase),phase) and from_node != to_node):
                        # Having a check on the nodes and making sure from and to nodes arent the same
                        token_list['Current_Source'].append({'name': name, 'from_node': from_node, 'to_node': to_node, 'ac_or_dc': ac_or_dc, 'mag': mag, 'phase': phase})
                    else:
                        sys.exit('Error: Invalid inputs provided while defining the {} AC Current source. Correct Format is :- "I.. n1 n2 ac mag phase"')
                
                elif tokens[3] == 'dc':
                    try: # Extracting the values from the tokens
                        name, from_node, to_node, ac_or_dc, value = tokens
                    except:
                        sys.exit('Error: Invalid number of arguments provided while defining the {} DC Current Source. Correct Format is :- "I.. n1 n2 ac mag phase"'.format(tokens[0]))
                    if(from_node.isalnum() and to_node.isalnum() and isinstance(float(value),float) and from_node != to_node):
                        # Having a check on the nodes and making sure from and to nodes arent the same
                        token_list['Current_Source'].append({'name': name, 'from_node': from_node, 'to_node': to_node, 'value': value, 'ac_or_dc': ac_or_dc, 'value': value})
                    else:
                        sys.exit('Error: Invalid inputs provided while defining the {} AC Current source. Correct Format is :- "I.. n1 n2 ac mag phase"')

                else:
                    sys.exit('Error: Invalid type provided for the {} Volatge source. Specify the Current sources as dc or ac in the declaration. Correct Format is :- "I.. n1 n2 dc value (or) I.. n1 n2 ac mag phase"'.format(tokens[0]))
            
            else:
                try: # Extracting the values from the tokens
                    name, from_node, to_node, value = tokens
                except:
                    sys.exit('Error: Invalid number of arguments provided while defining the {} Voaltge Source. Correct Format is :- "I... n1 n2 value"'.format(tokens[0]))
                if(from_node.isalnum() and to_node.isalnum() and isinstance(float(value),float) and from_node != to_node):
                    # Having a check on the nodes and making sure from and to nodes arent the same
                    token_list['Current_Source'].append({'name': name, 'from_node': from_node, 'to_node': to_node, 'value': value, 'value': value})
                else:
                    sys.exit('Error: Invalid inputs provided while defining the {} Volatge Source. Correct Format is :- "I... n1 n2 value"'.format(tokens[0]))

        elif tokens[0][0] == 'E':
            try: # Extracting the values from the tokens
                name, from_node, to_node, control_voltage_from_node, control_voltage_to_node, value = tokens
            except:
                sys.exit('Error: Invalid number of arguments provided while defining the {} Voltage Controlled Voltage Source. Correct Format is :- "E.. n1 n2 n3 n4 value"'.format(tokens[0]))
            if(from_node.isalnum() and to_node.isalnum() and from_node != to_node and control_voltage_from_node.isalnum() and control_voltage_to_node.isalnum() and isinstance(float(value),float)):
                # Having a check on the nodes and making sure from and to nodes arent the same
                token_list['Voltage_Controlled_Voltage_Source'].append({'name': name, 'from_node': from_node, 'to_node': to_node,'control_voltage_from_node': control_voltage_from_node, 'control_voltage_to_node': control_voltage_to_node, 'value': value})
            else:
                sys.exit('Error: Invalid inputs provided while defining the {} Voltage Controlled Voltage Source. Correct Format is :- "E.. n1 n2 n3 n4 value"'.format(tokens[0]))

        elif tokens[0][0] == 'G':
            try: # Extracting the values from the tokens
                name, from_node, to_node, control_voltage_from_node, control_voltage_to_node, value = tokens
            except:
                sys.exit('Error: Invalid number of arguments provided while defining the {} Voltage Controlled Current Source. Correct Format is :- "G.. n1 n2 n3 n4 value"'.format(tokens[0]))
            if(from_node.isalnum() and to_node.isalnum() and from_node != to_node and control_voltage_from_node.isalnum() and control_voltage_to_node.isalnum() and isinstance(float(value),float)):
                # Having a check on the nodes and making sure from and to nodes arent the same
                token_list['Voltage_Controlled_Current_Source'].append({'name': name, 'from_node': from_node, 'to_node': to_node,'control_voltage_from_node': control_voltage_from_node, 'control_voltage_to_node': control_voltage_to_node, 'value': value})
            else:
                sys.exit('Error: Invalid inputs provided while defining the {} Voltage Controlled Current Source. Correct Format is :- "G.. n1 n2 n3 n4 value"'.format(tokens[0]))

        elif tokens[0][0] == 'H':
            try: # Extracting the values from the tokens
                name, from_node, to_node, controlling_voltage, value = tokens
            except:
                sys.exit('Error: Invalid number of arguments provided while defining the {} Current Controlled Voltage Source. Correct Format is :- "H.. n1 n2 V.. value"'.format(tokens[0]))
            if(from_node.isalnum() and to_node.isalnum() and from_node != to_node and controlling_voltage.isalnum() and isinstance(float(value),float)):
                # Having a check on the nodes and making sure from and to nodes arent the same
                token_list['Current_Controlled_Voltage_Source'].append({'name': name, 'from_node': from_node, 'to_node': to_node, 'controlling_voltage': controlling_voltage, 'value': value})
            else:
                sys.exit('Error: Invalid inputs provided while defining the {} Current Controlled Voltage Source. Correct Format is :- "H.. n1 n2 V.. value"'.format(tokens[0]))
        
        elif tokens[0][0] == 'F':
            try: # Extracting the values from the tokens
                name, from_node, to_node, controlling_voltage, value = tokens
            except:
                sys.exit('Error: Invalid number of arguments provided while defining the {} Current Controlled Current Source. Correct Format is :- "F.. n1 n2 V.. value"'.format(tokens[0]))
            if(from_node.isalnum() and to_node.isalnum() and from_node != to_node and controlling_voltage.isalnum() and isinstance(float(value),float)):
                # Having a check on the nodes and making sure from and to nodes arent the same
                token_list['Current_Controlled_Current_Source'].append({'name': name, 'from_node': from_node, 'to_node': to_node, 'controlling_voltage': controlling_voltage, 'value': value})
            else:
                sys.exit('Error: Invalid inputs provided while defining the {} Current Controlled Current Source. Correct Format is :- "F.. n1 n2 V.. value"'.format(tokens[0]))

    else:
        sys.exit("Error: The element names should be alphanumeric")

    return token_list

# A function defined to generate the nodes dictionary
def generate_nodes_dict(token_list):

    nodes_dict = {} # Defining an empty dictionary to store the nodes information.
    nodes_dict['GND'] = 0 # By defaut setting the 'GND' node to 0
    ind = 1 # An auxillary index variable

    for element in token_list['Resistor']: # Iteraing through each element

        if element['from_node'] in nodes_dict: # Checking if the node is already in nodes dictionary
            pass
        else:
            nodes_dict[element['from_node']] = ind
            ind += 1

        if element['to_node'] in nodes_dict: # Checking if the node is already in nodes dictionary
            pass
        else:
            nodes_dict[element['to_node']] = ind
            ind += 1

    for element in token_list['Inductor']: # Iteraing through each element
        if element['from_node'] in nodes_dict: # Checking if the node is already in nodes dictionary
            pass
        else:
            nodes_dict[element['from_node']] = ind
            ind += 1

        if element['to_node'] in nodes_dict: # Checking if the node is already in nodes dictionary
            pass
        else:
            nodes_dict[element['to_node']] = ind
            ind += 1

    for element in token_list['Capacitor']: # Iteraing through each element
        if element['from_node'] in nodes_dict: # Checking if the node is already in nodes dictionary
            pass
        else:
            nodes_dict[element['from_node']] = ind
            ind += 1

        if element['to_node'] in nodes_dict: # Checking if the node is already in nodes dictionary
            pass
        else:
            nodes_dict[element['to_node']] = ind
            ind += 1

    for element in token_list['Voltage_Source']: # Iteraing through each element
        if element['from_node'] in nodes_dict: # Checking if the node is already in nodes dictionary
            pass
        else:
            nodes_dict[element['from_node']] = ind
            ind += 1

        if element['to_node'] in nodes_dict: # Checking if the node is already in nodes dictionary
            pass
        else:
            nodes_dict[element['to_node']] = ind
            ind += 1

    for element in token_list['Current_Source']: # Iteraing through each element

        if element['from_node'] in nodes_dict: # Checking if the node is already in nodes dictionary
            pass
        else:
            nodes_dict[element['from_node']] = ind
            ind += 1

        if element['to_node'] in nodes_dict: # Checking if the node is already in nodes dictionary
            pass
        else:
            nodes_dict[element['to_node']] = ind
            ind += 1

    return nodes_dict

 
# A function defined to solve the circuit
def solve_the_circuit(token_list):
    if len(token_list['Voltage_Controlled_Voltage_Source']) or len(token_list['Voltage_Controlled_Current_Source']) or len(token_list['Current_Controlled_Current_Source']) or len(token_list['Current_Controlled_Voltage_Source']) > 0:
        sys.exit('Sorry!! The circuit given contains a dependent source, cant compute the output')

    # Calling the generate nodes function to get the nodes dictionary
    nodes_dict = generate_nodes_dict(token_list)

    key_list = list(nodes_dict.keys()) # Getting the keys of nodes dictionary
    val_list = list(nodes_dict.values()) # Getting the values stored in the nodes dictionary

    num_nodes = len(nodes_dict) - 1 + len(token_list['Voltage_Source']) + len(token_list['Voltage_Controlled_Voltage_Source'])
    variable_list = [] # A list to store all the variables to be computed

    for i in range(len(nodes_dict) - 1): # Iterating the nodes dictionary and creating the variable list.
        variable_list.append("Voltage at the node "+ key_list[val_list.index(i+1)])

    admittance_matrix = np.zeros((num_nodes, num_nodes), dtype=complex) # Creating an empty admittance matrix with the appropriate size
    current_matrix = np.zeros((num_nodes, 1), dtype=complex) # Creating an empty current matrix with the appropriate size 


    for element in token_list['Resistor']: # Iterating through each element
        # Resistor contributes only to the admittance matrix
        node_high = int(nodes_dict[element['from_node']]) - 1 # Getting the high node
        node_low = int(nodes_dict[element['to_node']]) - 1 # Getting the low node

        admittance = 1/float(element['value']) # Computinng the admittance value

        # Making changes in the admittance matrix as per the KVL and KCL equations
        if node_high != -1 and node_low != -1:
            admittance_matrix[node_high][node_high] += admittance
            admittance_matrix[node_high][node_low] -= admittance
            admittance_matrix[node_low][node_high] -= admittance
            admittance_matrix[node_low][node_low] += admittance

        elif node_high == -1 and node_low != -1:
            admittance_matrix[node_low][node_low] += admittance

        elif node_low == -1 and node_high != -1:
            admittance_matrix[node_high][node_high] += admittance

    for element in token_list['Inductor']: # Iterating through each element
        # Inductor contributes only to the admittance matrix
        node_high = int(nodes_dict[element['from_node']]) - 1 # Getting the high node
        node_low = int(nodes_dict[element['to_node']]) - 1 # Getting the low node

        if(is_ac):
            try: # Computinng the admittance value as per the frequency
                admittance = complex(0, -(1/(frequency * float(element['value']))))
            except:
                sys.exit('Error: .ac is not declared in the netlist')
        else:
            admittance = 10e50 ##Giving a high value of admittance in case of DC 

        # Making changes in the admittance matrix as per the KVL and KCL equations
        if node_high != -1 and node_low != -1:
            admittance_matrix[node_high][node_high] += admittance
            admittance_matrix[node_high][node_low] -= admittance
            admittance_matrix[node_low][node_high] -= admittance
            admittance_matrix[node_low][node_low] += admittance

        elif node_high == -1 and node_low != -1:
            admittance_matrix[node_low][node_low] += admittance

        elif node_low == -1 and node_high != -1:
            admittance_matrix[node_high][node_high] += admittance

    for element in token_list['Capacitor']: # Iterating through each element
        # Capacitor contributes only to the admittance matrix
        node_high = int(nodes_dict[element['from_node']]) - 1 # Getting the high node
        node_low = int(nodes_dict[element['to_node']]) - 1 # Getting the low node

        if(is_ac):
            try: # Computinng the admittance value as per the frequency
                admittance = complex(0, frequency * float(element['value']))  
            except:
                sys.exit('Error: .ac is not declared in the netlist')
        else:
            admittance = 10e-50 ##Giving a low value of admittance in case of DC
        
        # Making changes in the admittance matrix as per the KVL and KCL equations
        if node_high != -1 and node_low != -1:
            admittance_matrix[node_high][node_high] += admittance
            admittance_matrix[node_high][node_low] -= admittance
            admittance_matrix[node_low][node_high] -= admittance
            admittance_matrix[node_low][node_low] += admittance

        elif node_high == -1 and node_low != -1:
            admittance_matrix[node_low][node_low] += admittance

        elif node_low == -1 and node_high != -1:
            admittance_matrix[node_high][node_high] += admittance

    for element in token_list['Voltage_Source']: # Iterating through each element
        # Voltage source contributes to both cuurent and admittance matrix
        node_high = int(nodes_dict[element['from_node']]) - 1 # Getting the high node
        node_low = int(nodes_dict[element['to_node']]) - 1 # Getting the low node

        if(is_ac): # Checking if the defined source is ac or dc
            if element['ac_or_dc'] == 'ac':
                voltage = cmath.rect(float(element['mag'])/2, float(element['phase'])) # The phase is here defined in degree.
            elif element['ac_or_dc'] == 'dc':
                voltage = cmath.rect(float(element['value']), 0)
        else:
            voltage = float(element['value'])

        # Creating a new variable to store the current through the voltage source
        new_var = 'Current flowing from node ' + key_list[val_list.index(node_high + 1)]+' to node ' + key_list[val_list.index(node_low + 1)]
        variable_list.append(new_var)
        idx = variable_list.index(new_var)

        # Making changes in the admittance matrix as per the KVL and KCL equations
        if node_high != -1 and node_low != -1:
            admittance_matrix[node_high][idx] += 1
            admittance_matrix[node_low][idx] -= 1
            admittance_matrix[idx][node_high] += 1
            admittance_matrix[idx][node_low] -= 1
            current_matrix[idx][0] += voltage

        elif node_high == -1 and node_low != -1:
            admittance_matrix[node_low][idx] -= 1
            admittance_matrix[idx][node_low] -= 1
            current_matrix[idx][0] += voltage

        elif node_low == -1 and node_high != -1:
            admittance_matrix[node_high][idx] += 1
            admittance_matrix[idx][node_high] += 1
            current_matrix[idx][0] += voltage

    for element in token_list['Current_Source']: # Iterating through each element
        # Current source contributes only to current matrix
        node_high = int(nodes_dict[element['from_node']]) - 1
        node_low = int(nodes_dict[element['to_node']]) - 1

        if(is_ac): # Checking if the defined source is ac or dc
            if element['ac_or_dc'] == 'ac':
                current = cmath.rect(float(element['mag'])/2, float(element['phase'])) # The phase is here defined in degree.
            elif element['ac_or_dc'] == 'dc':
                current = cmath.rect(float(element['value']), 0)
        else:
            current = float(element['value'])

        # Making changes in the current matrix as per the KCL equations
        if node_high != -1 and node_low != -1:
            current_matrix[node_high][0] += current
            current_matrix[node_low][0] -= current

        elif node_high == -1 and node_low != -1:
            current_matrix[node_low][0] -= current

        elif node_high != -1 and node_low == -1:
            current_matrix[node_high][0] += current

    # Finally solving the Mx=b linear equation
    try:
        output_matrix = np.linalg.solve(admittance_matrix, current_matrix)

    except:
        sys.exit('Error: Unable to calculate inverse since the determinant is zero, Please check the circuit again.')
    
    # Finally printing all the variables after solving the circuit
    print("The Volatges and Currents in the circuit are as follows:")
    for i in range(len(variable_list)):
        if variable_list[i][0] == 'V':
            print('   {} = {} V'.format(variable_list[i], '{:.2e}'.format(output_matrix[i][0])))
        if variable_list[i][0] == 'C':
            print('   {} = {} A'.format(variable_list[i], '{:.2e}'.format(output_matrix[i][0])))

try:
    if(len(sys.argv) != 2):# Check if the file is given as a arguement
        sys.exit('Error: Invalid number of arguments')
            
    name = sys.argv[1] # Get the filename from the arguements given in the command line
        
    f = open(name) # Open the file given
    lines = f.readlines() # Read the content of the file line by line array
    f.close() # Close the file after reading its contents
    
    for index,line in enumerate(lines):# Enumerate through the lines of the file to find the index of the satrt and end line
        try:
            if line.split()[0] == '.circuit\n' or line.split()[0] == '.circuit':# Checking for the start line
                index_start = index # Saving the index of start line 
                
            elif line.split()[0] == '.end' or line.split()[0]  == '.end\n':# Checking for the end line
                index_end = index # Saving the index of start line
            
            elif line.split()[0] == '.ac' or line.split()[0]  == '.ac\n':# Checking for the ac line
                index_ac = index # Saving the index of the .ac line
                is_ac = True
                try:
                    frequency = int(line.split()[2])
                except Exception as e:
                    sys.exit('Error: Invalid declaration of ".ac" command. The correct format is :- ".ac V... frequency"')

        except IndexError:# Except all the index error to continue iterating 
            continue
    
    try:
        netlist = lines[index_start+1:index_end] # Selecting only the valid lines that are having the circuit net's details
    except Exception:
        sys.exit('Error: Invalid File')
    
    for net in netlist:# Looping through the nets to get further details
        if net.find('#') != -1: # Finding for any comments mentioned in the line
            index = net.find('#')# If any comment is present, we just neglect those part
            line = net[:index]

        else:
            line = net # If no comment is present then we consider entire line

        if (line != "" or line != "\n"):
            if line.find("GND") != -1: # Checking if the GND Component has been defined
                is_ground_def = True 
            line = line.split() # Splitting the line into the words

            token_list = analyseToken(line,is_ac) # Analysing the tokens 

    if is_ground_def: # When the ground componet is properly defined, we solve the circuit.
        solve_the_circuit(token_list)
    else:
        sys.exit('Error: Kindly specify the GND component to solve the circuit')

except Exception as e:
    print('Error: Please rectify the following error: \n ', e)