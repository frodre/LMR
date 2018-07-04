cesm_linear:
	slmr -c config_cesm_linear_0-2000.yml -n 16 -e slmr.slurm@gmail.com -x test_cesm_linear_0-2000_n16

cesm_linear_850-1000_n1_nof2py:
	slmr -c config_cesm_linear.yml -n 1 -nn gold -rp 850 1000 -e slmr.slurm@gmail.com -x test_cesm_linear_850-1000_n1_nof2py

cesm_linear_850-1000_n8_nof2py:
	slmr -c config_cesm_linear.yml -n 8 -nn gold -rp 850 1000 -e slmr.slurm@gmail.com -x test_cesm_linear_850-1000_n8_nof2py

cesm_linear_850-1000_n1_f2py:
	slmr -c config_cesm_linear.yml -n 1 -nn gold -rp 850 1000 -e slmr.slurm@gmail.com -x test_cesm_linear_850-1000_n1_f2py_new -f

cesm_linear_850-1000_n8_f2py:
	slmr -c config_cesm_linear.yml -n 8 -nn gold -rp 850 1000 -e slmr.slurm@gmail.com -x test_cesm_linear_850-1000_n8_f2py_new -f

clean:
	rm -f ./slurm-* ./run*.sh ./test_*.log

