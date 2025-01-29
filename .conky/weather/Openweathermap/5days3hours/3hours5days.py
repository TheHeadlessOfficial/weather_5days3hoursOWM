import os, sys
from PIL import Image
import requests
import time
import datetime
import json
import pprint
import urllib.request
# import module GEOPY
from geopy.geocoders import Photon
# initialize Nominatim API or Photon API
geolocator = Photon(user_agent="measurements")
################################ my API url forecast (insert it between apostrophe, DON'T delete apostrophes)
# set latitude and longitude
mylat = 45.40713
mylon = 11.87680
myAPPID = '51d41d4eb55111816d8609d52d702acc'
#url5days3hours = https://api.openweathermap.org/data/2.5/weather?lat=45.40713&lon=11.87680&units=metric&appid=51d41d4eb55111816d8609d52d702acc
url_current = 'https://api.openweathermap.org/data/2.5/weather?lat=' + str(mylat) + '&lon=' + str(mylon) + '&units=metric&appid=' + myAPPID
res_current = requests.get(url_current).json()
datacurrent = res_current
url_forecast = 'https://api.openweathermap.org/data/2.5/forecast?lat=' + str(mylat) + '&lon=' + str(mylon) + '&units=metric&appid=' + myAPPID
res_forecast = requests.get(url_forecast).json()
dataforecast = res_forecast
################################ get your HOME name automatically
homepath = os.environ['HOME']
homename = homepath
homename = homename[6:]
################################ set variables
vminutely = 60
vhourly = 40
vdaily = 40
vtext = 'n/a'
temporary = ''
grouph = 19
groupd = 28
################################ set error variables
coderrcurrent = 0
coderrforecast = 0
################################ create variables for GENERAL data
lat = 0
lon = 0
tz = ''
tz_off = 0
################################ create variables and array for CURRENT data
cdt = ''
csunrise = []
csunset = []
ctemp = 0
ctempfeelslike = 0
cpressure = 0
chumidity = 0
cdew_point = 0
cuvi = 0
cclouds = 0
cvisibility = 0
cwindspeed = 0
cwinddeg = 0
cwindgust = 0
crain1 = 0
csnow1 = 0
cidw = 0
cmain = ""
cdesc = ""
cicon = ""
cidw2 = 0
cmain2 = ""
cdesc2 = ""
cicon2 = ""
################################ create array for MINUTELY data
mdt = []
mprecip = []
################################ create array for HOURLY data
hdt = []
htemp = []
htempfeelslike = []
hpressure = []
hhumidity = []
hdew_point = []
huvi = []
hclouds = []
hvisibility =[]
hwindspeed = []
hwinddeg = []
hwindgust = []
hidw = []
hmain = []
hdesc = []
hicon = []
hpop = []
hrain = []
hsnow = []
################################ create array for DAILY data
ddt = []
dsunrise = []
dsunset = []
dmoonrise = []
dmoonset = []
dmoonphase = []
dday = []
dmin = []
dmax = []
dnight = []
deve = []
dmorn = []
ddayfs = []
dnightfs = []
devefs = []
dmornfs = []
dpressure = []
dhumidity = []
ddew_point = []
dwindspeed = []
dwinddeg = []
dwindgust = []
didw = []
dmain = []
ddesc = []
dicon = []
dclouds = []
dpop = []
duvi = []
drain = []
dsnow = []
################################ create variables for ALERTS data
asender_name = []
aevent = []
astart = []
aend = []
adesc = []
################################ set the tyemp paths
conky = '/conkyGITHUB/'
################################ set the paths for the ERROR
perrcurr = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/-errorcurr.txt'
perrfore = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/-errorfore.txt'
################################ set the paths for the API files
pgen = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/-general.txt'
pcur = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/-current.txt'
pmin = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/-minutely.txt'
phou = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/-hourly.txt'
pdai = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/-daily.txt'
################################ set the paths for the FLAGS
pflags = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/-flags.txt'
################################ set the paths for the GEOPY TIMEZONE data
pgeopy = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/-geopy.txt'
################################ set the paths for the logo
pathowmlogo = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/owmicon.txt'
################################ set the paths for the compass windrose
pathwindrose = "${image $HOME" + conky + "weather/compass/windsrose.png -p 305,70 -s 100x100}"
################################ set the paths for the CURRENT cicon
pathcicon = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/currenticon.txt'
################################ set the paths for the CURRENT cicon2
pathcicon2 = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/currenticon2.txt'
################################ set the paths for the COMPASS
patharrowt = '/home/' + homename + conky + 'weather/compass/arrowt.png'
patharrowt2 = '/home/' + homename + conky + 'weather/compass/arrowt2.png' 
pathcurcom = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/currentcompass.txt'
patharrow = '/home/' + homename + conky + 'weather/compass/arrow.png'
patharrow2 = '/home/' + homename + conky + 'weather/compass/arrow2.png'
################################ set the paths for the icons HOT and COLD
pathiconhot = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/currenticonhot.txt'
pathiconcold = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/currenticoncold.txt'
################################ set the paths for the DEW POINT (CURRENT, HOURLY, DAILY)
pathdewpc = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/currentowmdewpoint.txt'
pathdewph = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/hourlyowmdewpoint.txt'
pathdewpd = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/dailyowmdewpoint.txt'
################################ set the paths for the UVI INDEX (CURRENT, HOURLY, DAILY)
pathuvic = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/currentowmuvindex.txt'
pathuvih = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/hourlyowmuvindex.txt'
pathuvid = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/dailyowmuvindex.txt'
################################ set the paths for the CURRENT section
pathcur = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/current.txt'
################################ set the paths for the HOURLY section
pathhours = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/nexthours.txt'
################################ set the paths for the DAILY section
pathdays = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/nextdays.txt'
################################ set the paths for the ALERTS section
palerts = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/-alerts.txt'
################################ set the paths for the ALERTS for conky
palertsc = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/alerts.txt'
################################ set the paths for the MOON
pmoon = '/home/' + homename + conky + 'weather/Openweathermap/5days3hours/moon.txt'
################################ compass angle
myd = 72   # <--- insert angle of your North in 'myd'
tdeg = 0
################################ get data for ERROR section CURRENT
try:
    coderrcurrent = str(datacurrent['cod'])
except:
    coderrcurrent = 'error'
print(coderrcurrent)
################################ get data for ERROR section FORECAST
try:
    coderrforecast = str(dataforecast['cod'])
except:
    coderrforecast = 'error'
################################ write raw data for ERROR section CURRENT
fo = open(perrcurr, 'w')
fo.write('error: {}\n'.format(coderrcurrent))
fo.close()
################################ write raw data for ERROR section FORECAST
fo = open(perrfore, 'w')
fo.write('error: {}\n'.format(coderrforecast))
fo.close()
################################ get data for GENERAL section
lat = datacurrent['coord']['lat']
lon = datacurrent['coord']['lon']
tz = "Europa/Roma" #data['timezone']
tz = tz + '        '
tz_off = datacurrent['timezone']
################################ write raw data for GENERAL section
fo = open(pgen, 'w')
fo.write('lat: {}\n'.format(lat))
fo.write('lon: {}\n'.format(lon))
fo.write('TimeZone: {}\n'.format(tz))
fo.write('TimeZoneoffset: {}\n'.format(tz_off))
fo.close()
############################################### GEOPY NEW SYNTAX
urlGeopy = 'https://photon.komoot.io/reverse?lon=' + str(lon) + '&lat='  + str(lat)
resGeopy = requests.get(urlGeopy).json()
dataGeopy = resGeopy
location = urllib.request.urlopen(urlGeopy)
housenumber = "housenumber is old syntax"
road = "street is old syntax"#dataGeopy['features'][0]['properties']['street']
suburb = dataGeopy['features'][0]['properties']['district']
municipality = "municipality is old syntax"
city = dataGeopy['features'][0]['properties']['city']
county = dataGeopy['features'][0]['properties']['county']
state = dataGeopy['features'][0]['properties']['state']
country = dataGeopy['features'][0]['properties']['country']
codetemp = dataGeopy['features'][0]['properties']['countrycode']
code = codetemp.lower()
zipcode = dataGeopy['features'][0]['properties']['postcode']
################################ write raw data for GEOPY
fo = open(pgeopy, 'w')
fo.write('lat: {}\n'.format(lat))
fo.write('lon: {}\n'.format(lon))
fo.write('TimeZone: {}\n'.format(tz))
fo.write('TimeZoneoffset: {}\n'.format(tz_off))
fo.write('house number: {}\n'.format(housenumber))
fo.write('road: {}\n'.format(road))
fo.write('suburb: {}\n'.format(suburb))
fo.write('municipality: {}\n'.format(municipality))
fo.write('city: {}\n'.format(city))
fo.write('state: {}\n'.format(state))
fo.write('county: {}\n'.format(county))
fo.write('country: {}\n'.format(country))
fo.write('country_code: {}\n'.format(code))
fo.write('zip: {}\n'.format(zipcode))
#                   next row writes geopy data as dict
fo.write('addressraw: {}\n'.format(location.read()))
fo.close()
################################ create FLAG path
pi = '${image /home/'
pi2 = homename
pi3 = conky + 'flags/'
pf = '.png -p 381,0 -s 19x13}'
tot = pi + pi2 + pi3 + code + pf
if code == vtext:
   fo = open(pflags, 'w')
   tot = 'transparent'
   fo.write('{}\n'.format(tot))
