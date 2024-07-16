def pattern_A():
    print("*****")
    print("*   *")
    print("*   *")
    print("*****")
    print("*   *")
    print("*   *")

def pattern_B():
    print("**** ")
    print("*   *")
    print("**** ")
    print("*   *")
    print("**** ")
    print("*   *")

def pattern_C():
    print("*****")
    print("*    ")
    print("*    ")
    print("*    ")
    print("*    ")
    print("*****")

def pattern_D():
    print("**** ")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*   *")
    print("**** ")

def pattern_E():
    print("*****")
    print("*    ")
    print("*****")
    print("*    ")
    print("*****")
    print("*    ")

def pattern_F():
    print("*****")
    print("*    ")
    print("*****")
    print("*    ")
    print("*    ")
    print("*    ")

def pattern_G():
    print("*****")
    print("*    ")
    print("* ***")
    print("*   *")
    print("* ***")
    print("*****")

def pattern_H():
    print("*   *")
    print("*   *")
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")

def pattern_I():
    print("*****")
    print("  *  ")
    print("  *  ")
    print("  *  ")
    print("  *  ")
    print("*****")

def pattern_J():
    print(" *****")
    print("     *")
    print("     *")
    print("     *")
    print("*   * ")
    print(" *****")

def pattern_K():
    print("*   *")
    print("*  * ")
    print("* *  ")
    print("*  * ")
    print("*   *")
    print("*   *")

def pattern_L():
    print("*    ")
    print("*    ")
    print("*    ")
    print("*    ")
    print("*    ")
    print("*****")

def pattern_M():
    print("*   *")
    print("* * *")
    print("*  * ")
    print("*   *")
    print("*   *")
    print("*   *")

def pattern_N():
    print("*   *")
    print("*  * ")
    print("* *  ")
    print("*  * ")
    print("*   *")
    print("*   *")

def pattern_O():
    print(" *****")
    print("*   * ")
    print("*   * ")
    print("*   * ")
    print("*   * ")
    print(" *****")

def pattern_P():
    print("**** ")
    print("*   *")
    print("**** ")
    print("*    ")
    print("*    ")
    print("*    ")

def pattern_Q():
    print(" *****")
    print("*   * ")
    print("*   * ")
    print("*   * ")
    print("*  *  ")
    print(" *****")

def pattern_R():
    print("**** ")
    print("*   *")
    print("**** ")
    print("*  * ")
    print("*   *")
    print("*   *")

def pattern_S():
    print(" *****")
    print("*    ")
    print(" *****")
    print("    * ")
    print(" *****")
    print("*    ")

def pattern_T():
    print("*****")
    print("  *  ")
    print("  *  ")
    print("  *  ")
    print("  *  ")
    print("  *  ")

def pattern_U():
    print("*   *")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*   *")
    print(" *****")

def pattern_V():
    print("*   *")
    print("*   *")
    print("*   *")
    print(" * * ")
    print("  *  ")
    print("  *  ")

def pattern_W():
    print("*   *")
    print("*   *")
    print("*   *")
    print("*  * ")
    print("* *  ")
    print("*   *")

def pattern_X():
    print("*   *")
    print(" * * ")
    print("  *  ")
    print("  *  ")
    print(" * * ")
    print("*   *")

def pattern_Y():
    print("*   *")
    print(" * * ")
    print("  *  ")
    print("  *  ")
    print("  *  ")
    print("  *  ")

def pattern_Z():
    print("*****")
    print("    *")
    print("   * ")
    print("  *  ")
    print("*****")

def print_pattern(n):
    if n.upper() == 'A':
        pattern_A()
    elif n.upper() == 'B':
        pattern_B()
    elif n.upper() == 'C':
        pattern_C()
    elif n.upper() == 'D':
        pattern_D()
    elif n.upper() == 'E':
        pattern_E()
    elif n.upper() == 'F':
        pattern_F()
    elif n.upper() == 'G':
        pattern_G()
    elif n.upper() == 'H':
        pattern_H()
    elif n.upper() == 'I':
        pattern_I()
    elif n.upper() == 'J':
        pattern_J()
    elif n.upper() == 'K':
        pattern_K()
    elif n.upper() == 'L':
        pattern_L()
    elif n.upper() == 'M':
        pattern_M()
    elif n.upper() == 'N':
        pattern_N()
    elif n.upper() == 'O':
        pattern_O()
    elif n.upper() == 'P':
        pattern_P()
    elif n.upper() == 'Q':
        pattern_Q()
    elif n.upper() == 'R':
        pattern_R()
    elif n.upper() == 'S':
        pattern_S()
    elif n.upper() == 'T':
        pattern_T()
    elif n.upper() == 'U':
        pattern_U()
    elif n.upper() == 'V':
        pattern_V()
    elif n.upper() == 'W':
        pattern_W()
    elif n.upper() == 'X':
        pattern_X()
    elif n.upper() == 'Y':
        pattern_Y()
    elif n.upper() == 'Z':
        pattern_Z()
    else:
        print("Invalid input")

n = input("Enter a letter: ")
print_pattern(n)