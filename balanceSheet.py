# this is for balance sheet and for annual only
def alfred(query):
    quest=input("what is the " + str(query)+ "? ")
    return quest
# 21
template=['Price',
          'OutstandingShares',
          'DividendsPerShare',
          'Inventory',
          'TotalCurrentAsset',
          'PropertyNEquipment',
          'goodwill',
          'IntangibleAsset',
          'TotalAssets',
          'ShortermDebt',
          'TotalCurrentLiabilities',
          'LongTermDebt',
          "TotalLiabilities",
          'PreferredShares',
          'TotalEquity',
          'Revenue',
          'TotalCostOfSalesOrRevenue',
          'ResearchNDevelopment',
          'SalesNMarketing',
          'GeneralNAdmin',
          'Depreciation',
          'Interests',
          'Tax']
def askLoop(list):
    listLength=len(list)
    # this is just numbers; all numbers according to the list
    emptyList=[0]*(listLength)
    for i in range(listLength):
            # asking according to the list
            delta = float(alfred(list[i]))
            emptyList[i] = delta
    modifiedList=emptyList
    return modifiedList
# hello=askLoop(template);print(hello)
def calcRatios(numList):
    #round place
    numRound=3
    # Working With List
    emptyList=[0]*14
    closingPrice = numList[0]
    outstandingShares = numList[1]
    dividendsPerShare = numList[2]
    inventory = numList[3]
    totalCurrentAsset = numList[4]
    propertyNEquipment= numList[5]
    goodwill = numList[6]
    intangibleAsset = numList[7]
    totalAssets = numList[8]
    shortermDebt = numList[9]
    totalCurrentLiabilities = numList[10]
    longTermDebt = numList[11]
    totalLiabilities = numList[12]
    preferredShares = numList[13];print(preferredShares, "preferred shares")
    totalEquity =  numList[14]
    revenue = numList[15]
    totalCostOfSalesOrRevenue = numList[16]
    researchNDevelopment = numList[17]
    salesNMarketing = numList[18]
    generalNAdmin = numList[19]
    depreciation = numList[20]
    interests = numList[21];print(interests)
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
    grossProfitRatioMargin =round((grossProfit/revenue)*100, numRound)#..................................Rate On Equity
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
def combine(template):
    # asking for values
    rawData = template #askLoop(template)
    modifiedData=calcRatios(rawData)
    return  modifiedData

lish=[147.0, 7643.0, 1.84, 2063.0, 175552.0, 36477.0,42026, 7750.0, 286556.0, 5516.0, 69420.0, 66662.0, 184226.0, 0.0, 102330.0, 125843.0, 42910.0, 16876.0, 18213.0, 4885.0, 11682.0, 729.0, 4448.0]
damn=combine(lish)
print(damn[0], "\n", damn[1])