cesm_linear:
	slmr -c config_cesm_linear_0-2000.yml -n 16 -em slmr.slurm@gmail.com -x test_cesm_linear_0-2000_n16

cesm_linear_850-1000_n1:
	slmr -c config_cesm_linear.yml -n 1 -nn gold -rp 850 1000 -em slmr.slurm@gmail.com -x test_cesm_linear_850-1000_n1

cesm_bilinear_850-1000_n8:
	slmr -c config_cesm_bilinear.yml -n 8 -nn gold -rp 850 1000 -em slmr.slurm@gmail.com -x test_cesm_bilinear_850-1000_n8

cesm_linear_0-2000_n1:
	slmr -c config_cesm_linear.yml -n 1 -nn gold -rp 0 2000 -em slmr.slurm@gmail.com -x test_cesm_linear_0-2000_n1

cesm_bilinear_0-2000_n1:
	slmr -c config_cesm_bilinear.yml -n 1 -nn gold -rp 0 2000 -em slmr.slurm@gmail.com -x test_cesm_bilinear_0-2000_n1

cesm_bilinear_0-2000_n2:
	slmr -c config_cesm_bilinear.yml -n 2 -nn gold -rp 0 2000 -em slmr.slurm@gmail.com -x test_cesm_bilinear_0-2000_n2

cesm_bilinear_0-2000_n4:
	slmr -c config_cesm_bilinear.yml -n 4 -nn gold -rp 0 2000 -em slmr.slurm@gmail.com -x test_cesm_bilinear_0-2000_n4

cesm_bilinear_0-2000_n8:
	slmr -c config_cesm_bilinear.yml -n 8 -nn gold -rp 0 2000 -em slmr.slurm@gmail.com -x test_cesm_bilinear_0-2000_n8

cesm_bilinear_0-2000_n16:
	slmr -c config_cesm_bilinear.yml -n 16 -nn gold -rp 0 2000 -em slmr.slurm@gmail.com -x test_cesm_bilinear_0-2000_n16

cesm_bilinear_0-2000_n8_MC_01_05:
	for MC_idx in {01..05}; do \
		slmr -c config_cesm_bilinear.yml -n 8 -rp 0 2000 -em slmr.slurm@gmail.com -x test_cesm_linear_0-2000_n8_MC$$MC_idx -f; \
	done

cesm_linear_0-2000_n8_MC_06_10:
	for MC_idx in 0{6..9} 10; do \
		slmr -c config_cesm_linear.yml -n 8 -rp 0 2000 -em slmr.slurm@gmail.com -x test_cesm_linear_0-2000_n8_MC$$MC_idx -f; \
	done

cesm_linear_0-2000_n8_MC_11_15:
	for MC_idx in {11..15}; do \
		slmr -c config_cesm_linear.yml -n 8 -rp 0 2000 -em slmr.slurm@gmail.com -x test_cesm_linear_0-2000_n8__MC$$MC_idx -f; \
	done

clean:
	rm -f ./slurm-* ./run*.sh ./test_*.log

