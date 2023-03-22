echo "address: (leave empty if you dont have)"
read addr
bssid="airodump-ng wlan1mon --bssid ${addr}"

if [ -z "$addr" ]
then
	bash -c "airodump-ng wlan1mon"
else
	bash -c "${bssid}"
fi
