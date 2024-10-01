from data import *


# def ask_for_the_init_number():
#     a = input(int("Saisissez un entier"))
#     return a 

# def ask_for_the_init_base():
#     "" = input("Saisissez la base du nombre choisie (bin, )")
#     return ""

# def ask_for_the_target_base ():
#     "" = input("saisissez la base visée")
#     return ""

ask_for_the_init_number_text = "Par pitié donnes moi un nombre ? :"

ask_again_for_the_init_number_text = "Mauvais nombre, redonne moi un bon ! : "

bin_number_valid_chars = ["0", "1"]

dec_number_valid_chars = \
    bin_number_valid_chars \
  + ["2", "3", "4", "5", "6", "7", "8", "9"]


def check_char_number_validity (char):
    return char in hex_number_valid_chars

def is_a_valid_number (number):
    i = 0
    is_a_valid_char = True
    while is_a_valid_char == True and i <= len (number) - 1:
        is_a_valid_char = check_char_number_validity (number [i])
        i = i + 1
    return is_a_valid_char

def ask_for_the_init_number ():
    init_number = input (ask_for_the_init_number_text)
    while not (is_a_valid_number (init_number)) == True:
        init_number = input (ask_again_for_the_init_number_text)
    return init_number
        
ask_for_the_init_number ()



def bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base):
    
    if ask_for_the_init_base() == "bin" and ask_for_the_target_base() == "decimal":
        targetnumber = bin_to_decimal (init_number)
    
      
def bin_to_decimal("binary"):
    
    decimal = 0
    for i, bit in enumerate(binaire):
        if bit == '1':
            decimal += 2 ** (len(binaire) - 1 - i)
    return decimal
    
print (bin_to_decimal(10))


def ... (n, d):
    restes="" 
    q= n//d
    while q>0
        reste = n % d
        restes = reste + restes
        n=q
        q = n//2
        return restes