import time
import CryptoFunctions

diff = 3
nonce = 0
number = 1
arrayOfValues = []
currentArray = []
currentIndex = 0
previous_hash = "0" *64


senderData = ["Sender_One", "Sender_Two", "Sender_Three", "Sender_Four", "Sender_Five"]
recipientData = ["Recieve_One", "Recieve_Two", "Recieve_Three", "Recieve_Four", "Recieve_Five"]
amountData = ["1", "2", "3", "4", "5"]
transactionIndex = 0


class BlockValue:

    def __init__(self, index, transactions, timestamp, previous_hash, number, transactionIndexUpdated):
        self.index = index
        self.transactions = transactions 
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.number = number
        self.transactionIndex = transactionIndexUpdated


    def new_data(self):
        timestamp = time.time()
        transactions = CryptoFunctions.newTransactionData(    
        senderData[self.transactionIndex],     
        recipientData[self.transactionIndex],
        amountData[self.transactionIndex], [])
        currentArray, number = CryptoFunctions.runData(self.index, 
        transactions, timestamp, previous_hash, nonce, self.number,     
        arrayOfValues,diff)
        
        return currentArray, number

 

class main:
    for value in range(len(senderData)):
     
      genisisBlock = BlockValue(currentIndex, [], time.time(), 
      "0" * 64, number, transactionIndex)
      
      currentArray, number = genisisBlock.new_data()
    arrayOfValues.append(currentArray)
    print(CryptoFunctions.returnBlock(currentIndex,  
      arrayOfValues))
    currentIndex += 1
    transactionIndex += 1
    print(CryptoFunctions.verifyChain(arrayOfValues,   
    len(senderData)))     

main()
if __name__ == '__main__':
   main()


     