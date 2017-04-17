# Planetary-Start
Run programs and poweroff your Raspberry Pi with a few LEDs and  a simple switch

### Installation
The installation is quite simple. Either run the install script or run these few commands:

-------
1. Move the .service file to its proper place:
	`sudo cp planetary_start_service.txt /lib/systemd/system/planetary_start.service`
2. Set the right file permissions to the file:
	`sudo chmod 644 /lib/systemd/system/myscript.service`
3. Reload systemd:
	`sudo systemctl daemon-reload`
4. Enable the service to run on boot:
	`sudo systemctl enable planetary_start.service`
5. Finally start the service:
	`sudo systemctl start planetary_start.service`

Then reboot the computer to make sure it starts on boot. You should see the LEDs blink.

### Contributing
Contributions are welcome!
Please see the CONTRIBUTING file for more details.
