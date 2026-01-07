#############################################################
########## General settings
#############################################################
# flag to be Tested
flags = {
    'reco' : '(passingRECO == 1)',
}

tnpTreeDir = 'tnpEleReco'
enable_mcFit = True # -- add weights to "data" ntuples as well
import etc.inputs.tnpSampleDef_dataFit as tnpSamples

# -- 2016, preAPV
puTree_nom = "/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2016_AOD/PU_Trees/preVFP/DY_madgraph_ele.pu.puTree.root"
puTree_alt = "/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2016_AOD/PU_Trees/preVFP/DY_amcatnloext_ele.pu.puTree.root"
weightName = 'weights_2016_run2016.totWeight'
theTnPSample = tnpSamples.dataFit_16pre_RECO
baseOutDir = 'results/UL2016pre/RECO_highPt/'

# -- 2016, postAPV
# puTree_nom = "/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2016_AOD/PU_Trees/postVFP/DY_madgraph_ele.pu.puTree.root"
# puTree_alt = "/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2016_AOD/PU_Trees/postVFP/DY_amcatnloext_ele.pu.puTree.root"
# weightName = 'weights_2016_run2016.totWeight'
# theTnPSample = tnpSamples.dataFit_16post_RECO
# baseOutDir = 'results/UL2016post/RECO_highPt/'

# -- 2017
# puTree_nom = "/eos/cms/store/group/phys_egamma/swmukher/UL2017/PU_AOD/DY_1j_madgraph_ele.pu.puTree.root"
# puTree_alt = "/eos/cms/store/group/phys_egamma/swmukher/UL2017/PU_AOD/DY_amcatnloext_ele.pu.puTree.root"
# weightName = 'weights_2017_runBCDEF.totWeight'
# theTnPSample = tnpSamples.dataFit_17_RECO
# baseOutDir = 'results/UL2017/RECO_highPt/'

# -- 2018
# puTree_nom  = "/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2018_AOD/PU_Trees/DY_madgraph_ele.pu.puTree.root"
# puTree_alt = "/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2018_AOD/PU_Trees/DY_amcatnloext_ele.pu.puTree.root"
# weightName = 'weights_2018_runABCD.totWeight'
# theTnPSample = tnpSamples.dataFit_18_RECO
# baseOutDir = 'results/UL2018/RECO_highPt/'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs

samplesDef = {
    'data'   : theTnPSample['data'].clone(),
    'mcNom'  : theTnPSample['DY_madgraph'].clone(),
    'mcAlt'  : theTnPSample['DY_amcatnloext'].clone(),
    'tagSel' : theTnPSample['DY_madgraph'].clone(),
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
    samplesDef['tagSel'].rename('mcAltSel_DY_madgraph')
    samplesDef['tagSel'].set_cut('tag_Ele_pt > 37') #canceled non trig MVA cut


## set MC weight, can use several pileup rw for different data taking periods
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree(puTree_nom)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree(puTree_alt)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_puTree(puTree_nom)

#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
   # { 'var' : 'sc_eta' , 'type': 'float', 'bins': [-2.5, -2.0, -1.566, -1.444, -1.0, -0.5, 0.0, 0.5, 1.0, 1.444, 1.566, 2.0, 2.5] },
   { 'var' : 'sc_abseta' , 'type': 'float', 'bins': [0.0, 0.5, 1.0, 1.444, 1.566, 2.0, 2.5] },
   # { 'var' : 'sc_pt' , 'type': 'float', 'bins': [20, 45, 75, 100, 500] },
   { 'var' : 'sc_pt' , 'type': 'float', 'bins': [75, 100, 500] },
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
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    # "acmsF[10.,0.1.,80.]","betaF[0.01,0.001,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",
    # "meanP[-0.0,-5.0,5.0]","sigmaP[0.1,0.1,5.0]", # -- bin 04
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

#############################################################
########## pT bin-specific fit function configuration
########## Define different fit functions for different pT bins
#############################################################
# Nominal fit: Use 2nd order Chebyshev polynomial for 75 < pT < 100 GeV bin
# Format: {(pt_min, pt_max): (parameter_list, fit_function_type)}
# Available fit function types: 'RooCMSShape' (default), 'Chebychev2', 'Chebychev1', 'Exponential'
tnpParNomFitByPt = {
    (75, 100): (
        [
            "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
            "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
            "c0P[1.0,0.0,10.0]","c1P[0.0,-5.0,5.0]","c2P[0.0,-5.0,5.0]",
            "c0F[1.0,0.0,10.0]","c1F[0.0,-5.0,5.0]","c2F[0.0,-5.0,5.0]",
        ],
        'Chebychev2'
    ),
    # Add more pT bin ranges as needed
    # (100, 500): (
    #     [
    #         "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    #         "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    #         "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    #         "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",
    #     ],
    #     'RooCMSShape'
    # ),
}

# Alternate signal fit: pT bin-specific fit function and parameter configuration
# Format: {(pt_min, pt_max): (full_parameter_list, background_function_type)}
# Available types: 'RooCMSShape' (default), 'Chebychev2', 'Chebychev1'
# Note: Full parameter list should include both signal and background parameters
# This is consistent with other fit types (nominal, altBkg)
tnpParAltSigFitByPt = {
    (75, 100): (
        [
            # Signal parameters
            "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
            "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
            # Background parameters (Chebychev2)
            "c0P[1.0,0.0,10.0]","c1P[0.0,-5.0,5.0]","c2P[0.0,-5.0,5.0]",
            "c0F[1.0,0.0,10.0]","c1F[0.0,-5.0,5.0]","c2F[0.0,-5.0,5.0]",
        ],
        'Chebychev2'
    ),
}

# Alternate background fit: pT bin-specific background function configuration
# Format: {(pt_min, pt_max): (parameter_list, background_function_type)}
# Available types: 'Exponential' (default), 'Chebychev2', 'Chebychev1', 'ExpPlusConst' (a*exp(bx)+c)
tnpParAltBkgFitByPt = {
    # (20, 45): (
    #     [
    #         "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    #         "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    #         "c0P[1.0,0.0,10.0]","c1P[0.0,-5.0,5.0]","c2P[0.0,-5.0,5.0]",
    #         "c0F[1.0,0.0,10.0]","c1F[0.0,-5.0,5.0]","c2F[0.0,-5.0,5.0]",
    #     ],
    #     'Chebychev2'
    # ),
    # (45, 75): (
    #     [
    #         "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    #         "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    #         "c0P[1.0,0.0,10.0]","c1P[0.0,-5.0,5.0]","c2P[0.0,-5.0,5.0]",
    #         "c0F[1.0,0.0,10.0]","c1F[0.0,-5.0,5.0]","c2F[0.0,-5.0,5.0]",
    #     ],
    #     'Chebychev2'
    # ),
    (75, 100): (
        [
            "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
            "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
            "aP[1.0,0.0,10.0]","bP[-0.1,-1.0,1.0]","cP[0.0,-5.0,5.0]",
            "aF[1.0,0.0,10.0]","bF[-0.1,-1.0,1.0]","cF[0.0,-5.0,5.0]",
        ],
        'ExpPlusConst'
    ),
    # 100 < pT < 500 GeV uses default Exponential (no need to specify)
}