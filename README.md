# Fit MiNNLO using Madgraph template
* Starting point: from mcFit branch

## Recipe

### First setup (@ BE T2)

```bash
cd /user/kplee/Analysis/EGMTnP/Fitter
git clone git@github.com:KyeongPil-Lee/egm_tnp_analysis.git -b mcFit 250925_MiNNLO
cd 250925_MiNNLO
make
source setup.sh # -- setup CMSSW env.
git checkout -b minnlo
git push origin minnlo
```

### Usual setup

```bash
cd /user/kplee/Analysis/EGMTnP/Fitter/250925_MiNNLO
# cmssw-el7
source setup.sh
```

## Update
* on top of the changes in `mcFit` branch

