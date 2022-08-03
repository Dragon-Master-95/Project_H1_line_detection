# Project_H1_line_detection
This project explains hardware and software for a backyard H1 line detection.

# Code Usage
    pyhton3 data_avg.py [-h HELP] [-ip INPUTFILE] [-io OUTPUTFILE] [-t AVGTIME]
                       [-plt PLOTFILENAME] [-res TIMERES] [-cali CALIBRATIONFILE]
                       [-l LOWERCUTOFF] [-u UPPERCUTOFF]
                   
argument description:
          -h, --help            show this help message and exit
          -ip INPUTFILE, --inputfile INPUTFILE
                                input filename with path (must be provided)
          -io OUTPUTFILE, --outputfile OUTPUTFILE
                                output filename with path
          -t AVGTIME, --avgtime AVGTIME
                                average time in seconds (default = 10s)
          -plt PLOTFILENAME, --plotfilename PLOTFILENAME
                                plot the and save the filename with path
          -res TIMERES, --timeres TIMERES
                                time resolution of data in seconds (default = 1s)
          -cali CALIBRATIONFILE, --calibrationfile CALIBRATIONFILE
                                To remove system error provide clibration file path
                                (default setting is to plot non calibrated result)
          -l LOWERCUTOFF, --lowercutoff LOWERCUTOFF
                                lower cutoff for waterfall plot
          -u UPPERCUTOFF, --uppercutoff UPPERCUTOFF
                                lower cutoff for waterfall plot


Example:
python3 data_avg.py -ip [Input file path] -t [average time in seconds] -cali [calibration file path] -l [lower limit of waterfall plot] -u [upper limit of waterfall plot]


# Sample Data
Sample data file link: https://www.dropbox.com/sh/fiapt4wd439nawa/AAAxG33dJw-1ByZ5uw9c7XEaa?dl=0
