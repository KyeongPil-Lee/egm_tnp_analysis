To fit on UL with respect to seed gain

## PU reweighting

* Update the files with the latest setup
  * `etc/scripts/puReweighter.py`
    * Proper PU distribution for each era
  * `etc/scripts/pureweight_sGain.py`
    * Input files (MC tree)
  * `etc/scripts/tnpSampleDef.py`
    * Definition of TnP samples, path to the trees

### Run the code

```bash
export PYTHONPATH=$PYTHONPATH:$CMSSW_BASE/egm_tnp_analysis
echo $PYTHONPATH
python etc/scripts/pureweight_sGain.py >&pureweight_sGain.log&
tail -f pureweight_sGain.log
```



## Run the fit

### Configuration

Update `etc/config/settings_ele_sGain_UL2018.py`

* Setup PU trees



## Recipe

```bash
python tnpEGM_fitter.py etc/config/settings_ele_sGain_UL2018.py --flag mediumID --checkBins
python tnpEGM_fitter.py etc/config/settings_ele_sGain_UL2018.py --flag mediumID --createBins
python tnpEGM_fitter.py etc/config/settings_ele_sGain_UL2018.py --flag mediumID --createHists >&createHists.log& tail -f createHists.log
python tnpEGM_fitter.py etc/config/settings_ele_sGain_UL2018.py --flag mediumID --doFit
python tnpEGM_fitter.py etc/config/settings_ele_sGain_UL2018.py --flag mediumID --doFit --mcSig --altSig
# python tnpEGM_fitter.py etc/config/settings_ele_sGain_UL2018.py --flag mediumID --doFit --mcSig --addGaus --altSig
python tnpEGM_fitter.py etc/config/settings_ele_sGain_UL2018.py --flag mediumID --doFit  --altSig
# python tnpEGM_fitter.py etc/config/settings_ele_sGain_UL2018.py --flag mediumID --doFit  --altSig --addGaus
python tnpEGM_fitter.py etc/config/settings_ele_sGain_UL2018.py --flag mediumID --doFit  --altBkg
python tnpEGM_fitter.py etc/config/settings_ele_sGain_UL2018.py --flag mediumID --doFit  --altSigBkg
# -- may skip the syst. part
# -- re-perform the fit
# -- change the initial paeramter for ths this bin in settings_ele_sGain_UL2018.py as well
python tnpEGM_fitter.py etc/config/settings_ele_sGain_UL2018.py --flag mediumID --doFit --iBin ib
python tnpEGM_fitter.py etc/config/settings_ele_sGain_UL2018.py --flag mediumID --sumUp

```

