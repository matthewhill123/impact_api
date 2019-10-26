def compute_warming_from_transport_co2(events_co2):
    """
    Computes the warming from a list of CO2 over a
    certain period.

    Currently the period is assumed.

        Expected format: [10., 20.]

    Returns the warming as float
    """


   carbon_equiv_total = sum(events_co2) # for an array of input carbon_equivs
   if (carbon_equiv_total <= 170308):
       temp = 1.5
       carbon_excess = carbon_equiv_total - 88670
       heating_potential = 6.1E-6
   else:
       temp = 2.0
       carbon_excess = carbon_equiv_total - 170308
       heating_potential = 3.7E-6

   total_warming_value = (temp + carbon_excess * heating_potential)
   return total_warming_value
