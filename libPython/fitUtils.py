import ROOT as rt
rt.gROOT.LoadMacro('./libCpp/histFitter.C+')
rt.gROOT.LoadMacro('./libCpp/RooCBExGaussShapeTNP.cc+')
rt.gROOT.LoadMacro('./libCpp/RooCMSShape.cc+')
rt.gROOT.SetBatch(1)

from ROOT import tnpFitter

import re
import math


minPtForSwitch = 70

def ptMin( tnpBin ):
    ptmin = 1
    if tnpBin['name'].find('pt_') >= 0:
        ptmin = float(tnpBin['name'].split('pt_')[1].split('p')[0])
    elif tnpBin['name'].find('et_') >= 0:
        ptmin = float(tnpBin['name'].split('et_')[1].split('p')[0])
    return ptmin

def ptMax( tnpBin ):
    ptmax = 10000
    if tnpBin['name'].find('pt_') >= 0:
        ptstr = tnpBin['name'].split('pt_')[1]
        if 'To' in ptstr:
            ptmax = float(ptstr.split('To')[1].split('p')[0])
    elif tnpBin['name'].find('et_') >= 0:
        ptstr = tnpBin['name'].split('et_')[1]
        if 'To' in ptstr:
            ptmax = float(ptstr.split('To')[1].split('p')[0])
    return ptmax

def getPtBinRange( tnpBin ):
    """Return (ptmin, ptmax) tuple for the bin"""
    return (ptMin(tnpBin), ptMax(tnpBin))

def createWorkspaceForAltSig( sample, tnpBin, tnpWorkspaceParam ):

    ### tricky: use n < 0 for high pT bin (so need to remove param and add it back)
    cbNList = ['tailLeft']
    ptmin = ptMin(tnpBin)        
    if ptmin >= 35 :
        for par in cbNList:
            for ip in range(len(tnpWorkspaceParam)):
                x=re.compile('%s.*?' % par)
                listToRM = filter(x.match, tnpWorkspaceParam)
                for ir in listToRM :
                    print '**** remove', ir
                    tnpWorkspaceParam.remove(ir)                    
            tnpWorkspaceParam.append( 'tailLeft[-1]' )

    if sample.isMC:
        return tnpWorkspaceParam

    
    fileref = sample.mcRef.altSigFit
    filemc  = rt.TFile(fileref,'read')

    from ROOT import RooFit,RooFitResult
    fitresP = filemc.Get( '%s_resP' % tnpBin['name']  )
    fitresF = filemc.Get( '%s_resF' % tnpBin['name'] )

    listOfParam = ['nF','alphaF','nP','alphaP','sigmaP','sigmaF','sigmaP_2','sigmaF_2','meanGF','sigmaGF', 'sigFracF']
    
    fitPar = fitresF.floatParsFinal()
    for ipar in range(len(fitPar)):
        pName = fitPar[ipar].GetName()
        print '%s[%2.3f]' % (pName,fitPar[ipar].getVal())
        for par in listOfParam:
            if pName == par:
                x=re.compile('%s.*?' % pName)
                listToRM = filter(x.match, tnpWorkspaceParam)
                for ir in listToRM :
                    tnpWorkspaceParam.remove(ir)                    
                tnpWorkspaceParam.append( '%s[%2.3f]' % (pName,fitPar[ipar].getVal()) )
                              
  
    fitPar = fitresP.floatParsFinal()
    for ipar in range(len(fitPar)):
        pName = fitPar[ipar].GetName()
        print '%s[%2.3f]' % (pName,fitPar[ipar].getVal())
        for par in listOfParam:
            if pName == par:
                x=re.compile('%s.*?' % pName)
                listToRM = filter(x.match, tnpWorkspaceParam)
                for ir in listToRM :
                    tnpWorkspaceParam.remove(ir)
                tnpWorkspaceParam.append( '%s[%2.3f]' % (pName,fitPar[ipar].getVal()) )

    filemc.Close()

    return tnpWorkspaceParam


