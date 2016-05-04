#!/usr/bin/env python3
import sys
import os
def fix(f):

  if f.startswith("VID_") or f.startswith("IMG_"):
    os.rename(f,f[4:])
    f = f[4:]
  
  year = f[0:4]
  month = f[4:6]
  day = f[6:8]
  hour = f[9:11]
  min = f[11:13]
  sec = f[13:15]
  print("year={0} month={1} day={2} hour={3} min={4} sec={5}".format(year, month, day, hour, min, sec))

  date = "{0}:{1}:{2} {3}:{4}:{5}".format(year,month,day,hour,min,sec)
  cmd = "exiftool -overwrite_original '-AllDates={0}' {1}".format(date, f)
  print(cmd)
  os.system(cmd)  

  date = "{0}/{1}/{2} {3}:{4}:{5}".format(month,day,year,hour,min,sec)
  cmd = "SetFile -m  \"{0}\" \"{1}\"".format(date, f)
  print(cmd)
  os.system(cmd)

for f in sys.argv[1:]:
  fix(os.path.basename(f))
