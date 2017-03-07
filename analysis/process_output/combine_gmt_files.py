#======================================================================
# This script reads in the individual gmt files for each iteration and
# saves them into a single file.
#    author: Michael Erb
#    date  : 3/7/2017
#======================================================================

import numpy as np
import glob


# --- Begin section of user-defined parameters ---

# name of directory where the output of LMR experiments are located
datadir = '/home/scec-00/lmr/erbm/LMR/archive_output'

# name of the experiment
nexp = 'pages2kv2_tropicalyear_ccsm4_annual_linear_GISTEMP_2ka_tas'

# --- End section of user-defined parameters ---


expdir = datadir + '/'+nexp

# where the netcdf files are created 
outdir = expdir

print '\n Getting information on Monte-Carlo realizations...\n'

dirs = glob.glob(expdir+"/r*")
# sorted
#dirs.sort()
# keep names of MC directories (i.r. "r...") only 
mcdirs = [item.split('/')[-1] for item in dirs]
# number of MC realizations found
niters = len(mcdirs) 

print 'mcdirs:' + str(mcdirs)
print 'niters = ' + str(niters)

print "Loading data: " + expdir

# LOAD DATA
# Loop through the LMR members, saving each into an array.
for i, iteration in enumerate(mcdirs):
    print str(i+1) + "/" + str(niters)
    gmt_ensemble_file = np.load(expdir + '/' + iteration + '/gmt_ensemble.npz')
    if i == 0:
        recon_times = gmt_ensemble_file['recon_times']
        nyears = len(recon_times)
        #
        # Initialize the data arrays as nan.
        gmt_ensemble = np.zeros([nyears,100,niters])
        gmt_ensemble[:] = np.nan
        nhmt_ensemble = np.zeros([nyears,100,niters])
        nhmt_ensemble[:] = np.nan
        shmt_ensemble = np.zeros([nyears,100,niters])
        shmt_ensemble[:] = np.nan
    #
    gmt_ensemble[:,:,i] = gmt_ensemble_file['gmt_ensemble']
    nhmt_ensemble[:,:,i] = gmt_ensemble_file['nhmt_ensemble']
    shmt_ensemble[:,:,i] = gmt_ensemble_file['shmt_ensemble']
    gmt_ensemble_file.close()


# Save the joined variables.
filen = outdir + '/gmt_ensemble_alliters'
np.savez(filen, gmt_ensemble=gmt_ensemble, nhmt_ensemble=nhmt_ensemble, shmt_ensemble=shmt_ensemble, recon_times=recon_times)


