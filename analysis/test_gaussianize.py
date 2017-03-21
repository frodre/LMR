#================================================================================
# This script reads in the preprocessed PAGES2kv2 datasets and a PSM file and
# does two things:
#  1) Produces a list of all proxy types and units.
#  2) Produces individual figures of all 692 proxy records, along with metadata.
#
# Note: You'll need to make the preprocessed and PSM files before using this.
# Also, change the "data_directory" and "output_directory" to point to the
# appropriate places on your machine.
#
#    author: Michael P. Erb
#    date  : 2/13/2017
#================================================================================

import sys
sys.path.append('/home/scec-00/lmr/erbm/LMR_github/LMR/misc')
import numpy as np
import matplotlib.pyplot as plt
from gaussianize import gaussianize

### LOAD DATA

# Load the pages2kv2 proxy data and metadata as dataframes.
save_instead_of_plot = False
data_directory = "/home/scec-00/lmr/erbm/LMR/"
proxies_pages2k = np.load(data_directory+'data/proxies/NCDC_Pages2kv2_Proxies.df.pckl')
metadata_pages2k = np.load(data_directory+'data/proxies/NCDC_Pages2kv2_Metadata.df.pckl')


### CALCULATIONS

i = 307
#i = 3
data = proxies_pages2k[metadata_pages2k['NCDC ID'][i]]
data_gaussian = gaussianize(data)


### FIGURES
plt.style.use('ggplot')

# Make a plot of each proxy.
plt.figure(figsize=(20,12))

ax = plt.axes([.1,.6,.8,.3])
plt.plot(data,'b-')
plt.title("Pages2k v2 proxy time series\n"+metadata_pages2k['NCDC ID'][i])
plt.xlabel("Year")
plt.ylabel(metadata_pages2k['Proxy measurement'][i])

ax = plt.axes([.1,.1,.8,.3])
plt.plot(data_gaussian,'b-')
#plt.plot(CDF,'b-')
plt.title("Pages2k v2 proxy time series\n"+metadata_pages2k['NCDC ID'][i]+", gaussianized")
plt.xlabel("Year")

plt.show()


plt.figure(figsize=(20,12))
ax = plt.axes([.05,.1,.4,.8])
plt.hist(data.dropna(),50)
plt.title("Data")
plt.ylabel("Frequency")
ax = plt.axes([.55,.1,.4,.8])
plt.hist(data_gaussian.dropna(),50)
#plt.hist(Xn.dropna(),50)
plt.title("Data, gaussianized")
plt.ylabel("Frequency")
plt.show()


plt.figure(figsize=(12,12))

ax = plt.axes([.1,.1,.8,.8])
plt.scatter(data,data_gaussian)
plt.title("Data vs. gaussianized data.")
plt.xlabel("Data")
plt.ylabel("Data, gaussianized")
plt.show()

