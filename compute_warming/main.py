def compute_warming_from_transport_co2(humanity_CO2_extrapolated):
    """
    Computes the warming from a list of CO2 over a
    certain period.

    Currently the period is assumed.

        Expected format: [10., 20.]

    Returns the warming as float
    """

    if humanity_CO2_extrapolated <= 651.68E12:
        # temp =< 1.5 --> temp difference = 1.5
        total_warming_value = 1.5*(humanity_CO2_extrapolated/651.68E12)
    elif humanity_CO2_extrapolated <= 1251.68E12:
        # 1.5 =< temp =< 2.0  --> temp difference = 0.5
        total_warming_value = 0.5*(humanity_CO2_extrapolated - 651.68E12)/(1251.68E12-651.68E12) + 1.5
    else:
        # 2.0 <= temp =< 3.0 --> temp difference = 1
        total_warming_value = 1.0*(humanity_CO2_extrapolated - 1251.68E12)/(3251.68E12-1251.68E12) + 2.0

    return total_warming_value


# import numpy as np
# import matplotlib.pyplot as plt
#
# test_range = np.arange(0,4000E12,100E12)
#
# test_results = []
# for i in test_range:
#     test_results.append(compute_warming_from_transport_co2(i))
# plt.plot(test_range,test_results)
# plt.show()
