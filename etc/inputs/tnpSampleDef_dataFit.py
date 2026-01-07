from libPython.tnpClassUtils import tnpSample

# -- RECO trees
# -- ref: S43 of https://indico.cern.ch/event/1484434/contributions/6255682/attachments/2981971/5250669/20241206_DrellYan_HighMee_KLee_v1.pdf
dir_16pre_RECO = "/eos/cms/store/group/phys_egamma/akapoor/Tag-and-Probe_Tree/UL2016_ntuples/"
tree_16pre_RECO = {
  "data" : dir_16pre_RECO + "UL2016_SingleEle_preVFP_BBv2CDEFpreVFP_AOD.root",
  "DY_madgraph": dir_16pre_RECO + "DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_preVFP_UL2016_AOD.root",
  "DY_amcatnloext": dir_16pre_RECO + "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_preVFP_UL2016_AOD.root"
}

dir_16post_RECO = dir_16pre_RECO
tree_16post_RECO = {
  "data" : dir_16post_RECO + "UL2016_SingleEle_postVFP_FpostVFPandGH_AOD.root",
  "DY_madgraph": dir_16post_RECO + "DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_postVFP_UL2016_AOD.root",
  "DY_amcatnloext": dir_16post_RECO + "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_postVFP_UL2016_AOD.root"
}

dir_17_RECO = "/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2017_AOD/"
tree_17_RECO = {
  "data" : dir_17_RECO + "Run_BCDEF_SingEle.root",
  "DY_madgraph": dir_17_RECO + "DYJetsToEE_fs.root",
  "DY_amcatnloext": dir_17_RECO + "DYJetsToLL_amcatnloFXFX.root"
}

dir_18_RECO = "/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2018_AOD/"
tree_18_RECO = {
  "data" : dir_18_RECO + "EGamma_RunABCD.root",
  "DY_madgraph": dir_18_RECO + "DYJetsToLL_madgraphMLM.root",
  "DY_amcatnloext": dir_18_RECO + "DYJetsToLL_amcatnloFXFX.root"
}


dataFit_16pre_RECO = {
    'DY_madgraph' : tnpSample('DY_madgraph',
                              tree_16pre_RECO['DY_madgraph'],
                              isMC = True, nEvts = -1 ),

    'DY_amcatnloext' : tnpSample('DY_amcatnloext',
                              tree_16pre_RECO['DY_amcatnloext'],
                              isMC = True, nEvts =  -1 ),

    'data' : tnpSample('data',
                       tree_16pre_RECO['data'],
                       lumi = 19.76329286),
}

dataFit_16post_RECO = {
    'DY_madgraph' : tnpSample('DY_madgraph',
                              tree_16post_RECO['DY_madgraph'],
                              isMC = True, nEvts = -1 ),

    'DY_amcatnloext' : tnpSample('DY_amcatnloext',
                              tree_16post_RECO['DY_amcatnloext'],
                              isMC = True, nEvts =  -1 ),

    'data' : tnpSample('data',
                       tree_16post_RECO['data'],
                       lumi = 16.851738703),
}

dataFit_17_RECO = {
    'DY_madgraph' : tnpSample('DY_madgraph',
                              tree_17_RECO['DY_madgraph'],
                              isMC = True, nEvts = -1 ),

    'DY_amcatnloext' : tnpSample('DY_amcatnloext',
                              tree_17_RECO['DY_amcatnloext'],
                              isMC = True, nEvts =  -1 ),

    'data' : tnpSample('data',
                       tree_17_RECO['data'],
                       lumi = 41.497435514),
}

dataFit_18_RECO = {
    'DY_madgraph' : tnpSample('DY_madgraph',
                              tree_18_RECO['DY_madgraph'],
                              isMC = True, nEvts = -1 ),

    'DY_amcatnloext' : tnpSample('DY_amcatnloext',
                              tree_18_RECO['DY_amcatnloext'],
                              isMC = True, nEvts =  -1 ),

    'data' : tnpSample('data',
                       tree_18_RECO['data'],
                       lumi = 59.724318946),
}

# -- ID trees
# -- from https://github.com/lsoffi/egm_tnp_analysis/blob/egm_tnp_CleanedCodeForUL_17March2020/etc/inputs/tnpSampleDef.py
eosUL2016 = '/eos/cms/store/group/phys_egamma/akapoor/Tag-and-Probe_Tree/UL2016_ntuples/'
eosUL2017 = '/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2017_MINIAOD_Nm1/'
eosUL2018 = '/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2018_MINIAOD_Nm1/'
#TODO check the difference with tnpSampleDef.py trees e.g.:
### eosUL2018 = '/eos/cms/store/group/phys_egamma/tnpTuples/tomc/2020-05-20/UL2018/merged/' ### from tnpSampleDef.py
### Paths were changed in this commit (August 2022) : https://github.com/cms-egamma/egm_tnp_analysis/commit/2b2bc72da1996e5843e0f6c5a3e9d718ab908e20

