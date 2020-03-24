def date(today):
    #------------Month ----------------------
    #dictionary for date
    # only str for month
    monthLabel=["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"]
    # this month
    monthValue=int(today[5]+today[6])
    # Value corresponding value
    monthNumb=[1,2,3,4,5,6,7,8,9,10,11,12]
    # ASSIGNING MONTH
    monthSTR=catergoryMonth[monthValue-1]
    #-----------Year Related----------------
    year=today[0]+today[1]+today[2]+today[3]
    #-----------Day ------------------------
    day=today[8]+today[9]
    #-----------Compile Date----------------
    result=monthSTR+" " +day+","+year
    return result
# exclusively for asking
def alfred(query):
    quest=input("what is " + str(query) + "?")
    return quest
# import date
def importDate():
    #import date from datetime
    from datetime import date
    # today's date want to have a date in string format
    today = str(date.today())  # today's date 2020-03-05 format
    # print(today)
    # type(todayIs); this makes the variable give out the data type
    return today
# loop for query

def trade(list):
    today = False
    # will ask if the user records the date
    isItToday=input("Is it Today?")
    if isItToday =="Y":
        today=True
    listLength=len(list)
    # this is for new trade
    emptyList=[0]*(listLength-1)
    if today =="false":
        for i in range(listLength):
            if i < listLength - 1:
                # asking according to the list
                delta = alfred(list[i])
                emptyList[i] = delta
            else:
                PL = float(emptyList[4]) - float(emptyList[3])
        # this is to modify previous trade
        # later to come
        emptyList.append(str(PL))
        modifiedList = emptyList
        return modifiedList
    else:
        for i in range(listLength):
            if i < listLength - 1:
                # asking according to the list
                delta = alfred(list[i])
                emptyList[i] = delta
            else:
                PL = float(emptyList[4]) - float(emptyList[3])
        # this is to modify previous trade
        # later to come
        emptyList.append(str(PL))
        modifiedList = emptyList
        return modifiedList
# list1=[DO,DB,Stock,BID,ASK,SD,AD,PL]
list1=["DateOrdered","DateB","StockName","BID","ASK","AD","SD","PL"]
doing=trade(list1); print(doing)
