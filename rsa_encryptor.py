'''
 CS5002: Group Final Project
 '''

import math
 
#Check if Input's are Prime
'''THIS FUNCTION AND THE CODE IMMEDIATELY BELOW THE FUNCTION CHECKS WHETHER THE INPUTS ARE PRIME OR NOT.'''
def prime_check(a):
    if(a==2):
        return True
    elif((a<2) or ((a%2)==0)):
        return False
    elif(a>2):
        for i in range(2,a):
            if not(a%i):
                return False
    return True

#GCD
'''CALCULATION OF GCD FOR 'e' CALCULATION.'''
# solves what e is

# What is the difference between this and euclid? 
def exponent_gcd(e,r):
    while(r!=0):
        # updates r becomes e & r
        e,r=r,e%r
        # e = r 
        # r = e % r
    return e
 
# Euclid's Algorithm
# The Euclidean algorithm is a method to compute the gcd of two non-zero integers, a and b. 
# what is r? 
def eugcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
            if(b!=0):
                print("%d = %d*(%d) + %d"%(r,a,e,b))
            r=e
            e=b
 
#Extended Euclidean Algorithm
# One of the uses of the Euclidean Algorithm is to find integer solutions to equations of the form ax + by = c. Given integers a, b, and c, this is solvable (for x and y inters) whenever the gcd(a, b) divides c. 
# Recursive function
def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)
 
#Multiplicative Inverse
# why this one and where? for what
def multiplicative_inverse(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return None
    else:
        if(s<0):
            print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d."%(s,s,s%r))
        elif(s>0):
            print("s=%d."%(s))
        return s%r
 

#Encryption
'''ENCRYPTION ALGORITHM.'''
def encrypt(pub_key,n_text):
    e,n=pub_key
    encryption_output =[]
    # for loop iteratates through message and encodes message from letters to numbers
    # encrypts message using public exoponent and performing mod n
    for i in n_text:
            # converts to Unicode               
            m = ord(i)
            #encrypts message()
            c=(m**e)%n
            # encrypted message appeneded to output list
            encryption_output.append(c)
    # returns encryption_ouput string
    return encryption_output
     
 
#Decryption
'''DECRYPTION ALGORITHM'''
# make variable namees more descriptive
def decrypt(priv_key,c_text):
    d,n=priv_key
    cipher_text_list=c_text.split(',')
    print("This is my value cipher_text_str", cipher_text_list, type(cipher_text_list))
    # output string 
    decrypt_message_output=''
    # variable that we're using to store the vauee of each out our decrypted element
  
    for element in cipher_text_list:
            # decrypt element(num) using d(trapdoor)
            message_element=(int(element)**d)%n
            #convert decrypted element to letter
            c=chr(message_element)
            #add decrypted element to output string
            decrypt_message_output+=c
    return decrypt_message_output
 

def main():

    # part 1:Generate Public/Private Key for Alice
    print("RSA ENCRYPTOR/DECRYPTOR")
    print("*****************************************************")
 
    #Input Prime Numbers: Alice Creates Lock
    print("PLEASE ENTER THE 'p' AND 'q' VALUES BELOW:")
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))
    print("*****************************************************")

    #Check if inputs are prime number
    check_p = prime_check(p)
    check_q = prime_check(q)

    #conditional runs if either input is fal (not a prime number)
    while(((check_p==False)or(check_q==False))):
        p = int(input("Enter a prime number for p: "))
        q = int(input("Enter a prime number for q: "))
        check_p = prime_check(p)
        check_q = prime_check(q)

    #RSA Modulus
    # n: Alice's public key 
    # find n which is equal to p * q
    # why is this significant * 1 * we still need 
    '''CALCULATION OF RSA MODULUS 'n'.'''
    n = p * q
    print("RSA Modulus(n) is:",n)
 
    #Eulers Toitent / Phi(n)
    # number of 1> coprimes less than that number
    # phi(n): counts from 1> to n, returns numbers that are copprime with n (gcd is 1)     
    # clarify if 1 is included? *************
    # phi(n): phi(n) 
    # r is phi(n) = the product of (p-1) * (q-1)
    # to figure out phi(n) of a large number will take a while
    # r = is the phi(n), whivh can be easily figured out because the phi of a prime mumber is simply = p - 1, etc.  
    '''CALCULATION OF EULERS TOITENT 'r'.'''
    r = (p-1)*(q-1)
    print("Phi(n)/Eulers Toitent(r) is:",r)
    print("*****************************************************")

    #Calculating Alice's exponent which is part of the public key
    #  Value Calculation
    # Two numbers that don't share any common factors beside one (Could be prime or nonprime?)
    # Why coprime?

    '''FINDS THE HIGHEST POSSIBLE VALUE OF 'e' BETWEEN 1 and 1000 THAT MAKES (e,r) COPRIME.'''
    # e becomes 1 at start of loop
    # for number in range (1, 1000)
    # egcd(num, phi(n)) == 1 
    for i in range(1,1000):
        if(exponent_gcd(i,r)==1):
         e=i
    print("The value of e is:",e)
    print("*****************************************************")

    #d, Private and Public Keys
    '''CALCULATION OF 'd', PRIVATE KEY, AND PUBLIC KEY.'''
    print("EUCLID'S ALGORITHM:")
    eugcd(e,r)
    print("END OF THE STEPS USED TO ACHIEVE EUCLID'S ALGORITHM.")
    print("*****************************************************")
    print("EUCLID'S EXTENDED ALGORITHM:")
    d = multiplicative_inverse(e,r)
    print("END OF THE STEPS USED TO ACHIEVE THE VALUE OF 'd'.")
    print("The value of d is:",d)
    print("*****************************************************")
    # public, e, n 
    public = (e,n)
    # private key: alices: d, n
    private = (d,n)
    print("Private Key is:",private)
    print("Public Key is:",public)
    print("*****************************************************")
 
    done = False

    # Part 2: Encrypt Message using Alice's public key(e, n) and decrpyt using private key(d, n)
    # Bob receives open lock, locks message
    # Alice receives locked message from Bob and opens with her private key 
    while (done != True):
        #Message
        message = input("What message would you like to encrypt? ")
        print("Your message is:", message)

        #Choose Encrypt or Decrypt and Print
        choose = input("Type '1' for encryption or x to exit: ")

        if(choose=='1'):
            enc_msg=encrypt(public,message)
            # converts ints in list to string
            string_ints = [str(int) for int in enc_msg]
            print("This is string ints", string_ints)
            decrypt_message = ",".join(string_ints)
            print("Your encrypted message is: ",enc_msg)

            choose = input("Type '2' for decryption or x to exit: ")
         
            if(choose=='2'):
                print("This is the private key: ", private)
                print("this is the message, message")
                print("Your decrypted message is: ", decrypt(private, decrypt_message))
                choose = input("Type any key to continue or x to exit: ")
                if (choose == "x"):
                    done = True
              
            elif(choose == "x"):
                print("Goodbye!")
                done = True  
            else:
                print("Please type a valid option")
                choose = input("Type '2' for decryption or x to exit: ")

        elif(choose=='x'):
             print("Thank you for using the RSA Encryptor. Goodbye!")
             done = True

        else:
            print("You entered the wrong option.")
            print("Please type a valid option")
            choose = input("Type '1' for encryption or x to exit: ")
            done = True 
            
main()