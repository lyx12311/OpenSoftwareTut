import OpenSoftwareTut
import numpy as np

def test_print():
    """
    testing the print function"
    """
    s1, s2=OpenSoftwareTut.SampleCode()
    
    assert np.isnan(s1), "statement1 number is not nan!"
