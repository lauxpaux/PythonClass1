print("hello world")

#naming variables
ex_var = 5
print(ex_var)
ex_var = 7
print(ex_var)


#Examples of variables
float_1= 1.34
int_1 = 74
bool_1 = True
bool_2 = False
print(bool_2)

#Examples of expressions and basic math operators
addition = 4 + 5
subtraction = 5 - 2
division = 7 / 2
multiplication = 3 * 8
exponentiation = 4 ** 4
floor_division = 16 // 5 #.2 is discarded
modulo = 7 % 3 #the remainder after the division
print(modulo)


add_assign = 5
add_assign += 7
sub = 10
sub -= 5
mult = 10
mult *= 5
div = 10
div /= 5
expo = 10
expo **= 2
floor = 10
floor //= 6
mod = 10
mod %= 7
print(expo)

#operator precedence
# 1. ()
# 2. **
# 3. %, /, //, and *
# 4. + and -
precedence = (9-7) * 2 ** 3 + 10 % 6 // -1 * 2 -1
print(precedence)

#approximation errors with floats
#floats produce approximate errors and can be avoided by using integers, example:
ex2 = (123 + 280) / 100
print(ex2)
#instead of
ex3 = 1.23 + 2.80
print(1.23 + 2.80) # this actually worked-- maybe they fixed it ?

#user round function:
print(round(ex3, 2)) #round to the second decimal point

