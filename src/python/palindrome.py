# program for Palindrome
def palindrom (input):
   input.upper()
   reverse=input[::-1]
   if input == reverse:
      print ("this is a palindrome")

   else:
      print ("this is not a palindrome")

print(palindrom("Apoorva"))
print (palindrom("Madam"))

         

    
         

   