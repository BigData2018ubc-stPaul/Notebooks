import pandas as pd
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib as mpl
# %matplotlib inline
# plt.style.use('seaborn-whitegrid')
# plt.style.use('seaborn-bright')
plt.style.use('seaborn-whitegrid')

# fivethirtyeight
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['axes.titlesize'] = 24
mpl.rcParams['xtick.labelsize'] = 16
mpl.rcParams['ytick.labelsize'] = 16
mpl.rcParams['axes.labelsize'] = 20
plt.rcParams['figure.facecolor'] = 'White'

files = ['EGF','IL1B','MIP1A']
for filename in files:
    # df = pd.read_table('new_egf.assoc', delim_whitespace=True)
    df = pd.read_table(filename + '.assoc', delim_whitespace=True)
    y = -np.log10(df['P'])
    x = df['CHR']
    plt.clf()
    plt.axhline(6, c='k', ls='--',lw=1.5)
    plt.plot(x,y,'go',alpha=0.5)
    plt.title(filename + ' GWAS')
    plt.ylabel('$log_{10} (p)$')
    plt.xlabel('SNP')
    plt.savefig(filename+'.png')