elif code != vtext:
   fo = open(pflags, 'w')
   fo.write('{}\n'.format(tot))
fo.close()
################################ get data for CURRENT section
cdt = datacurrent['dt']
cdt = time.strftime("%d-%B-%Y %H:%M:%S", time.localtime(cdt))
csunrise = datacurrent['sys']['sunrise']
csunset = datacurrent['sys']['sunset']
cdiffss = csunset - csunrise
cdiffss = time.strftime("%H:%M:%S %Z", time.localtime(cdiffss))
csunrise = time.strftime("%H:%M:%S %Z", time.localtime(csunrise))
csunset = time.strftime("%H:%M:%S %Z", time.localtime(csunset))
ctemp = datacurrent['main']['temp']
ctempfeelslike = datacurrent['main']['feels_like']
cpressure = datacurrent['main']['pressure']
chumidity = datacurrent['main']['humidity']
cdew_point = vtext #data['current']['dew_point']
cuvi = vtext #data['current']['uvi']
cclouds = datacurrent['clouds']['all']
cvisibility = datacurrent['visibility']
#                   cwindspeed is in m/s as default value
cwindspeed = datacurrent['wind']['speed']
#                   transform in Km/h (if you want m/s put a # at the beginning of the next row)
cwindspeed = round(cwindspeed * 3.6, 2)
cwinddeg = datacurrent['wind']['deg']
try:
   cwindgust = datacurrent['wind']['gust']
#                   transform in Km/h (if you want m/s put a # at the beginning of the next row)
   cwindgust = round(cwindgust * 3.6, 2)
except:
   cwindgust = vtext
try:
   crain1 = datacurrent['current']['rain']['1h']
except:
   crain1 = vtext
try:
   csnow1 = datacurrent['current']['snow']['1h']
except:
   csnow1 = vtext
cidw = datacurrent['weather'][0]['id']
cmain = datacurrent['weather'][0]['main']
cdesc = datacurrent['weather'][0]['description']
cicon = datacurrent['weather'][0]['icon']
try:
   cidw2 = datacurrent['weather'][1]['id']
except:
   cidw2 = vtext
try:
   cmain2 = datacurrent['weather'][1]['main']
except:
   cmain2 = vtext
try:
   cdesc2 = datacurrent['weather'][1]['description']
except:
   cdesc2 = vtext
try:
   cicon2 = datacurrent['weather'][1]['icon']
except:
   cicon2 = vtext
################################ write raw data for CURRENT section
fo = open(pcur, 'w')
fo.write('dt: {}\n'.format(cdt))
fo.write('SUNRISE: {}\n'.format(csunrise))
fo.write('SUNSET: {}\n'.format(csunset))
fo.write('temp: {}\n'.format(ctemp))
fo.write('feels: {}\n'.format(ctempfeelslike))
fo.write('PRESSURE: {}\n'.format(cpressure))
fo.write('HUMIDITY: {}\n'.format(chumidity))
fo.write('DEWPOINT: {}\n'.format(cdew_point))
fo.write('UVI: {}\n'.format(cuvi))
fo.write('CLOUDS: {}\n'.format(cclouds))
fo.write('VISIBILITY: {}\n'.format(cvisibility))
fo.write('windspeed: {}\n'.format(cwindspeed))
fo.write('winddeg: {}\n'.format(cwinddeg))
fo.write('windgust: {}\n'.format(cwindgust))
fo.write('rain1h: {}\n'.format(crain1))
fo.write('snow1h: {}\n'.format(csnow1))
fo.write('idw: {}\n'.format(cidw))
fo.write('main: {}\n'.format(cmain))
fo.write('description: {}\n'.format(cdesc))
fo.write('icon: {}\n'.format(cicon))
fo.write('idw2: {}\n'.format(cidw2))
fo.write('main2: {}\n'.format(cmain2))
fo.write('description2: {}\n'.format(cdesc2))
fo.write('icon2: {}\n'.format(cicon2))
fo.write('cdiffss: {}\n'.format(cdiffss))
fo.close()
################################ get data for HOURLY section
for i in range(0, vhourly):
    temporary = dataforecast['list'][i]['dt']
    temporary = time.strftime("%d-%B-%Y %H:%M:%S", time.localtime(temporary))
    hdt.append(temporary)
    htemp.append(dataforecast['list'][i]['main']['temp'])
    htempfeelslike.append(dataforecast['list'][i]['main']['feels_like'])
    hpressure.append(dataforecast['list'][i]['main']['pressure'])
    hhumidity.append(dataforecast['list'][i]['main']['humidity'])
    hdew_point.append(vtext)
    huvi.append(vtext)
    hclouds.append(dataforecast['list'][i]['clouds']['all'])
    hvisibility.append(dataforecast['list'][i]['visibility'])
    hwindspeed.append(dataforecast['list'][i]['wind']['speed'])
    hwinddeg.append(dataforecast['list'][i]['wind']['deg'])
    try:
       hwindgust.append(dataforecast['list'][i]['wind']['gust'])
    except:
       hwindgust[i] = vtext
    hidw.append(dataforecast['list'][i]['weather'][0]['id'])
    hmain.append(dataforecast['list'][i]['weather'][0]['main'])
    hdesc.append(dataforecast['list'][i]['weather'][0]['description'])
    hicon.append(dataforecast['list'][i]['weather'][0]['icon'])
    hpop.append(vtext)
    try:
        hrain.append(dataforecast['list'][i]['rain']['1h'])
    except:
        hrain.append(vtext)
    try:
        hsnow.append(dataforecast['list'][i]['snow']['1h'])
    except:
        hsnow.append(vtext)
################################ write raw data for HOURLY section
fo = open(phou, 'w')
for i in range(0, vhourly):
    fo.write('dt: {}\n'.format(hdt[i]))
    fo.write('temp: {}\n'.format(htemp[i]))
    fo.write('feelslike: {}\n'.format(htempfeelslike[i]))
    fo.write('pressure: {}\n'.format(hpressure[i]))
    fo.write('humidity: {}\n'.format(hhumidity[i]))
    fo.write('dewpoint: {}\n'.format(hdew_point[i]))
    fo.write('uvi: {}\n'.format(huvi[i]))
    fo.write('clouds: {}\n'.format(hclouds[i]))
    fo.write('visibility: {}\n'.format(hvisibility[i]))
#                   transform in Km/h (if you want m/s put a # at the beginning of the next row)
    hwindspeed[i] = round(hwindspeed[i] * 3.6, 2)
    fo.write('windspeed: {}\n'.format(hwindspeed[i]))
    fo.write('winddeg: {}\n'.format(hwinddeg[i]))
#                   transform in Km/h (if you want m/s put a # at the beginning of the next 2 rows)
    if hwindgust[i] != vtext:
        hwindgust[i] = round(hwindgust[i] * 3.6, 2)
    fo.write('windgust: {}\n'.format(hwindgust[i]))
    fo.write('idw: {}\n'.format(hidw[i]))
    fo.write('main: {}\n'.format(hmain[i]))
    fo.write('description: {}\n'.format(hdesc[i]))
    fo.write('icon: {}\n'.format(hicon[i]))
    fo.write('pop: {}\n'.format(hpop[i]))
    fo.write('rain1h: {}\n'.format(hrain[i]))
    fo.write('snow1h: {}\n'.format(hsnow[i]))
