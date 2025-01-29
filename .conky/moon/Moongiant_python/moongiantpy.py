import os, sys
from PIL import Image
import re
import string
import shutil
import time
import requests
import datetime
import pprint
from bleach.sanitizer import Cleaner
from glob import glob
#
homepath = os.environ['HOME']
homename = homepath
homename = homename[6:]
#                   set your emisphere (north or south)
emi = 'north'
###################################                 r=row, m=minus, p=plus, i=image, p=phase, t=today, imm=image
rm2i = 972
rm2p = 973
rm1i = 978
rm1p = 979
rti = 981
rp1i = 987
rp1p = 988
rp2i = 993
rp2p = 994
rimm = 1068
###################################                  paths
filepath = '/home/' + homename + '/.conky/moon/Moongiant_python/raw.txt'
filepath2 = '/home/' + homename + '/.conky/moon/Moongiant_python/rawstripped.txt'
filepath3 = '/home/' + homename + '/.conky/moon/Moongiant_python/rawstrippedclean.txt'
filepath4 = '/home/' + homename + '/.conky/moon/Moongiant_python/rawstrippedcleanrows.txt'
filepath5 = '/home/' + homename + '/.conky/moon/Moongiant_python/illumidays.txt'
filepath6 = '/home/' + homename + '/.conky/moon/Moongiant_python/picspath.txt'
filepath7 = '/home/' + homename + '/.conky/moon/Moongiant_python/moongiant_icons_' + emi + '/'
filepath8 = '/home/' + homename + '/.conky/moon/Moongiant_python/riseicons' + '/'
filepath9 = '/home/' + homename + '/.conky/moon/Moongiant_python/phases.txt'
filepath10 = '/home/' + homename + '/.conky/moon/Moongiant_python/rise.jpg'
#                                                    moon pics patterns PNG
picspatterns = ['moon_day_first.png', 'moon_day_full.png', 'moon_day_last.png', 'moon_day_new.png', 'moon_day_WanC_0.png', 'moon_day_WanC_5.png', 'moon_day_WanC_10.png', 'moon_day_WanC_15.png', 'moon_day_WanC_20.png', 'moon_day_WanC_25.png', 'moon_day_WanC_30.png', 'moon_day_WanC_35.png', 'moon_day_WanC_40.png', 'moon_day_WanC_45.png', 'moon_day_WanG_50.png', 'moon_day_WanG_55.png', 'moon_day_WanG_60.png', 'moon_day_WanG_65.png', 'moon_day_WanG_70.png', 'moon_day_WanG_75.png', 'moon_day_WanG_80.png', 'moon_day_WanG_85.png', 'moon_day_WanG_90.png', 'moon_day_WanG_95.png', 'moon_day_WaxC_0.png', 'moon_day_WaxC_5.png', 'moon_day_WaxC_10.png', 'moon_day_WaxC_15.png', 'moon_day_WaxC_20.png', 'moon_day_WaxC_25.png', 'moon_day_WaxC_30.png', 'moon_day_WaxC_35.png', 'moon_day_WaxC_40.png', 'moon_day_WaxC_45.png', 'moon_day_WaxG_50.png', 'moon_day_WaxG_55.png', 'moon_day_WaxG_60.png', 'moon_day_WaxG_65.png', 'moon_day_WaxG_70.png', 'moon_day_WaxG_75.png', 'moon_day_WaxG_80.png', 'moon_day_WaxG_85.png', 'moon_day_WaxG_90.png', 'moon_day_WaxG_95.png', 'moon_day_first.jpg', 'moon_day_full.jpg', 'moon_day_last.jpg', 'moon_day_new.jpg', 'moon_day_WanC_0.jpg', 'moon_day_WanC_5.jpg', 'moon_day_WanC_10.jpg', 'moon_day_WanC_15.jpg', 'moon_day_WanC_20.jpg', 'moon_day_WanC_25.jpg', 'moon_day_WanC_30.jpg', 'moon_day_WanC_35.jpg', 'moon_day_WanC_40.jpg', 'moon_day_WanC_45.jpg', 'moon_day_WanG_50.jpg', 'moon_day_WanG_55.jpg', 'moon_day_WanG_60.jpg', 'moon_day_WanG_65.jpg', 'moon_day_WanG_70.jpg', 'moon_day_WanG_75.jpg', 'moon_day_WanG_80.jpg', 'moon_day_WanG_85.jpg', 'moon_day_WanG_90.jpg', 'moon_day_WanG_95.jpg', 'moon_day_WaxC_0.jpg', 'moon_day_WaxC_5.jpg', 'moon_day_WaxC_10.jpg', 'moon_day_WaxC_15.jpg', 'moon_day_WaxC_20.jpg', 'moon_day_WaxC_25.jpg', 'moon_day_WaxC_30.jpg', 'moon_day_WaxC_35.jpg', 'moon_day_WaxC_40.jpg', 'moon_day_WaxC_45.jpg', 'moon_day_WaxG_50.jpg', 'moon_day_WaxG_55.jpg', 'moon_day_WaxG_60.jpg', 'moon_day_WaxG_65.jpg', 'moon_day_WaxG_70.jpg', 'moon_day_WaxG_75.jpg', 'moon_day_WaxG_80.jpg', 'moon_day_WaxG_85.jpg', 'moon_day_WaxG_90.jpg', 'moon_day_WaxG_95.jpg', 'rise_FirstQuarter.jpg', 'rise_FullMoon.jpg', 'rise_LastQuarter.jpg', 'rise_NewMoon.jpg', 'rise_WaningCrescent.jpg', 'rise_WaningGibbous.jpg', 'rise_WaxingCrescent.jpg', 'rise_WaxingGibbous.jpg']
###################################                  phases patterns
phasespatterns = ['Full Moon', 'New Moon', 'First Quarter', 'Last Quarter', 'Waxing Crescent', 'Waxing Gibbous', 'Waning Gibbous', 'Waning Crescent']
###################################                  chars patterns
#charspatterns = ['(', ')', ',', '<', ';', ' ', '%', "'"]
###################################                  chars patterns
#charspatterns2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December','(', ')', ',', '<', ';', ' ', '%', "'"]
###################################                  alphabet patterns
alphabetpatterns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'z']
###################################                  website url
url = 'https://www.moongiant.com/phase/today/'
res = requests.get(url)
data = res
###################################                  get the HTML page source code in a txt file named RAW.TXT
with open(filepath, 'w') as f:
    f.write(data.text)
