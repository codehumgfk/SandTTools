import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

def PlotLots(results, labels, figname):
    x = np.arange(len(results))
    plt.bar(x, results, tick_label = labels, log = True)
    plt.ylabel("Lots for hedge")
    plt.savefig(figname, dpi = 300)
    plt.close()


folders = [
    "Results",
    "Results-NoHedge",
    "Results-DeltaHedge",
    "Results-DeltaGamma",
    "Results-DeltaVega",
    "Results-DeltaGammaVega",
    "Results-DeltaGamma30.0Vega",
    "Results-DeltaGamma20.0Vega",
    "Results-DeltaGamma10.0Vega",
    "Results-DeltaGamma5.0Vega",
    "Results-DeltaGammaVegaTheta",
    "Results-DeltaGammaVegaTheta5.0",
    "Results-DeltaGammaVegaTheta10.0"
]
shortName = {
    "NoHedge":"No",
    "DeltaHedge":"D",
    "DeltaGamma":"DG",
    "DeltaVega":"DV",
    "DeltaGammaVega":"DGV",
    "DeltaGammaVegaTheta":"DGVT",
    "DeltaGammaVegaTheta5.0":"DGVT5",
    "DeltaGammaVegaTheta10.0":"DGVT10",
    "DeltaGamma30.0Vega":"DG30V",
    "DeltaGamma20.0Vega":"DG20V",
    "DeltaGamma10.0Vega":"DG10V",
    "DeltaGamma5.0Vega":"DG5V"
}

targetFolders = folders[3:10]
#targetFolders = [folders[len(folders)-1]]
figname = "LotsCompare5.png"

labels = []
results = []
for targetFolder in targetFolders:
    pathPos = os.path.join(targetFolder, "Position")
    csvfiles = os.listdir(pathPos)
    print(pathPos)
    lot = 0.0
    for csvfile in csvfiles:
        filepath = os.path.join(pathPos, csvfile)
        df = pd.read_csv(filepath)
        lot +=  df["Lot"][1:].sum()
    
    results.append(lot)
    labels.append(shortName[targetFolder[8:]])
    
assert len(results) == len(labels)
PlotLots(results, labels, figname)
print(results)
print(labels)
"""
[0.0, 236662.4391077378, 769912.4503996093, 261478.548440402, 830578.3195352925, 264302180.23879325]
['No', 'D', 'DG', 'DV', 'DGV', 'DGVT']
"""

"""
[0.0, 236662.4391077378, 769912.4503996093, 261478.548440402, 830578.3195352925, 340154.52445126016, 375462.41124965047]
['No', 'D', 'DG', 'DV', 'DGV', 'DG30V', 'DG20V']
"""