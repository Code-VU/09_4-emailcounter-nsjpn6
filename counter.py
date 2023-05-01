def countEmail():
    # This first line is provided for you
    # slide 28 for count
    # 
    file_name = input("Enter file:")
    if len(file_name) < 1 : file_name = "mbox-short.txt"
    fromDict = {}
    
    handle = open(file_name)
    for line in handle :
        if line.startswith("From "):
            sender = line.split()[1]
            
            if sender not in fromDict:
                fromDict[sender] = 1
            else:
                fromDict[sender] += 1

    dictVals = fromDict.values()
    maxVal = max(dictVals)

    print(max(fromDict, key=fromDict.get), maxVal)
   


    

    





        

                    
                




  
                
        

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
