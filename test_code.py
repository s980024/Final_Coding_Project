# to install in terminal --> pip install pytest
# to run in terminal --> pytest 
#20 of assert statements 
from get_data.fetch_data import load_heart_data
import ast
import os

def test_file_creation():
    assert os.path.isfile("//workspaces/Final_Coding_Project/plots/trestbpsvsthalach.png")
    assert os.path.isfile("//workspaces/Final_Coding_Project/plots/oldpeakvsthalach.png")
    assert os.path.isfile("//workspaces/Final_Coding_Project/plots/agevstrestbps.png")

def test_input():
    user_input = "22.3"
    assert type(ast.literal_eval(user_input)) is float

def test_terminal_print_accuracy():
    get_accuracy()
    captured = capsys.readouterr()
    assert captured.out = "Acuracy: \n"
def test_terminal_print_what_info():
    get_info_input()
    captured = capsys.readouterr()
    assert captured.out = "Please enter what info you would like? \n"
def test_terminal_print_accuracy():
    get_accuracy()
    captured = capsys.readouterr()
    assert captured.out = "Acuracy: \n"
def test_terminal_info_printed():
    get_info_printed())
    captured = capsys.readouterr()
    assert captured.out = " \n" #infromation that will be in this will come later & prob more of these for info
def test_where_they_are_in_graph():
    get_where_they_are()
    captured capsys.readouterr()
    assert captured.out "You are in this area of the graph. \n"  

     # assert info_returns()
def test_terminal_print():
    get_response()
    captured = capsys.readouterr()
    assert captured.out == "Please type Yes if you want more information about your heart diseas or no if you do not. \n"
def test_loading():
    assert load_heart_data() is not None
   
    