#############################################################
########## nominal fitter
#############################################################
def histFitterNominal( sample, tnpBin, tnpWorkspaceParam, tnpParNomFitByPt=None ):
    """
    Nominal fitter with optional pT bin-specific fit functions
    
    Args:
        sample: sample object
        tnpBin: bin definition dictionary
        tnpWorkspaceParam: list of workspace parameters (can be a function or dict)
        tnpParNomFitByPt: optional dictionary mapping pT bin ranges to (params, fitFunc) tuples
                         e.g., {(75, 100): (params_list, 'Chebychev2'), ...}
                         If None, uses default RooCMSShape for all bins
    """
    
    # Determine which fit function and parameters to use based on pT bin
    ptmin, ptmax = getPtBinRange(tnpBin)
    useParams = tnpWorkspaceParam
    useFitFunc = 'RooCMSShape'  # default
    
    # Check if pT-specific configuration is provided
    if tnpParNomFitByPt is not None:
        # Find matching pT bin range
        # Match if bin's ptmin falls within the specified range
        for (pt_range_min, pt_range_max), (params, fitFunc) in tnpParNomFitByPt.items():
            if ptmin >= pt_range_min and ptmin < pt_range_max:
                useParams = params
                useFitFunc = fitFunc
                break
    
    # Handle case where tnpWorkspaceParam is a function
    if callable(useParams):
        useParams = useParams(tnpBin)
    
    # Define fit functions based on selected type
    if useFitFunc == 'Chebychev2':
        # 2nd order Chebyshev polynomial
        tnpWorkspaceFunc = [
            "Gaussian::sigResPass(x,meanP,sigmaP)",
            "Gaussian::sigResFail(x,meanF,sigmaF)",
            "Chebychev::bkgPass(x, {c0P, c1P, c2P})",
            "Chebychev::bkgFail(x, {c0F, c1F, c2F})",
        ]
    elif useFitFunc == 'Chebychev1':
        # 1st order Chebyshev polynomial
        tnpWorkspaceFunc = [
            "Gaussian::sigResPass(x,meanP,sigmaP)",
            "Gaussian::sigResFail(x,meanF,sigmaF)",
            "Chebychev::bkgPass(x, {c0P, c1P})",
            "Chebychev::bkgFail(x, {c0F, c1F})",
        ]
    elif useFitFunc == 'Exponential':
        # Exponential background
        tnpWorkspaceFunc = [
            "Gaussian::sigResPass(x,meanP,sigmaP)",
            "Gaussian::sigResFail(x,meanF,sigmaF)",
            "Exponential::bkgPass(x, alphaP)",
            "Exponential::bkgFail(x, alphaF)",
        ]
    else:  # default: RooCMSShape
        tnpWorkspaceFunc = [
            "Gaussian::sigResPass(x,meanP,sigmaP)",
            "Gaussian::sigResFail(x,meanF,sigmaF)",
            "RooCMSShape::bkgPass(x, acmsP, betaP, gammaP, peakP)",
            "RooCMSShape::bkgFail(x, acmsF, betaF, gammaF, peakF)",
        ]

    tnpWorkspace = []
    tnpWorkspace.extend(useParams)
    tnpWorkspace.extend(tnpWorkspaceFunc)
    
    ## init fitter
    infile = rt.TFile( sample.histFile, "read")
    hP = infile.Get('%s_Pass' % tnpBin['name'] )
    hF = infile.Get('%s_Fail' % tnpBin['name'] )
    fitter = tnpFitter( hP, hF, tnpBin['name'] )
    infile.Close()

    ## setup
    fitter.useMinos()
    rootpath = sample.nominalFit.replace('.root', '-%s.root' % tnpBin['name'])
    rootfile = rt.TFile(rootpath,'update')
    fitter.setOutputFile( rootfile )
    
    ## generated Z LineShape
    ## for high pT change the failing spectra to any probe to get statistics
    fileTruth  = rt.TFile(sample.mcRef.histFile,'read')
    histZLineShapeP = fileTruth.Get('%s_Pass'%tnpBin['name'])
    histZLineShapeF = fileTruth.Get('%s_Fail'%tnpBin['name'])
    # if ptMin( tnpBin ) > minPtForSwitch:
    #    histZLineShapeF = fileTruth.Get('%s_Pass'%tnpBin['name'])
#        fitter.fixSigmaFtoSigmaP()
    fitter.setZLineShapes(histZLineShapeP,histZLineShapeF)

    fileTruth.Close()

    ### set workspace
    workspace = rt.vector("string")()
    for iw in tnpWorkspace:
        workspace.push_back(iw)
    fitter.setWorkspace( workspace )

    title = tnpBin['title'].replace(';',' - ')
    title = title.replace('probe_sc_eta','#eta_{SC}')
    title = title.replace('probe_Ele_pt','p_{T}')
    fitter.fits(sample.mcTruth,sample.isMC,title)
    rootfile.Close()



