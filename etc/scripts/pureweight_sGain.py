import etc.inputs.tnpSampleDef as tnpSamples
from libPython.tnpClassUtils import mkdir
import libPython.puReweighter as pu

"""
Before run:
export PYTHONPATH=$PYTHONPATH:$CMSSW_BASE/egm_tnp_analysis
echo $PYTHONPATH
"""

######
# path_merged = "/pnfs/iihe/cms/store/user/kplee/EGMTnPTree/2024-09-19/UL2018/merged_240923/"
path_merged = "/pnfs/iihe/cms/store/user/kplee/EGMTnPTree/2024-09-19/UL2018/merged_240926/"
######

puType = 0

#for sName in tnpSamples.Moriond18_94X.keys():    
#    sample = tnpSamples.Moriond18_94X[sName]
#for sName in tnpSamples.UL2018.keys():    
#    sample = tnpSamples.UL2018[sName]
for sName in tnpSamples.UL2018_sGain.keys():
    sample = tnpSamples.UL2018_sGain[sName]
    if sample is None : continue
    if not 'DY' in sName: continue
    if not sample.isMC: continue
    
    trees = {}
    trees['ele'] = 'tnpEleIDs'
    # trees['pho'] = 'tnpPhoIDs' # -- no photon tree for this study
#    trees['rec'] = 'GsfElectronToSC'
    for tree in trees:
#        dirout =  '/eos/cms/store/group/phys_egamma/swmukher/ntuple_2017_v2/PU/'
#        dirout =  '/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2018_MINIAOD_Nm1/PU_Trees/'
#        dirout =  '/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2018_AOD/PU_Trees/'
        # dirout =  '/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2016/PU_Trees/preVFP/'
        dirout = path_merged
        mkdir(dirout)
        
        if   puType == 0 : sample.set_puTree( dirout + '%s_%s.pu.puTree.root'   % (sample.name,tree) )
        elif puType == 1 : sample.set_puTree( dirout + '%s_%s.nVtx.puTree.root' % (sample.name,tree) )
        elif puType == 2 : sample.set_puTree( dirout + '%s_%s.rho.puTree.root'  % (sample.name,tree) )
        sample.set_tnpTree(trees[tree]+'/fitter_tree')
        sample.dump()
        pu.reweight(sample, puType )
