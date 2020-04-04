# this is for balance sheet and for annual only
def alfred(query):
    quest = input("what is the " + str(query)+ "? ")
    return quest
# 21
template = ['Price',
          'OutstandingShares',
          'DividendsPerShare',
          'Inventory',
          'TotalCurrentAsset',
          'PropertyNEquipment',
          'goodwill',
          'IntangibleAsset-or-nonCurrentAssets',
          'TotalAssets',
          'ShortermDebt-or-TermDebt',
          'TotalCurrentLiabilities',
          'LongTermDebt',
          "TotalLiabilities",
          'PreferredShares',
          'TotalEquity-or-totalShareholderEquity',
          'TotalRevenue-or-totalNetSales-or-consolidatedStatementOfOperations-or-netEarnings',
          'TotalCostOfSalesOrRevenue-or-netOperatingExpenses',
          'ResearchNDevelopment',
          'SalesNMarketing',
          'GeneralNAdmin',
          'Depreciation',
          'Interests-from-otherincome/(expense),net',
          'Tax-or-provisionForIncomeTax']
def askLoop(list):
    listLength = len(list)
    # this is just numbers; all numbers according to the list
    emptyList = [0]*(listLength)
    for i in range(listLength):
            # asking according to the list
            delta = float(alfred(list[i]))
            emptyList[i] = delta
    modifiedList = emptyList
    return modifiedList
# hello=askLoop(template);print(hello)
def calcRatios(numList):
    #round place
    numRound = 3
    # Working With List
    emptyList = [0]*14
    closingPrice = numList[0]
    outstandingShares = numList[1]
    dividendsPerShare = numList[2]
    inventory = numList[3]
    totalCurrentAsset = numList[4]
    propertyNEquipment = numList[5]
    goodwill = numList[6]
    intangibleAsset = numList[7]
    totalAssets = numList[8]
    shortermDebt = numList[9]
    totalCurrentLiabilities = numList[10]
    longTermDebt = numList[11]
    totalLiabilities = numList[12]
    preferredShares = numList[13];#print(preferredShares, "preferred shares")
    totalEquity =  numList[14]
    revenue = numList[15]
    totalCostOfSalesOrRevenue = numList[16]
    researchNDevelopment = numList[17]
    salesNMarketing = numList[18]
    generalNAdmin = numList[19]
    depreciation = numList[20]
    interests = numList[21];#print(interests)
    tax = numList[22]

    #----------------------------------------------------- Math Calculations
    totalDividend = outstandingShares*dividendsPerShare
    otherCurrentAsset = totalCurrentAsset-inventory
    goodwillNintabgibleAsset = intangibleAsset + goodwill
    grossProfit = revenue-totalCostOfSalesOrRevenue
    SGA = salesNMarketing+generalNAdmin-depreciation
    operatingIncome = grossProfit - researchNDevelopment - depreciation - SGA#..........Operating income or profit
    EBIT = operatingIncome+ interests
    netIncome=EBIT-tax
    #------------------------------------------------------ Ratios
    # Liquidity Ratio
    currentRatio = round(totalCurrentAsset/totalCurrentLiabilities,numRound)#..................................High = Good
    quickRatio = round((totalCurrentAsset-inventory)/totalCurrentLiabilities, numRound)#.................High = Good
    # Profitibility Ratio
    grossProfitRatioMargin = round((grossProfit/revenue)*100, numRound)#..................................Rate On Equity
    operatingProfitMargin = round((operatingIncome/revenue)*100, numRound)#..............................Rate On Equity
    netProfitMargin = round((netIncome/revenue)*100,numRound)#..........................................Rate On Equity
    # Debt/Leverage Ratio
    debtToEquityRatio = round((shortermDebt + longTermDebt)/totalEquity,numRound)#......................High = Bad
    cashflowDebt = round((depreciation+netIncome)/(shortermDebt + longTermDebt),numRound)#..............High = Good
    interestsCoverage = round(EBIT/interests,numRound)#.................................................High = Good; interests= interestsIncome
    assetCoverage = round((totalAssets-goodwillNintabgibleAsset)/(shortermDebt + longTermDebt), numRound)#...............High = Good
    # Valuation
    EPSc = round(netIncome/outstandingShares,numRound)#.................................................High = Good
    PE = round(closingPrice/EPSc, numRound)#..............................................................High = Good
    BVPSa =round((totalEquity-preferredShares)/outstandingShares,numRound)#.............................High = Good (compared to closed price)
    PBV = round((closingPrice)/ BVPSa, numRound)#........................................................ High = Good
    ROE = round(netIncome/totalEquity, numRound)#........................................................High = Bad. Different Principle and same result
    emptyList[0] = currentRatio
    emptyList[1] = quickRatio
    emptyList[2] = grossProfitRatioMargin
    emptyList[3] = operatingProfitMargin
    emptyList[4] = netProfitMargin
    emptyList[5] = debtToEquityRatio
    emptyList[6] = cashflowDebt
    emptyList[7] = interestsCoverage
    emptyList[8] = assetCoverage
    emptyList[9] = EPSc
    emptyList[10] = PE
    emptyList[11] = BVPSa
    emptyList[12] = PBV
    emptyList[13] = ROE
    templateList=["currRatio",
                  "quicRatio",
                  "grossProfitRatioMargin",
                  "operatingProfitMargin",
                  "netProfitMargin",
                  "debtToEquityRatio",
                  "cashflowDebt",
                  "interestsCoverage",
                  "assetCoverage",
                  "EPSc",
                  "P/E",
                  "BVPS",
                  "P/BV",
                  "ROE"]
    return templateList, emptyList
# conversion of INT into FLOAT
def intToFloat(list):
    for i in range(len(list)):
        list[i] = float(list[i])
    return list
def evaluateManual(template):
    # asking for values
    rawData = askLoop(template)#template
    modifiedData = calcRatios(rawData)
    return  modifiedData
# automatic with given list
def evaluateAuto(template):
    intToFloat(template)
    modifiedData = calcRatios(template)
    print(modifiedData[0],modifiedData[1])
    return  modifiedData
def asker(template,list):
    ask = str(input("manual?" + "y/n ?"))
    if ask == str("y"):
        result=evaluateManual(list)
        print(result[0], "\n", result[1])
        return result
    else:
        result=evaluateAuto(list)
        print(result[0], "\n", result[1])
        return  result
#lish=[147.0, 7643.0, 1.84, 2063.0, 175552.0, 36477.0,42026, 7750.0, 286556.0, 5516.0, 69420.0, 66662.0, 184226.0, 0.0, 102330.0, 125843.0, 42910.0, 16876.0, 18213.0, 4885.0, 11682.0, 729.0, 4448.0]
#listApple=[147,7643,1.84,2063,175552,36477,42026,7750,286556,5516,69420,66662,184226,0,102330,125843,42910,16876,18213,4885,11682,729,4448]
#listAppleFloat=intToFloat(listApple)
#appleCompany=evaluateAuto(listApple);print(appleCompany[0],appleCompany[1])
#firstCompany=evaluateManual(template)#lish
#doWork=asker(template,listApple)

listCadTire=[70,
615,
4.25,
2212.9,
9555.3,
4283.3,
2414.3,
0,
19518.3,
450,
5751.4,
3730.2,
14013.6,
0,
5504.7,
14534.4,
9660.6,
0,
312.8,
3437.5,
252,
297.3,
347.9]
cadTire=evaluateAuto(listCadTire)