fo.close()
################################ get data for DAILY section
for i in range(0, vdaily):
    temporary = dataforecast['list'][i]['dt']
    temporary = time.strftime("%d-%B-%Y %H:%M:%S", time.localtime(temporary))
    ddt.append(temporary)
    temporary = vtext
    dsunrise.append(temporary)
    temporary = vtext
    dsunset.append(temporary)
    temporary = vtext
    dmoonrise.append(temporary)
    temporary = vtext
    dmoonset.append(temporary)
    dmoonphase.append(vtext)
    dmin.append(dataforecast['list'][i]['main']['temp_min'])
    dmax.append(dataforecast['list'][i]['main']['temp_max'])
    dnight.append(vtext)
    deve.append(vtext)
    dmorn.append(vtext)
    ddayfs.append(vtext)
    dnightfs.append(vtext)
    devefs.append(vtext)
    dmornfs.append(vtext)
    dpressure.append(dataforecast['list'][i]['main']['pressure'])
    dhumidity.append(dataforecast['list'][i]['main']['humidity'])
    ddew_point.append(vtext)
    dwindspeed.append(dataforecast['list'][i]['wind']['speed'])
    dwinddeg.append(dataforecast['list'][i]['wind']['deg'])
    try:
        dwindgust.append(dataforecast['list'][i]['wind']['gust'])
    except:
        dwindgust.append(vtext)
    didw.append(dataforecast['list'][i]['weather'][0]['id'])
    dmain.append(dataforecast['list'][i]['weather'][0]['main'])
    ddesc.append(dataforecast['list'][i]['weather'][0]['description'])
    dicon.append(dataforecast['list'][i]['weather'][0]['icon'])
    dclouds.append(dataforecast['list'][i]['clouds']['all'])
    dpop.append(vtext)
    try:
        drain.append(dataforecast['list'][i]['rain'])
    except:
        drain.append(vtext)
    try:
        dsnow.append(dataforecast['list'][i]['snow'])
    except:
        dsnow.append(vtext)
    duvi.append(vtext)
################################ write raw data for DAILY section
fo = open(pdai, 'w')
for i in range(0, vdaily):
    fo.write('dt: {}\n'.format(ddt[i]))
    fo.write('sunrise: {}\n'.format(dsunrise[i]))
    fo.write('sunset: {}\n'.format(dsunset[i]))
    fo.write('tempday: {}\n'.format(dday[i]))
    fo.write('min: {}\n'.format(dmin[i]))
    fo.write('max: {}\n'.format(dmax[i]))
    fo.write('tempnight: {}\n'.format(dnight[i]))
    fo.write('tempeve: {}\n'.format(deve[i]))
    fo.write('tempmorn: {}\n'.format(dmorn[i]))
    fo.write('tempdayfeel: {}\n'.format(ddayfs[i]))
    fo.write('tempnightfeel: {}\n'.format(dnightfs[i]))
    fo.write('tempevefeel: {}\n'.format(devefs[i]))
    fo.write('tempmornfeel: {}\n'.format(dmornfs[i]))
    fo.write('pressure: {}\n'.format(dpressure[i]))
    fo.write('humidity: {}\n'.format(dhumidity[i]))
    fo.write('dewpoint: {}\n'.format(ddew_point[i]))
#                   transform in Km/h (if you want m/s put a # at the beginning of the next row)
    dwindspeed[i] = round(dwindspeed[i] * 3.6, 2)
    fo.write('windspeed: {}\n'.format(dwindspeed[i]))
    fo.write('winddeg: {}\n'.format(dwinddeg[i]))
#                   transform in Km/h (if you want m/s put a # at the beginning of the next 2 rows)
    if dwindgust[i] != vtext:
        dwindgust[i] = float(round(dwindgust[i] * 3.6, 2))
    fo.write('windgust: {}\n'.format(dwindgust[i]))
    fo.write('idw: {}\n'.format(didw[i]))
    fo.write('main: {}\n'.format(dmain[i]))
    fo.write('description: {}\n'.format(ddesc[i]))
    fo.write('icon: {}\n'.format(dicon[i]))
    fo.write('clouds: {}\n'.format(dclouds[i]))
    fo.write('pop: {}\n'.format(dpop[i]))
    fo.write('dailyrain: {}\n'.format(drain[i]))
    fo.write('dailysnow: {}\n'.format(dsnow[i]))
    fo.write('uvi: {}\n'.format(duvi[i]))
fo.close()
################################ create the path for openweathermap logo icon
pi = '${image /home/'
pi2 = homename
pi3 = conky + 'weather/Openweathermap/owmicon'
est = '.png -p '
x = 280
virg = ','
y = 460
pf = ' -s 140x140}'
fo = open(pathowmlogo, 'w')
tot = pi + pi2 + pi3 + est + str(x) + virg + str(y) + pf
fo.write('{}\n'.format(tot))
fo.close()
################################ create CURRENT cicon path
pi = '${image /home/'
pi2 = homename
pi3 = conky + 'weather/Openweathermap/icons/'
icontemp = (cicon[2:3])
pf = '.png -p 0,30 -s 160x120}'
tot = pi + pi2 + pi3 + str(cidw) + icontemp + pf
if icontemp == 'd':
   fo = open(pathcicon, 'w')
   fo.write('{}\n'.format(tot))
elif icontemp == 'n':
   fo = open(pathcicon, 'w')
   fo.write('{}\n'.format(tot))
fo.close()
################################ create CURRENT cicon2 path
pi = '${image /home/'
pi2 = homename
pi3 = conky + 'weather/Openweathermap/icons/'
pi4 = conky + 'weather/Openweathermap/owmicon'
pitest = conky + 'weather/Openweathermap/test2'
icontemp = (cicon2[2:3])
pf = '.png -p 240,73 -s 40x28}'
pfowmiconsmall = '.png -p 245,60 -s 65x65}'
pfowmiconbig = '.png -p 185,0 -s 75x75}'
tot = pi + pi2 + pi3 + str(cidw2) + icontemp + pf
totowmiconsmall = pi + pi2 + pi4 + pfowmiconsmall
totowmiconbig = pi + pi2 + pi4 + pfowmiconbig
if cicon2 != vtext:
   if icontemp == 'd':
      fo = open(pathcicon2, 'w')
      fo.write('{}\n'.format(tot + totowmiconbig))
   elif icontemp == 'n':
      fo = open(pathcicon2, 'w')
      fo.write('{}\n'.format(tot + totowmiconbig))
   fo.close()
elif cicon2 == vtext:
   cidw2 = 'transparent'
   tot2 = pi + pi2 + pi3 + cidw2 + pf
   fo = open(pathcicon2, 'w')
   fo.write('{}\n'.format(totowmiconsmall))
   fo.close()
################################ write the path for COMPASS icon
#grades calculation for cwinddeg, trasparent image if no wind (use negative tdeg to rotate clockwise)
if cwinddeg == 'empty':
    tdeg = myd
    temp1 = Image.open(patharrowt)
    temp2 = temp1.rotate(-tdeg)
    temp2.save(patharrowt2)
    temp3 = '${image /home/'
    temp4 = homename
    temp5 = conky + 'weather/compass/arrowt2'
    pfcomp = '.png -p 305,70 -s 100x100}'# set this in pathwindrose too
    totcomp = temp3 + temp4 + temp5 + pfcomp
    fo = open(pathcurcom, 'w')
    fo.write('{}\n'.format(totcomp))
    fo.write('{}\n'.format(pathwindrose))
elif cwinddeg != 'empty':
    tdeg = myd + cwinddeg
    temp1 = Image.open(patharrow)
    temp2 = temp1.rotate(-tdeg)
    temp2.save(patharrow2)
    temp3 = '${image /home/'
    temp4 = homename
    temp5 = conky + 'weather/compass/arrow2'
    pfcomp = '.png -p 305,70 -s 100x100}'# set this in pathwindrose too
    totcomp = temp3 + temp4 + temp5 + pfcomp
    fo = open(pathcurcom, 'w')
    fo.write('{}\n'.format(totcomp))
    fo.write('{}\n'.format(pathwindrose))
fo.close()
################################ write thermo icon HOT path
pi = '${image /home/'
pi2 = homename
pi3 = conky + 'weather/Openweathermap/icons/'
cicon = 'hot'
pf = '.png -p 275,100 -s 14x45}'
if ctempfeelslike >= 38:
   tot = pi + pi2 + pi3 + str(cicon) + pf
   fo = open(pathiconhot, 'w')
   fo.write('{}\n'.format(tot))
   fo.close()
