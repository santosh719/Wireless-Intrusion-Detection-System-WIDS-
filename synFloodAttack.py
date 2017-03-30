#!/usr/bin/env python
import sys
from scapy.all import *
#print "Fields of packets"
p=IP(dst="192.168.0.112",id=1111,ttl=99)/TCP(sport=RandShort(),dport=[22],seq=12345,ack=1000,window=1000,flags="S")/"HaX0r SVP"
ls(p)
print "sending packets in 0.3 second and interval of 4 second"
ans,unans=srloop(p,inter=0.3,retry=5,timeout=4)
ans.summary()
unans.summary()
print "source port flag"
ans.make_table(lambda(s,r):(s.dst,s.dport,r.sprintf("%iP.id%\t%IP.ttl%\t%TCP.flags%")))

