alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# def encrypt(text, shift):
#   input()
    
  
  #find each letter in text - 
letter_in_text = []
text_no = len(text)
alphabet_no = len(alphabet)
letter_in_A = []
positition_in_A = []
# print(text_no)
for position in range(text_no):
  letter_in_text = text[position]
  for position_A in range(alphabet_no):
      position_in_Alphabet = alphabet[position_A]
      if letter_in_text == position_in_Alphabet:
          shift = position_A + shift
          print(alphabet[shift])
          #letter_in_text = letter in text
          #text[position] = letter position in Text
          #positition_in_A = letter position in Alphabet
          #shift = position_in_A + shift
          #print(shift)
          


    
  

  #position = alphabet[n]
  #check for each letter of text in alphabet 
  #for every n in text
  #
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 