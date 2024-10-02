
# -- custom -- #
list_binEdge_eta = [-2.5, -1.566,-1.4442, 0.0, 1.4442, 1.566, 2.5]
list_binEdge_pt  = [10,20,35,50,100,200,500]
################

import sys, csv
from math import sqrt
from array import array
from ROOT import TH2D, TFile

def GetBinIndex(var, list_binEdge, binName):
  nBin = len(list_binEdge) - 1

  for i in range(0, nBin):
    lowerEdge = list_binEdge[i]
    upperEdge = list_binEdge[i+1]
    str_binRange = "%.2fTo%.2f" % (lowerEdge, upperEdge)
    str_binRange = str_binRange.replace("-", "m")
    str_binRange = str_binRange.replace(".", "p")
    # print("str_binR`ange = %s" % str_binRange)

    str_binInfo = "%s_%s" % (var, str_binRange)

    if str_binInfo in binName:
      return i+1 # -- (i_bin = i+1)

  print("no corresponding %s info for %s" % (var, binName))
  sys.exit()

  return 0

def GetBinIndex_Eta(binName):
  return GetBinIndex("el_sc_eta", list_binEdge_eta, binName)

def GetBinIndex_Pt(binName):
  return GetBinIndex("el_pt", list_binEdge_pt, binName)

def GetSeedGain(binName):
  if "el_seedGainEq12" in binName: return 12
  elif "el_seedGainEq6" in binName: return 6
  elif "el_seedGainEq1" in binName: return 1

def Make2DEffHist(histName):
  # -- (eta, pt) hist
  return TH2D(histName, "", len(list_binEdge_eta)-1, array("d", list_binEdge_eta), len(list_binEdge_pt)-1, array("d", list_binEdge_pt))


# -- dic_allHist[gain][data/mc]
def MakeDic_2DEffHist():
  dic_allHist = {}

  list_gain = [12, 6, 1]
  for gain in list_gain:
    histName = "eff_data_gain%d" % gain

    dic_hist = {}
    dic_hist["data"] = Make2DEffHist(histName)

    histName = histName.replace("data", "mc")
    dic_hist["mc"] = Make2DEffHist(histName)

    histName = histName.replace("eff_mc", "sf")
    dic_hist["sf"] = Make2DEffHist(histName)

    dic_allHist[gain] = dic_hist

  return dic_allHist


def Fill_EffInfo(dic_hist, effInfo):
  dic_hist[effInfo["gain"]]["data"].SetBinContent(effInfo["etaBinNum"], effInfo["ptBinNum"], effInfo["eff_data"])
  dic_hist[effInfo["gain"]]["data"].SetBinError(effInfo["etaBinNum"], effInfo["ptBinNum"], effInfo["absUnc_data"])

  dic_hist[effInfo["gain"]]["mc"].SetBinContent(effInfo["etaBinNum"], effInfo["ptBinNum"], effInfo["eff_mc"])
  dic_hist[effInfo["gain"]]["mc"].SetBinError(effInfo["etaBinNum"], effInfo["ptBinNum"], effInfo["absUnc_mc"])

  dic_hist[effInfo["gain"]]["sf"].SetBinContent(effInfo["etaBinNum"], effInfo["ptBinNum"], effInfo["sf"])
  dic_hist[effInfo["gain"]]["sf"].SetBinError(effInfo["etaBinNum"], effInfo["ptBinNum"], effInfo["absUnc_sf"])


def CalcAbsUnc_AoverB(A, unc_A, B, unc_B):
  if A == 0: return 0.0
  if B == 0: return 0.0

  relUnc_A = unc_A / A
  relUnc_B = unc_B / B
  relUnc_sf = sqrt(relUnc_A*relUnc_A + relUnc_B*relUnc_B)

  return (A/B)*relUnc_sf # -- convert to abs. unc.


def Convert_EffInfo(line):
  effInfo = {}
  effInfo["binName"] = line[0] # -- e.g. bin000_el_sc_eta_m2p50Tom1p57_el_pt_10p00To20p00_el_seedGainEq1
  effInfo["eff_data"] = float(line[1])
  effInfo["absUnc_data"] = float(line[2])
  effInfo["eff_mc"] = float(line[3])
  effInfo["absUnc_mc"] = float(line[4])
  sf = 0
  if effInfo["eff_mc"] != 0: sf = effInfo["eff_data"] / effInfo["eff_mc"]
  effInfo["sf"] = effInfo["eff_data"] / effInfo["eff_mc"] if effInfo["eff_mc"] != 0 else 0.0
  effInfo["absUnc_sf"] = CalcAbsUnc_AoverB(effInfo["eff_data"], effInfo["absUnc_data"], effInfo["eff_mc"], effInfo["absUnc_mc"])
  effInfo["ptBinNum"] = GetBinIndex_Pt(effInfo["binName"])
  effInfo["etaBinNum"] = GetBinIndex_Eta(effInfo["binName"])
  effInfo["gain"] = GetSeedGain(effInfo["binName"])

  return effInfo


# -- main part -- #
fileName = "egammaEff_csv.txt"
f_input = open(fileName, "r")
reader = csv.reader(f_input)

dic_hist = MakeDic_2DEffHist()

for line in reader:
  effInfo = Convert_EffInfo(line)
  print( "binName = %s -> (ptBin, etaBin, gain) = (%d, %d, %d)" % (effInfo["binName"], effInfo["ptBinNum"], effInfo["etaBinNum"], effInfo["gain"]) )
  Fill_EffInfo(dic_hist, effInfo)

f_output = TFile("eff_electron_mediumID_perGain.root", "recreate")
f_output.cd()

for gain in dic_hist.keys():
  dic_histPerGain = dic_hist[gain]
  for type in dic_histPerGain:
    dic_histPerGain[type].Write()
