def anagram(s1,s2):
    count = [0] * 26
    for i in s1: 
        count[ord(i) - ord('a')] += 1
    for i in s2: 
        count[ord(i) - ord('a')] -= 1
    return sum(map(abs,count)) 
  
    
if __name__=="__main__":
    s1=raw_input()
    s2=raw_input()
    anagram(s1,s2)