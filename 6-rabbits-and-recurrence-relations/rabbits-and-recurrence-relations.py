calculated_fibonachies={1:1,2:1}
def Weighted_Fibonachi_Calculator(weight:int,idx:int)->int:
    """
    
    ## params
        idx: an integer represent 
            - this param must be lower than 1999
        weight: an integer corresponds for the number of pair rabbits that will produced from re-productive rabbits (at least 1 month old)
    
    """
    re_production_age=calculated_fibonachies.get(idx-2)
    if not re_production_age:
        re_production_age=calculated_fibonachies[idx-2]=Weighted_Fibonachi_Calculator(weight=weight,idx=idx-2)
    
    none_re_production_age=calculated_fibonachies.get(idx-1)
    if not none_re_production_age:
        none_re_production_age=calculated_fibonachies[idx-1]=Weighted_Fibonachi_Calculator(weight=weight,idx=idx-1)
    
    return weight*re_production_age+none_re_production_age

print(Weighted_Fibonachi_Calculator(
    idx=8,weight=3
))
