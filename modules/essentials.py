#--------------------------------------------------------------------------------------------------------------------------------------------
# date important
def convertDates():
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
# date?
def inputDate():
    # of course ask first
    asdf=str(input("Mannually input Date? ----Y/N-----")); asdf=asdf.capitalize()
    if asdf[0]=="Y":
        delta = str(alfred("Date ---- Jan 24, 2020"))
        return delta
    else:
        delta=convertDates()
        return delta
#--------------------------------------------------------------------------------------------------------------------------------------------
# ask loop
def alfred(query):
    # query is interchangeable
    quest = input("what is the " + str(query)+ "? ")
    return quest
# Asking in Loop
def askLoop(list):
    listLength = len(list)
    # this is just numbers; all numbers according to the list
    emptyList = [0]*(listLength)
    for i in range(listLength):
        #strings exclusive
        if list[i] == "Date":
            emptyList[i] = inputDate()
        elif list[i] == "Category":
            delta = str(alfred(list[i]))
            emptyList[i] = delta
        elif list[i] == "Reason":
            delta = str(alfred(list[i]))
            emptyList[i] = delta
        elif list[i] == "Due":
            delta = str(alfred(list[i]))
            emptyList[i] = delta
        elif list[i] == "ConfirmationNumber":
            delta = int(float(alfred(list[i])))
            emptyList[i] = delta
        else:
            if list[i] == "TAN101SA" or list[i] == "BNS-AMEX" or list[i] == "Simplii":
                delta = round(float(alfred(list[i])), 2)
                emptyList[i] = delta
            elif delta > 0:
                   list[i]=0
            # non-strings
            else:
                delta = int(float(alfred(list[i])))
                emptyList[i] = delta
    modifiedList = emptyList
    return modifiedList
#--------------------------------------------------------------------------------------------------------------------------------------------