###################################                  strip HTML and save in file RAWSTRIPPED.TXT
cleaner = Cleaner(tags=['img'], attributes={'img': ['srcset']}, styles=[], protocols=[], strip=True, strip_comments=True, filters=None)
fo = open(filepath2, 'w')
fo.write(cleaner.clean(data.text))
fo.close()
###################################                  delete no usefull rows from the previous txt file and save in RAWSTRIPPEDCLEAN.TXT
with open(filepath2) as old, open(filepath3, 'w') as new:
    lines = old.readlines()
    new.writelines(lines[950:-180])
###################################                 delete empty rows and save in RAWSTRIPPEDCLEANROWS.TXT
with open(filepath3) as infile, open(filepath4, 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)  # non-empty line. Write it to output
###################################                  GET THE ILLUMINATION NUMBER
with open(filepath4) as fo:
    lines = fo.read().splitlines()
lines[3] = lines[3].strip()
illumi3 = lines[3]
lines[5] = lines[5].strip()
illumi5 = lines[5]
lines[9] = lines[9].strip()
illumi9 = lines[9]
lines[11] = lines[11].strip()
illumi11 = lines[11]
illumi3 = illumi3[-3:]
if illumi3 == '00%':
   illumi3 = '100%'
illumi5 = illumi5[-3:]
if illumi5 == '00%':
   illumi5 = '100%'
illumi9 = illumi9[-3:]
if illumi9 == '00%':
   illumi9 = '100%'
illumi11 = illumi11[-3:]
if illumi11 == '00%':
   illumi11 = '100%'
for pattern in alphabetpatterns:
   if re.findall(pattern, illumi3):
      illumi3 = illumi3[1:]
   if re.findall(pattern, illumi5):
      illumi5 = illumi5[1:]
   if re.findall(pattern, illumi9):
      illumi9 = illumi9[1:]
   if re.findall(pattern, illumi11):
      illumi11 = illumi11[1:]  
