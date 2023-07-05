#HS
import FWCore.ParameterSet.Config as cms

hltHpsL1JetsHLTDoublePFTauTrackPt1MediumChargedIsolationMatch = cms.EDProducer( "L1THLTTauMatching",
    L1TauTrigger = cms.InputTag( "hltL1sDoubleTauBigOR" ),
    JetSrc = cms.InputTag( "hltHpsSelectedPFTausTrackPt1MediumChargedIsolation" ),
    EtMin = cms.double( 0.0 ),
    ReduceTauContent = cms.bool( True ),
    KeepOriginalVertex = cms.bool( False )
)