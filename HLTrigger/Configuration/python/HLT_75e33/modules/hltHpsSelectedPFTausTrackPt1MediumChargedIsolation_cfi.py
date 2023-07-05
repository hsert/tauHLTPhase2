#HS
import FWCore.ParameterSet.Config as cms

hltHpsSelectedPFTausTrackPt1MediumChargedIsolation = cms.EDFilter( "PFTauSelector",
    src = cms.InputTag( "hltHpsPFTauProducer" ),
    cut = cms.string( "pt > 0" ),
    discriminators = cms.VPSet( 
      cms.PSet(  discriminator = cms.InputTag( "hltHpsPFTauTrackPt1Discriminator" ),
        selectionCut = cms.double( 0.5 )
      ),
      cms.PSet(  discriminator = cms.InputTag( "hltHpsPFTauMediumAbsOrRelChargedIsolationDiscriminator" ),
        selectionCut = cms.double( 0.5 )
      )
    ),
    discriminatorContainers = cms.VPSet( 
    )
)