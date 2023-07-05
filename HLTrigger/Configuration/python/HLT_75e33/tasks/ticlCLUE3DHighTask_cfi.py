import FWCore.ParameterSet.Config as cms

from ..modules.filteredLayerClustersCLUE3DHigh_cfi import *
from ..modules.ticlSeedingGlobal_cfi import *
from ..modules.ticlTrackstersCLUE3DHigh_cfi import *

ticlCLUE3DHighStepTask = cms.Task(
    ticlSeedingGlobal, filteredLayerClustersCLUE3DHigh, ticlTrackstersCLUE3DHigh)
