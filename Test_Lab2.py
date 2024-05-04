import Lab2
print("test_lab2.py")

def test_find_min_max():
    input_list= [1,4,21,42,12]
    expected_result = [1,42]
    test_result =Lab2.find_min_max(input_list)
    assert expected_result == test_result
def test_calc_average(): 
    input_list= [1,4,21,42,12]
    expected_result = [16.0]
    test_result = Lab2.calc_average(input_list)
    assert expected_result == test_result
def test_calc_median_temperature():
    input_list= [1,4,21,42,12]
    expected_result = 12.0
    test_result = Lab2.calc_median_temperature(input_list)
    assert expected_result == test_result