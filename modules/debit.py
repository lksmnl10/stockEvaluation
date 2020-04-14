import essentials,savings#, stockPortfolio, writeFiles#, credit,
#--------------------------------------------------------------------------------------------------------------------------------------------

#using=essentials.askLoop(templateCheque);print(using)
def listCheque():
    templateCheque = ["Date", "Category", "Reason", "ConfirmationNumber", "TAN","CM", "BNS"]
    return templateCheque

def payment(list):
    (tangerine,simplii,scotiabank)=(4,5,6)
    modifiedList=[0]*len(list);change=0
    modifiedList[0]=essentials.checkDate()
    modifiedList[3] = essentials.singleAsk(list[3])
    nonSinglePayment=str(input("is it NON-singleTransaction? Y/N")); nonSinglePayment=nonSinglePayment.capitalize();nonSinglePayment=nonSinglePayment[0]
    if nonSinglePayment=="Y":
        # LOOP
        for i in range(3):
            change = round(float(essentials.singleAsk(list[i + 4])), 2)
            modifiedList[i + 4] = change
        (TAN, CM, BNS) = (0, 0, 0)
    else:
        # LOOP
        #single loop
        for i in range(3):
            if list[i + 4] == "Tangerine":
                change = round(float(essentials.singleAsk(list[i + 4])), 2)
                modifiedList[i + 4] = change
            # LOOP
            elif change > 0:
                modifiedList[i + 4] = 0
            else:
                change = round(float(essentials.singleAsk(list[i + 4])), 2)
                modifiedList[i + 4] = change
        if modifiedList[4] >0:
            #savings reference
            (TAN, CM, BNS)=(4,0,0);ref=TAN
            modifiedList[1]="CC Payment"
            modifiedList[2]="TAN Payment"
            change=modifiedList[4]
        elif modifiedList[5] >0:
            # savings reference
            (TAN, CM, BNS)=(0,5,0);ref=CM
            modifiedList[1]="CC Payment"
            modifiedList[2]="CM Payment"
            change = modifiedList[5]
        elif modifiedList[6]>0:
            # savings reference
            (TAN, CM, BNS)=(0,0,10);ref=BNS
            modifiedList[1]="CC Payment"
            modifiedList[2]="BNS Payment"
            change = modifiedList[6]
    #changing savings list
    modSavingList=[0]*len(savings.listSA())
    for i in range(4):
        modSavingList[i]= modifiedList[i]
    modSavingList[ref]=-1*change
    return modifiedList,modSavingList

def transfer(list):
    modifiedList=[0]*len(list);change=0
    modifiedList[0]=essentials.checkDate()
    modifiedList[3] = essentials.singleAsk(list[3])
    # LOOP
     #single loop
    for i in range(3):
        if list[i + 4] == "TAN":
            change = round(float(essentials.singleAsk(list[i + 4])), 2)
            modifiedList[i + 4] = change
            # LOOP
        elif change > 0:
            modifiedList[i + 4] = 0
        else:
            change = round(float(essentials.singleAsk(list[i + 4])), 2)
            modifiedList[i + 4] = change
    if modifiedList[4] >0:
        #savings reference
        (TAN, CM, BNS)=(4,0,0);ref=TAN
        modifiedList[1]="Transfer"
        modifiedList[2]="TAN Movement"
        change=modifiedList[4]
    elif modifiedList[5] >0:
            # savings reference
        (TAN, CM, BNS)=(0,5,0);ref=CM
        modifiedList[1]="Transfer"
        modifiedList[2]="CM Movement"
        change = modifiedList[5]
    elif modifiedList[6]>0:
            # savings reference
        (TAN, CM, BNS)=(0,0,10);ref=BNS
        modifiedList[1]="Transfer"
        modifiedList[2]="BNS Movement"
        change = modifiedList[6]
    #changing savings list
    modSavingList=[0]*len(savings.listSA())
    for i in range(4):
        modSavingList[i]= modifiedList[i]
    modSavingList[ref]=-1*change
    return modifiedList,modSavingList

def eTransfer(list):
    modifiedList=[0]*len(list);change=0
    modifiedList[0]=essentials.checkDate()
    modifiedList[3] = essentials.singleAsk(list[3])
    # LOOP
     #single loop
    for i in range(3):
        if list[i + 4] == "Tangerine":
            change = round(float(essentials.singleAsk(list[i + 4])), 2)
            modifiedList[i + 4] = change
            # LOOP
        elif change > 0:
            modifiedList[i + 4] = 0
        else:
            change = round(float(essentials.singleAsk(list[i + 4])), 2)
            modifiedList[i + 4] = change
    if modifiedList[4] >0:
        #savings reference
        (TAN, CM, BNS)=(4,0,0);ref=TAN
        modifiedList[1]="Transfer"
        modifiedList[2]="TAN Movement"
        change=modifiedList[4]
    elif modifiedList[5] >0:
            # savings reference
        (TAN, CM, BNS)=(0,5,0);ref=CM
        modifiedList[1]="Transfer"
        modifiedList[2]="CM Movement"
        change = modifiedList[5]
    elif modifiedList[6]>0:
            # savings reference
        (TAN, CM, BNS)=(0,0,10);ref=BNS
        modifiedList[1]="Transfer"
        modifiedList[2]="BNS Movement"
        change = modifiedList[6]
    #changing savings list
    modSavingList=[0]*len(listCheque())
    for i in range(4):
        modSavingList[i]= modifiedList[i]
    modSavingList[ref]=-1*change
    return modifiedList,modSavingList
list=listCheque()
c=transfer(list);print(c)