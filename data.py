password = ''
phoneNo = ''
carNo = ''
zoneID = ''
url = 'https://lk.aparking.kz/'

data = {
	'page':	'login',
	'username':	'+' + phoneNo,
	'password':	password,
	'login':	'Залогиниться',
	'_reqNo':	'2'
}

headers = {
	'Host': 'lk.aparking.kz',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
	'Accept-Encoding': 'gzip, deflate, br',
	'Referer': 'https://lk.aparking.kz/',
	'Cache-Control': 'max-age=0',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1'
}

data_start = {
	'module': 'Parking',
	'operation': 'startParking',
	'parkingPhone': '',
	'parkingPhoneSession': '',
	'extendDuration': '',
	'page': 'frontpage',
	'defaultDuration': 'default',
	'locationSearchText': '+'.join(['Парковка:', zoneID, '(Казахстан)']),
	'locationID': '',
	'locationType': '',	
	'searchID': zoneID,
	'zoneID': zoneID,
	'zoneType': 'O',
	'zoneOwner': 'KAZAKHSTAN',
	'spaceNo': '',
	'placeType': 'A',
	'accessCode': '',
	'accessControlMode': '',
	'parkTicketNumber': '',
	'carNo': carNo,
	'addNewCar': '',
	'durations': '60,120,180,240,300,360,480,720,1440,',
	'duration': '60',
	'phoneNo': phoneNo,
	'_reqNo': '2'
}

data_stop = {
	'module': 'Parking',
	'operation': 'stopParking',
	'parkingPhone': phoneNo,
	'parkingPhoneSession' :'',
	'extendDuration': '60',
	'page': 'frontpage',
	'defaultDuration':'default',
	'locationSearchText': '',
	'locationID': '',
	'locationType': '',
	'searchID': '',
	'zoneID': '',
	'zoneType': 'O',
	'zoneOwner': '',
	'spaceNo': '',
	'placeType': '',
	'accessCode' : '',
	'accessControlMode': '',
	'parkTicketNumber': '',
	'carNo': carNo,
	'addNewCar': '',
	'durations': '60,120,180,240,300,360,480,720,1440,',
	'duration': '60',
	'phoneNo': phoneNo
}