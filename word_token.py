from nltk.tokenize import sent_tokenize, word_tokenize
import array
inputStr = "Sau trận hòa trước tuyển Việt Nam, ĐT Thái Lan nhập cuộc với khí thế rất cao trên sân của Indonesia."\
    "Ở hàng công, HLV Nishino quyết định tăng cường hỏa lực với mũi nhọn Supachai Jaided."

arrToken = word_tokenize(inputStr)

keys4 = []
keys3 = []
keys2 = []
keys1 = []
with open('vnDictionary.txt', encoding="utf8") as fileData:
    for line in fileData:
        if len(line.split(" ")) == 4:
            keys4.append(line.split("\n")[0])
        if len(line.split(" ")) == 3:
            keys3.append(line.split("\n")[0])
        if len(line.split(" ")) == 2:
            keys2.append(line.split("\n")[0])
        if len(line.split(" ")) == 1:
            keys1.append(line.split("\n")[0])

print("1 word length: ", len(keys1), "character")
print("2 word length: ", len(keys2), "character")
print("3 word length: ", len(keys3), "character")
print("4 word length: ", len(keys4), "character")

result = []
i = 0
while len(arrToken) -i > 0:
    if len(arrToken) -i >= 4:
        singleWord = " ".join(arrToken[i:i+4]).lower()
        if singleWord in keys4:
            result.append("_".join(arrToken[i:i+4]))
            i+= 4
            continue

    if len(arrToken) -i >= 3:
        singleWord = " ".join(arrToken[i:i+3]).lower()
        if singleWord in keys3:
            result.append("_".join(arrToken[i:i+3]))
            i+= 3
            continue

    if len(arrToken) -i >= 2:
        singleWord = " ".join(arrToken[i:i+2]).lower()
        if singleWord in keys2:
            result.append("_".join(arrToken[i:i+2]))
            i+= 2
            continue

    if len(arrToken) -i >= 1:
        singleWord = " ".join(arrToken[i:i+1]).lower()
        if singleWord in keys1:
            result.append("_".join(arrToken[i:i+1]))
            i+= 1
            continue
        else:
            result.append(str(arrToken[i]))
            i += 1
            
print("Result using longest matching: ", result)






