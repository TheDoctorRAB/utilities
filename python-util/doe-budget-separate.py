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
draftBudget.LoadFromFile('doe-draft.xlsx')
doeBudget.LoadFromFile('doe-format.xlsx')
#
#######
#
#
#
####### load worksheets
#
# first worksheet = 0 just like array
#
### doe draft
draftTOTALS = draftBudget.Worksheets[0]
draftBudgetWK = draftBudget.Worksheets[1]
draftTravelBudget = draftBudget.Worksheets[2]
draftDataSheet = draftBudget.Worksheets[3]
draftTravel = draftBudget.Worksheets[4]
#
### doe required
#
doe1AB = doeBudget.Worksheets[0]
doe2AB = doeBudget.Worksheets[3]
doe3AB = doeBudget.Worksheets[6]
doe1CE = doeBudget.Worksheets[1]
doe2CE = doeBudget.Worksheets[4]
doe3CE = doeBudget.Worksheets[7]
doe1FK = doeBudget.Worksheets[2]
#
#######
#
#
#
####### get and define data to move
#
### doe draft
#
print('Loading from the doe draft')
#
# still trying to figure out when to use Formula.Value v. Value
#
draftDUNS = draftDataSheet.Range['N23']
draftTitlePI = draftDataSheet.Range['Q3']
draftFirstNamePI = draftDataSheet.Range['R3']
draftLastNamePI = draftDataSheet.Range['S3']
draftRolePI = draftDataSheet.Range['T3']
draftBaseSalaryPI = draftDataSheet.Range['C9']
draftAYHoursPI = draftBudgetWK.Range['E10'].FormulaValue
draftSummerHoursPI = draftBudgetWK.Range['E11'].FormulaValue
#
draftAYPIY1 = draftDataSheet.Range['C64'].FormulaValue
draftSummerPIY1 = draftDataSheet.Range['C69'].FormulaValue
draftAYFringePIY1 = draftBudgetWK.Range['H26'].FormulaValue
draftSummerFringePIY1 = draftBudgetWK.Range['H27'].FormulaValue
#
draftAYHoursMS = draftBudgetWK.Range['E22'].FormulaValue
draftSummerHoursMS = draftBudgetWK.Range['E23'].FormulaValue
draftStudentsMSY1calc = draftBudgetWK.Range['F22'].Value
draftStudentsMSY1 = draftBudgetWK.Range['F22']
#
draftAYStudentMSY1 = draftDataSheet.Range['C75'].FormulaValue
draftSummerStudentMSY1 = draftDataSheet.Range['C80'].FormulaValue
draftAYFringeStudentMSY1 = draftBudgetWK.Range['H28'].FormulaValue
draftSummerFringeStudentMSY1 = draftBudgetWK.Range['H29'].FormulaValue
#
draftTravelY21 = draftTravelBudget.Range['N10'].FormulaValue
draftTravelY22 = draftTravelBudget.Range['N13'].FormulaValue
draftTravelY23 = draftTravelBudget.Range['N14'].FormulaValue
draftTravelY31 = draftTravelBudget.Range['T10'].FormulaValue
draftTravelY32 = draftTravelBudget.Range['T15'].FormulaValue
draftTravelY33 = draftTravelBudget.Range['T16'].FormulaValue
#
draftTuition = draftBudgetWK.Range['H57']
#
draftIndirectCosts= draftBudgetWK.Range['H51']
#
# calculations
#
print('Calculations')
#
draftAYMonthsPI = float(draftAYHoursPI)/160
draftSummerMonthsPI = float(draftSummerHoursPI)/160
draftTotalMonthsPI = draftAYMonthsPI+draftSummerMonthsPI
#
draftPISalaryY1 = float(draftAYPIY1) + float(draftSummerPIY1)
draftPIFringeY1 = float(draftAYFringePIY1) + float(draftSummerFringePIY1) #total students included
#
draftAYMonthsMS = float(draftAYHoursMS)/160*float(draftStudentsMSY1calc)
draftSummerMonthsMS = float(draftSummerHoursMS)/160*float(draftStudentsMSY1calc)
draftTotalMonthsMS = draftAYMonthsMS + draftSummerMonthsMS
#
draftStudentSalaryMSY1 = float(draftAYStudentMSY1) + float(draftSummerStudentMSY1) #total students included
draftStudentFringeMSY1 = float(draftAYFringeStudentMSY1) + float(draftSummerFringeStudentMSY1) #total students included
#
draftTravelY2 = float(draftTravelY21) + float(draftTravelY22) + float(draftTravelY23)
draftTravelY3 = float(draftTravelY31) + float(draftTravelY32) + float(draftTravelY33)
### doe required
#
# manual entry
#
print('Manual data entry')
#
#doe1AB.Range['D4'].Value = 'x' #lead organization
doe1AB.Range['H4'].Value = 'x' #subaward
#
print('Verify lead or subaward!')
#
doe1AB.Range['D6'].Value = 'Regents of the University of Idaho'
doe1AB.Range['C8'].Value = '08/01/2025'
doe1AB.Range['F8'].Value = '07/31/2026'
doe1AB.Range['K12'].Value = str(draftTotalMonthsPI)
doe1AB.Range['L12'].Value = str(draftAYMonthsPI)
doe1AB.Range['M12'].Value = str(draftSummerMonthsPI)
doe1AB.Range['K28'].Value = str(draftTotalMonthsMS)
doe1AB.Range['L28'].Value = str(draftAYMonthsMS)
doe1AB.Range['M28'].Value = str(draftSummerMonthsMS)
doe1AB.Range['N12'].Value = str(draftPISalaryY1)
doe1AB.Range['O12'].Value = str(draftPIFringeY1)
doe1AB.Range['N28'].Value = str(draftStudentSalaryMSY1)
doe1AB.Range['O28'].Value = str(draftStudentFringeMSY1)
doe2CE.Range['J32'].Value = str(draftTravelY2)
doe3CE.Range['J32'].Value = str(draftTravelY3)
#
print('Verify project period!',doe1AB.Range['C8'].Value)
#
# define fields/cells
#
doeDUNS = doe1AB.Range['D2']
doeTitlePI = doe1AB.Range['B12']
doeFirstNamePI = doe1AB.Range['C12']
doeLastNamePI = doe1AB.Range['G12']
doeRolePI = doe1AB.Range['I12']
doeTotalMonthsPI = doe1AB.Range['K12']
doeBaseSalaryPI = doe1AB.Range['J12']
doeFringePIY1 = doe1AB.Range['O12']
doeStudentsMSY1 = doe1AB.Range['A28']
doeTuition = doe1FK.Range['J20']
doeIndirectCosts= doe1FK.Range['H31']
#
######
#
#
#
####### move data
#
print('Moving data')
#
draftDataSheet.Copy(draftDUNS,doeDUNS)
draftDataSheet.Copy(draftTitlePI,doeTitlePI)
draftDataSheet.Copy(draftFirstNamePI,doeFirstNamePI)
draftDataSheet.Copy(draftLastNamePI,doeLastNamePI)
draftDataSheet.Copy(draftRolePI,doeRolePI)
draftDataSheet.Copy(draftBaseSalaryPI,doeBaseSalaryPI)
draftBudgetWK.Copy(draftStudentsMSY1,doeStudentsMSY1)
draftBudgetWK.Copy(draftTuition,doeTuition)
draftBudgetWK.Copy(draftIndirectCosts,doeIndirectCosts)
#
#######
#
#
#
###### formulas
#
# formulas are not preserved when loading workbook
#
# for some reason new formulas can be written in
# have to hard code
#
print('Writing formulas')
#
for row in range(1, doe1AB.Rows.Count + 1):
    for column in range(1, doe1AB.Columns.Count + 1):
        cell = doe1AB.Range[row,column]
        if cell.Formula:
            formula = cell.Formula #store formula as string
