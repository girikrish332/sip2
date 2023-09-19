#! /bin/python3
import os 
import psutil
import logging

# Configure logging
log_file = '/home/test/daily_sip/SIP_$(date +"%F %T").log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to monitor CPU and RAM usage
def monitor_system_resources():
    cpu_percent = psutil.cpu_percent(interval=1)  # CPU usage over the last second
    ram_percent = psutil.virtual_memory().percent  # RAM usage as a percentage

    logging.info(f"CPU Usage: {cpu_percent}%")
    logging.info(f"RAM Usage: {ram_percent}%")

# Function to check for buffer overflow
def check_buffer_overflow():
    try:
        # Allocate a large amount of memory to trigger a MemoryError (buffer overflow)
        buffer_size = 10 * 1024 * 1024  # 10 MB
        buffer = bytearray(buffer_size)
    except MemoryError as e:
        logging.error(f"Buffer Overflow Detected: {e}")
    else:
        logging.info("No Buffer Overflow Detected")

if __name__ == "__main__":
    while True:
        monitor_system_resources()
        check_buffer_overflow()

#BSNL 

bsnl = "BSNL_SIP" 
response1 = os.system("ping -c 5 " + "10.181.33.1") 
if response1 == 0: 
  print (bsnl, 'is up!^^^^^^^^^^^^^^^^^^^')
  #os.system('/usr/bin/python3 /home/administrator/SIP_A/BSNL_SIP_UP.py')
else: 
  print (bsnl, 'is down!********************')
  #os.system('/usr/bin/python3 /home/administrator/SIP_A/BSNL_SIP_DOWN.py')

#TATA 
tata = "TATA_SIP"
response2 = os.system("ping -c 5 " + "10.52.15.2") 
if response2 == 0: 
  print (tata, 'is up!^^^^^^^^^^^^^^^^^^^^') 
 # os.system('/usr/bin/python3 /home/administrator/SIP_A/TATA_SIP_UP.py')
else: 
  print (tata, 'is down!*******************') 
  #os.system('/usr/bin/python3 /home/administrator/SIP_A/TATA_SIP_DOWN.py')


#a="asterisk -rx 'sip show peers'" 
#b=os.system(a) 
#c="asterisk -rx 'sip show registry'" 
#d=os.system(c)
