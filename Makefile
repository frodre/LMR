cesm_linear:
	slmr -c config_cesm_linear_0-2000.yml -n 16 -em slmr.slurm@gmail.com -x test_cesm_linear_0-2000_n16

cesm_linear_850-1000_n1_nof2py:
	slmr -c config_cesm_linear.yml -n 1 -nn gold -rp 850 1000 -em slmr.slurm@gmail.com -x test_cesm_linear_850-1000_n1_nof2py

cesm_linear_850-1000_n8_nof2py:
	slmr -c config_cesm_linear.yml -n 8 -nn gold -rp 850 1000 -em slmr.slurm@gmail.com -x test_cesm_linear_850-1000_n8_nof2py

cesm_linear_850-1000_n1_f2py:
	slmr -c config_cesm_linear.yml -n 1 -nn gold -rp 850 1000 -em slmr.slurm@gmail.com -x test_cesm_linear_850-1000_n1_f2py -f

cesm_linear_850-1000_n8_f2py:
	slmr -c config_cesm_linear.yml -n 8 -nn gold -rp 850 1000 -em slmr.slurm@gmail.com -x test_cesm_linear_850-1000_n8_f2py -f

cesm_linear_0-2000_n16_f2py:
	slmr -c config_cesm_linear.yml -n 16 -rp 0 2000 -nn hungus -em slmr.slurm@gmail.com -x test_cesm_linear_0-2000_n16_f2py -f

cesm_linear_0-2000_n16_nof2py:
	slmr -c config_cesm_linear.yml -n 16 -rp 0 2000 -nn hungus -em slmr.slurm@gmail.com -x test_cesm_linear_0-2000_n16_nof2py

cesm_bilinear_850-1000_n1_nof2py:
	slmr -c config_cesm_bilinear.yml -n 1 -nn gold -rp 850 1000 -em slmr.slurm@gmail.com -x test_cesm_bilinear_850-1000_n1_nof2py

cesm_bilinear_850-1000_n8_f2py:
	slmr -c config_cesm_bilinear.yml -n 8 -nn gold -rp 850 1000 -em slmr.slurm@gmail.com -x test_cesm_bilinear_850-1000_n8_f2py -f

cesm_linear_0-2000_n8_f2py_MC_01_05:
	for MC_idx in {01..05}; do \
		slmr -c config_cesm_linear.yml -n 8 -rp 0 2000 -em slmr.slurm@gmail.com -x test_cesm_linear_0-2000_n8_f2py_MC$$MC_idx -f; \
	done

cesm_linear_0-2000_n8_f2py_MC_06_10:
	for MC_idx in 0{6..9} 10; do \
		slmr -c config_cesm_linear.yml -n 8 -rp 0 2000 -em slmr.slurm@gmail.com -x test_cesm_linear_0-2000_n8_f2py_MC$$MC_idx -f; \
	done

cesm_linear_0-2000_n8_f2py_MC_11_15:
	for MC_idx in {11..15}; do \
		slmr -c config_cesm_linear.yml -n 8 -rp 0 2000 -em slmr.slurm@gmail.com -x test_cesm_linear_0-2000_n8_f2py_MC$$MC_idx -f; \
	done

clean:
	rm -f ./slurm-* ./run*.sh ./test_*.log

