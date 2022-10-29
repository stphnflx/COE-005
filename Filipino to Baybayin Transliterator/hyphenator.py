consonant="qwrtypsdfghjklzxcvbnm"
vowels="aeiou"

def hyphenate(word):
    pantig=""
    word = word.lower()
    i = len(word)       
    sy=""
    ii=0
    sylla=[]
    c=0
    for letter in word:
        
        if letter =="e":
            letter="i"

        if letter =="o":
            letter ="u"
            
        if letter =="c":
            letter="k"
            
        if letter =="z":
            letter="s"
            
        if letter =="f":
            letter="p"
            
        sy=sy+letter

        if letter in vowels and i!=len(word):
            sylla.append(sy) 
            sy=""
            i=i-2            
            c=0
            
        elif letter in vowels:
            sylla.append(sy)
            sy=""
            i=i-1            
            c=0
        if letter in consonant:
            c= c+1
            
            
            
            if c==1 and ii==len(word)-1:
                
                sylla.append(sy)
                sy=""
                c=0
           
            if c==2 and ii==len(word)-1:
                    
                    sylla.append(sy)
                    sy=""
                    c=0
                    
            if ii !=len(word)-1 and word[ii+1] in consonant and word[ii+1] !="g":
                
                sylla.append(sy)
                sy=""
                c=0
                
        ii=ii+1

   # for element in sylla:
   #     if element in special:
    #        sylla.remove(element)
    return(sylla)

