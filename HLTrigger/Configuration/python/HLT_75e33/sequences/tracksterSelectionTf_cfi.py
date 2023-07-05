import FWCore.ParameterSet.Config as cms

tracksterSelectionTf = cms.ESProducer("TfGraphDefProducer",
    ComponentName = cms.string('tracksterSelectionTf'),
    FileName = cms.FileInPath('RecoHGCal/TICL/data/tf_models/energy_id_v0.pb'),
    appendToDataLabel = cms.string('')
)