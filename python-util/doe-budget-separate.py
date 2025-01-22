#######
# @TheDoctorRAB
#######
#
# DOE budget transfer file
# Transfer from the budget worksheet to the DOE worksheet
#
# https://www.e-iceblue.com/Knowledgebase/Python/Spire.XLS-for-Python/Program-Guide/Data/Python-Set-Text-Alignment-and-Orientation-in-Excel.html
# https://www.e-iceblue.com/Tutorials/Python/Spire.XLS-for-Python/Program-Guide/Cells/Python-Add-or-Remove-Cell-Borders-in-Excel.html#:~:text=With%20Spire.,outside%20border%20using%20the%20CellRange.
# https://www.e-iceblue.com/Tutorials/Python/Spire.XLS-for-Python.html
#
#######
#
#
#
####### imports
#
import numpy
import spire.xls as xls
import openpyxl
from spire.xls import *
from spire.xls.common import *
#
#######
#
#
#
####### create workbook objects
#
# does not like hyphens in object definition
#
draftBudget = Workbook() #google sheet draft budget
doeBudget = Workbook()   #doe required format
#
#######
#
#
#
####### load excel worksheets
#
doeBudget.LoadFromFile('doe-draft.xlsx')
#
#######
#
#
#
####### load worksheets
#
# first worksheet = 0 just like array
#
doe1AB = doeBudget.Worksheets[5]
doe1CE = doeBudget.Worksheets[6]
doe1FK = doeBudget.Worksheets[7]
doe2AB = doeBudget.Worksheets[8]
doe2CE = doeBudget.Worksheets[9]
doe2FK = doeBudget.Worksheets[10]
doe3AB = doeBudget.Worksheets[11]
doe3CE = doeBudget.Worksheets[12]
doe3FK = doeBudget.Worksheets[13]
doe3FK = doeBudget.Worksheets[13]
doeCumulative = doeBudget.Worksheets[14]
#
#######
#
#
#
###### save
#
doeBudget.SaveToFile('doe-format.xlsx')
#
######
