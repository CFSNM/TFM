ifconfig br-ex 15.0.3.1/24 up
ifconfig enp0s20f0u11 15.0.0.70/24 up
ip route add 15.0.2.0/24 via 15.0.0.59
ip route del default