from opentrons import robot, labware, instruments

robot.connect()

tiprack = labware.load('opentrons_96_tiprack_300ul', '1')
pipette = instruments.P300_Single(mount = 'right', tip_racks = [tiprack])

pipette.pick_up_tip(tiprack.wells('A1'))
pipette.drop_tip(tiprack.wells('A1'))
pipette.pick_up_tip(tiprack.wells('H1'))
pipette.drop_tip(tiprack.wells('H1'))
pipette.pick_up_tip(tiprack.wells('A12'))
pipette.drop_tip(tiprack.wells('A12'))
pipette.pick_up_tip(tiprack.wells('H12'))
pipette.drop_tip(tiprack.wells('H12'))