#            print(row,column,formula)
            cell.ClearContents() #clear the cell value
            cell.Formula = formula #write formula back
#
###
#
for row in range(1, doe2AB.Rows.Count + 1):
    for column in range(1, doe2AB.Columns.Count + 1):
        cell = doe2AB.Range[row,column]
        if cell.Formula:
            formula = cell.Formula #store formula as string
#            print(row,column,formula)
            cell.ClearContents() #clear the cell value
            cell.Formula = formula #write formula back
#
###
#
for row in range(1, doe3AB.Rows.Count + 1):
    for column in range(1, doe3AB.Columns.Count + 1):
        cell = doe3AB.Range[row,column]
        if cell.Formula:
            formula = cell.Formula #store formula as string
#            print(row,column,formula)
            cell.ClearContents() #clear the cell value
            cell.Formula = formula #write formula back
#
###
#
for row in range(1, doe1CE.Rows.Count + 1):
    for column in range(1, doe1CE.Columns.Count + 1):
        cell = doe1CE.Range[row,column]
        if cell.Formula:
            formula = cell.Formula #store formula as string
#            print(row,column,formula)
            cell.ClearContents() #clear the cell value
            cell.Formula = formula #write formula back
#
###
#
for row in range(1, doe2CE.Rows.Count + 1):
    for column in range(1, doe2CE.Columns.Count + 1):
        cell = doe2CE.Range[row,column]
        if cell.Formula:
            formula = cell.Formula #store formula as string
