def areFollowingPatterns(strings, patterns):
    shash,phash={},{}
    for i in range(len(strings)):
        if strings[i] in shash:
            shash[strings[i]]=shash[strings[i]]+[i]
        else:
            shash[strings[i]]=[i]
            

    for j in range(len(patterns)):
        if patterns[j] in phash:
            phash[patterns[j]]=phash[patterns[j]]+[j]
        else:
            phash[patterns[j]]=[j]
    
    for v in shash.values():
        for w in phash.values():
            if (len(v)>1 and v not in phash.values()) or (len(w)>1 and w not in shash.values()):
                    return False
    return True
