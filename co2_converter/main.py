from datetime import time, datetime

# fuel_consumption = {
#     "lorry": {"diesel": 7, "petrol": None, "electric": 1.6},
#     "van": {"diesel": 25, "petrol": 25, "electric": 0.4},
#     "large_car": {"diesel": 28, "petrol": 18, "electric": 0.4},
#     "medium_car": {"diesel": 35, "petrol": 27, "electric": 0.3},
#     "small_car": {"diesel": 43, "petrol": 34, "electric": 0.2},
#     "motorbike": {"diesel": None, "petrol": 45, "electric": 0.15},
#     "scooter": {"diesel": None, "petrol": 120, "electric": 0.06},
#     "motorised_bike": {"diesel": 7, "petrol": 184, "electric": 	0.04},
#     "electric_scooter": {"electric": 0.15},
#     "electric_bike": {"electric": 0.05}
# }

emissions_per_km = {
    "small_car" : 0.15,
    "train" : 0.067
}

co2_conversion = {
    "fossil": 14.3,
    "electric": {
        "2016": 0.351,
        "2017": 0.214,
        "2018": 0.205,
        "2019": 0.195,
        "2020": 0.182,
        "2021": 0.171,
        "2022": 0.149,
        "2023": 0.145,
        "2024": 0.15,
        "2025": 0.141,
        "2026": 0.115,
        "2027": 0.12,
        "2028": 0.109,
        "2029": 0.097,
        "2030": 0.105,
        "2031": 0.096,
        "2032": 0.078,
        "2033": 0.075,
        "2034": 0.066,
        "2035": 0.056,
        "2036": 0.055,
        "2037": 0.054,
        "2038": 0.053,
        "2039": 0.052,
        "2040": 0.052,
        "2041": 0.049,
        "2042": 0.046,
        "2043": 0.043,
        "2044": 0.04,
        "2045": 0.037,
        "2046": 0.036,
        "2047": 0.035,
        "2048": 0.034,
        "2049": 0.033,
        "2050": 0.032,
        "2051": 0.031,
        "2052": 0.03,
        "2053": 0.029,
        "2054": 0.028,
        "2055": 0.027,
        "2056": 0.026,
        "2057": 0.025,
        "2058": 0.024,
        "2059": 0.023,
        "2060": 0.022,
        "2061": 0.021,
        "2062": 0.02,
        "2063": 0.019,
        "2064": 0.018,
        "2065": 0.017
    }
}

def convert_to_co2(events):
    """
    Computes the CO2 equivalent for a list of events

    Expected format:
        {
            "transport" : [
                {"mode" : "small_car",
                 "distance" : 50
                 "unit" : "km"
                    },
                {"mode": "train",
                 "distance": 100,
                 "unit": "mi"
                    }
            ]
        }

    Returns a list of CO2 equivalent: [10., 20.]
    """
    result = list()
    for event in events["transport"]:
        mode = event["mode"]
        distance = event["distance"] # TODO Use distance unit to calculate distances to km
        result.append(compute_transport_event_co2(mode,distance))
    return result
    
def compute_transport_event_co2(mode, distance, fuel="petrol"):
    """Returns the co2 emitted in kg by a transport event made by mode 'mode' and distance 'distance' in km"""
    co2 = distance * emissions_per_km[mode]
    return co2