else:
   cicon = 'transparent'
   tot = pi + pi2 + pi3 + str(cicon) + pf
   fo = open(pathiconhot, 'w')
   fo.write('{}\n'.format(tot))
   fo.close()
################################ write thermo icon COLD path
cicon = 'cold'
if ctempfeelslike <= 0:
   tot = pi + pi2 + pi3 + str(cicon) + pf
   fo = open(pathiconcold, 'w')
   fo.write('{}\n'.format(tot))
   fo.close()
else:
   cicon = 'transparent'
   tot = pi + pi2 + pi3 + str(cicon) + pf
   fo = open(pathiconcold, 'w')
   fo.write('{}\n'.format(tot))
   fo.close()
################################ calculate CURRENT dew point color and write it
dpc = cdew_point
color = 'white'
#      calculate the DEW POINT color font based on index
if (dpc == vtext):
    color = ''
elif (dpc < 19):
    color = 6
elif (dpc >=19 and dpc < 22):
    color = 9
elif (dpc >=22):
    color = 4
else:
    color = ''
fo = open(pathdewpc, 'w')
fo.write('{}\n'.format(cdew_point))
fo.write('{}\n'.format(color))
fo.close()
############################### calculate HOURLY dew point color and write it
color = 'white'
#      calculate the DEW POINT color font based on index
fo = open(pathdewph, 'w')
for i in range(0, vhourly):
    value = hdew_point[i]
    if (value == vtext):
        color = ''
    elif (value < 19):
        color = 6
    elif (value >=19 and value < 22):
        color = 9
    elif (value >=22):
        color = 4
    else:
        color = 'white'
    fo.write('{}\n'.format(value))
    fo.write('{}\n'.format(color))
fo.close()
############################### calculate DAILY dew point color and write it
color = 'white'
#      calculate the DEW POINT color font based on index
fo = open(pathdewpd, 'w')
for i in range(0, vdaily):
    value = ddew_point[i]
    if (value == vtext):
        color = ''
    elif (value < 19):
        color = 6
    elif (value >=19 and value < 22):
        color = 9
    elif (value >=22):
        color = 4
    else:
        color = ''
    fo.write('{}\n'.format(value))
    fo.write('{}\n'.format(color))
fo.close()
############################### calculate CURRENT UV index color and write it
value = cuvi
if (value == vtext):
    color = ''
elif (value >=0 and value < 3):
    color = 6
elif (value >=3 and value < 6):
    color = 9
elif (value >=6 and value < 8):
    color = 3
elif (value >=8 and value < 11):
    color = 4
elif (value >= 11):
    color = 0
else:
    color = 2
fo = open(pathuvic, 'w')
fo.write('{}\n'.format(value))
fo.write('{}\n'.format(color))
fo.close()
############################### calculate HOURLY UV index color and write it
fo = open(pathuvih, 'w')
for i in range(0, vhourly):
    value = huvi[i]
    if (value == vtext):
        color = ''
    elif (value >=0 and value < 3):
        color = 6
    elif (value >=3 and value < 6):
        color = 9
    elif (value >=6 and value < 8):
        color = 3
    elif (value >=8 and value < 11):
        color = 4
    elif (value >= 11):
        color = 0
    else:
        color = 2
    fo.write('{}\n'.format(value))
    fo.write('{}\n'.format(color))
fo.close()
############################### calculate DAILY UV index color and write it
fo = open(pathuvid, 'w')
for i in range(0, vdaily):
    value = duvi[i]
    if (value == vtext):
        color = ''
    elif (value >=0 and value < 3):
        color = 6
    elif (value >=3 and value < 6):
        color = 9
    elif (value >=6 and value < 8):
        color = 3
    elif (value >=8 and value < 11):
        color = 4
    elif (value >= 11):
        color = 0
    else:
        color = 2
    fo.write('{}\n'.format(value))
    fo.write('{}\n'.format(color))
