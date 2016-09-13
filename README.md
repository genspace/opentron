# opentron

This is a repo for Genspace's usage of the OpenTron.

With the Mac app, the Opentron saves calibration files in its app data: /Users/\<username\>/Library/Application Support/OT One App/otone\_data/

Current instructions to use the OpenTron:
1. Plug power in OpenTron.
2. Open OpenTron app on laptop, and plug in usb cable from OpenTron to laptop. (Ignore the Raspberry Pi)
3. Open a protocol folder in this repo. Overwrite the pipette\_calibrations.json file in the app data folder with the pipette\_calibrations.json file from the folder.
4. Drag the protocol json to the app
5. Set up OpenTron deck as specified by the protocol
6. Run!
