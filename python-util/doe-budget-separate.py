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
draftBudget = Workbook() #source xlsx
doeBudget = Workbook()   #destination xlsx
#
#######
#
#
#
####### load excel worksheets
#
draftBudget.LoadFromFile('doe-draft.xlsx')
#
#######
#
#
#
####### move worksheets to new file
#
# blank Sheet1, Sheet2, Sheet3 created
# can only remove first two sheets without deleting some of the moved sheets even on reload
#
doeBudget.Worksheets.RemoveAt(0)
doeBudget.Worksheets.RemoveAt(1)
#
doeBudget.Worksheets.Add(draftBudget.Worksheets[5].Name).CopyFrom(draftBudget.Worksheets[5])
doeBudget.Worksheets.Add(draftBudget.Worksheets[6].Name).CopyFrom(draftBudget.Worksheets[6])
doeBudget.Worksheets.Add(draftBudget.Worksheets[7].Name).CopyFrom(draftBudget.Worksheets[7])
doeBudget.Worksheets.Add(draftBudget.Worksheets[8].Name).CopyFrom(draftBudget.Worksheets[8])
doeBudget.Worksheets.Add(draftBudget.Worksheets[9].Name).CopyFrom(draftBudget.Worksheets[9])
doeBudget.Worksheets.Add(draftBudget.Worksheets[10].Name).CopyFrom(draftBudget.Worksheets[10])
doeBudget.Worksheets.Add(draftBudget.Worksheets[11].Name).CopyFrom(draftBudget.Worksheets[11])
doeBudget.Worksheets.Add(draftBudget.Worksheets[12].Name).CopyFrom(draftBudget.Worksheets[12])
doeBudget.Worksheets.Add(draftBudget.Worksheets[13].Name).CopyFrom(draftBudget.Worksheets[13])
doeBudget.Worksheets.Add(draftBudget.Worksheets[14].Name).CopyFrom(draftBudget.Worksheets[14])
#
#######
#
#
#
####### save
#
doeBudget.SaveToFile('doe-format.xlsx')
#
#######
















