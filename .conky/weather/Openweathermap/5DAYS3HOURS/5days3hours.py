import os, sys
import requests
import time
import urllib.request
# import module GEOPY
from geopy.geocoders import Photon
# initialize Nominatim API or Photon API
geolocator = Photon(user_agent="measurements")
# Lock file to tell conky that the script is running
lock_file = "/tmp/script_5days3hours.lock"
# Crea il file di lock all'inizio
try:
    open(lock_file, 'w').close()
    ################################ my API url forecast (insert it between apostrophe, DON'T delete apostrophes)
    # set latitude and longitude
    mylat = 45.40713
    mylon = 11.87680
    myAPPID = ''
    url_forecast = 'https://api.openweathermap.org/data/2.5/forecast?lat=' + str(mylat) + '&lon=' + str(mylon) + '&units=metric&appid=' + myAPPID
    res_forecast = requests.get(url_forecast).json()
    dataforecast = res_forecast
    ################################ get your HOME name automatically
    homepath = os.environ['HOME']
    homename = homepath
    homename = homename[6:]
    ################################ set variables
    vhourly = 40
    vtext = 'n/a'
    temporary = ''
    grouph = 22
    ################################ set error variables
    coderrforecast = 0
    # ################################ create variables for GENERAL data
    tz = ''
    tz_off = 0
    ################################ create array for HOURLY data
    hdt = []
    htemp = []
    htempfeelslike = []
    htempmin = []
    htempmax = []
    hpressure = []
    hsealev = []
    hgrndlev = []
    hhumidity = []
    htempkf = []
    hidw = []
    hmain = []
    hdesc = []
    hicon = []
    hclouds = []
    hwindspeed = []
    hwinddeg = []
    hwindgust = []
    hvisibility =[]
    hpop = []
    hpod = []
    hdttext = []
    ################################ set the tyemp paths
    home = '/home/'
    conky = '/.conky/'
    ################################ set the paths for the ERROR
    perrfore = home + homename + conky + 'weather/Openweathermap/5DAYS3HOURS/-errorfore.txt'
    ################################ set the paths for the API files
    pgenraw = home + homename + conky + 'weather/Openweathermap/5DAYS3HOURS/-general.txt'
    pgenclean = home + homename + conky + 'weather/Openweathermap/5DAYS3HOURS/general.txt'
    phouraw = home + homename + conky + 'weather/Openweathermap/5DAYS3HOURS/-hourly.txt'
    phouclean = home + homename + conky + 'weather/Openweathermap/5DAYS3HOURS/hourly.txt'
    ################################ set the paths for the FLAGS
    pflags = home + homename + conky + 'weather/Openweathermap/5DAYS3HOURS/-flags.txt'
    ################################ set the paths for the GEOPY TIMEZONE data
    pgeopy = home + homename + conky + 'weather/Openweathermap/5DAYS3HOURS/-geopy.txt'
    ################################ set the paths for the logo
    pathowmlogo = home + homename + conky + 'weather/Openweathermap/5DAYS3HOURS/owmicon.txt'
    ################################ set the paths for the HOURLY section
    pathhours = home + homename + conky + 'weather/Openweathermap/5DAYS3HOURS/nexthours.txt'
    ################################ compass angle
    myd = 72   # <--- insert angle of your North in 'myd'
    tdeg = 0
    ################################ get data for ERROR section FORECAST
    try:
        coderrforecast = str(dataforecast['cod'])
    except:
        coderrforecast = 'error'
    ################################ write raw data for ERROR section FORECAST
    fo = open(perrfore, 'w')
    fo.write('error: {}\n'.format(coderrforecast))
    fo.close()
    ################################ get general data for HOURLY section
    fcod = dataforecast['cod']
    fmes = dataforecast['message']
    fcnt = dataforecast['cnt']
    fid = dataforecast['city']['id']
    fname = dataforecast['city']['name']
    flat = dataforecast['city']['coord']['lat']
    flon = dataforecast['city']['coord']['lon']
    fcountry = dataforecast['city']['country']
    fpop = dataforecast['city']['population']
    ftz = dataforecast['city']['timezone']
    fsunrise = dataforecast['city']['sunrise']
    fsunset = dataforecast['city']['sunset']
    ################################ write general raw data for HOURLY
    fo = open(pgenraw, 'w')
    fo.write('cod: {}\n'.format(fcod))
    fo.write('message: {}\n'.format(fmes))
    fo.write('cnt: {}\n'.format(fcnt))
    fo.write('id: {}\n'.format(fid))
    fo.write('name: {}\n'.format(fname))
    fo.write('lat: {}\n'.format(flat))
    fo.write('lon: {}\n'.format(flon))
    fo.write('country: {}\n'.format(fcountry))
    fo.write('population: {}\n'.format(fpop))
    fo.write('TimeZone: {}\n'.format(ftz))
    fo.write('sunrise: {}\n'.format(fsunrise))
    fo.write('sunset: {}\n'.format(fsunset))
    ################################ write general clean data for HOURLY
    fo = open(pgenclean, 'w')
    fo.write('{}\n'.format(fcod))
    fo.write('{}\n'.format(fmes))
    fo.write('{}\n'.format(fcnt))
    fo.write('{}\n'.format(fid))
    fo.write('{}\n'.format(fname))
    fo.write('{}\n'.format(flat))
    fo.write('{}\n'.format(flon))
    fo.write('{}\n'.format(fcountry))
    fo.write('{}\n'.format(fpop))
    fo.write('{}\n'.format(ftz))
    fo.write('{}\n'.format(fsunrise))
    fo.write('{}\n'.format(fsunset))
    fo.close()
    ############################################### GEOPY NEW SYNTAX
    urlGeopy = 'https://photon.komoot.io/reverse?lon=' + str(flon) + '&lat='  + str(flat)
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
    fo.write('lat: {}\n'.format(mylat))
    fo.write('lon: {}\n'.format(mylon))
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
    ################################ get data for HOURLY section
    for i in range(0, vhourly):
        temporary = dataforecast['list'][i]['dt']
        temporary = time.strftime("%d-%B-%Y %H:%M:%S", time.localtime(temporary))
        hdt.append(temporary)
        htemp.append(dataforecast['list'][i]['main']['temp'])
        htempfeelslike.append(dataforecast['list'][i]['main']['feels_like'])
        htempmin.append(dataforecast['list'][i]['main']['temp_min'])
        htempmax.append(dataforecast['list'][i]['main']['temp_max'])
        hpressure.append(dataforecast['list'][i]['main']['pressure'])
        hsealev.append(dataforecast['list'][i]['main']['sea_level'])
        hgrndlev.append(dataforecast['list'][i]['main']['grnd_level'])
        hhumidity.append(dataforecast['list'][i]['main']['humidity'])
        htempkf.append(dataforecast['list'][i]['main']['temp_kf'])
        hidw.append(dataforecast['list'][i]['weather'][0]['id'])
        hmain.append(dataforecast['list'][i]['weather'][0]['main'])
        hdesc.append(dataforecast['list'][i]['weather'][0]['description'])
        hicon.append(dataforecast['list'][i]['weather'][0]['icon'])
        hclouds.append(dataforecast['list'][i]['clouds']['all'])
        hwindspeed.append(dataforecast['list'][i]['wind']['speed'])
        hwinddeg.append(dataforecast['list'][i]['wind']['deg'])
        hwindgust.append(dataforecast['list'][i]['wind']['gust'])
        hvisibility.append(dataforecast['list'][i]['visibility'])
        hpop.append(dataforecast['list'][i]['pop'])
        hpod.append(dataforecast['list'][i]['sys']['pod'])
        hdttext.append(dataforecast['list'][i]['dt_txt'])
    ################################ write raw data for HOURLY section
    fo = open(phouraw, 'w')
    for i in range(0, vhourly):
        fo.write('dt: {}\n'.format(hdt[i]))
        fo.write('temp: {}\n'.format(htemp[i]))
        fo.write('feelslike: {}\n'.format(htempfeelslike[i]))
        fo.write('tempmin: {}\n'.format(htempmin[i]))
        fo.write('tempmax: {}\n'.format(htempmax[i]))
        fo.write('pressure: {}\n'.format(hpressure[i]))
        fo.write('sea_level: {}\n'.format(hsealev[i]))
        fo.write('ground_level: {}\n'.format(hgrndlev[i]))
        fo.write('humidity: {}\n'.format(hhumidity[i]))
        fo.write('temp_kf: {}\n'.format(htempkf[i]))
        fo.write('idw: {}\n'.format(hidw[i]))
        fo.write('main: {}\n'.format(hmain[i]))
        fo.write('description: {}\n'.format(hdesc[i]))
        fo.write('icon: {}\n'.format(hicon[i]))
        fo.write('clouds: {}\n'.format(hclouds[i]))
    #                   transform in Km/h (if you want m/s put a # at the beginning of the next row)
        hwindspeed[i] = round(hwindspeed[i] * 3.6, 2)
        fo.write('windspeed: {}\n'.format(hwindspeed[i]))
        fo.write('winddeg: {}\n'.format(hwinddeg[i]))
    #                   transform in Km/h (if you want m/s put a # at the beginning of the next 2 rows)
        if hwindgust[i] != vtext:
            hwindgust[i] = round(hwindgust[i] * 3.6, 2)
        fo.write('windgust: {}\n'.format(hwindgust[i]))
        fo.write('visibility: {}\n'.format(hvisibility[i]))
        fo.write('pop: {}\n'.format(hpop[i]))
        fo.write('pod: {}\n'.format(hpod[i]))
        fo.write('dt_txt: {}\n'.format(hdttext[i]))
    fo.close()
    ################################ write clean data for HOURLY section
    fo = open(phouclean, 'w')
    for i in range(0, vhourly):
        fo.write('{}\n'.format(hdt[i]))
        fo.write('{}\n'.format(htemp[i]))
        fo.write('{}\n'.format(htempfeelslike[i]))
        fo.write('{}\n'.format(htempmin[i]))
        fo.write('{}\n'.format(htempmax[i]))
        fo.write('{}\n'.format(hpressure[i]))
        fo.write('{}\n'.format(hsealev[i]))
        fo.write('{}\n'.format(hgrndlev[i]))
        fo.write('{}\n'.format(hhumidity[i]))
        fo.write('{}\n'.format(htempkf[i]))
        fo.write('{}\n'.format(hidw[i]))
        fo.write('{}\n'.format(hmain[i]))
        fo.write('{}\n'.format(hdesc[i]))
        fo.write('{}\n'.format(hicon[i]))
        fo.write('{}\n'.format(hclouds[i]))
        fo.write('{}\n'.format(hwindspeed[i]))
        fo.write('{}\n'.format(hwinddeg[i]))
        fo.write('{}\n'.format(hwindgust[i]))
        fo.write('{}\n'.format(hvisibility[i]))
        fo.write('{}\n'.format(hpop[i]))
        fo.write('{}\n'.format(hpod[i]))
        fo.write('{}\n'.format(hdttext[i]))
    fo.close()
except Exception as e:
    # Manage exceptions (optional)
    filelockerror = (f"Error during script execution: {e}")
finally:
    # remove lock file
    try:
        os.remove(lock_file)
    except FileNotFoundError:
        pass  # file already removed
