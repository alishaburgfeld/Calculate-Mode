#from collections import Counter             #found counter on this site: https://stackoverflow.com/questions/54472677/how-to-make-dictionary-for-number-of-occurrences-in-a-list


from optparse import Values

# Pseudo
# Create a dictionary of the occurences
# find max of the Values
# push the key(s) that match the max

def calculate_mode(list):
    counts={}
    answer=[]
    for item in list:
        if item in counts:
            counts[item]+=1
        else:
            counts[item]=1

    for key in counts:
        if counts[key]==max(counts.values()):
            answer.append(key)
    return answer

print(calculate_mode(["who", "what", "where", "who"]))
print(calculate_mode([1,2,3]))

