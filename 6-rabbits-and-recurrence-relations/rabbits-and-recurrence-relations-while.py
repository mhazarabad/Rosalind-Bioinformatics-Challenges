
def Weighted_Fibonachi_Calculator(weight:int,idx:int)->int:
    """
    
    ## params
        idx: an integer represent 
            - no need to be lower than 1999
        weight: an integer corresponds for the number of pair rabbits that will produced from re-productive rabbits (at least 1 month old)
    
    """
    current_fibonachi=2
    re_production_age=1
    not_re_production_age=1
    current_count=1
    while current_fibonachi<idx:
        re_production_age=not_re_production_age
        not_re_production_age=current_count
        current_count=(re_production_age*weight)+not_re_production_age
        current_fibonachi+=1
    
    return current_count

print(Weighted_Fibonachi_Calculator(
    idx=8,weight=3
))
