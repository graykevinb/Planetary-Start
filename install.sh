#Prepare for your computer to teleport to mars.
cp planetary_start_service.txt lib/systemd/system/planetary_start.service
systemctl daemon-reload
systemctl enable planetary_start.service
systemctl start planetary_start.service
systemctl status planetary_start.service

echo "If the it says its active everything installed ok!"
echo "If any problems arise do not hesitate to submit an issue."
