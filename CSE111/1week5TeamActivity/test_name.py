from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    given_name = "Sally"
    family_name = "Brown"
    expected_result = "Brown, Sally" 
    
    result = make_full_name(given_name, family_name)
    assert result == expected_result
    
    
    
def test_extract_family_name():
    full_name = ""
    expected_result = ""

    result = extract_family_name(full_name)
    assert result == expected_result

def test_extract_given_name():
    full_name = ""
    expected_result = ""

    result = extract_given_name(full_name)

    assert result == expected_result  
    
pytest.main(["-v", "--tb=line", "-rN", __file__])      