def bankRequests(accounts, requests):
    
    for i in range(len(requests)):
        r = list(requests[i].split(" "))

        if r[0] == "withdraw":
            if int(r[1])-1 not in range(len(accounts)) or accounts[int(r[1])-1]-int(r[2]) < 0:
                return [-i-1]
            accounts[int(r[1])-1] = accounts[int(r[1])-1]-int(r[2])
        elif r[0] == "transfer":
            if int(r[1])-1 not in range(len(accounts)) or int(r[2])-1 not in range(len(accounts)) or accounts[int(r[1])-1]-int(r[3]) < 0:
                return [-i-1]
            accounts[int(r[1])-1] = accounts[int(r[1])-1]-int(r[3])
            accounts[int(r[2])-1] = accounts[int(r[2])-1]+int(r[3])
        else:
            if int(r[1])-1 not in range(len(accounts)):
                return [-i-1]
            accounts[int(r[1])-1] = accounts[int(r[1])-1]+int(r[2])
    
    return accounts