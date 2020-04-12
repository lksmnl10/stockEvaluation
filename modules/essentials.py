#--------------------------------------------------------------------------------------------------------------------------------------------
# ask
def singleAsk(query):
    # query is interchangeable
    quest = input("what is the " + str(query)+ "? ")
    return quest
# Asking in Loop
def askLoop(list,type):
    listLength = len(list)
    modifiedList = [0]*(listLength)
    # query is interchangeable
    for i in range(listLength):
        modifiedList[i]=singleAsk(list[i])
    return modifiedList
#--------------------------------------------------------------------------------------------------------------------------------------------
# date important
def autoDate():
    # import
    from datetime import date
    date = date.today()
    # data converted to str and chopped
    date=str(date);month=date[5]+date[6]# month == '03' something like that
    toDate=date[8]+date[9]
    index=["01","02","03","04","05","06","07","08","09","10","11","12"]
    replacement = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    realDate=""
    for i in range(12):
        # checking if the month maches then replaces with the letter month
        if month==index[i]:
            realDate+=replacement[i]      # replaces the number month with the letter month
            realDate+=" " + toDate + ", " # adds space, today, coma, and space respectively
            for i in range(4):            # adds the year
                realDate += date[i]
            return realDate
# manual date or automatic Date?
def checkDate():
    # of course ask first
    quest=str(input("Mannually input Date? ----Y/N-----")); quest=quest.capitalize()
    if quest[0]=="Y":
        delta = str(singleAsk("Date? ---- Jan 24, 2020 -----------"))
        return delta
    else:
        delta=autoDate()
        return delta
#--------------------------------------------------------------------------------------------------------------------------------------------
