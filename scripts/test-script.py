# imports
from opentrons import labware, instruments



# metadata
metadata = {
    'protocolName': 'My Protocol',
    'author': 'WTMoose <wtmoose@thingconnect.cc>',
    'description': 'Simple protocol, work, dammit!',
}

# labware
#plate = labware.load('96-flat', '2')

# Try this plate which I found in the labware library. Don’t forget to comment out the above.
plate = labware.load('corning_24_wellplate_3.4ml_flat', '3')

tiprack = labware.load('opentrons-tiprack-300ul', '1')

# pipettes
pipette = instruments.P300_Single(mount='right', tip_racks=[tiprack])

# commands
pipette.transfer(100, plate.wells('A1'), plate.wells('B2')) 


