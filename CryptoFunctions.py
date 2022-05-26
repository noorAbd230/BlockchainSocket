from hashlib import sha256


def getPreviousHash(currentIndex, arrayOfValues):
   if (currentIndex == 0):
      return "0" * 64
   else:
      array = arrayOfValues[currentIndex - 1]
      return array[1]


def returnBlock(arrayIndex, arrayOfValues):
   arraySubsection = arrayOfValues[arrayIndex]     
   newValue =  ("Block Number: " + str(arraySubsection[0]) +      
   "\nHash: " + str(arraySubsection[1]) + "\nPrevious: "                
   + str(arraySubsection[2]) + "\nTransactional Data: " +  
   str(arraySubsection[3]) + "\nNonce: " + 
   str(arraySubsection[4]) + "\nTimestamp: " +      
   str(arraySubsection[5]) + "\n")
   return (newValue)


def setHash(*args):
   hashing_text = ""
   hashing = sha256()
   for arg in args: 
        hashing_text += str(arg)
   hashing.update(hashing_text.encode('utf-8'))
   return hashing.hexdigest()   


def mine(transactions, nonce, hash, number, previous_hash, timestamp, currentIndex, diff):
    while (hash[:diff] != "0" * diff):
      nonce += 1
      hash = setHash(transactions,timestamp,previous_hash, nonce,    
      number)
    return (nonce, hash)   


def newTransactionData(sender, recipient, amount, values):
    values.extend([sender, recipient, amount])
    return values  


def verifyChain (arrayOfValues, lengthData):
   if (lengthData > 1):        
      for x in range(lengthData-1):            
          currentArray = arrayOfValues[x]            
          secondaryArray = arrayOfValues[x+1]            
          if (currentArray[1] == secondaryArray[2]):                    
             continue            
          else:                
             return(False)     
   return (True)      



def runData(currentIndex, transactions, timestamp, previous_hash, nonce, number, arrayOfValues, diff):
    previous_hash = getPreviousHash(currentIndex, arrayOfValues)
    hash = setHash(transactions, timestamp, previous_hash, nonce, 
     number)
    nonce, hash = mine(transactions, nonce, hash, number,   
     previous_hash, timestamp, currentIndex, diff)
    arrayOfValues = [number, hash, previous_hash, transactions,     
     nonce, timestamp]
    number += 1
    return arrayOfValues, number   