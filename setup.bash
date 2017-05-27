#!/bin/bash -xve

exec 2> /tmp/setup.log

cd /home/kuroiwa/RaspberryPiMouse/src/drivers/
/sbin/insmod rtmouse.ko

sleep 1 #Wait for make device file
chmod 666 /dev/rt*

echo 0 > /dev/rtmotoren0 #Turn off motor for safty
