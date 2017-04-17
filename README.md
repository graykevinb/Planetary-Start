# Planetary-Start
Run programs and poweroff your Raspberry Pi with a few LEDs and  a simple switch

### Installation
The installation is quite simple. Either run the install script or run these few commands:
`sudo cp planetary_start_service.txt /lib/systemd/system/planetary_start.service`
`sudo chmod 644 /lib/systemd/system/myscript.service`
`sudo systemctl daemon-reload`
`sudo systemctl enable planetary_start.service`
`sudo systemctl start planetary_start.service`

Then reboot the computer to make sure it starts on boot. You should see the LEDs blink.

### Contributing
Contributions are welcome!
Please see the CONTRIBUTING file for more details.
