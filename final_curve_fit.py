# ECOR 1042 Lab 6 - Template for curve_fit function



# Remember to include docstring and type annotations for your functions



# Update "" with your name (e.g., Cristina Ruiz Martin)

__author__ = ""



# Update "" with your student number (e.g., 100100100)

__student_number__ = ""



# Update "" with your team (e.g. T-102, use the notation provided in the example)

__team__ = ""



#==========================================#

# Place your curve_fit function after this line

# Importing necessary library
import numpy as np

def curve_fit(characters: list[dict], attribute: str, degree: int) -> str:
    """
    """
    # Creating empty lists to store attribute and health associated values
    attribute_list = []
    health_list = []
    
    # Going through the dictionaries provided within the list
    for character in characters:
        
        # If the attribute is not in the list
        if character[attribute] not in attribute_list:
            
            # Adding the attribute value to the attribute list
            attribute_list.append(character[attribute])
            
            # Adding the health value to the health list
            health_list.append([character["Health"]])
        else:
            
            # Creating variable of index of the attribute from attribute list
            index = attribute_list.index(character[attribute])
            
            # Using the index variable to add that to health list
            health_list[index].append(character["Health"])
    
    # Going through the health list
    for i in range(len(health_list)):
        
        # First time numpy, np is used
        # Calculating the average  of each individual index using counter i
        health_list[i] = np.mean(health_list[i])
    
    # Comparing the length of the attribute list with given degree
    if len(attribute_list) <= degree:
        
        # Setting degree value to one less than the list length
        deg = len(attribute_list) - 1
    else:
        
        # Setting degreee value to given one
        deg = degree
    
    # Using polynomial() function to fit final calculated values
    coefficients = np.polyfit(attribute_list, health_list, deg)
    
    # Creating string for beginning of expression
    expression = "y = "
    
    # Buildiing equation usinf coef() function
    for i, coef in enumerate(coefficients):
        # Creating and setting the power 
        power = len(coefficients) - i - 1
        
        # Setting the expression depending on the power
        if power > 1:
            expression += f"{coef:.2f}x^{power} + "
        elif power == 1:
            expression += f"{coef:.2f}x + "
        else:
            expression += f"{coef:.2f}"
    
    # Returning the finalized expression
    return expression


     

# What function tells you what attributes are available??
# dir()
# Use of dir():
# attributes = dir(example)
# print(attributes)

# Test you print statements once more!

     #if len(attribute_list) > (degree + 1):

     #     deg = degree

     #else:

     #     deg = len(attribute_list) - 1

     

     #coefficients = np.polyfit(attribute_list, health_list, deg)



# Do NOT include a main script in your submission



#if __name__ == "__main__":
    #print("Success")
    
  #  curve_fit([{"Stamina": 3, "Health": 7}, {"Stamina": 2, "Health": 12}, {"Health": 13, "Stamina": 2}], "Stamina", 2)
    

