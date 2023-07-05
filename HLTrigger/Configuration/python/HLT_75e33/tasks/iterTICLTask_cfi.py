import FWCore.ParameterSet.Config as cms

from ..tasks.ticlCLUE3DHighTask_cfi import *
from ..tasks.ticlLayerTileTask_cfi import *
from ..tasks.ticlPFTask_cfi import *
from ..tasks.ticlTracksterMergeTask_cfi import *

iterTICLTask = cms.Task(
    ticlCLUE3DHighStepTask,
    ticlLayerTileTask,
    ticlPFTask,
    ticlTracksterMergeTask,
)
