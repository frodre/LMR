from astropy.time import Time
import datetime

    # Datetime does not accept years of 0 or older.  This is a bad solution, but none of my other solutions have worked.
    data_raw = data_raw[time_raw>=1]
    time_raw = time_raw[time_raw>=1]
        
    # Get the integer values of all years.
    years_all = [int(time_raw[k]) for k in range(0,len(time_raw))]
    years = list(set(years_all)) # 'set' is used to get unique values in list
    years = sorted(years) # sort the list
    years = np.insert(years,0,years[0]-1) # Add a year prior to the first year

    time_annual = np.asarray(years,dtype=np.float64)
    data_annual = np.zeros(shape=[len(years)], dtype=np.float64)        
    # fill with NaNs for default values
    data_annual[:] = np.NAN

        
    # If some of the time values are floats and year_type is tropical_year, use the calendar method.
    if np.equal(np.mod(time_raw,1),0).all() == False and year_type == "tropical year":
        print "Tropical year method"

        # Convert float years into datetime objects
        time_datetime = Time(time_raw,format='byear')
        time_datetime.format = 'datetime'
        time_datetime = time_datetime.datetime
        
        # Loop over years in dataset
        for i, year in enumerate(years): 
            ind = np.where((time_datetime >= np.datetime64(datetime.datetime(year,4,1))) & (time_datetime < np.datetime64(datetime.datetime(year+1,4,1))))

            nbdat = len(ind)
            #print i, year, ind, nbdat, time_resolution

            # TODO: check nb of non-NaN values !!!!! ... ... ... ... ... ...

            if time_resolution <= 1.0: 
                frac = float(nbdat)/float(max_nb_per_year)
                if frac > valid_frac:
                    data_annual[i] = np.nanmean(data_raw[ind],axis=0)
            else:
                if nbdat > 1:
                    print '***WARNING! Found multiple records in same year in data with multiyear resolution!'
                    print '   year=', years[i], nbdat 
                # Note: this calculates the mean if multiple entries found
                data_annual[i] = np.nanmean(data_raw[ind],axis=0)

            #print years[i], nbdat, max_nb_per_year, data_annual[i,:]

