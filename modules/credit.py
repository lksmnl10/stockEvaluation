import essentials#, credit, debit, stockPortfolio
#--------------------------------------------------------------------------------------------------------------------------------------------
def ccList():
    purchaseCC = ["Date", "Category", "Reason", "BNS-AMEX", "TD-Visa", "Tangerine-MC"]  # ,"Due"
    templateCCpayment = ["Date", "Category", "Reason","ConfirmationNumber", "BNS-AMEX", "TD-Visa", "Tangerine-MC"]
    return purchaseCC , templateCCpayment



def purchase(list):
    simultaenous = str(essentials.singleAsk("simultaenous?"));simultaenous=simultaenous.capitalize();simultaenous[0]
    modifiedList=[0]*len(list);change=0
    for i in range(len(list)):
        #string
        if i<4:
            if list[i]=="Date":
                modifiedList[i]=essentials.checkDate()
            else:
                modifiedList[i]=str(essentials.singleAsk(list[i]))
        else:
        #non strings
        # first CC
            if list[i]=="BNS-AMEX":
                change=round(float(essentials.singleAsk(list[i])), 2)
                modifiedList[i] = change
            #LOOP
            elif change>0:
                modifiedList[i] = 0
            else:
                change=round(float(essentials.singleAsk(list[i])), 2)
                modifiedList[i] = change
    return modifiedList


y=ccList()[0]
x=purchase(y);print(x)
