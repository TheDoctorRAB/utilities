########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.24.December.2015
# v1.0
########################################################################
#
# Display screen resolution
#
########################################################################
#
# imports
#
import Tkinter
root=Tkinter.Tk()
#
########################################################################
#
#
#
#######
#
# pixels
#
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
#
#######
#
# mm
#
width_mm=root.winfo_screenmmwidth()
height_mm=root.winfo_screenmmheight()
#
#######
#
# inches
#
width_in=width_mm/25.4
height_in=height_mm/25.4
#
#######
#
# dpi
#
width_dpi=width/width_in
height_dpi=height/height_in
#
dpi_values=(96,120,144,168,192)
current_dpi=width_dpi
minimum=1000
#
for dval in dpi_values:
  difference=abs(dval-width_dpi)
  if difference<minimum:
    minimum=difference
    current_dpi=dval
#
#######
#
# output
#
print('width: %i px, height: %i px'%(width,height))
print('width: %i mm, height: %i mm'%(width_mm,height_mm))
print('width: %0.f in, height: %0.f in'%(width_in,height_in))
print('width: %0.f dpi, height: %0.f dpi'%(width_dpi,height_dpi))
print('current DPI is %0.f' % (current_dpi))
#
#
#
########################################################################
#
# EOF
#
########################################################################
