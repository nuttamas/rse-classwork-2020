import pytest
from times import time_range, compute_overlap_time
from datetime import datetime

def test_given_input():
    
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    #print(large)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    #print(short)
    
    result = compute_overlap_time(large,short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    
    assert result == expected

    ###### Below codes are the classwork #####

#def test_non_overlap():
 #    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
 #    short = time_range("2010-01-12 14:30:00", "2010-01-12 14:45:00", 2, 60)
 #    result = compute_overlap_time(large, short)
 #    #print (result)
 #    expected = []
 #   
 #    assert result == expected