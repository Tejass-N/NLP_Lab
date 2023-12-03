# ASSIGNMENT NO : 5
# NAME: Tejas Dilip Nagare 
# ROLL NO: 40
# Regular Expression for URL's,ip addresses,PAN number and Dates.

import re

#Regular Expression
def find_entities(text):

    result = {
        'URLs': re.findall(r'https?://\S+|www\.\S+', text),
        'IP Addresses': re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text),
        'Dates': re.findall(r'([1-9]|[12][0-9]|3[01])\/(0[1-9]|1[1,2])\/(19|20)\d{2}', text),
        'PAN Numbers': re.findall(r'[A-Z]{5}[0-9]{4}[A-Z]', text),
    }
    return result

# INPUT:
text = """
First Dataset:
Visit our website at https://www.google.com.
For support, contact us at support@example.com.
IP address: 192.168.0.2
Date: 27/11/2023
PAN number: GIWPM3635J

Second Dataset:
Visit our website at https://www.youtube.com.
For more info connect with  info@example.com.
IP address: 192.168.9.5
Date: 25/11/2023
PAN number: HYZIW9885K

Third Dataset:
Visit our website at https://www.netflix.com.
For more info connect with  customer@example.com.
IP address: 192.168.9.5
Date: 26/10/2023
PAN number: SKAYT6542D
"""

r = find_entities(text)

for entity_type, entities in r.items():
    print(f"{entity_type}: {entities}")


#OUTPUT:
   # URLs: ['https://www.google.com.', 'https://www.youtube.com.', 'https://www.netflix.com.']
   # IP Addresses: ['192.168.0.2', '192.168.9.5', '192.168.9.5']
   # Dates: [('27', '11', '20'), ('25', '11', '20')]
   # PAN Numbers: ['GIWPM3635J', 'HYZIW9885K', 'SKAYT6542D']
