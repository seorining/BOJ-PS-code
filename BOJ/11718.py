printWord = []

while True:
    try: 
        printWord.append(input())
    except:
        break
    
print(*printWord, sep='\n')