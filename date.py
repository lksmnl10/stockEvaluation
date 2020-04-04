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
#z=convertDates();print(z)
def askDate():
    asker=str(str(input("Manually Input Date?")))
    print(asker)
x=askDate();print(x)