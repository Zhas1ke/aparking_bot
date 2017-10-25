import requests
import time

from data import url, data, headers, data_start, data_stop

def login():
	session = requests.Session()
	response = session.post(url=url, data=data)
	cookies = session.cookies.get_dict()
	return session, response, cookies

def logout(session):
	url = 'https://lk.aparking.kz/?page=logout'
	r = session.get(url)

def main():
	session, response, cookies = login()
	session.post(url=url, data=data_start)
	time.sleep(20)
	session.post(url=url, data=data_stop)
	logout(session)

if __name__ == '__main__':
	main()