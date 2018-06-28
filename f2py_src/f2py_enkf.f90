!---------------------------------------------------------------------------------
! @author: fzhu (fengzhu@usc.edu)
! adapted from the function enkf_update_array() in LRM_DA.py
! 2017-06-26 09:30:38
!---------------------------------------------------------------------------------

! #define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION

module f2py_enkf
    implicit none

    contains

    subroutine enkf_update_array(Xb, obvalue, Ye, ob_err, inflate, Nx, Nens, Xa)
        implicit none
        !---------------------------------------------------------------------------------
        integer, intent(in) :: Nx, Nens
        double precision, dimension(Nx, Nens), intent(in) :: Xb
        double precision, dimension(Nens), intent(in) :: Ye
        double precision, intent(in) :: obvalue, ob_err, inflate
        double precision, dimension(Nx, Nens), intent(out) :: Xa
        !---------------------------------------------------------------------------------
        double precision :: mye, varye, innov, kdenom, beta
        double precision, dimension(Nx) :: xbm, kcov, xam, kmat
        double precision, dimension(Nx, Nens) :: Xbp, Xap
        double precision, dimension(Nens) :: yep
        double precision, dimension(1, Nens) :: yepT
        ! double precision, intent(out) :: kmat
        double precision, dimension(Nx, 1) :: kcovT, kmatT

        ! ensemble mean background and perturbations
        xbm = sum(Xb, 2) / size(Xb, 2)
        Xbp = Xb - spread(xbm, 2, Nens)

        ! ensemble mean and variance of the background estimate of the proxy
        mye = sum(Ye) / size(Ye)
        varye = (norm2(Ye)*norm2(Ye) - sum(Ye)*sum(Ye)/size(Ye)) / (size(Ye) - 1)

        ! yep is Ye has ensemble-mean removed
        yep = Ye - spread(mye, 1, Nens)

        ! innovation
        innov = obvalue - mye

        ! innovation variance (denominator of serial Kalman gain)
        kdenom = varye + ob_err

        ! numerator of serial Kalman gain cov(x,Hx)
        yepT(1, :) = yep
        kcovT = matmul(Xbp, transpose(yepT))
        kcov = inflate * kcovT(:, 1) / (Nens - 1)

        ! Kalman gain
        kmat = kcov / kdenom

        ! update ensemble mean
        xam = xbm + innov*kmat

        ! update the ensemble members using the square-root approach
        beta = 1 / (1 + sqrt(ob_err/(varye + ob_err)))
        kmat = beta*kmat
        kmatT(:, 1) = kmat
        Xap = Xbp - matmul(kmatT, yepT)

        ! full state
        Xa = Xap + spread(xam, 2, Nens)

    end subroutine
end module