#############################################################
########## alternate signal fitter
#############################################################
def histFitterAltSig( sample, tnpBin, tnpWorkspaceParam, isaddGaus=0, tnpParAltSigFitByPt=None ):
    """
    Alternate signal fitter with optional pT bin-specific fit functions and parameters
    
    Args:
        sample: sample object
        tnpBin: bin definition dictionary
        tnpWorkspaceParam: list of workspace parameters (base parameters)
        isaddGaus: flag to add Gaussian to failing probe
        tnpParAltSigFitByPt: optional dictionary mapping pT bin ranges to (params, fitFunc) tuples
                            e.g., {(75, 100): (full_params_list, 'Chebychev2'), ...}
                            If None, uses default RooCMSShape with base parameters for all bins
                            params_list should include both signal and background parameters
    """
    # Determine which background fit function and parameters to use based on pT bin
    ptmin, ptmax = getPtBinRange(tnpBin)
    useBkgFunc = 'RooCMSShape'  # default
    useParams = tnpWorkspaceParam  # default to base parameters
    
    # Check if pT-specific configuration is provided
    if tnpParAltSigFitByPt is not None:
        # Find matching pT bin range
        for (pt_range_min, pt_range_max), config in tnpParAltSigFitByPt.items():
            if ptmin >= pt_range_min and ptmin < pt_range_max:
                # Support both old format (string only) and new format (tuple)
                if isinstance(config, tuple) and len(config) == 2:
                    useParams, useBkgFunc = config
                else:
                    # Backward compatibility: if just a string, use it as function type
                    useBkgFunc = config
                break
    
    # Handle case where useParams is a function
    if callable(useParams):
        useParams = useParams(tnpBin)
    
    # Create a copy to avoid modifying the original
    useParams = list(useParams)
    
    tnpWorkspacePar = createWorkspaceForAltSig( sample,  tnpBin, useParams )
    
    # Define background functions based on selected type
    if useBkgFunc == 'Chebychev2':
        bkgFuncPass = "Chebychev::bkgPass(x, {c0P, c1P, c2P})"
        bkgFuncFail = "Chebychev::bkgFail(x, {c0F, c1F, c2F})"
    elif useBkgFunc == 'Chebychev1':
        bkgFuncPass = "Chebychev::bkgPass(x, {c0P, c1P})"
        bkgFuncFail = "Chebychev::bkgFail(x, {c0F, c1F})"
    else:  # default: RooCMSShape
        bkgFuncPass = "RooCMSShape::bkgPass(x, acmsP, betaP, gammaP, peakP)"
        bkgFuncFail = "RooCMSShape::bkgFail(x, acmsF, betaF, gammaF, peakF)"
    
    tnpWorkspaceFunc = [
        "tailLeft[1]",
        "RooCBExGaussShapeTNP::sigResPass(x,meanP,expr('sqrt(sigmaP*sigmaP+sosP*sosP)',{sigmaP,sosP}),alphaP,nP, expr('sqrt(sigmaP_2*sigmaP_2+sosP*sosP)',{sigmaP_2,sosP}),tailLeft)",
        "RooCBExGaussShapeTNP::sigResFail(x,meanF,expr('sqrt(sigmaF*sigmaF+sosF*sosF)',{sigmaF,sosF}),alphaF,nF, expr('sqrt(sigmaF_2*sigmaF_2+sosF*sosF)',{sigmaF_2,sosF}),tailLeft)",
        bkgFuncPass,
        bkgFuncFail,
        ]
    if isaddGaus==1:
        tnpWorkspaceFunc += [ "Gaussian::sigGaussFail(x,meanGF,sigmaGF)", ]
        if sample.isMC:
            tnpWorkspaceFunc += [ "sigFracF[0.5,0.0,1.0]", ]

    tnpWorkspace = []
    tnpWorkspace.extend(tnpWorkspacePar)
    tnpWorkspace.extend(tnpWorkspaceFunc)
        
    ## init fitter
    infile = rt.TFile( sample.histFile, "read")
    hP = infile.Get('%s_Pass' % tnpBin['name'] )
    hF = infile.Get('%s_Fail' % tnpBin['name'] )
    ## for high pT change the failing spectra to passing probe to get statistics 
    ## MC only: this is to get MC parameters in data fit!
    if sample.isMC and ptMin( tnpBin ) > minPtForSwitch:     
        hF = infile.Get('%s_Pass' % tnpBin['name'] )
    fitter = tnpFitter( hP, hF, tnpBin['name'] )