#            print(row,column,formula)
            cell.ClearContents() #clear the cell value
            cell.Formula = formula #write formula back
#
###
#
for row in range(1, doe3CE.Rows.Count + 1):
    for column in range(1, doe3CE.Columns.Count + 1):
        cell = doe3CE.Range[row,column]
        if cell.Formula:
            formula = cell.Formula #store formula as string
#            print(row,column,formula)
            cell.ClearContents() #clear the cell value
            cell.Formula = formula #write formula back
#
for row in range(1, doe1FK.Rows.Count + 1):
    for column in range(1, doe1FK.Columns.Count + 1):
        cell = doe1FK.Range[row,column]
        if cell.Formula:
            formula = cell.Formula #store formula as string
#            print(row,column,formula)
            cell.ClearContents() #clear the cell value
            cell.Formula = formula #write formula back
######
#
#
#
###### formatting
#
# only can set for each worksheet
# have to specify range
#
### font
#
doe1AB.Range['A1:Z90'].Style.Font.FontName = 'Arial'
doe1AB.Range['A1:Z90'].Style.Font.Size = 10
doe2AB.Range['A1:Z90'].Style.Font.FontName = 'Arial'
doe2AB.Range['A1:Z90'].Style.Font.Size = 10
doe3AB.Range['A1:Z90'].Style.Font.FontName = 'Arial'
doe3AB.Range['A1:Z90'].Style.Font.Size = 10
doe1CE.Range['A1:Z90'].Style.Font.FontName = 'Arial'
doe1CE.Range['A1:Z90'].Style.Font.Size = 10
doe2CE.Range['A1:Z90'].Style.Font.FontName = 'Arial'
doe2CE.Range['A1:Z90'].Style.Font.Size = 10
doe3CE.Range['A1:Z90'].Style.Font.FontName = 'Arial'
doe3CE.Range['A1:Z90'].Style.Font.Size = 10
#
### alignments
#
doe1AB.Range['A1:Z90'].Style.VerticalAlignment = VerticalAlignType.Bottom
doe1AB.Range['D2'].Style.HorizontalAlignment = HorizontalAlignType.Left
doe1AB.Range['B12:I12'].Style.HorizontalAlignment = HorizontalAlignType.Left
doe1AB.Range['J12'].Style.HorizontalAlignment = HorizontalAlignType.Right
#
### borders and fill
#
doe1AB.Range['D2'].BorderAround()
doe1AB.Range['B12'].Borders[BordersLineType.EdgeLeft].LineStyle = LineStyleType.Thin
doe1AB.Range['B12'].Borders[BordersLineType.EdgeRight].LineStyle = LineStyleType.Thin
doe1AB.Range['J12'].Borders[BordersLineType.EdgeLeft].LineStyle = LineStyleType.Thin
doe1AB.Range['N12'].Borders[BordersLineType.EdgeLeft].LineStyle = LineStyleType.Thin
doe1AB.Range['A28'].Style.Color = Color.get_White()
doe2CE.Range['J32'].BorderAround()
doe3CE.Range['J32'].BorderAround()
#
### number
#
doe1AB.Range['K12:M12'].NumberFormat = '0.0000'
doe1AB.Range['K28:M28'].NumberFormat = '0.0000'
doe1AB.Range['J12'].NumberFormat = '_(\$* #,##0.00_);_(\$* \(#,##0.00\);_(\$* -??_);_(@_)'
doe1AB.Range['N12:O12'].NumberFormat = '_(\$* #,##0.00_);_(\$* \(#,##0.00\);_(\$* -??_);_(@_)'
doe1AB.Range['N28:O28'].NumberFormat = '_(\$* #,##0.00_);_(\$* \(#,##0.00\);_(\$* -??_);_(@_)'
doe2CE.Range['J32'].NumberFormat = '_(\$* #,##0.00_);_(\$* \(#,##0.00\);_(\$* -??_);_(@_)'
doe3CE.Range['J32'].NumberFormat = '_(\$* #,##0.00_);_(\$* \(#,##0.00\);_(\$* -??_);_(@_)'
#
######
#
#
#
###### save
#
doeBudget.SaveToFile('doe-format.xlsx')
#
######
