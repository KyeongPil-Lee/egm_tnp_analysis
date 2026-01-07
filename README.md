# Fit on DATA, RECO efficiency
* To update the RECO data efficiency without template substitution
  * The reproduction of the official SF was also performed to validate the machienry & input TnP trees

* Recipe, setup: similar with `mcFit` branch (use `CMSSW_11_2_0` env.)
  * working directory: `/afs/cern.ch/user/k/kplee/work_Detector/EGMFitter/dataFit/egm_tnp_analysis` under lxplus

* Run: `source run_RECO.sh`

## Update
* Base branch: `mcFit`

* `libPython/fitUtils.py`: 
  * Remove template substitution part for high-pT region
  * Add a new feature: change the fit function per pT bins
