#! /bin/python
import os
import sys

os.system('/usr/bin/python3 /home/test/Documents/gitfiles/sip/SIP/sip.py >> /home/test/daily_sip/SIP_$(date +"%F %T").log')
