import FWCore.ParameterSet.Config as cms
from RecoEgamma.EgammaIsolationAlgos.egammaHBHERecHitThreshold_cff import egammaHBHERecHit

pathToHaloMVATrainingFile = "RecoEgamma/PhotonIdentification/data/xgboostToTMVA_BHtagger.xml"
mvaHaloVariable = cms.PSet(
    #required inputs
    trainingFileName = cms.string(pathToHaloMVATrainingFile),
    rhoLabel = cms.InputTag("fixedGridRhoFastjetAllTmp"),
    barrelEcalRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    endcapEcalRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    esRecHitCollection = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES"),
    HBHERecHitsCollection = egammaHBHERecHit.hbheRecHits,
    recHitEThresholdHB = egammaHBHERecHit.recHitEThresholdHB,
    recHitEThresholdHE = egammaHBHERecHit.recHitEThresholdHE,
    noiseThrES = cms.double(0.0)
    
    
)


