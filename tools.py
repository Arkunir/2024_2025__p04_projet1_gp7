from data import *


def ask_for_the_init_number():
    a = input(int("Saisissez un entier"))
    return a 

def ask_for_the_init_base():
    "" = input("Saisissez la base du nombre choisie (bin, )")
    return ""

def ask_for_the_target_base ():
    "" = input("saisissez la base visée")
    return ""



def bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base):
    
    if ask_for_the_init_base() == "bin" and ask_for_the_target_base() == "decimal":
        targetnumber = bin_to_decimal (init_number)
    
      
def bin_to_decimal():
    