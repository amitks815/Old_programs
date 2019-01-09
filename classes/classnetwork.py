class network:
	def __init__(self,ipaddress,netname):
		self.ip=ipaddress
		self.name=netname
	def get_ipaddress(self):
		return self.ip
	def get_netname(self):
		return self.name

define=network(192.3,"firefox")
print("ipadress is ",define.get_ipaddress())
print("network name is ",define.get_netname())