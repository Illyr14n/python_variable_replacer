import re
import string

# Sample PowerShell script
powershell_script = input("Paste your payload ")

# Dictionary to store the consistent replacement strings
replacement_dict = {}
alphabet = string.ascii_uppercase

# Regular expression to match PowerShell variables
pattern = r'(\$[a-zA-Z_][a-zA-Z0-9_]*)'

# Function to replace PowerShell variables with consistent strings
def replace_variables_with_consistent_strings(script):
    matches = re.finditer(pattern, script)
    for match in matches:
        variable = match.group(0)
        if variable not in replacement_dict:
            if len(replacement_dict) < 26:
                replacement_dict[variable] = '$' + alphabet[len(replacement_dict)] * 30  # You can change the number of characters here
            else:
                # If more than 26 variables, use numbers
                replacement_dict[variable] = '$' + str(len(replacement_dict) - 25) * 30  # You can change the number of characters here
        script = script.replace(variable, replacement_dict[variable])
    return script

enhanced_script = replace_variables_with_consistent_strings(powershell_script)
print(enhanced_script)
