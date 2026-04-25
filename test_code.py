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
    assert os.path.isfile("//workspaces/Final_Coding_Project/plots/cholvstrestbps.png")
    assert os.path.isfile("//workspaces/Final_Coding_Project/plots/cholvsoldpeak.png")
    assert os.path.isfile("//workspaces/Final_Coding_Project/plots/cholvsthalach.png")
    assert os.path.isfile("//workspaces/Final_Coding_Project/plots/cholvsage.png")
    assert os.path.isfile("//workspaces/Final_Coding_Project/plots/oldpeakvsage.png")

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
#advice
def test_terminal_info():
    get_info_printed() #this function may be changed later
    captured = capsys.readouterr()
    assert captured.out = "If you are smoking it is recommended that you stop, as nicotine can narrow your blood vessels which is not good. \n"

def test_terminal_info_printed():
    get_info_printed())
    captured = capsys.readouterr()
    assert captured.out = "It is recommended to change your diet to a low soidum/low fat diet and manage your weight. \n" #infromation that will be in this will come later & prob more of these for info

def test_terminal_info_printed():
    get_info_printed())
    captured = capsys.readouterr()
    assert captured.out = "It you have not seen a doctor yet and you information says you have heart disease, it would be a good idea to check in with a doctor. \n"

def test_terminal_info_printed():
    get_info_printed())
    captured = capsys.readouterr()
    assert captured.out = "It is recommended to aim for at least of 150 minutes of moderate intensity of exercise once a week to try and keep it from getting worse. \n"

def test_terminal_info_printed():
    get_info_printed())
    captured = capsys.readouterr()
    assert captured.out = "If you have a doctor and are on medications, it is recommended that you keep taking that medication until your doctor tells you not to. \n"

def test_terminal_info_printed():
    get_info_printed())
    captured = capsys.readouterr()
    assert captured.out = "It is also good to get between 7-8 hours of sleep to help keep blood pressure low. \n"

#advice ends and other tests are run
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
   
    






