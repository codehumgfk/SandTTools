import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


def PlotTimeValues(elapsedTimes, xs, figname):
    for i in range(len(xs)):
        plt.plot(elapsedTimes[i], xs[i])
    plt.xlabel("Day")
    plt.ylabel("value")
    plt.title(os.path.splitext(figname.split("_")[1])[0])
    plt.savefig(figname, dpi = 300)
    plt.close()


folders = [
    "Results",
    "Results-NoHedge",
    "Results-DeltaHedge",
    "Results-DeltaGamma",
    "Results-DeltaVega",
    "Results-DeltaGammaVega",
    "Results-DeltaGammaVegaTheta",
    "Results-DeltaGammaVegaTheta5.0",
    "Results-DeltaGammaVegaTheta10.0",
    "Results-DeltaGamma30.0Vega",
    "Results-DeltaGamma20.0Vega",
    "Results-DeltaGamma10.0Vega",
    "Results-DeltaGamma5.0Vega"
]
#targetFolders = folders[2:]
targetFolders = [folders[len(folders)-1]]

for targetFolder in targetFolders:
    pathRisk = os.path.join(targetFolder, "Risk")
    csvfiles = os.listdir(pathRisk)

    npvs = []
    deltas = []
    gammas = []
    vegas = []
    thetas = []

    elapsedDays = []
    print(targetFolder)
    for csvfile in csvfiles:
        filepath = os.path.join(pathRisk, csvfile)
        df = pd.read_csv(filepath)
        dtns = pd.to_datetime(df.Date)
        dtns1 = dtns - dtns[0]
        dtns2 = [dtns1[i].days for i in range(len(dtns1))]
        elapsedDays.append(dtns2)
        npvs.append(df.Npv.values)
        deltas.append(df.Delta.values)
        gammas.append(df.Gamma.values)
        vegas.append(df.Vega.values)
        thetas.append(df.Theta.values)
        
    data = [
        npvs,
        deltas,
        gammas,
        vegas,
        thetas
        ]
    fignames = [
        targetFolder + "_npv.png",
        targetFolder + "_delta.png",
        targetFolder + "_gamma.png",
        targetFolder + "_vega.png",
        targetFolder + "_theta.png"
        ]
    for i in range(len(data)):
        PlotTimeValues(elapsedDays, data[i], fignames[i])
    