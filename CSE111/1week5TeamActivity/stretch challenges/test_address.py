from address import extract_city, extract_state, extract_zipcode
import pytest
"""Extract and return the name of a city from
a properly formatted U.S. mailing address.
Parameter
    full_address: a U.S. mailing address in this format:
        number and street, city, state zipcode
Return: the city name
"""

def test_extract_city():
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("78 Pine St, Avon Park, FL 33825") == "Avon Park"
    assert extract_city("123 W Main, Rexburg, ID 83440") == "Rexburg"
    
def test_extract_state():
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("78 Pine St, Avon Park, FL 33825") == "FL"
    assert extract_state("78 Pine St, Avon Park, Florida 33825") == "Florida"
    assert extract_state("123 W Main, Rexburg, ID 83440") == "ID"
    
def test_extract_zipcode():
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"    
    assert extract_zipcode("78 Pine St, Avon Park, FL 33825") == "33825"  
    assert extract_zipcode("123 W Main, Rexburg, ID 83440") == "83440" 
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])