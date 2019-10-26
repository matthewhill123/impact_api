from co2_converter import main

test_data = {
    "transport": [
        {"mode": "small_car",
                 "distance": 50,
                 "unit": "km"
         },
        {"mode": "train",
                 "distance": 100,
                 "unit": "mi"
         }
    ]
}


def test_expected_type():
    result = main.convert_to_co2(test_data)
    assert(isinstance(result, list))
    
def test_expected_length():
    result = main.convert_to_co2(test_data)
    assert(len(result)==2)

def test_small_car_co2():
    result = main.convert_to_co2(test_data)[0]
    assert(result == 7.5)

def test_train():
    result = main.convert_to_co2(test_data)[1]
    assert(result == 6.7)