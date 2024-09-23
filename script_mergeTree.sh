#!/bin/bash

###
baseSEDir=/pnfs/iihe/cms/store/user/kplee/EGMTnPTree/2024-09-19
targetDir=$baseSEDir/UL2018/merged_240923
###

hadd $targetDir/Run2018A.root \
$baseSEDir/UL2018/data/EGamma/crab_UL2018_Run2018A/240920_102308/0000/*.root \
$baseSEDir/UL2018/data/EGamma/crab_UL2018_Run2018A/240920_102308/0001/*.root \
$baseSEDir/UL2018/data/EGamma/crab_UL2018_Run2018A/240920_102308/0002/*.root
echo "================"
echo "[Run2018A: done]"
echo "================"\n

hadd $targetDir/Run2018B.root \
$baseSEDir/UL2018/data/EGamma/crab_UL2018_Run2018B/240920_102322/0000/*.root \
$baseSEDir/UL2018/data/EGamma/crab_UL2018_Run2018B/240920_102322/0001/*.root
echo "================"
echo "[Run2018B: done]"
echo "================"\n

hadd $targetDir/Run2018C.root \
$baseSEDir/UL2018/data/EGamma/crab_UL2018_Run2018C/240920_102338/0000/*.root \
$baseSEDir/UL2018/data/EGamma/crab_UL2018_Run2018C/240920_102338/0001/*.root
echo "================"
echo "[Run2018C: done]"
echo "================"\n

hadd $targetDir/Run2018D.root \
$baseSEDir/UL2018/data/EGamma/crab_UL2018_Run2018D/240920_102351/0000/*.root \
$baseSEDir/UL2018/data/EGamma/crab_UL2018_Run2018D/240920_102351/0001/*.root \
$baseSEDir/UL2018/data/EGamma/crab_UL2018_Run2018D/240920_102351/0002/*.root
echo "================"
echo "[Run2018D: done (CAVEAT: you need to add 0003 directory later)]"
echo "================"\n


hadd $targetDir/DY_LO.root \
$baseSEDir/UL2018/mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/crab_UL2018_DY_LO/240920_102418/0000/*.root
echo "================"
echo "[DY_LO: done]"
echo "================"\n

hadd $targetDir/DY_NLO.root \
$baseSEDir/UL2018/mc/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_UL2018_DY_NLO/240920_102406/0000/*.root
echo "================"
echo "[DY_NLO: done]"
echo "================"\n

