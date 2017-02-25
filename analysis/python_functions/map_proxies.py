#====================================================================
# A function which plots the locations of all proxy records.  Inputs:
#    experiment_dir:  The path preceding the experiment directory.
#    experiment_name: The name of the experiment directory.
#    niter:           The number of LRM iterations.
#    m:               The map projection (using Basemap).
#    year:            The proxies of what years should be plotted.
#                        Set this to "all" to plot all proxies.
#    marker:          The marker symbol.  Set to "proxy type" to
#                        use a different symbol for each proxy.
#    size:            The size of the symbols.
#    color:           The color of the symbols.
#    alpha:           The opacity of the symbols, 0 (invisible) to 1 (solid). 
#       author: Michael Erb
#       date  : 2/17/2017
#====================================================================

import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


# Plot the location of proxies on a map.  Specify a year or "all" for all years.  See the comments above for more customization.
def map_proxies(experiment_dir,experiment_name,niter,m,year='all',marker='o',size=10,color='k',alpha=1):
    print "Plotting locations of assimilated proxies."
    #
    proxy_names = []
    proxy_types = []
    proxy_lats = []
    proxy_lons = []
    #
    for iteration in range(0,niter):
        # Load the assimilated proxies
        assimilated_proxies = np.load('/home/scec-00/lmr/erbm/LMR/archive_output/'+experiment_name+'/r'+str(iteration)+'/assimilated_proxies.npy')
        #
        # Determine the names of all the assimilated proxies which exist for a given year.
        for i in range(0,len(assimilated_proxies)):
            proxy_type = assimilated_proxies[i].keys()[0]
            proxy_name = assimilated_proxies[i][proxy_type][0]
            #
            # Find only the proxies for the given year.  If a proxy has already been loaded, don't load it again.
            if ((year == "all") or (year in assimilated_proxies[i][proxy_type][3])) and (proxy_name not in proxy_names):
                #print assimilated_proxies[i][proxy_type][0]
                proxy_names.append(proxy_name)
                proxy_types.append(proxy_type)
                proxy_lats.append(assimilated_proxies[i][proxy_type][1])
                proxy_lons.append(assimilated_proxies[i][proxy_type][2])
    #
    # Plot the proxy locations.
    #     If the "marker" variable is set to "proxytypes," each proxy type gets a specific color and symbol.
    #     Otherwise all proxies are given the same maker.
    x,y = m(proxy_lons,proxy_lats)
    #
    if marker == "proxytypes":
        for i in range(0,len(proxy_names)):
            if   ("Tree"       in proxy_types[i]) or ("tree"       in proxy_types[i]): m.scatter(x[i],y[i],size,marker='^',facecolor='#32CC32',edgecolor='k',alpha=alpha)
            elif ("Coral"      in proxy_types[i]) or ("coral"      in proxy_types[i]): m.scatter(x[i],y[i],size,marker='o',facecolor='#FF8B00',edgecolor='k',alpha=alpha)
            elif ("Lake"       in proxy_types[i]) or ("lake"       in proxy_types[i]): m.scatter(x[i],y[i],size,marker='s',facecolor='#4169E0',edgecolor='k',alpha=alpha)
            elif ("Marine"     in proxy_types[i]) or ("marine"     in proxy_types[i]): m.scatter(x[i],y[i],size,marker='s',facecolor='#8A4513',edgecolor='k',alpha=alpha)
            elif ("Speleothem" in proxy_types[i]) or ("speleothem" in proxy_types[i]): m.scatter(x[i],y[i],size,marker='d',facecolor='#FF1492',edgecolor='k',alpha=alpha)
            elif ("Ice"        in proxy_types[i]) or ("ice"        in proxy_types[i]): m.scatter(x[i],y[i],size,marker='h',facecolor='#FFD600',edgecolor='k',alpha=alpha)
            elif ("Document"   in proxy_types[i]) or ("document"   in proxy_types[i]): m.scatter(x[i],y[i],size,marker='p',facecolor='k',      edgecolor='k',alpha=alpha)
            elif ("Hybrid"     in proxy_types[i]) or ("hybrid"     in proxy_types[i]): m.scatter(x[i],y[i],size,marker='*',facecolor='#00BEFF',edgecolor='k',alpha=alpha)
            else: m.scatter(x[i],y[i],size,marker='v',facecolor='k',edgecolor='k',alpha=alpha)
            #plt.legend()
    else:
        m.scatter(x,y,size,marker=marker,color=color,alpha=alpha)


