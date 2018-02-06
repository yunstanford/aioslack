import aiohttp
from .clients.channel import ChannelClient


SLACK_API_BASE = "https://slack.com/api/{method}"


class Slack:

	def __init__(self, token):
		self.token = token
		self.session = aiohttp.ClientSesion()
		self.channel_client = ChannelClient(session, token)

	# Channel APIs


	# Team APIs

	# ...