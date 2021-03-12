import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

def PlotHistogram(results, width, figname):
    xmin = float("{:.1f}".format(results.min())) - width
    xmax = float("{:.1f}".format(results.max())) + width
    sep = int((xmax - xmin) / width)
    hist = []
    x = []
    for i in range(sep):
        x.append(xmin + i * width)
        up = xmin + i * width <= results
        down = results < xmin + (i + 1) * width 
        hist.append((up == down).sum())

    plt.bar(x, hist, width = width)
    plt.xlabel("pay off")
    plt.ylabel("frequency")
    info = " mean:{:.2f} std:{:.2f}".format(results.mean(), results.std())
    plt.title(os.path.splitext(figname)[0][:-5] + info)
    plt.savefig(figname, dpi = 300)
    plt.close()

def PlotLineGraph(results, width, figname):
    xmin = float("{:.1f}".format(results.min())) - width
    xmax = float("{:.1f}".format(results.max())) + width
    sep = int((xmax - xmin) / width)
    hist = []
    x = []
    for i in range(sep):
        x.append(xmin + i * width)
        up = xmin + i * width <= results
        down = results < xmin + (i + 1) * width 
        hist.append((up == down).sum())

    plt.plot(x, hist)
    plt.xlabel("pay off")
    plt.ylabel("frequency")
    info = " mean:{:.2f} std:{:.2f}".format(results.mean(), results.std())
    plt.title(os.path.splitext(figname)[0][:-5] + info)
    plt.savefig(figname, dpi = 300)
    plt.close()


folders = [
    "Results",
    "Results-DeltaHedge",
    "Results-NoHedge",
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
#targetFolders = folders[1:]
targetFolders = [folders[len(folders)-1]]
width = [10, 1]

for targetFolder in targetFolders:
    pathRisk = os.path.join(targetFolder, "Risk")
    csvfiles = os.listdir(pathRisk)

    results = []
    for csvfile in csvfiles:
        print(csvfile)
        filepath = os.path.join(pathRisk, csvfile)
        df = pd.read_csv(filepath)
        results.append(df.Npv[len(df)-1])
    results = np.array(results)

    figname = [targetFolder + "_hist.png", targetFolder + "_line.png"]

    PlotHistogram(results, width[0], figname[0])
    PlotLineGraph(results, width[1], figname[1])