import os
import time
from novaclient import client as novaclient
#from credentials import get_nova_creds
 
#creds = get_nova_creds()
nova = novaclient.Client("2", "admin","123","admin","http://10.0.2.15:5000/v2.0")

image = nova.images.find(name = "cirros-0.3.4-x86_64-uec")
flavor = nova.flavors.find(name = "m1.nano")
instance = nova.servers.create(name="yuan",image = image, flavor = flavor)

status = instance.status
while status == 'BUILD':
	time.sleep(2)
	instance = nova.servers.get(instance.id)
	status = instance.status
print "status: %s" %status
print "lanuch sucessfully"