fo.close()
# ################################ create CURRENT, HOURLY and DAILY section
# #                 main CURRENT in current.txt
# owmpylogo = "${image $HOME" + conky + "weather/Openweathermap/python_logo.png -p 145,0 -s 15x15}"
# infotz = "${color2}${font = 'URW Gothic L:size=8'}OPENWEATHERMAP${font}${color1}${alignr}${execpi 900 sed -n '3p' $HOME" + conky + "weather/Openweathermap/5days3hours/-general.txt}"
# infotzerrcurrent = "${color2}${font = 'URW Gothic L:size=8'}OPENWEATHERMAP     ${color4}Ecurrent:" + coderrcurrent + "${font}${color1}${alignr}${execpi 900 sed -n '3p' $HOME" + conky + "weather/Openweathermap/5days3hours/-general.txt}"
# infotzerrforecast = "${color2}${font = 'URW Gothic L:size=8'}OPENWEATHERMAP     ${color4}Eforecast:" + coderrforecast + "${font}${color1}${alignr}${execpi 900 sed -n '3p' $HOME" + conky + "weather/Openweathermap/5days3hours/-general.txt}"
# latlon = "${alignr}(${execpi 900 sed -n '1p' $HOME" + conky + "weather/Openweathermap/5days3hours/-general.txt} - ${execpi 900 sed -n '2p' $HOME" + conky + "weather/Openweathermap/5days3hours/-general.txt})${font}${color}"
# curricon = "${execpi 900 sed -n '1p' $HOME" + conky + "weather/Openweathermap/5days3hours/currenticon.txt}"
# firstdesc = "${color4}${goto 190}${execpi 900 sed -n '18p' $HOME" + conky + "weather/Openweathermap/5days3hours/-current.txt | awk '{print $2}'}${color} - ${execpi 900 sed -n '19p' $HOME" + conky + "weather/Openweathermap/5days3hours/-current.txt | awk '{print $2}'}"
# seconddesc = "${color}${goto 190}${execpi 900 sed -n '22p' $HOME" + conky + "weather/Openweathermap/5days3hours/-current.txt | awk '{print $2}'}${color} - ${execpi 900 sed -n '23p' $HOME" + conky + "weather/Openweathermap/5days3hours/-current.txt | awk '{print $2}'}"
# currtemp = "${color}${goto 190}${execpi 900 sed -n '4p' $HOME" + conky + "weather/Openweathermap/5days3hours/-current.txt}${color}°C"
# currtempf = "${goto 190}(${execpi 900 sed -n '5p' $HOME" + conky + "weather/Openweathermap/5days3hours/-current.txt}°C)"
# thermo = "${execpi 900 sed -n '1p' $HOME" + conky + "weather/Openweathermap/5days3hours/currenticonhot.txt}${execpi 900 sed -n '1p' $HOME" + conky + "weather/Openweathermap/5days3hours/currenticoncold.txt}"
# minmax = "${goto 190}${color1}${execpi 900 sed -n '5p' $HOME" + conky + "weather/Openweathermap/5days3hours/-daily.txt | awk '{print $2}'}°${color}/${color4}${execpi 900 sed -n '6p' $HOME" + conky + "weather/Openweathermap/5days3hours/-daily.txt | awk '{print $2}'}°${color}C"
# winds = "${color}${goto 190}${execpi 900 sed -n '12p' $HOME" + conky + "weather/Openweathermap/5days3hours/-current.txt} Km/h"
# windg = "${color}${goto 190}${execpi 900 sed -n '14p' $HOME" + conky + "weather/Openweathermap/5days3hours/-current.txt} Km/h"
# c1 = "${goto 50}${color2}T morn(r/f): ${color}${execpi 900 sed -n '9p' $HOME" + conky + "weather/Openweathermap/5days3hours/-daily.txt | awk '{print $2}'}/${execpi 900 sed -n '13p' $HOME" + conky + "weather/Openweathermap/5days3hours/-daily.txt | awk '{print $2}'}${color2}${goto 250}V rain1h: ${color}${execpi 900 sed -n '15p' $HOME" + conky + "weather/Openweathermap/5days3hours/-current.txt | awk '{print $2}'} mm"
# c2 = "${goto 50}${color2}T day(r/f): ${color}${execpi 900 sed -n '4p' $HOME" + conky + "weather/Openweathermap/5days3hours/-daily.txt | awk '{print $2}'}/${execpi 900 sed -n '10p' $HOME" + conky + "weather/Openweathermap/5days3hours/-daily.txt | awk '{print $2}'}${color2}${goto 250}V snow1h: ${color}${execpi 900 sed -n '16p' $HOME" + conky + "weather/Openweathermap/5days3hours/-current.txt | awk '{print $2}'} mm"
# c3 = "${goto 50}${color2}T eve(r/f): ${color}${execpi 900 sed -n '8p' $HOME" + conky + "weather/Openweathermap/5days3hours/-daily.txt | awk '{print $2}'}/${execpi 900 sed -n '12p' $HOME" + conky + "weather/Openweathermap/5days3hours/-daily.txt | awk '{print $2}'}${color2}${goto 250}V dailyrain: ${color}${execpi 900 sed -n '26p' $HOME" + conky + "weather/Openweathermap/5days3hours/-daily.txt | awk '{print $2}'} mm"
# c4 = "${goto 50}${color2}T night(r/f): ${color}${execpi 900 sed -n '7p' $HOME" + conky + "weather/Openweathermap/5days3hours/-daily.txt | awk '{print $2}'}/${execpi 900 sed -n '11p' $HOME" + conky + "weather/Openweathermap/5days3hours/-daily.txt | awk '{print $2}'}${color2}${goto 250}V dailysnow: ${color}${execpi 900 sed -n '27p' $HOME" + conky + "weather/Openweathermap/5days3hours/-daily.txt | awk '{print $2}'} mm"
# c5 = "${goto 50}${color2}pop1h: ${color}${execpi 900 sed -n '38p' $HOME" + conky + "weather/Openweathermap/5days3hours/-hourly.txt | awk '{print $2}'}${color2}${goto 250}popday: ${color}${execpi 900 sed -n '25p' $HOME" + conky + "weather/Openweathermap/5days3hours/-daily.txt | awk '{print $2}'}"
# info1 = "${color2}HUMIDITY: $color${execpi 900 sed -n '7p' $HOME" + conky + "weather/Openweathermap/5days3hours/-current.txt | awk '{print $2}'}%${goto 295}${color2}PRESSURE: $color${execpi 900 sed -n '6p' $HOME" + conky + "weather/Openweathermap/5days3hours/-current.txt | awk '{print $2}'}hPa "
# info2 = "${color2}UV INDEX (${color6}0${color2}-${color0}11+${color2}): ${eval $${color${execpi 900 sed -n '2p' $HOME" + conky + "weather/Openweathermap/5days3hours/currentowmuvindex.txt}}}${execpi 900 sed -n '1p' $HOME" + conky + "weather/Openweathermap/5days3hours/currentowmuvindex.txt}${goto 295}${color2}CLOUD COVER: $color${execpi 900 sed -n '10p' $HOME" + conky + "weather/Openweathermap/5days3hours/-current.txt | awk '{print $2}'}% "
# info3 = "${color2}DEW POINT: ${eval $${color${execpi 900 sed -n '2p' $HOME" + conky + "weather/Openweathermap/5days3hours/currentowmdewpoint.txt}}}${execpi 900 sed -n '1p' $HOME" + conky + "weather/Openweathermap/5days3hours/currentowmdewpoint.txt}${color}°C${color2}${goto 295}VISIBILITY: $color${execpi 900 sed -n '11p' $HOME" + conky + "weather/Openweathermap/5days3hours/-current.txt | awk '{print $2}'}m"
# info4= "${color2}SUN R/S: $color${execpi 900 sed -n '2p' $HOME" + conky + "weather/Openweathermap/5days3hours/-current.txt | awk '{print $2}'}/${execpi 900 sed -n '3p' $HOME" + conky + "weather/Openweathermap/5days3hours/-current.txt | awk '{print $2}'}${execpi 900 sed -n '3p' $HOME" + conky + "weather/Openweathermap/5days3hours/-current.txt | awk '{print $3}'}${color2}${goto 295}SUN DURAT.: $color${execpi 900 sed -n '25p' $HOME" + conky + "weather/Openweathermap/5days3hours/-current.txt | awk '{print $2}'}${color}"
# fo = open(pathcur, 'w')
# if coderrcurrent != '200':
#     fo.write('{}\n'.format(owmpylogo + infotzerrcurrent))
# else:
#     fo.write('{}\n'.format(owmpylogo + infotz))
#     fo.write('{}\n'.format(latlon))
#     fo.write('{}\n'.format(firstdesc))
#     fo.write('{}\n'.format(seconddesc))
#     fo.write('{}\n'.format(currtemp))
#     fo.write('{}\n'.format(currtempf + thermo))
#     fo.write('{}\n'.format(minmax))
#     fo.write('{}\n'.format(winds))
#     fo.write('{}\n'.format(windg))
#     fo.write('{}\n'.format(c1))
#     fo.write('{}\n'.format(c2))
#     fo.write('{}\n'.format(c3))
#     fo.write('{}\n'.format(c4))
#     fo.write('{}\n'.format(c5))
#     fo.write('{}\n'.format(info1))
#     fo.write('{}\n'.format(info2))
#     fo.write('{}\n'.format(info3))
#     fo.write('{}\n'.format(info4))
# fo.close()
# #                 general variables
# firsth = 1
# blokh = 2
# firstd = 8
# blokd = 7
# #                 general settings
# rowgoto = '${goto '
# gotonumh = 100
# rowgraph = '}'
# rowcolor = '${color}'
# rowcolor1 = '${color1}'
# rowcolor2 = '${color2}'
# rowcolor3 = '${color3}'
# rowcolor4 = '${color4}'
# rowcolor5 = '${color5}'
# rowcolor6 = '${color6}'
# rowcolor9 = '${color9}'
# rowinfo = "${execpi 900 sed -n '"
# rowp = "p'"
# rowpathh = " $HOME" + conky + "weather/Openweathermap/5days3hours/-hourly.txt"
# rowpathd = " $HOME" + conky + "weather/Openweathermap/5days3hours/-daily.txt"
# rowprint2 = " | awk '{print $2}'"
# rowprint3 = " | awk '{print $3}'"
# rowbar = '/'
# rowfont6 = '${font URW Gothic L:size=6}'
# rowfont7 = '${font URW Gothic L:size=7}'
# rowfont8 = '${font URW Gothic L:size=8}'
# #                 time settings
# gotohourh = 50
# gotohourd = 35
# rowhour = "h${execpi 900 sed -n '"
# rowcut = ' | cut -c1-5'
# #                 icons settings
# pi = '${image /home/'
# pi2 = homename
# pi3 = conky + 'weather/Openweathermap/icons/'
# est = '.png -p '
# y = 0
# virg = ','
# zh = 325
# zd = 420
# pfh = ' -s 95x65}'
# pfd = ' -s 95x65}'
# #                 temperature, feellike settings
# rowtemph = "${execpi 900 sed -n '"
# rowtempfh = "Tf:${execpi 900 sed -n '"
# rowtempdd = "Td:${execpi 900 sed -n '"
# rowtempnd = "Tn:${execpi 900 sed -n '"
# rowtemped = "Te:${execpi 900 sed -n '"
# rowtempmd = "Tm:${execpi 900 sed -n '"
# rowtempdfd = "Tdf:${execpi 900 sed -n '"
# rowtempnfd = "Tnf:${execpi 900 sed -n '"
# rowtempefd = "Tef:${execpi 900 sed -n '"
# rowtempmfd = "Tmf:${execpi 900 sed -n '"
# rowtemp2 = '°C'
# rowtemp3 = '°'
# #                 pressure settings
# rowpres = "${execpi 900 sed -n '"
# rowpres2 = 'hPa'
# #                 humidity settings
# rowhum = "H:${execpi 900 sed -n '"
# rowhum2 = '%'
# #                 dew point settings
# rowdew = "Dp:${eval $${color${execpi 900 sed -n '"
# rowdewpathcolor1h = " $HOME" + conky + "weather/Openweathermap/5days3hours/hourlyowmdewpoint.txt}}}"
# rowdewpathcolor1d = " $HOME" + conky + "weather/Openweathermap/5days3hours/dailyowmdewpoint.txt}}}"
# #rowdewpathcolor2h = "${execpi 900 sed -n '"
# rowdewpathvalue1h = " $HOME" + conky + "weather/Openweathermap/5days3hours/hourlyowmdewpoint.txt}"
# rowdewpathvalue1d = " $HOME" + conky + "weather/Openweathermap/5days3hours/dailyowmdewpoint.txt}"
# #rowdewpathvalue2h = '${color}'
# #                 uvi settings
# rowuvi = "UV:${eval $${color${execpi 900 sed -n '"
# rowuvipathcolor1h = " $HOME" + conky + "weather/Openweathermap/5days3hours/hourlyowmuvindex.txt}}}"
# rowuvipathcolor1d = " $HOME" + conky + "weather/Openweathermap/5days3hours/dailyowmuvindex.txt}}}"
# #rowuvipathcolor2h = "${execpi 900 sed -n '"
# rowuvipathvalue1h = " $HOME" + conky + "weather/Openweathermap/5days3hours/hourlyowmuvindex.txt}"
# rowuvipathvalue1d = " $HOME" + conky + "weather/Openweathermap/5days3hours/dailyowmuvindex.txt}"
# #rowuvipathvalue2h = '${color}'
# #                 cloudness settings
# rowclo= "Cl:${execpi 900 sed -n '"
# rowclo2 = '%'
# #                 visibility settings
# rowvis= "V:${execpi 900 sed -n '"
# rowvis2 = 'm'
# #                 wind speed settings
# rowwins= "Ws:${execpi 900 sed -n '"
# rowwins2 = 'm/s'
# #                 wind gust settings
# rowwing= "Wg:${execpi 900 sed -n '"
# #                 pop settings
# rowpop= "Pop:${execpi 900 sed -n '"
# #                 rain1h settings
# rowrain1= "R1:${execpi 900 sed -n '"
# rowrain2 = 'mm'
# #                 snow1h settings
# rowsnow1= "S1:${execpi 900 sed -n '"
# rowsnow2 = 'mm'
# #                 main HOURLY (3 blocks 5-10-15 hours) in nexthours.txt
# counter = 0
# fo = open(pathhours, 'w')
# for i in range(firsth, grouph , blokh):
#     if (hicon[i][2:3]) == 'd':
#         if i == 1:
#             y = 0
#         i2 = 1 + (grouph * i)
#         totrowhourh = rowcolor + rowfont8 + rowgoto + str(gotohourh) + rowgraph + rowhour + str(i2) + rowp + rowpathh + rowprint3 + rowcut + rowgraph + rowfont7
#         gotohourh = gotohourh + 133
#         fo.write('{}\n'.format(totrowhourh))
#         totico = pi + pi2 + pi3 + str(hidw[i]) + (hicon[i][2:3]) + est + str(y) + virg + str(zh) + pfh
#         y = y + 133
#         fo.write('{}\n'.format(totico))
#         vtemp = i2 + 1
#         totrowtemp = rowgoto + str(gotonumh) + rowgraph + rowtemph + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph + rowtemp2
#         fo.write('{}\n'.format(totrowtemp))
#         vtemp = i2 + 2
#         totrowfeel = rowgoto + str(gotonumh) + rowgraph + rowtempfh + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph + rowtemp2
#         fo.write('{}\n'.format(totrowfeel))
#         vtemp = i2 + 3
#         totrowpres = rowgoto + str(gotonumh) + rowgraph + rowpres + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph + rowpres2
#         fo.write('{}\n'.format(totrowpres))
#         vtemp = i2 + 4
#         totrowhum = rowgoto + str(gotonumh) + rowgraph + rowhum + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph + rowhum2
#         fo.write('{}\n'.format(totrowhum))
#         vtemp1 = 1 + (i * 2)
#         vtemp2 = 2 + (i * 2)
#         totrowdew = rowgoto + str(gotonumh) + rowgraph + rowdew + str(vtemp2) + rowp + rowdewpathcolor1h + rowinfo + str(vtemp1) + rowp + rowdewpathvalue1h + rowcolor + rowtemp2
#         fo.write('{}\n'.format(totrowdew))
#         vtemp1 = 1 + (i * 2)
#         vtemp2 = 2 + (i * 2)
#         totrowuvi = rowgoto + str(gotonumh) + rowgraph + rowuvi + str(vtemp2) + rowp + rowuvipathcolor1h + rowinfo + str(vtemp1) + rowp + rowuvipathvalue1h + rowcolor
#         fo.write('{}\n'.format(totrowuvi))
#         vtemp = i2 + 7
#         totrowclo = rowgoto + str(gotonumh) + rowgraph + rowclo + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph  + rowclo2
#         fo.write('{}\n'.format(totrowclo))
#         vtemp = i2 + 8
#         totrowvis = rowgoto + str(gotonumh) + rowgraph + rowvis + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph + rowvis2
#         fo.write('{}\n'.format(totrowvis))
#         vtemp = i2 + 9
#         totrowwins = rowgoto + str(gotonumh) + rowgraph + rowwins + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph + rowwins2
#         fo.write('{}\n'.format(totrowwins))
#         vtemp = i2 + 11
#         totrowwing = rowgoto + str(gotonumh) + rowgraph + rowwing + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph + rowwins2
#         fo.write('{}\n'.format(totrowwing))
#         vtemp = i2 + 13
#         totrowmain = rowgoto + str(gotonumh) + rowgraph + rowinfo + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph
#         fo.write('{}\n'.format(totrowmain))
#         vtemp = i2 + 14
#         totrowdesc = rowgoto + str(gotonumh) + rowgraph + rowinfo + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph
#         fo.write('{}\n'.format(totrowdesc))
#         vtemp = i2 + 16
#         totrowpop = rowgoto + str(gotonumh) + rowgraph + rowpop + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph
#         fo.write('{}\n'.format(totrowpop))
#         vtemp = i2 + 17
#         totrowrain1 = rowgoto + str(gotonumh) + rowgraph + rowrain1 + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph + rowrain2
#         fo.write('{}\n'.format(totrowrain1))
#         vtemp = i2 + 18
#         totrowsnow1 = rowgoto + str(gotonumh) + rowgraph + rowsnow1 + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph + rowsnow2
#         fo.write('{}\n'.format(totrowsnow1))
#         gotonumh = gotonumh + 133
#         counter = counter + 1
#     elif (hicon[i][2:3]) == 'n':
#         if i == 1:
#             y = 0
#         i2 = 1 + (grouph * i)
#         totrowhourh = rowcolor + rowfont8 + rowgoto + str(gotohourh) + rowgraph + rowhour + str(i2) + rowp + rowpathh + rowprint3 + rowcut + rowgraph + rowfont7
#         gotohourh = gotohourh + 133
#         fo.write('{}\n'.format(totrowhourh))
#         totico = pi + pi2 + pi3 + str(hidw[i]) + (hicon[i][2:3]) + est + str(y) + virg + str(zh) + pfh
#         y = y + 133
#         fo.write('{}\n'.format(totico))
#         vtemp = i2 + 1
#         totrowtemp = rowgoto + str(gotonumh) + rowgraph + rowtemph + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph + rowtemp2
#         fo.write('{}\n'.format(totrowtemp))
#         vtemp = i2 + 2
#         totrowfeel = rowgoto + str(gotonumh) + rowgraph + rowtempfh + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph + rowtemp2
#         fo.write('{}\n'.format(totrowfeel))
#         vtemp = i2 + 3
#         totrowpres = rowgoto + str(gotonumh) + rowgraph + rowpres + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph +rowpres2
#         fo.write('{}\n'.format(totrowpres))
#         vtemp = i2 + 4
#         totrowhum = rowgoto + str(gotonumh) + rowgraph + rowhum + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph + rowhum2
#         fo.write('{}\n'.format(totrowhum))
#         vtemp1 = 1 + (i * 2)
#         vtemp2 = 2 + (i * 2)
#         totrowdew = rowgoto + str(gotonumh) + rowgraph + rowdew + str(vtemp2) + rowp + rowdewpathcolor1h +rowinfo + str(vtemp1) + rowp + rowdewpathvalue1h + rowcolor + rowtemp2
#         fo.write('{}\n'.format(totrowdew))
#         vtemp1 = 1 + (i * 2)
#         vtemp2 = 2 + (i * 2)
#         totrowuvi = rowgoto + str(gotonumh) + rowgraph + rowuvi + str(vtemp2) + rowp + rowuvipathcolor1h + rowinfo + str(vtemp1) + rowp + rowuvipathvalue1h + rowcolor
#         fo.write('{}\n'.format(totrowuvi))
#         vtemp = i2 + 7
#         totrowclo = rowgoto + str(gotonumh) + rowgraph + rowclo + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph + rowclo2
#         fo.write('{}\n'.format(totrowclo))
#         vtemp = i2 + 8
#         totrowvis = rowgoto + str(gotonumh) + rowgraph + rowvis + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph + rowvis2
#         fo.write('{}\n'.format(totrowvis))
#         vtemp = i2 + 9
#         totrowwins = rowgoto + str(gotonumh) + rowgraph + rowwins + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph + rowwins2
#         fo.write('{}\n'.format(totrowwins))
#         vtemp = i2 + 11
#         totrowwing = rowgoto + str(gotonumh) + rowgraph + rowwing + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph + rowwins2
#         fo.write('{}\n'.format(totrowwing))
#         vtemp = i2 + 13
#         totrowmain = rowgoto + str(gotonumh) + rowgraph + rowinfo + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph
#         fo.write('{}\n'.format(totrowmain))
#         vtemp = i2 + 14
#         totrowdesc = rowgoto + str(gotonumh) + rowgraph + rowinfo + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph
#         fo.write('{}\n'.format(totrowdesc))
#         vtemp = i2 + 16
#         totrowpop = rowgoto + str(gotonumh) + rowgraph + rowpop + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph
#         fo.write('{}\n'.format(totrowpop))
#         vtemp = i2 + 17
#         totrowrain1 = rowgoto + str(gotonumh) + rowgraph + rowrain1 + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph + rowrain2
#         fo.write('{}\n'.format(totrowrain1))
#         vtemp = i2 + 18
#         totrowsnow1 = rowgoto + str(gotonumh) + rowgraph + rowsnow1 + str(vtemp) + rowp + rowpathh + rowprint2 + rowgraph + rowsnow2
#         fo.write('{}\n'.format(totrowsnow1))
#         gotonumh = gotonumh + 133
#         counter = counter + 1
# fo.write(str(counter))
# fo.close()
# #                main DAILY (+1, +2, +3, +4, +5, +6 days) in nextdays.txt
# gotonumd = 100
# y = 0
# counter = 0
# fo = open(pathdays, 'w')
# if coderrforecast != '200':
#     fo.write('{}\n'.format(owmpylogo + infotzerrforecast))
# else:
#     for i in range(firstd, vdaily, blokd):
#         if (dicon[i][2:3]) == 'd':
#             i2 = 1 + (groupd * i)
#             totrowhourd = rowcolor + rowfont7 + rowgoto + str(gotohourd) + rowgraph + rowinfo + str(i2) + rowp + rowpathd + rowprint2 + rowgraph + rowfont7
#             gotohourd = gotohourd + 133
#             fo.write('{}\n'.format(totrowhourd))
#             totico = pi + pi2 + pi3 + str(didw[i]) + (dicon[i][2:3]) + est + str(y) + virg + str(zd) + pfd
#             y = y + 133
#             fo.write('{}\n'.format(totico))
#             vtemp = i2 + 3
#             totrowtempdd = rowgoto + str(gotonumd) + rowgraph + rowtempdd + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowtemp2
#             fo.write('{}\n'.format(totrowtempdd))
#             vtemp = i2 + 4
#             totrowtempmind = rowgoto + str(gotonumd) + rowgraph + rowcolor1 + rowinfo + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowcolor + rowtemp2
#             fo.write('{}\n'.format(totrowtempmind))
#             vtemp = i2 + 5
#             totrowtempmaxd = rowgoto + str(gotonumd) + rowgraph + rowcolor4 + rowinfo + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowcolor + rowtemp2
#             fo.write('{}\n'.format(totrowtempmaxd))
#             vtemp = i2 + 6
#             totrowtempnd = rowgoto + str(gotonumd) + rowgraph + rowtempnd + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowtemp2
#             fo.write('{}\n'.format(totrowtempnd))
#             vtemp = i2 + 7
#             totrowtemped = rowgoto + str(gotonumd) + rowgraph + rowtemped + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowtemp2
#             fo.write('{}\n'.format(totrowtemped))
#             vtemp = i2 + 8
#             totrowtempmd = rowgoto + str(gotonumd) + rowgraph + rowtempmd + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowtemp2
#             fo.write('{}\n'.format(totrowtempmd))
#             vtemp = i2 + 9
#             totrowtempdfd = rowgoto + str(gotonumd) + rowgraph + rowtempdfd + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowtemp2
#             fo.write('{}\n'.format(totrowtempdfd))
#             vtemp = i2 + 10
#             totrowtempnfd = rowgoto + str(gotonumd) + rowgraph + rowtempnfd + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowtemp2
#             fo.write('{}\n'.format(totrowtempnfd))
#             vtemp = i2 + 11
#             totrowtempefd = rowgoto + str(gotonumd) + rowgraph + rowtempefd + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowtemp2
#             fo.write('{}\n'.format(totrowtempefd))
#             vtemp = i2 + 12
#             totrowtempmfd = rowgoto + str(gotonumd) + rowgraph + rowtempmfd + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowtemp2
#             fo.write('{}\n'.format(totrowtempmfd))
#             vtemp = i2 + 13
#             totrowpresd = rowgoto + str(gotonumd) + rowgraph + rowpres + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowpres2
#             fo.write('{}\n'.format(totrowpresd))
#             vtemp = i2 + 14
#             totrowhumd = rowgoto + str(gotonumd) + rowgraph + rowhum + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowhum2
#             fo.write('{}\n'.format(totrowhumd))
#             vtemp1 = 1 + (i * 2)
#             vtemp2 = 2 + (i * 2)
#             totrowdewd = rowgoto + str(gotonumd) + rowgraph + rowdew + str(vtemp2) + rowp + rowdewpathcolor1d + rowinfo + str(vtemp1) + rowp + rowdewpathvalue1d + rowcolor + rowtemp2
#             fo.write('{}\n'.format(totrowdewd))
#             vtemp = i2 + 16
#             totrowwinsd = rowgoto + str(gotonumd) + rowgraph + rowwins + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowwins2
#             fo.write('{}\n'.format(totrowwinsd))
#             vtemp = i2 + 18
#             totrowwingd = rowgoto + str(gotonumd) + rowgraph + rowwing + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowwins2
#             fo.write('{}\n'.format(totrowwingd))
#             vtemp = i2 + 20
#             totrowmaind = rowgoto + str(gotonumd) + rowgraph + rowinfo + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph
#             fo.write('{}\n'.format(totrowmaind))
#             vtemp = i2 + 21
#             totrowdescd = rowgoto + str(gotonumd) + rowgraph + rowinfo + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph
#             fo.write('{}\n'.format(totrowdescd))
#             vtemp = i2 + 23
#             totrowclod = rowgoto + str(gotonumd) + rowgraph + rowclo + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowclo2
#             fo.write('{}\n'.format(totrowclod))
#             vtemp = i2 + 24
#             totrowpopd = rowgoto + str(gotonumd) + rowgraph + rowpop + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph
#             fo.write('{}\n'.format(totrowpopd))
#             vtemp = i2 + 25
#             totrowrain1d = rowgoto + str(gotonumd) + rowgraph + rowrain1 + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowrain2
#             fo.write('{}\n'.format(totrowrain1d))
#             vtemp = i2 + 26
#             totrowsnow1d = rowgoto + str(gotonumd) + rowgraph + rowsnow1 + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowsnow2
#             fo.write('{}\n'.format(totrowsnow1d))
#             vtemp1 = 1 + (i * 2)
#             vtemp2 = 2 + (i * 2)
#             totrowuvid = rowgoto + str(gotonumd) + rowgraph + rowuvi + str(vtemp2) + rowp + rowuvipathcolor1d + rowinfo + str(vtemp1) + rowp + rowuvipathvalue1d + rowcolor
#             fo.write('{}\n'.format(totrowuvid))
#             gotonumd = gotonumd + 133
#             counter = counter + 1
#             if counter == 3:
#                 zd = zd + 105
#                 gotohourd = 35
#                 gotonumd = 100
#                 y = 0              
#         elif (dicon[i][2:3]) == 'n':
#             i2 = 1 + (groupd * i)
#             totrowhourd = rowcolor + rowfont7 + rowgoto + str(gotohourd) + rowgraph + rowinfo + str(i2) + rowp + rowpathd + rowprint2 + rowgraph + rowfont7
#             gotohourd = gotohourd + 133
#             fo.write('{}\n'.format(totrowhourd))
#             totico = pi + pi2 + pi3 + str(didw[i]) + (dicon[i][2:3]) + est + str(y) + virg + str(zd) + pfd
#             y = y + 133
#             fo.write('{}\n'.format(totico))
#             vtemp = i2 + 3
#             totrowtempdd = rowgoto + str(gotonumd) + rowgraph + rowtempdd + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowtemp2
#             fo.write('{}\n'.format(totrowtempdd))
#             vtemp = i2 + 4
#             totrowtempmind = rowgoto + str(gotonumd) + rowgraph + rowcolor1 + rowinfo + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowcolor + rowtemp2
#             fo.write('{}\n'.format(totrowtempmind))
#             vtemp = i2 + 5
#             totrowtempmaxd = rowgoto + str(gotonumd) + rowgraph + rowcolor4 + rowinfo + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowcolor + rowtemp2
#             fo.write('{}\n'.format(totrowtempmaxd))
#             vtemp = i2 + 6
#             totrowtempnd = rowgoto + str(gotonumd) + rowgraph + rowtempnd + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowtemp2
#             fo.write('{}\n'.format(totrowtempnd))
#             vtemp = i2 + 7
#             totrowtemped = rowgoto + str(gotonumd) + rowgraph + rowtemped + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowtemp2
#             fo.write('{}\n'.format(totrowtemped))
#             vtemp = i2 + 8
#             totrowtempmd = rowgoto + str(gotonumd) + rowgraph + rowtempmd + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowtemp2
#             fo.write('{}\n'.format(totrowtempmd))
#             vtemp = i2 + 9
#             totrowtempdfd = rowgoto + str(gotonumd) + rowgraph + rowtempdfd + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowtemp2
#             fo.write('{}\n'.format(totrowtempdfd))
#             vtemp = i2 + 10
#             totrowtempnfd = rowgoto + str(gotonumd) + rowgraph + rowtempnfd + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowtemp2
#             fo.write('{}\n'.format(totrowtempnfd))
#             vtemp = i2 + 11
#             totrowtempefd = rowgoto + str(gotonumd) + rowgraph + rowtempefd + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowtemp2
#             fo.write('{}\n'.format(totrowtempefd))
#             vtemp = i2 + 12
#             totrowtempmfd = rowgoto + str(gotonumd) + rowgraph + rowtempmfd + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowtemp2
#             fo.write('{}\n'.format(totrowtempmfd))
#             vtemp = i2 + 13
#             totrowpresd = rowgoto + str(gotonumd) + rowgraph + rowpres + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowpres2
#             fo.write('{}\n'.format(totrowpresd))
#             vtemp = i2 + 14
#             totrowhumd = rowgoto + str(gotonumd) + rowgraph + rowhum + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowhum2
#             fo.write('{}\n'.format(totrowhumd))
#             vtemp1 = 1 + (i * 2)
#             vtemp2 = 2 + (i * 2)
#             totrowdewd = rowgoto + str(gotonumd) + rowgraph + rowdew + str(vtemp2) + rowp + rowdewpathcolor1d + rowinfo + str(vtemp1) + rowp + rowdewpathvalue1d + rowcolor + rowtemp2
#             fo.write('{}\n'.format(totrowdewd))
#             vtemp = i2 + 16
#             totrowwinsd = rowgoto + str(gotonumd) + rowgraph + rowwins + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowwins2
#             fo.write('{}\n'.format(totrowwinsd))
#             vtemp = i2 + 18
#             totrowwingd = rowgoto + str(gotonumd) + rowgraph + rowwing + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowwins2
#             fo.write('{}\n'.format(totrowwingd))
#             vtemp = i2 + 20
#             totrowmaind = rowgoto + str(gotonumd) + rowgraph + rowinfo + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph
#             fo.write('{}\n'.format(totrowmaind))
#             vtemp = i2 + 21
#             totrowdescd = rowgoto + str(gotonumd) + rowgraph + rowinfo + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph
#             fo.write('{}\n'.format(totrowdescd))
#             vtemp = i2 + 23
#             totrowclod = rowgoto + str(gotonumd) + rowgraph + rowclo + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowclo2
#             fo.write('{}\n'.format(totrowclod))
#             vtemp = i2 + 24
#             totrowpopd = rowgoto + str(gotonumd) + rowgraph + rowpop + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph
#             fo.write('{}\n'.format(totrowpopd))
#             vtemp = i2 + 25
#             totrowrain1d = rowgoto + str(gotonumd) + rowgraph + rowrain1 + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowrain2
#             fo.write('{}\n'.format(totrowrain1d))
#             vtemp = i2 + 26
#             totrowsnow1d = rowgoto + str(gotonumd) + rowgraph + rowsnow1 + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph + rowsnow2
#             fo.write('{}\n'.format(totrowsnow1d))
#             vtemp1 = 1 + (i * 2)
#             vtemp2 = 2 + (i * 2)
#             totrowuvid = rowgoto + str(gotonumd) + rowgraph + rowuvi + str(vtemp2) + rowp + rowuvipathcolor1d + rowinfo + str(vtemp1) + rowp + rowuvipathvalue1d + rowcolor
#             fo.write('{}\n'.format(totrowuvid))
#             gotonumd = gotonumd + 133
#             counter = counter + 1
#             if counter == 3:
#                 zd = zd + 105
#                 gotohourd = 35
#                 gotonumd = 100
#                 y = 0
# fo.write(str(counter))
# fo.close()
# ################################ create MOON section
# rowm1= "${alignr}${font URW Gothic L:size=6}${color7}by moongiant.com ${color2}$hr${color}${font}"
# rowm2= """${alignc}${color1}Details for ${execi 3600 echo `date --date="0 day" | awk '{print $1" "$3" "$2" "$6}'`}${color}"""
# rowm3= "${color2}Illumination: ${color}${execpi 600 sed -n '3p' $HOME" + conky + "moon/Moongiant_python/todaymooninfo.txt | awk '{print $2}'}"
# rowm4= "${color2}Sun Angle: ${color}${execpi 600 sed -n '7p' $HOME" + conky + "moon/Moongiant_python/todaymooninfo.txt | awk '{print $3}'}"
# rowm5= "${color2}Sun Distance: ${color}${execpi 600 sed -n '8p' $HOME" + conky + "moon//Moongiant_python/todaymooninfo.txt | awk '{print $3}'}"
# rowm6= "${color2}Moon Age: ${color}${execpi 600 sed -n '4p' $HOME" + conky + "moon/Moongiant_python/todaymooninfo.txt | awk '{print $3}'}"
# rowm7= "${color2}Moon Angle: ${color}${execpi 600 sed -n '5p' $HOME" + conky + "moon/Moongiant_python/todaymooninfo.txt | awk '{print $3}'}${color}${goto 230}${alignc}${execpi 600 sed -n '2p' $HOME" + conky + "moon/Moongiant_python/todaymooninfo.txt | awk '{print $2}'}"
# rowm8= "${color2}Moon Distance: ${color}${execpi 600 sed -n '6p' $HOME" + conky + "moon/Moongiant_python/todaymooninfo.txt | awk '{print $3}'}${color}${goto 230}${alignc}${execpi 600 sed -n '2p' $HOME" + conky + "moon/Moongiant_python/todaymooninfo.txt | awk '{print $3}'}"
# rowm9= "${alignc}${color1}Average moonrise and moonset times${color}"
# rowm10= "${image $HOME" + conky + "moon/Moongiant_python/0.png -p 280,625 -s 90x90}${image $HOME" + conky + "moon/Moongiant_python/rise.jpg -p 0,730 -s 400x99}${image $HOME" + conky + "moon/Moongiant_python/0.png -p 45,780 -s 30x30}${image $HOME" + conky + "moon/Moongiant_python/0.png -p 325,780 -s 30x30}${image $HOME" + conky + "moon/Moongiant_python/0.png -p 185,730 -s 30x30}"
# fo = open(pmoon, 'w')
# fo.write('{}\n'.format(rowm1))
# fo.write('{}\n'.format(rowm2))
# fo.write('{}\n'.format(rowm3))
# fo.write('{}\n'.format(rowm4))
# fo.write('{}\n'.format(rowm5))
# fo.write('{}\n'.format(rowm6))
# fo.write('{}\n'.format(rowm7))
# fo.write('{}\n'.format(rowm8))
# fo.write('{}\n'.format(rowm9))
# fo.write('{}\n'.format(rowm10))
# fo.close()