dataFit_16pre_ID = {
    ### MiniAOD TnP for IDs scale factors
    'DY_madgraph'    : tnpSample('DY_madgraph',
                                 eosUL2016 + 'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_preVFP_UL2016.root',
                                 isMC = True, nEvts =  -1 ),
    'DY_amcatnloext' : tnpSample('DY_amcatnloext',
                                 eosUL2016 + 'DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_preVFP_UL2016.root',
                                 isMC = True, nEvts =  -1 ),

     'data_Run2016B' :      tnpSample('data_Run2016B' ,      eosUL2016 + 'UL2016_SingleEle_Run2016B.root' , lumi = 0.030493962),
     'data_Run2016B_ver2' : tnpSample('data_Run2016B_ver2' , eosUL2016 + 'UL2016_SingleEle_Run2016B_ver2.root' , lumi = 5.879330594),
     'data_Run2016C' :      tnpSample('data_Run2016C' ,      eosUL2016 + 'UL2016_SingleEle_Run2016C.root' , lumi = 2.64992914),
     'data_Run2016D' :      tnpSample('data_Run2016D' ,      eosUL2016 + 'UL2016_SingleEle_Run2016D.root' , lumi = 4.292865604),
     'data_Run2016E' :      tnpSample('data_Run2016E' ,      eosUL2016 + 'UL2016_SingleEle_Run2016E.root' , lumi = 4.185165152),
     'data_Run2016F' :      tnpSample('data_Run2016F' ,      eosUL2016 + 'UL2016_SingleEle_Run2016F.root' , lumi = 2.725508364),
    # 'data' : tnpSample('data', eosUL2016+'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_preVFP_UL2016.root', lumi = 19.76329286,),
}

dataFit_16post_ID = {
    ### MiniAOD TnP for IDs scale factors
    'DY_madgraph'    : tnpSample('DY_madgraph',
                                  eosUL2016 + 'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_postVFP_UL2016.root',
                                  isMC = True, nEvts =  -1 ),
    'DY_amcatnloext' : tnpSample('DY_amcatnloext',
                                  eosUL2016 + 'DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_postVFP_UL2016.root',
                                  isMC = True, nEvts =  -1 ),

     'data_Run2016F_postVFP' : tnpSample('data_Run2016F_postVFP' , eosUL2016 + 'UL2016_SingleEle_Run2016F_postVFP.root' , lumi = 0.414987426),
     'data_Run2016G' :         tnpSample('data_Run2016G' ,         eosUL2016 + 'UL2016_SingleEle_Run2016G.root' , lumi = 7.634508755),
     'data_Run2016H' :         tnpSample('data_Run2016H' ,         eosUL2016 + 'UL2016_SingleEle_Run2016H.root' , lumi = 8.802242522),
    # 'data' : tnpSample('data', eosUL2016+'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_postVFP_UL2016.root', lumi = 16.851738703, ),

    }

dataFit_17_ID = {
    ### MiniAOD TnP for IDs scale factors
    'DY_madgraph'              : tnpSample('DY_madgraph',
                                           eosUL2017 + 'DYJetsToEE.root',
                                           isMC = True, nEvts =  -1 ),

    'DY_amcatnloext'           :  tnpSample('DY_amcatnloext',
                                            eosUL2017 + 'DYJetsToLL_amcatnloFXFX.root',
                                            isMC = True, nEvts =  -1 ),


    'data_Run2017B' : tnpSample('data_Run2017B' , eosUL2017 + 'SingleEle_RunB.root' , lumi = 4.793961427),
    'data_Run2017C' : tnpSample('data_Run2017C' , eosUL2017 + 'SingleEle_RunC.root' , lumi = 9.631214821),
    'data_Run2017D' : tnpSample('data_Run2017D' , eosUL2017 + 'SingleEle_RunD.root' , lumi = 4.247682053),
    'data_Run2017E' : tnpSample('data_Run2017E' , eosUL2017 + 'SingleEle_RunE.root' , lumi = 9.313642402),
    'data_Run2017F' : tnpSample('data_Run2017F' , eosUL2017 + 'SingleEle_RunF.root' , lumi = 13.510934811),
    #'data' : tnpSample('data', eosUL2017+'DYJetsToEE.root', lumi = 41.497435514, ),
}

dataFit_18_ID = {
    ### MiniAOD TnP for IDs scale factors
    'DY_madgraph'    : tnpSample('DY_madgraph',
                                 eosUL2018 + 'DYJetsToLL_madgraphMLM.root',
                                 isMC = True, nEvts =  -1 ),
    'DY_amcatnloext' : tnpSample('DY_amcatnloext',
                                 eosUL2018 + 'DYJetsToLL_amcatnloFXFX.root',
                                 isMC = True, nEvts =  -1 ),

    'data_Run2018A' : tnpSample('data_Run2018A' , eosUL2018 + 'EGamma_RunA.root' , lumi = 14.02672485),
    'data_Run2018B' : tnpSample('data_Run2018B' , eosUL2018 + 'EGamma_RunB.root' , lumi = 7.060617355),
    'data_Run2018C' : tnpSample('data_Run2018C' , eosUL2018 + 'EGamma_RunC.root' , lumi = 6.894770971),
    'data_Run2018D' : tnpSample('data_Run2018D' , eosUL2018 + 'EGamma_RunD.root' , lumi = 31.74220577),
    #'data' : tnpSample('data', eosUL2018+'DYJetsToLL_madgraphMLM.root', lumi = 59.724318946, ),
}
