def tax(filing_status, income):
    if filing_status == 'single':
        if (income <= 9275):
            return (income * 0.1)
        if ((income > 9275) and (income <= 37650)):
            return (9275* 0.1 + (income - 9276)*0.15)
        if ((income > 37650) and (income <= 91150)):
            return (9275* 0.1 + (37650 - 9276)*0.15)+ (income - 37651)* 0.25 
        if ((income > 91151) and (income <= 190150)):
            return (9275* 0.1 + (37650 - 9276)*0.15)+ (91150 - 37651)* 0.25 + (income - 91151)*0.28
        if ((income > 190151) and (income <= 413350)):
            return (9275* 0.1 + (37650 - 9276)*0.15)+ (91150 - 37651)* 0.25 + (190150 - 91151)*0.28 + (income - 190151)* 0.33
        if ((income > 413351) and (income <= 415050)):
            return (9275* 0.1 + (37650 - 9276)*0.15)+ (91150 - 37651)* 0.25 + (190150 - 91151)*0.28 + (413350 - 190151)* 0.33 + (income - 413351)* 0.35
        if (income >= 415051):
            return (9275* 0.1 + (37650 - 9276)*0.15)+ (91150 - 37651)* 0.25 + (190150 - 91151)*0.28 + (413350 - 190151)* 0.33 + (415050 - 413351)* 0.35 + (income - 415051)* 0.396                                                                                                
    if filing_status == 'married filing jointly':
        if (income <= 18550):
            return (income * 0.1)
        if ((income > 18550) and (income <= 75300)):
            return (18550* 0.1 + (income - 18550)*0.15)
        if ((income > 75301) and (income <= 151900)):
            return (18550* 0.1 + (75300 - 18551)*0.15)+ (income - 75301)* 0.25
        if ((income > 151901) and (income <= 231450)):
            return (18550* 0.1 + (75300 - 18551)*0.15)+ (151900 - 75301)* 0.25 + (income - 151901)*0.28 
        if ((income > 231451) and (income <= 413350)):
            return (18550* 0.1 + (75300 - 18551)*0.15)+ (151900 - 75301)* 0.25 + (2321451 - 154901)*0.28 + (income - 231451)* 0.33
        if ((income > 413351) and (income <= 466950)):
            return (18550* 0.1 + (75350 - 18551)*0.15)+ (151900 - 75301)* 0.25 + (231451 - 154901)*0.28 + (413350 - 231451)* 0.33 + (income - 413351)* 0.35
        if (income >= 466951):
            return (18550* 0.1 + (75350 - 18551)*0.15)+ (151900 - 75301)* 0.25 + (231451 - 154901)*0.28 + (413350 - 231451)* 0.33 + (466950 - 413351)* 0.35 + (income - 466951)* 0.396
    if filing_status == 'widower':
        if (income <= 18550):
            return (income * 0.1)
        if ((income > 18550) and (income <= 75300)):
            return (18550* 0.1 + (income - 18550)*0.15)
        if ((income > 75301) and (income <= 151900)):
            return (18550* 0.1 + (75300 - 18551)*0.15)+ (income - 75301)* 0.25
        if ((income > 151901) and (income <= 231450)):
            return (18550* 0.1 + (75300 - 18551)*0.15)+ (151900 - 75301)* 0.25 + (income - 151901)*0.28
        if ((income > 231451) and (income <= 413350)):
            return (18550* 0.1 + (75300 - 18551)*0.15)+ (151900 - 75301)* 0.25 + (2321451 - 154901)*0.28 + (income - 231451)* 0.33
        if ((income > 413351) and (income <= 466950)):
            return (18550* 0.1 + (75350 - 18551)*0.15)+ (151900 - 75301)* 0.25 + (231451 - 154901)*0.28 + (413350 - 231451)* 0.33 + (income - 413351)* 0.35
        if (income >= 466951):
            return (18550* 0.1 + (75350 - 18551)*0.15)+ (151900 - 75301)* 0.25 + (231451 - 154901)*0.28 + (413350 - 231451)* 0.33 + (466950 - 413351)* 0.35 + (income - 466951)* 0.396   
    if filing_status == 'married filing separately':
        if (income <= 9275):
            return (income * 0.1)
        if ((income > 9275) and (income <= 37650)):
            return (9275* 0.1 + (income - 9276)*0.15)
        if ((income > 37650) and (income <= 75950)):
            return (9275* 0.1 + (37650 - 9276)*0.15)+ (income - 37651)* 0.25
        if ((income > 76951) and (income <= 115725)):
            return (9275* 0.1 + (37650 - 9276)*0.15)+ (76950 - 37651)* 0.25 + (income - 76951)*0.28
        if ((income > 115726) and (income <= 206675)):
            return (9275* 0.1 + (37650 - 9276)*0.15)+ (76950 - 37651)* 0.25 + (115725 - 76951)*0.28 + (income - 115726)* 0.33
        if ((income > 206676) and (income <= 233475)):
            return (9275* 0.1 + (37650 - 9276)*0.15)+ (76950 - 37651)* 0.25 + (115725 - 76951)*0.28 + (206765 - 115725)* 0.33 + (income - 206676)* 0.35
        if (income >= 233476):
            return (9275* 0.1 + (37650 - 9276)*0.15)+ (76950 - 37651)* 0.25 + (115725 - 76951)*0.28 + (206765 - 115725)* 0.33 + (233475 - 206676)* 0.35 + (income - 233476)* 0.396                                                                                              
    if filing_status == 'Head of Household' : 
        if (income <= 13250):
            return (income * 0.1)
        if ((income > 13251) and (income <= 50400)):
            return (13250* 0.1 + (income - 13251)*0.15)
        if ((income > 50401) and (income <= 130150)):
            return (13250* 0.1 + (50400 - 13251)*0.15)+ (income - 50400)* 0.25
        if ((income > 130151) and (income <= 210800)):
            return (13250* 0.1 + (50400 - 13251)*0.15)+ (130150 - 50401)* 0.25 + (income - 130151)*0.28
        if ((income > 210801) and (income <= 413350)):
            return (13250* 0.1 + (50400 - 13251)*0.15)+ (130150 - 50401)* 0.25 + (210800 - 130151)*0.28 + (income - 210801)* 0.33
        if ((income > 413351) and (income <= 441000)):
            return (13250* 0.1 + (50400 - 13251)*0.15)+ (130150 - 50401)* 0.25 + (210800 - 130151)*0.28 + (413350 - 210801)* 0.33 + (income - 413351)* 0.35
        if (income >= 441001):
            return (13250* 0.1 + (50400 - 13251)*0.15)+ (130150 - 50401)* 0.25 + (210800 - 130151)*0.28 + (413350 - 210801)* 0.33 + (441000 - 413351)* 0.35 + (income - 441001)* 0.396                                                                            
def is_valid(filing_status, income):      
    if (income <0 ):
        return False
    elif((filing_status != "single") and 
        (filing_status != "married filing jointly")and
        (filing_status != "widower") and 
        (filing_status != "married filing separately") and 
        (filing_status != "Head of Household")):
        return False
    return True  
def percent_of_income(tax, income): 
    return tax/income * 100
def main(filing_status, income):
    if is_valid(filing_status, income):
        tax_value = tax(filing_status, income)
        percent_value = percent_of_income(tax_value, income)
        print("tax: $" + str(tax_value))
        print("%" + (str(percent_value)))
    else: 
        print("invalid filing status")
        print("income must be greater than or equal to zero")  
filing_status = input('what is your filing status?:')
income = int(input('How much did you make last year?:'))  

main(filing_status, income)


