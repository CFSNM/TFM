from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.link import Intf
from mininet.cli import CLI
from mininet.nodelib import NAT
import time

class RedEspana():

    def __init__(self):

        net = Mininet()

        controller = net.addController('controller', controller = RemoteController, ip = '10.0.2.11')

        numberElements = 21


        for s in range(numberElements):
            switch = net.addSwitch('s'+str(s+1))
            switches.append(switch)


        for h in range(numberElements):
            if h not in vimIndexes:
                host = net.addHost('h'+str(h+1), ip = '15.0.0.'+str(h+1+50)+'/24')
                hosts.append(host)
	        net.addLink(host, switches[h])


        net.addLink(switches[0], switches[1])
        net.addLink(switches[0], switches[2])
        net.addLink(switches[1], switches[2])
        net.addLink(switches[1], switches[3])
        net.addLink(switches[2], switches[4])
        net.addLink(switches[2], switches[6])
        net.addLink(switches[3], switches[4])
        net.addLink(switches[3], switches[9])
        net.addLink(switches[4], switches[5])
        net.addLink(switches[4], switches[7])
        net.addLink(switches[5], switches[8])
        net.addLink(switches[6], switches[8])
        net.addLink(switches[6], switches[14])
        net.addLink(switches[7], switches[8])
        net.addLink(switches[7], switches[10])
        net.addLink(switches[7], switches[11])
        net.addLink(switches[8], switches[12])
        net.addLink(switches[9], switches[10])
        net.addLink(switches[9], switches[20])
        net.addLink(switches[10], switches[19])
        net.addLink(switches[10], switches[20])
        net.addLink(switches[11], switches[12])
        net.addLink(switches[11], switches[18])
        net.addLink(switches[11], switches[19])
        net.addLink(switches[12], switches[13])
        net.addLink(switches[12], switches[17])
        net.addLink(switches[13], switches[14])
        net.addLink(switches[13], switches[16])
        net.addLink(switches[14], switches[15])
        net.addLink(switches[15], switches[16])
        net.addLink(switches[16], switches[17])
        net.addLink(switches[17], switches[18])
        net.addLink(switches[18], switches[19])
        net.addLink(switches[19], switches[20])

	intf_vimone = Intf('enx0050b6253bb0',switches[8])
	intf_vimtwo = Intf('enx0050b6253baf',switches[19])

	print('Added physical interfaces '+str(intf_vimone)+' and '+str(intf_vimtwo))

	controller.start()

        net.start()

	time.sleep(3)

	net.pingAll()

	for host in hosts:
		host.cmd('ip route add 15.0.2.0/24 via 15.0.0.59')
		host.cmd('ip route add 15.0.3.0/24 via 15.0.0.70')
		host.cmd('/usr/sbin/sshd -D&')
		ping_vimone = host.cmd('ping 15.0.0.59 -c 1')
		print(str(ping_vimone))
		ping_vimtwo = host.cmd('ping 15.0.0.70 -c 1')
		print(str(ping_vimtwo))

        CLI(net)




topos = { 'mytopo' : ( lambda : RedEspana() ) }
