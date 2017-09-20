from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
import socket

ACCOUNT_SID = 'AC38fe79b2f02cf1addda70d2c706646f2'
API_KEY_SID = 'SK4ee5622d04c9d4628e620be7c98e12d9'
API_KEY_SECRET = 'FxLqUN1KD3vQf6mOIxwJzqBsM9gV0vSH'

class Utility():

	def __init__(self,name,room):
		self.name = name
		self.room = room

	def generate_token(self):
		token = AccessToken(ACCOUNT_SID, API_KEY_SID, API_KEY_SECRET)
		token.identity = self.name
		grant = VideoGrant(room=self.room)
		token.add_grant(grant)
		jwt = token.to_jwt()
		return jwt

	def getSystemIP(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		try:
			s.connect(('10.255.255.255',80))
			IP = s.getsockname()[0]
		except:
			IP = '127.0.0.1'
		finally:
			s.close()
			return IP