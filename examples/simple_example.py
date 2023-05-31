"""
For a Guided search through data run "python near-neighbor_app.py"
This will alow you to copy and paste in a list of data or load in a comma seperated list of points.
For exact syntax look at the mock_data.csv file in the examples folder
"""


"""
For a cli use, from directory of the pynn library run the follwowing commands.
python
from pynn import NearestNeighborIndex
uut = NearestNeighborIndex(["data to be inserted", "must be float or int and follow tuple syntax"), (5,5), (-4,0)])
uut.find_nearest((0,0)) #or whatever point you are looking for
This syntax can also be used when importing into other python files
"""

