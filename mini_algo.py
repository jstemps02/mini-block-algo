import sys


def sBox(pltR, key):
  if((pltR == "00" and key == "0000") or (pltR == "11" and key == "0001") or (pltR == "10" and key == "0001") or (pltR == "11" and key == "0010") or (pltR == "10" and key == "0010") or (pltR == "11" and key == "0010") or (pltR == "01" and key == "0011") or (pltR == "01" and key == "0100") or (pltR == "00" and key == "0111") or (pltR == "10" and key == "1000") or (pltR == "01" and key == "1001") or (pltR == "00" and key == "1010") or (pltR == "11" and key == "1010") or (pltR == "11" and key == "1101") or (pltR == "10" and key == "1101") or (pltR == "01" and key == "1110") or (pltR == "00" and key == "1110")):
    return "00"
  if((pltR == "00" and key == "0010") or (pltR == "10" and key == "0011") or (pltR == "11" and key == "0100") or (pltR == "00" and key == "0101") or (pltR == "01" and key == "0110") or (pltR == "01" and key == "0111") or (pltR == "11" and key == "0111") or (pltR == "01" and key == "1000") or (pltR == "00" and key == "1001") or (pltR == "10" and key == "1001") or (pltR == "00" and key == "1011") or (pltR == "11" and key == "1011") or (pltR == "10" and key == "1100") or (pltR == "01" and key == "1101") or (pltR == "11" and key == "1110") or (pltR == "10" and key == "1111")):
    return "01"
  if((pltR == "10" and key == "0000") or (pltR == "01" and key == "0000") or (pltR == "00" and key == "0001") or (pltR == "01" and key == "0010") or (pltR == "00" and key == "0100") or (pltR == "10" and key == "0101") or (pltR == "11" and key == "0101") or (pltR == "11" and key == "0110") or (pltR == "10" and key == "0111") or (pltR == "11" and key == "1000") or (pltR == "01" and key == "1011") or (pltR == "11" and key == "1100") or (pltR == "00" and key == "1100") or (pltR == "10" and key == "1110") or (pltR == "00" and key == "1111") or (pltR == "01" and key == "1111")):
    return "10"
  if((pltR == "11" and key == "0000") or (pltR == "01" and key == "0001") or (pltR == "00" and key == "0011") or (pltR == "11" and key == "0011") or (pltR == "10" and key == "0100") or (pltR == "01" and key == "0101") or (pltR == "00" and key == "0110") or (pltR == "10" and key == "0110") or (pltR == "00" and key == "1000") or (pltR == "11" and key == "1001") or (pltR == "10" and key == "1010") or (pltR == "01" and key == "1010") or (pltR == "10" and key == "1011") or (pltR == "01" and key == "1100") or (pltR == "00" and key == "1101") or (pltR == "11" and key == "1111")):
    return "11"

#this function rotates the key for the next iteration for the encryption, adding the most significant bit to the end
def round(key): 
  char = key[:1]
  rest = key[-3:]
  out = ""
  out += rest
  out += char
  return out

#this function rotates the key for the next iteration for the decryption, adding the least significant bit to the front
def roundDecrypt(key): 
  char = key[:3]
  rest = key[-1:]
  out = ""
  out += rest
  out += char
  return out  

#this function is for the encryption algorithm, it preforms the xor then the swap in one function. 
def xorAndSwap(sOut, lBlock, rBlock):
  valTo3 = int(sOut[0])
  valTo2 = int(sOut[1])
  val3 = int(lBlock[0])
  val2 = int(lBlock[1]) # takes the string values as integers
  newVal3 = valTo3 ^ val3
  newVal2 = valTo2 ^ val2 #preforms xor on them
  lblockNew = ""
  lblockNew += str(newVal3)
  lblockNew += str(newVal2)
  out = ""
  out += rBlock
  out += lblockNew
  return out

#for the decryption algorithm, this take a 4 char input and swaps the two sides
#ex: abcd -> cdab
def swap(block):
  rBlock = block[-2:]
  lBlock = block[:2]
  out = ""
  out += rBlock
  out += lBlock
  return out

#for the decryption algorithm, this takes the Sbox output values and xors them.
def xorLSide(sOut, lBlock, rBlock):
  valTo3 = int(sOut[0])
  valTo2 = int(sOut[1])
  val3 = int(lBlock[0])
  val2 = int(lBlock[1])
  newVal3 = valTo3 ^ val3
  newVal2 = valTo2 ^ val2
  lblockNew = ""
  lblockNew += str(newVal3)
  lblockNew += str(newVal2)
  out = ""
  out += lblockNew
  out += rBlock
  return out

#main encryption function that prints the output values
def encrypt(key, firstBlock):
  rBlock = firstBlock[-2:]
  lBlock = firstBlock[:2]
  newKey1 = round(key)
  sOut = sBox(rBlock, key)
  output1 = xorAndSwap(sOut, lBlock, rBlock)
  print("---ENCRYPTING---")
  print("Round 1: " + output1)
  rBlock = output1[-2:] #update rBlock and lBlock
  lBlock = output1[:2]
  newKey2 = round(newKey1)
  sOut1 = sBox(rBlock, newKey1)
  output2 = xorAndSwap(sOut1, lBlock, rBlock)
  print("Round 2: " + output2)


  rBlock = output2[-2:] #update rBlock and lBlock
  lBlock = output2[:2]
  sOut2 = sBox(rBlock, newKey2)
  output3 = xorAndSwap(sOut2, lBlock, rBlock)
  print("Round 3: " + output3)
  print("Last Key: " + newKey2)


#main decryption function that prints the output values
def decrypt(key, firstBlock):
  print("---DECRYPTING---")
  swappedBlock =swap(firstBlock)
  rBlock = swappedBlock[-2:]
  lBlock = swappedBlock[:2]
  newKey1 = roundDecrypt(key)
  sOut = sBox(rBlock, key)
  out1 = xorLSide(sOut, lBlock, rBlock) 
  print("Round 1: " + out1)


  swappedBlock =swap(out1)
  rBlock = swappedBlock[-2:]
  lBlock = swappedBlock[:2]
  newKey2 = roundDecrypt(newKey1)
  sOut = sBox(rBlock, newKey1)
  out2 = xorLSide(sOut, lBlock, rBlock) 
  print("Round 2: " + out2)

  swappedBlock =swap(out2)
  rBlock = swappedBlock[-2:]
  lBlock = swappedBlock[:2]
  sOut = sBox(rBlock, newKey2)
  out3 = xorLSide(sOut, lBlock, rBlock) 
  print("Round 3: " + out3)
  


def main():
  if __name__=="__main__": 
            main()
exitToF = False
while exitToF == False: #infinite loop until q is input
  var = input("enter e for encrypt, d for decrypt, or q to exit: ")
  if var == 'q':
    exitToF == True
    exit() #exits if q is input
  
  elif var == 'e':
    mainBlock = input("Enter input(4bit): ")
    key = input("Enter key(4bit): ")    
    encrypt(key, mainBlock) # if e is input, runs the encryption algorithm

  else: 
    mainBlock = input("Enter input(4bit): ")
    key = input("Enter key(4bit): ")
    decrypt(key, mainBlock) # if d is input, runs the decryption algorithm
    