###################################                  write the illumination
fo = open(filepath5, 'w')
fo.write('{}\n'.format(illumi3))
fo.write('{}\n'.format(illumi5))
fo.write('{}\n'.format(illumi9))
fo.write('{}\n'.format(illumi11))
fo.close()
###################################                  find the match for the phases and write them
for pattern in phasespatterns:
   if re.findall(pattern, lines[3]):
       lines[3] = re.findall(pattern, lines[3])
       lines[3] = str(lines[3]).replace("[", "")
       lines[3] = str(lines[3]).replace("]", "")
       lines[3] = str(lines[3]).replace("'", "")
   if re.findall(pattern, lines[5]):
       lines[5] = re.findall(pattern, lines[5])
       lines[5] = str(lines[5]).replace("[", "")
       lines[5] = str(lines[5]).replace("]", "")
       lines[5] = str(lines[5]).replace("'", "")
   if re.findall(pattern, lines[9]):
       lines[9] = re.findall(pattern, lines[9])
       lines[9] = str(lines[9]).replace("[", "")
       lines[9] = str(lines[9]).replace("]", "")
       lines[9] = str(lines[9]).replace("'", "")
   if re.findall(pattern, lines[11]):
       lines[11] = re.findall(pattern, lines[11])
       lines[11] = str(lines[11]).replace("[", "")
       lines[11] = str(lines[11]).replace("]", "")
       lines[11] = str(lines[11]).replace("'", "")
fo = open(filepath9, 'w')
fo.write('day-2: {}\n'.format(lines[3]))
fo.write('day-1: {}\n'.format(lines[5]))
fo.write('day+1: {}\n'.format(lines[9]))
fo.write('day+2: {}\n'.format(lines[11]))
fo.close()
###################################                 get the 5 moon pics (for the before and after days), the phases description and the rise image  (rows count start from zero)
with open(filepath) as fo:
    linespics = fo.read().splitlines()
