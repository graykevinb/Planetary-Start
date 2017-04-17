# Planetary-Start
Planetary-Start is a way to run programs on a Raspberry Pi with the push of a button.
A python script is run at boot with systemd. You can then run whatever code you specify when a hardware button is connected and a few LEDs (optional).

### Installation
The installation is quite simple. Either run the install script or run these few commands:
Before you install you'll need to setup a few things. First connect a button to GPIO pin #26.
Then if you want LEDs for status you can plug them in at GPIO #19 and another at GPIO #21. Of course you can change it if you want. 

Finally edit line 7 of planetary_start_service.txt to include the path to your code you want to run on the button press. (Its set up to use python3 but you can switch it to whatever you want.) 
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
