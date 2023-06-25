import reapy
from reapy import reascript_api as RPR


track = RPR.GetTrack(0, 0)
RPR.SetTrackSelected(x, 1)
RPR.InsertMedia('../../../Data/tabs/led-zeppelin-stairway_to_heaven/gtr_1/led-zeppelin-stairway_to_heaven_gtr_1_0.mid', 0)
