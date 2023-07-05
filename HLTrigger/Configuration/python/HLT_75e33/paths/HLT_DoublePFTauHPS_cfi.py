import FWCore.ParameterSet.Config as cms

from ..modules.hltPreDoublePFTauHPS_cfi import *
from ..sequences.HLTBeginSequence_cfi import *
from ..sequences.HLTEndSequence_cfi import *
from ..sequences.HLTParticleFlowSequence_cfi import *
from ..sequences.HLTAK4PFJetsReconstruction_cfi import *
from ..sequences.hltPFTauHPS_cfi import *
from ..sequences.HLTHPSMediumChargedIsoPFTauSequence_cfi import *
from ..modules.hltHpsSelectedPFTausTrackPt1MediumChargedIsolation_cfi import *
from ..sequences.hltHpsDoublePFTau40TrackPt1MediumChargedIsolation_cfi import *
from ..sequences.hltHpsL1JetsHLTDoublePFTauTrackPt1MediumChargedIsolationMatch_cfi import *

from ..modules.hltAK4PFJetsForTaus_cfi import *

HLT_DoublePFTauHPS = cms.Path(
    HLTBeginSequence + 
    hltPreDoublePFTauHPS +
    HLTParticleFlowSequence +
    HLTAK4PFJetsReconstruction +
    hltAK4PFJetsForTaus +
    hltPFTauHPS +
    HLTHPSMediumChargedIsoPFTauSequence+
    #hltHpsSelectedPFTausTrackPt1MediumChargedIsolation+
    #hltHpsDoublePFTau40TrackPt1MediumChargedIsolation+
    #hltHpsL1JetsHLTDoublePFTauTrackPt1MediumChargedIsolationMatch+
    HLTEndSequence
)
