import FWCore.ParameterSet.Config as cms
import os

maxevts   = 1000
globaltag = 'GR09_31X_V4P::All'
globaltag = 'STARTUP3XY_V9::All'
inputfile = '/store/data/CRAFT09/Cosmics/RECO/v1/000/109/468/F2CDA89C-B57D-DE11-B2C9-000423D98DC4.root'

process   = cms.Process("RPCTechnicalTrigger")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.MessageLogger.cerr.enable = False
process.MessageLogger.cout = cms.untracked.PSet(
        enable = cms.untracked.bool(True),
    	threshold = cms.untracked.string('DEBUG'),
	INFO = cms.untracked.PSet(
        limit = cms.untracked.int32(-1) ) )

#.. Geometry and Global Tags
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string( globaltag )
process.load("Configuration.StandardSequences.MagneticField_cff")

#.. if cosmics: reconstruction sequence for Cosmics
###process.load("Configuration.StandardSequences.ReconstructionCosmics_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(maxevts) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring( inputfile ) )

#..............................................................................................................
#.. EventSetup Configuration
#...

useEventSetup = 0
mytag         = 'test5'
database      = 'sqlite'

if database   == 'sqlite':
    dbconnection = 'sqlite_file:/afs/cern.ch/user/a/aosorio/public/rpcTechnicalTrigger/myrbconfig.db'
elif database == 'oraclerpc':
    dbconnection = 'oracle://devdb10/CMS_RPC_COMMISSIONING'
else:
    dbconnection = ''

if useEventSetup >= 1:

    from CondCore.DBCommon.CondDBCommon_cfi import *

    PoolDBESSource = cms.ESSource("PoolDBESSource",
                                  loadAll = cms.bool(True),
                                  toGet = cms.VPSet(cms.PSet( record = cms.string('RBCBoardSpecsRcd'),
                                                              tag = cms.string(mytag+'a')),
                                                    cms.PSet( record = cms.string('TTUBoardSpecsRcd'),
                                                              tag = cms.string(mytag+'b'))),
                                  DBParameters = cms.PSet( messageLevel = cms.untracked.int32(2),
                                                           authenticationPath = cms.untracked.string('')),
                                  messagelevel = cms.untracked.uint32(2),
                                  connect = cms.string(dbconnection) )

    CondDBCommon.connect = cms.string( dbconnection )

#..............................................................................................................

process.load("L1Trigger.RPCTechnicalTrigger.rpcTechnicalTrigger_cfi")

process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('rpcttbits.root'),
                               outputCommands = cms.untracked.vstring('drop *','keep L1GtTechnicalTriggerRecord_*_*_*') )

process.p = cms.Path(process.rpcTechnicalTrigger)

process.e = cms.EndPath(process.out)

