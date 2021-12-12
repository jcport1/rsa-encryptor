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
# solves what e (public exponent) is going to be
# by finding the high possible totient of r(phi(n))
# essentially we are performing Phi(n) % some k 
# the some k is going to be our publci exponent
# k is going to be equal to the iteration number 
def find_exponent_gcd(e,r):
    print("This is e and r before while loop: ", e, " ", r)
    # this function will until r = 0
    # since we're setting r = e % mod r, if we get 0 then e % r has no remindrs
    # e is being constantly  updated to equal what r is, so e is the reminder of e % r
    while(r!=0):
        # swap e and r simulteounsly by assiging multiple variables in one line
        # otherwise if we change the value of e or r in sequence, then we can't swap
        # could also use a temporary variable 
        e,r=r,e%r
    #     print("This is e: ", e, " and this is r: ", r)
    # print("This is my e which is the remainder of r mod num", e)
    return e
 
# Euclid's Algorithm
# The Euclidean algorithm is a method to compute the gcd of two non-zero integers, a and b. 
# computing the gcd of the public exponent and modulus n which is r  
def euclid_algo_gcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
            if(b!=0):
                print("%d = %d*(%d) + %d"%(r,a,e,b))
            r=e
            e=b

#Extended Euclidean Algorithm
# find thes gcd of 2 integers
# One of the uses of the Euclidean Algorithm is to find integer solutions to equations of the form ax + by = c. 
# Given integers a, b, and c, this is solvable (for x and y inters) whenever the gcd(a, b) divides c. 
# Recursive function
def extended_euclidean_algo(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = extended_euclidean_algo(b,a%b)
        s = s-((a//b) * t)
        print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)
 
#Multiplicative Inverse
# r = modulus number
# the modular inverse of an integer e mod r is the value of d
# such that ed = 1 mod r
# isolates d which is = k * phi(n) + 1
# another way to think about this is the muliplicative inverse
# of an integer a mod n is an integer x such that x * a mod n = 1
# we can use the eea to solve x * a + y * n = 1
# uses successive quotients 
# the inverse exists only if gcd(r, e)
def multiplicative_inverse(e,r):

    gcd,s,_=extended_euclidean_algo(e,r)
    print("This is gcd, s, _", gcd, s, _)
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
    # unpacks priv_key tuple
    # assigns tuple variable to multiple variables
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

    # Part 1:Generate Public/Private Key for Alice
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
    # n is the modulous n 
    n = p * q
    print("RSA Modulus(n) is:",n)
 
    #Eulers Toitent is also known as Phi(n), so eulers_phi
    # number of 1> coprimes less than that number
    # phi(n): counts from 1> to n, returns numbers that are copprime with n (gcd is 1)
    # clarify if 1 is included? *************
    # phi(n): phi(n) 
    # r is phi(n) = the product of (p-1) * (q-1)
    # to figure out phi(n) of a large number will take a while
    # r = is the phi(n), which can be easily figured out because the phi of a prime mumber is simply = p - 1, etc.  
    '''CALCULATION OF EULERS TOITENT 'r'.'''
    # r is also the product of the phi of modulus n (n)
    # the phi(modulus n) tells us how many numbers are coprime with modulus n
    # easy to figure out phi(modulus n) if we know what two prime numbers make up n

    # **** Another important way to think about phi(n) is that its the number of integers k
    # in range 1 <= k <= n for which the gcd(n, k) is 1
    r = (p-1)*(q-1)
    print("Phi(n)/Eulers Toitent(r) is:",r)
    print("*****************************************************")

    #Calculating Alice's exponent which is 2nd part of the public key
    # Two numbers that don't share any common factors beside one (Could be prime or nonprime?)
    # Why coprime?

    '''FINDS THE HIGHEST POSSIBLE VALUE OF 'e' BETWEEN 1 and 1000 THAT MAKES (e,r) COPRIME.'''
    # e number (public exponent) is coprime with r (phi(n)) if the only gcd of both of them is 1, 
    # thus we say e (public exponent) is coprime with n (modulus n)
    # e is 1 at start of loop
    # for number in range (1, 1000)

    # exponent_gcd(num, phi(n)) == 1 
    # the public exponenent is one of the the totatives of r (thus is it is coprime with r)
    # we're looking for the highest possible totative value of r (phi(n))
    # even if gcd(i, r) == 1, for loop forces operation to keep running for 1000 times
    # so the final e we get is the high possible totative of r(phi(n))

    # change back to range 1000
    # test numbers: 19 and 29
    for i in range(1,10):
        # essentially we are performing our function is performing: Phi(n) % some k 
        # the some k is going to be our public exponent
        # k is going to be equal to the iteration number 
        if(find_exponent_gcd(i,r)==1):
            # function returns final value of e after 10 iterations 
            # where the gcd of some k and r is ===1
         e=i

    print("The value of our public exponent e is:",e)
    print("*****************************************************")

    #d, Private and Public Keys
    '''CALCULATION OF 'd', PRIVATE KEY, AND PUBLIC KEY.'''
    print("EUCLID'S ALGORITHM:")
    # accepts paraments for public exponent and r(phi(n))
    # euclide algo is a way to compute the gcd of 2 integers
    # this is an extra function 
    euclid_algo_gcd(e,r)
    print("END OF THE STEPS USED TO ACHIEVE EUCLID'S ALGORITHM.")
    print("*****************************************************")
    print("EUCLID'S EXTENDED ALGORITHM:")

    d = multiplicative_inverse(e,r)
    print("END OF THE STEPS USED TO ACHIEVE THE VALUE OF 'd'.")
    print("The value of d is:",d)
    print("*****************************************************")

    # public, e, n, assigns both elements to a tuple
    public = (e,n)
    # private key: alices: d, n, assigns both elements to a tuple
    private = (d,n)
    print("Private Key is:",private)
    print("Public Key is:",public)
    print("*****************************************************")
 
    done = False

    # Part 2: Encrypt Message using Alice's public key(e, n) and decrpyt using private key(d, n)
    # Bob receives lock and then locks message. Send backs to Alice
    # Finally, Alice receives locked message from Bob and opens with her private key 
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