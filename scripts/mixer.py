# Mixing 3 things, and dumping the mix onto a target.

# imports
from opentrons import labware, instruments

# metadata
metadata = {
    'protocolName': 'My Protocol',
    'author': 'WTMoose <wtmoose@thingconnect.cc>',
    'description': 'Oh, Fry! I love the way you mix three things.',
}

# labware

# In the original example
tiprack = labware.load('opentrons-tiprack-300ul', '1')

# Adding a trough-type reservoire from the labware library
trough = labware.load('usascientific_12_reservoir_22ml', '2')

# In the original example
#plate = labware.load('96-flat', '2')

# Try this plate which I found in the labware library. Don’t forget to comment out the above. Changing it to 
plate = labware.load('corning_24_wellplate_3.4ml_flat', '3')

# pipettes
pipette = instruments.P300_Single(mount='right', tip_racks=[tiprack])

# commands

# This squirts the shmoo into the bottom of the well at plate-well A1
pipette.transfer(200, trough.wells('A1'), plate.wells('A1'))

#pipette.transfer(200, trough.wells('A2'), plate.wells('A1'))
#pipette.transfer(200, trough.wells('A3'), plate.wells('A1'))
#pipette.mix(4, 300, plate.wells('A1'))
#pipette.transfer(300, plate.wells('A1'), plate.wells('B1'))
#pipette.transfer(300, plate.wells('A1'), plate.wells('B2'))
