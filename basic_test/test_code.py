# to install in terminal --> pip install pytest
# to run in terminal --> pytest 
#20 of assert statements 
# from ___ import ___
import os

#attempt to test file
def test_file_creation():
     with open('animal_details_Sophie.txt', 'r') as f:
        content = f.read()
        assert content != ""


def test_input_&_other parts():
    assert isinstance (my_var, int)
    assert accuracy()
    assert if_they_want_more_info()
    assert info()
    assert where_they_are_in_graph
    assert load_heart_data()
    assert make_plot() #should equal image possibly
    assert info_returns()
    assert read_me()
    






