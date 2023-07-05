import FWCore.ParameterSet.Config as cms

from ..modules.ticlTrackstersMerge_cfi import *
from ..modules.ticlTrackstersMergev2_cfi import *

ticlTracksterMergeTask = cms.Task(ticlTrackstersMergev2)


