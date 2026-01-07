#!bin/bash

echo "Run under cmssw-el7"

cd /afs/cern.ch/user/k/kplee/work_Detector/EGMFitter/mcFit/CMSSW_11_2_0/
eval `scramv1 runtime -sh`
cd /afs/cern.ch/user/k/kplee/work_Detector/EGMFitter/dataFit/egm_tnp_analysis

echo "CMSSW environment set (CMSSW_11_2_0)"
