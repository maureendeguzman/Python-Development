from names import make_full_name, extract_family_name, extract_given_name
import pytest

#Core Requirements
'''rite a function named test_make_full_name that takes no parameters. 
Write assert statements inside this function to test the value returned from the make_full_name function. '''
def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"  
    assert make_full_name("James", "Madison") == "Madison; James"
    assert make_full_name("J", "Ng") == "Ng; J"
    assert make_full_name("", "") == "; "
    assert make_full_name("Sally G.", "Brown") == "Brown; Sally G."  

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"  
    assert extract_family_name("Madison; James") == "Madison"
    assert extract_family_name("Ng; J") == "Ng"
    assert extract_family_name("; ") == ""
    assert extract_family_name("Brown; Sally G.") == "Brown"  
        
def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"      
    assert extract_given_name("Madison; James") == "James"
    assert extract_given_name("Ng; J") == "J"
    assert extract_given_name("; ") == ""
    assert extract_given_name("Brown; Sally G.") == "Sally G." 
    

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])