#    fitter.fixSigmaFtoSigmaP()
    infile.Close()

    ## setup
    rootpath = sample.altSigFit.replace('.root', '-%s.root' % tnpBin['name'])
    rootfile = rt.TFile(rootpath,'update')
    fitter.setOutputFile( rootfile )
    
    ## generated Z LineShape
    fileTruth = rt.TFile('etc/inputs/ZeeGenLevel.root','read')
    histZLineShape = fileTruth.Get('Mass')
    fitter.setZLineShapes(histZLineShape,histZLineShape)
    fileTruth.Close()

    ### set workspace
    workspace = rt.vector("string")()
    for iw in tnpWorkspace:
        workspace.push_back(iw)
    fitter.setWorkspace( workspace, isaddGaus )

    title = tnpBin['title'].replace(';',' - ')
    title = title.replace('probe_sc_eta','#eta_{SC}')
    title = title.replace('probe_Ele_pt','p_{T}')
    fitter.fits(sample.mcTruth,sample.isMC,title, isaddGaus)

    rootfile.Close()



#############################################################
########## alternate background fitter
#############################################################
def histFitterAltBkg( sample, tnpBin, tnpWorkspaceParam, tnpParAltBkgFitByPt=None ):
    """
    Alternate background fitter with optional pT bin-specific background functions
    
    Args:
        sample: sample object
        tnpBin: bin definition dictionary
        tnpWorkspaceParam: list of workspace parameters
        tnpParAltBkgFitByPt: optional dictionary mapping pT bin ranges to (params, fitFunc) tuples
                            e.g., {(75, 100): (params_list, 'ExpPlusConst'), ...}
                            If None, uses default Exponential for all bins
    """
    # Determine which background fit function and parameters to use based on pT bin
    ptmin, ptmax = getPtBinRange(tnpBin)
    useParams = tnpWorkspaceParam
    useBkgFunc = 'Exponential'  # default
    
    # Check if pT-specific configuration is provided
    if tnpParAltBkgFitByPt is not None:
        # Find matching pT bin range
        for (pt_range_min, pt_range_max), (params, bkgFunc) in tnpParAltBkgFitByPt.items():
            if ptmin >= pt_range_min and ptmin < pt_range_max:
                useParams = params
                useBkgFunc = bkgFunc
                break
    
    # Handle case where tnpWorkspaceParam is a function
    if callable(useParams):
        useParams = useParams(tnpBin)
    
    # Define background functions based on selected type
    if useBkgFunc == 'Chebychev2':
        bkgFuncPass = "Chebychev::bkgPass(x, {c0P, c1P, c2P})"
        bkgFuncFail = "Chebychev::bkgFail(x, {c0F, c1F, c2F})"
    elif useBkgFunc == 'Chebychev1':
        bkgFuncPass = "Chebychev::bkgPass(x, {c0P, c1P})"
        bkgFuncFail = "Chebychev::bkgFail(x, {c0F, c1F})"
    elif useBkgFunc == 'ExpPlusConst':
        # a*exp(bx)+c form: using RooGenericPdf
        bkgFuncPass = "GenericPdf::bkgPass('aP*exp(bP*x)+cP',{x,aP,bP,cP})"
        bkgFuncFail = "GenericPdf::bkgFail('aF*exp(bF*x)+cF',{x,aF,bF,cF})"
    else:  # default: Exponential
        bkgFuncPass = "Exponential::bkgPass(x, alphaP)"
        bkgFuncFail = "Exponential::bkgFail(x, alphaF)"

    tnpWorkspaceFunc = [
        "Gaussian::sigResPass(x,meanP,sigmaP)",
        "Gaussian::sigResFail(x,meanF,sigmaF)",
        bkgFuncPass,
        bkgFuncFail,
        ]

    tnpWorkspace = []
    tnpWorkspace.extend(useParams)
    tnpWorkspace.extend(tnpWorkspaceFunc)
            
    ## init fitter
    infile = rt.TFile(sample.histFile,'read')
    hP = infile.Get('%s_Pass' % tnpBin['name'] )
    hF = infile.Get('%s_Fail' % tnpBin['name'] )
    fitter = tnpFitter( hP, hF, tnpBin['name'] )
    infile.Close()

    ## setup
    rootpath = sample.altBkgFit.replace('.root', '-%s.root' % tnpBin['name'])
    rootfile = rt.TFile(rootpath,'update')
    fitter.setOutputFile( rootfile )
