def binary_to_decimal(binary):
    binary = str(binary)  # Ensure binary is a string
    decimal = 0
    
    # Vérification des chiffres non valides
    for bit in binary:
        if bit not in ['0', '1']:
            print("Erreur : le chiffre '{}' n'est pas un chiffre binaire valide.".format(bit))
            return None
    
    # Conversion binaire-décimale
    for i, bit in enumerate(binary):
        if bit == '1':
            decimal += 2 ** (len(binary) - 1 - i)
    
    return decimal

def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def decimal_to_hexadecimal(decimal):
    if decimal is None:
        return None
    decimal = int(decimal)
    hexadecimal = ''
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
        decimal //= 16
    return hexadecimal

def hexadecimal_to_decimal(hexadecimal):
    decimal = 0
    for i, char in enumerate(reversed(hexadecimal)):
        if char.isdigit():
            decimal += int(char) * (16 ** i)
        else:
            decimal += (ord(char) - ord('A') + 10) * (16 ** i)
    return decimal

def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    if decimal is None:
        return None
    return decimal_to_hexadecimal(decimal)

def hexadecimal_to_binary(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    if decimal is None:
        return None
    return decimal_to_binary(decimal)

#binary ou hexadecimal ou decimal = 'nombre'
#basevoulue en résultat = base départ_to_base voulue(base de départ)
#print(base voulue)
binary = '1211'
decimal = binary_to_decimal(binary)
print(decimal)