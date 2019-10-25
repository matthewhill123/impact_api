# Basic formula from the spreadsheet to calculate 
# temperature rise from carbon equivalent input

# Heating potential in degrees C per kg CO2e

def warmingCalc(carbon_equiv):
    # input total carbonEquiv in kg CO2e
    
    #sum(carbon_equiv) # for an array of input carbon_equivs
    
    if (carbon_equiv <= 170308):
        temp = 1.5
        carbon_excess = carbon_equiv - 88670
        heating_potential = 6.1E-6
    elif (carbon_equiv <=  442437):
        temp = 2.0
        carbon_excess = carbon_equiv - 170308
        heating_potential = 3.7E-6
    else:
        print("Input carbon too high")
        # Or just use the 3.7E-6 for high levels of carbon equiv? Bad science?

    return (temp + carbon_excess * heating_potential)

# Example to return 2.7 deg C
print(warmingCalc(217226))