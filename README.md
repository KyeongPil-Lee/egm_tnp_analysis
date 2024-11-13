# Fit on MC (not counting)

## Recipe

### First setup (@ lxplus)

```bash
cd /afs/cern.ch/work/k/kplee/private/Detector/EGMFitter/mcFit/
cmsrel CMSSW_11_2_0
cd CMSSW_11_2_0/src
cmsenv

git clone git@github.com:KyeongPil-Lee/egm_tnp_analysis.git
cd egm_tnp_analysis
make

git checkout -b mcFit
git push origin mcFit
```

### Usual setup

```bash
cd /afs/cern.ch/work/k/kplee/private/Detector/EGMFitter/mcFit/CMSSW_11_2_0/src/egm_tnp_analysis
cmssw-el7

cmsenv
```



## Update

`libPython/histUtil.pyx`

* `makePassFailHistograms`: allow applying weights also for the data ntuple
  * To apply gen-weight & PU reweighting to the MC ntuple put in "data" slot (to perform the fit)
* Need to run `make cython-build` to update `.cpp` file

`libPython/efficiencyUtils.py`

* Add a few functions to make 2D histograms with the efficiencies (including alt. efficiencies)

`tnpEGM_fitter.py`

* Update to use the new functions in `libPython/efficiencyUtils.py`