#    fitter.setFitRange(65,115)

    ## generated Z LineShape
    ## for high pT change the failing spectra to any probe to get statistics
    fileTruth = rt.TFile(sample.mcRef.histFile,'read')
    histZLineShapeP = fileTruth.Get('%s_Pass'%tnpBin['name'])
    histZLineShapeF = fileTruth.Get('%s_Fail'%tnpBin['name'])
    if ptMin( tnpBin ) > minPtForSwitch: 
        histZLineShapeF = fileTruth.Get('%s_Pass'%tnpBin['name'])
#        fitter.fixSigmaFtoSigmaP()
    fitter.setZLineShapes(histZLineShapeP,histZLineShapeF)
    fileTruth.Close()

    ### set workspace
    workspace = rt.vector("string")()
    for iw in tnpWorkspace:
        workspace.push_back(iw)
    fitter.setWorkspace( workspace )

    title = tnpBin['title'].replace(';',' - ')
    title = title.replace('probe_sc_eta','#eta_{SC}')
    title = title.replace('probe_Ele_pt','p_{T}')
    fitter.fits(sample.mcTruth,sample.isMC,title)
    rootfile.Close()


#############################################################
########## alternate signal+background fitter
#############################################################
def histFitterAltSigBkg( sample, tnpBin, tnpWorkspaceParam):

    tnpWorkspaceFunc = [
        "tailLeft[1]",
        "RooCBExGaussShapeTNP::sigResPass(x,meanP,expr('sqrt(sigmaP*sigmaP+sosP*sosP)',{sigmaP,sosP}),alphaP,nP, expr('sqrt(sigmaP_2*sigmaP_2+sosP*sosP)',{sigmaP_2,sosP}),tailLeft)",
        "RooCBExGaussShapeTNP::sigResFail(x,meanF,expr('sqrt(sigmaF*sigmaF+sosF*sosF)',{sigmaF,sosF}),alphaF,nF, expr('sqrt(sigmaF_2*sigmaF_2+sosF*sosF)',{sigmaF_2,sosF}),tailLeft)",
        "Exponential::bkgPass(x, alphaP_2)",
        "Exponential::bkgFail(x, alphaF_2)",
        ]

    tnpWorkspace = []
    tnpWorkspace.extend(tnpWorkspaceParam)
    tnpWorkspace.extend(tnpWorkspaceFunc)
            
    ## init fitter
    infile = rt.TFile(sample.histFile,'read')
    hP = infile.Get('%s_Pass' % tnpBin['name'] )
    hF = infile.Get('%s_Fail' % tnpBin['name'] )
    fitter = tnpFitter( hP, hF, tnpBin['name'] )
    infile.Close()
    
    ## setup
    rootpath = sample.altSigBkgFit.replace('.root', '-%s.root' % tnpBin['name'])
    rootfile = rt.TFile(rootpath,'update')
    fitter.setOutputFile( rootfile )
#    fitter.setFitRange(65,115)


    ## generated Z LineShape
    ## for high pT change the failing spectra to any probe to get statistics
    fileTruth = rt.TFile(sample.mcRef.histFile,'read')
    histZLineShapeP = fileTruth.Get('%s_Pass'%tnpBin['name'])
    histZLineShapeF = fileTruth.Get('%s_Fail'%tnpBin['name'])
    if ptMin( tnpBin ) > minPtForSwitch: 
        histZLineShapeF = fileTruth.Get('%s_Pass'%tnpBin['name'])
#        fitter.fixSigmaFtoSigmaP()
    fitter.setZLineShapes(histZLineShapeP,histZLineShapeF)
    fileTruth.Close()

    ### set workspace
    workspace = rt.vector("string")()
    for iw in tnpWorkspace:
        workspace.push_back(iw)
    fitter.setWorkspace( workspace )

    title = tnpBin['title'].replace(';',' - ')
    title = title.replace('probe_sc_eta','#eta_{SC}')
    title = title.replace('probe_Ele_pt','p_{T}')
    fitter.fits(sample.mcTruth,sample.isMC,title)
    rootfile.Close()


