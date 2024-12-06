
# -- 2016, pre
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016pre.py --flag mediumID --checkBins
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016pre.py --flag mediumID --createBins
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016pre.py --flag mediumID --createHists
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016pre.py --flag mediumID --doFit
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016pre.py --flag mediumID --doFit --mcSig --altSig
# python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016pre.py --flag mediumID --doFit --mcSig --altSig --addGaus
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016pre.py --flag mediumID --doFit --altSig
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016pre.py --flag mediumID --doFit --altBkg
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016pre.py --flag mediumID --sumUp

python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016pre.py --flag mediumID --doFit --iBin 15
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016pre.py --flag mediumID --sumUp
echo "done: 2016-preAPV"

# -- 2016, post
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016post.py --flag mediumID --checkBins
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016post.py --flag mediumID --createBins
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016post.py --flag mediumID --createHists
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016post.py --flag mediumID --doFit
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016post.py --flag mediumID --doFit --mcSig --altSig
# python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016post.py --flag mediumID --doFit --mcSig --altSig --addGaus
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016post.py --flag mediumID --doFit --altSig
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016post.py --flag mediumID --doFit --altBkg
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016post.py --flag mediumID --sumUp

python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016post.py --flag mediumID --doFit --mcSig --altSig --iBin 01
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016post.py --flag mediumID --doFit --altSig --iBin 01
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016post.py --flag mediumID --doFit --iBin 26
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2016post.py --flag mediumID --sumUp
echo "done: 2016-postAPV"

# -- 2017
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2017.py --flag mediumID --checkBins
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2017.py --flag mediumID --createBins
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2017.py --flag mediumID --createHists
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2017.py --flag mediumID --doFit
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2017.py --flag mediumID --doFit --mcSig --altSig
# python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2017.py --flag mediumID --doFit --mcSig --altSig --addGaus
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2017.py --flag mediumID --doFit --altSig
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2017.py --flag mediumID --doFit --altBkg
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2017.py --flag mediumID --sumUp
echo "done: 2017"

# -- 2018
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2018.py --flag mediumID --checkBins
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2018.py --flag mediumID --createBins
# python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2018.py --flag mediumID --createHists >&createHists_mediumID_UL2018.log& tail -f createHists_mediumID_UL2018.log
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2018.py --flag mediumID --createHists
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2018.py --flag mediumID --doFit
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2018.py --flag mediumID --doFit --mcSig --altSig # -- constraint alt. fit parameter by fitting on mc
# python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2018.py --flag mediumID --doFit --mcSig --altSig --addGaus # -- add gaussian smearing
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2018.py --flag mediumID --doFit --altSig
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2018.py --flag mediumID --doFit --altBkg
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2018.py --flag mediumID --sumUp
# -- refit
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2018.py --flag mediumID --doFit --iBin 28
python tnpEGM_fitter.py etc/config/mcFit/ID/settings_ele_UL2018.py --flag mediumID --doFit --iBin 36
echo "done: 2018"