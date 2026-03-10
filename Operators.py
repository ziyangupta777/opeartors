# Operators are special symbols to perform certain operations on operands.


# By using operators, programmers can manipulate and perform calculations on variables and values within their code.

# Types of Operators
# Below are operators that are available in Python:
# 1.Arithmetic Operators
# 2.Comparison Operators
# 3.Assignment Operators
# 4.Logical Operators
# 5.Identity Operators
# 6.Membership Operators




# Arithmetic Operators 1. + meaning add 

a=5
b=10
print(a+b)

# 2. - subtract
a=5
b=10
print(a-b)

# 3. * multiply
a=5
b=10
print(a*b)

# 4./ divide 

a=50
b=10
print(a/b)

# 5. % modulo 
a=50
b=5
print(a%b)

# 6.**  Exponentiation

a=50
b=5
print(a**b)


# 7. // floor division

a=50
b=5
print(a//b)

# Comparison Operators
#   1.   == equal 

a=20
b=20
print(a==b)

# 2.  !=  not equal

a=2
b=20
print(a!=b)

# 3. > greater than 

a=7
b=50
print(a>b)

# 4.< less than
a=70
b=50
print(a<b)

# 5. greater than and equal to 

a=50
b=50
print(a>=b)

# 6. less than and equal to 

a=30
b=50
print(a<b)

# Assignment Operators
 
a= 20     #  =Assign value
print(a)

# 2.Increment and assign +=

a=20
a+= 9
print(a)

# 4.Subtract and assign  -=
z=20
z-= 8
print(z)

# 5.Multiply and assign *=

b=30
b*= 3
print(b)

# 6.Divide and assign  /=

c=100
c/= 10
print(c)

# 7.Modulo and assign %=

c=14
c%= 3
print(c)

# 8.Floor division and assign

d=50
d//=10
print(d)

# 9.Exponentiation and assign

e=11
e**=5
print(e)

# 10 Walrus operator :=
# first normal 

z= len("hello")
if z>3:
    print(z)

    # with walrus 

if  (a :=len ("how are you")) > 5:
   print(a)
      
#   Logical Operators
#  Operator      Meaning

        # and             True if both statements are true
        
        # or              True if one of the statements is true

        # not             Reverse the result, returns False if the result is true
        

# and             True if both statements are true

A=5
B=2
print(A<B and B<A)   #false and false =false
                     #true and false =false
                     #false and true =false
                     #true and true =true 


# or              True if one of the statements is true

A=5
B=2
print(A>B or A>B)    #true and true =true
                     #true and false =true
                     #true and true =true
                     #false and false =false 
                
# not             Reverse the result, returns False if the result is true

A=True
print(not A)      # Reverse the result, returns False if the result is true



# Identity Operators

# is meaning =Returns True if both variables are the same object

a=77
b=77.00

print(a is b ) # data type and values

# is not    meaning= Returns True if both variables are not the same object

x=80
y=80.00
print(x is not y )

# Membership Operators

# in meaning ==  Returns True if a sequence with the specified value is present in the object Operator


a="ziyan" 
print("z" in a )  # true 

# not in  meaning ====Returns True if a sequence with the specified value is not present in the object

n="vaishnavi"
print("v" not in n )  #false