linespics[rm2i] = str(linespics[rm2i]).strip()
linespics[rm2p] = str(linespics[rm2p]).strip()
linespics[rm1i] = str(linespics[rm1i]).strip()
linespics[rm1p] = str(linespics[rm1p]).strip()
linespics[rti] = str(linespics[rti]).strip()
linespics[rp1i] = str(linespics[rp1i]).strip()
linespics[rp1p] = str(linespics[rp1p]).strip()
linespics[rp2i] = str(linespics[rp2i]).strip()
linespics[rp2p] = str(linespics[rp2p]).strip()
linespics[rimm] = str(linespics[rimm]).strip()
linespics[rm2i] = linespics[rm2i][:-40]
linespics[rm2i] = linespics[rm2i][80:]
linespics[rm1i] = linespics[rm1i][:-40]
linespics[rm1i] = linespics[rm1i][80:]
linespics[rti] = linespics[rti][:-40]
linespics[rti] = linespics[rti][70:]
linespics[rp1i] = linespics[rp1i][:-40]
linespics[rp1i] = linespics[rp1i][80:]
linespics[rp2i] = linespics[rp2i][:-40]
linespics[rp2i] = linespics[rp2i][80:]
linespics[rimm] = linespics[rimm][:-20]
linespics[rimm] = linespics[rimm][500:]
##################################                  find the match for the moon images to show
linespics[rm2i] = re.findall(r'\b(moon_day_+)(\w+)(.png\b)', linespics[rm2i], re.IGNORECASE)
linespics[rm2i] = str(linespics[rm2i]).replace("(", "")
linespics[rm2i] = str(linespics[rm2i]).replace(")", "")
linespics[rm2i] = str(linespics[rm2i]).replace("[", "")
linespics[rm2i] = str(linespics[rm2i]).replace("]", "")
linespics[rm2i] = str(linespics[rm2i]).replace(" ", "")
linespics[rm2i] = str(linespics[rm2i]).replace(",", "")
linespics[rm2i] = str(linespics[rm2i]).replace("'", "")
linespics[rm1i] = re.findall(r'\b(moon_day_+)(\w+)(.png\b)', linespics[rm1i], re.IGNORECASE)
linespics[rm1i] = str(linespics[rm1i]).replace("(", "")
linespics[rm1i] = str(linespics[rm1i]).replace(")", "")
linespics[rm1i] = str(linespics[rm1i]).replace("[", "")
linespics[rm1i] = str(linespics[rm1i]).replace("]", "")
linespics[rm1i] = str(linespics[rm1i]).replace(" ", "")
linespics[rm1i] = str(linespics[rm1i]).replace(",", "")
linespics[rm1i] = str(linespics[rm1i]).replace("'", "")
linespics[rti] = re.findall(r'\b(moon_day_+)(\w+)(.jpg\b)', linespics[rti], re.IGNORECASE)
linespics[rti] = str(linespics[rti]).replace("(", "")
linespics[rti] = str(linespics[rti]).replace(")", "")
linespics[rti] = str(linespics[rti]).replace("[", "")
linespics[rti] = str(linespics[rti]).replace("]", "")
linespics[rti] = str(linespics[rti]).replace(" ", "")
linespics[rti] = str(linespics[rti]).replace(",", "")
linespics[rti] = str(linespics[rti]).replace("'", "")
linespics[rti] = linespics[rti][:-3]
linespics[rti] = linespics[rti] + 'png'
linespics[rp1i] = re.findall(r'\b(moon_day_+)(\w+)(.png\b)', linespics[rp1i], re.IGNORECASE)
linespics[rp1i] = str(linespics[rp1i]).replace("(", "")
linespics[rp1i] = str(linespics[rp1i]).replace(")", "")
linespics[rp1i] = str(linespics[rp1i]).replace("[", "")
linespics[rp1i] = str(linespics[rp1i]).replace("]", "")
linespics[rp1i] = str(linespics[rp1i]).replace(" ", "")
linespics[rp1i] = str(linespics[rp1i]).replace(",", "")
linespics[rp1i] = str(linespics[rp1i]).replace("'", "")
linespics[rp2i] = re.findall(r'\b(moon_day_+)(\w+)(.png\b)', linespics[rp2i], re.IGNORECASE)
linespics[rp2i] = str(linespics[rp2i]).replace("(", "")
linespics[rp2i] = str(linespics[rp2i]).replace(")", "")
linespics[rp2i] = str(linespics[rp2i]).replace("[", "")
linespics[rp2i] = str(linespics[rp2i]).replace("]", "")
linespics[rp2i] = str(linespics[rp2i]).replace(" ", "")
linespics[rp2i] = str(linespics[rp2i]).replace(",", "")
linespics[rp2i] = str(linespics[rp2i]).replace("'", "")
linespics[rimm] = re.findall(r'\b(rise_+)(\w+)(.jpg\b)', linespics[rimm], re.IGNORECASE)
linespics[rimm] = str(linespics[rimm]).replace("(", "")
linespics[rimm] = str(linespics[rimm]).replace(")", "")
linespics[rimm] = str(linespics[rimm]).replace("[", "")
linespics[rimm] = str(linespics[rimm]).replace("]", "")
linespics[rimm] = str(linespics[rimm]).replace(" ", "")
linespics[rimm] = str(linespics[rimm]).replace(",", "")
linespics[rimm] = str(linespics[rimm]).replace("'", "")
###################################                 copy the moon images into main directory
original1 = filepath7 + linespics[rm2i]
target1 = '/home/' + homename + '/.conky/moon/Moongiant_python/m2.png'
shutil.copyfile(original1, target1)
original2 = filepath7 + linespics[rm1i]
target2 = '/home/' + homename + '/.conky/moon/Moongiant_python/m1.png'
shutil.copyfile(original2, target2)
original3 = filepath7 + linespics[rti]
target3 = '/home/' + homename + '/.conky/moon/Moongiant_python/0.png'	
shutil.copyfile(original3, target3)
original4 = filepath7 + linespics[rp1i]
target4 = '/home/' + homename + '/.conky/moon/Moongiant_python/p1.png'
shutil.copyfile(original4, target4)
original5 = filepath7 + linespics[rp2i]
target5 = '/home/' + homename + '/.conky/moon/Moongiant_python/p2.png'
shutil.copyfile(original5, target5)
original6 = filepath8 + linespics[rimm]
target6 = filepath10
shutil.copyfile(original6, target6)
###################################                 create path for moon images and write into file
linespics[rm2i] = filepath7 + linespics[rm2i]
linespics[rm1i] = filepath7 + linespics[rm1i]
linespics[rti] = filepath7 + linespics[rti]
linespics[rp1i] = filepath7 + linespics[rp1i]
linespics[rp2i] = filepath7 + linespics[rp2i]
linespics[rimm] = filepath8 + linespics[rimm]
fo = open(filepath6, 'w')
fo.write('{}\n'.format(linespics[rm2i]))
fo.write('{}\n'.format(linespics[rm1i]))
fo.write('{}\n'.format(linespics[rti]))
fo.write('{}\n'.format(linespics[rp1i]))
fo.write('{}\n'.format(linespics[rp2i]))
fo.write('{}\n'.format(linespics[rimm]))
fo.close()