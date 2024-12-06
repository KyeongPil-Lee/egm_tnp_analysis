#############################################################
########## General settings
#############################################################
# flag to be Tested
# cutpass80 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.967083,0.929117,0.726311)
# cutpass90 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.913286,0.805013,0.358969)

# flag to be Tested
flags = {
    'reco' : '(passingRECO == 1)',
}

tnpTreeDir = 'tnpEleReco'
enable_mcFit = True # -- add weights to "data" ntuples as well
import etc.inputs.tnpSampleDef_mcFit as tnpSamples

# -- 2016, preAPV
puTree     = "/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2016_AOD/PU_Trees/preVFP/DY_madgraph_ele.pu.puTree.root"
weightName = 'weights_2016_run2016.totWeight'
theTnPSample = tnpSamples.mcFit_16pre_RECO
baseOutDir = 'results/UL2016pre/RECO_lowPt/'

# -- 2016, postAPV
# puTree     = "/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2016_AOD/PU_Trees/postVFP/DY_madgraph_ele.pu.puTree.root"
# weightName = 'weights_2016_run2016.totWeight'
# theTnPSample = tnpSamples.mcFit_16post_RECO
# baseOutDir = 'results/UL2016post/RECO_lowPt/'

# -- 2017
# puTree     = "/eos/cms/store/group/phys_egamma/swmukher/UL2017/PU_AOD/DY_1j_madgraph_ele.pu.puTree.root"
# weightName = 'weights_2017_runBCDEF.totWeight'
# theTnPSample = tnpSamples.mcFit_17_RECO
# baseOutDir = 'results/UL2017/RECO_lowPt/'

# -- 2018
# puTree     = "/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2018_AOD/PU_Trees/DY_madgraph_ele.pu.puTree.root"
# weightName = 'weights_2018_runABCD.totWeight'
# theTnPSample = tnpSamples.mcFit_18_RECO
# baseOutDir = 'results/UL2018/RECO_lowPt/'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs

samplesDef = {
    'data'   : theTnPSample['data'].clone(),
    'mcNom'  : theTnPSample['DY_madgraph'].clone(),
    'mcAlt'  : None,
    'tagSel' : None,
}

## can add data sample easily
# samplesDef['data'].add_sample( tnpSamples.UL2018['data_Run2018B'] )
# samplesDef['data'].add_sample( tnpSamples.UL2018['data_Run2018C'] )
# samplesDef['data'].add_sample( tnpSamples.UL2018['data_Run2018D'] )

## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')
samplesDef['data' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_tnpTree(tnpTreeDir)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_tnpTree(tnpTreeDir)

if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()
if not samplesDef['tagSel'] is None:
    samplesDef['tagSel'].rename('mcAltSel_DY_amcatnloext')
    samplesDef['tagSel'].set_cut('tag_Ele_pt > 37') #canceled non trig MVA cut


## set MC weight, can use several pileup rw for different data taking periods
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree(puTree)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree('') # -- not used anyway
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_puTree('') # -- not used anyway

if enable_mcFit:
    samplesDef['data'].set_weight(weightName)
    samplesDef['data'].set_puTree(puTree)

#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
   { 'var' : 'sc_eta' , 'type': 'float', 'bins': [-2.5, -2.0, -1.566, -1.444, -1.0, -0.5, 0.0, 0.5, 1.0, 1.444, 1.566, 2.0, 2.5] },
   # { 'var' : 'sc_pt' , 'type': 'float', 'bins': [20, 45, 75, 100, 500] }, # -- remove below 20 GeV bin
   { 'var' : 'sc_pt' , 'type': 'float', 'bins': [20, 45, 75] }, # -- remove below 20 GeV bin
]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
# cutBase   = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.17 && el_q*tag_Ele_q < 0'
# cutBase   = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.5 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60'
cutBase = 'tag_Ele_pt>35 && sc_pt>10  &&  tag_sc_abseta<2.5 && sc_abseta<2.5  &&  sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi)))<60'

additionalCuts = { 
    # 0 : 'tag_Ele_trigMVA > 0.92 ',
    # 1 : 'tag_Ele_trigMVA > 0.92 ',
    # 2 : 'tag_Ele_trigMVA > 0.92 ',
    # 3 : 'tag_Ele_trigMVA > 0.92 ',
    # 4 : 'tag_Ele_trigMVA > 0.92 ',
    # 5 : 'tag_Ele_trigMVA > 0.92 ',
    # 6 : 'tag_Ele_trigMVA > 0.92 ',
    # 7 : 'tag_Ele_trigMVA > 0.92 ',
    # 8 : 'tag_Ele_trigMVA > 0.92 ',
    # 9 : 'tag_Ele_trigMVA > 0.92 '
}

#### or remove any additional cut (default)
#additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    # "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    "meanP[-0.0,-5.0,5.0]","sigmaP[0.1,0.1,5.0]",
    ]

tnpParAltSigFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    ]

tnpParAltSigFit_addGaus = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,6.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "meanGF[80.0,70.0,100.0]","sigmaGF[15,5.0,125.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,85.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    ]
         
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "alphaP[0.,-5.,5.]",
    "alphaF[0.,-5.,5.]",
    ]