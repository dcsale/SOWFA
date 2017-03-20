## NREL 5-MW¶
# One example of a CCBlade application is the simulation of the 
# NREL 5-MW reference model’s aerodynamic performance. 
# First, define the geometry and atmospheric properties.

import numpy as np
from math import pi

#import matplotlib.backends.backend_tkagg
#

import matplotlib
matplotlib.use("Agg")  # or whichever backend you wish to use
import matplotlib.pyplot as plt
#matplotlib.use("Agg")  # or whichever backend you wish to use

#
#matplotlib.matplotlib_fname()
#
#matplotlib.use("Agg")

from ccblade import CCAirfoil, CCBlade
## Airfoil aerodynamic data is specified using the CCAirfoil class. 
# Rather than use the default constructor, this example uses the 
# special constructor designed to read AeroDyn files directly CCAirfoil.initFromAerodynFile().

afinit = CCAirfoil.initFromAerodynFile  # just for shorthand

# Geometry for the UW Labscale v2 turbine, using data from the WT_perf models
# including DOE-RM1 45:1 scaling, UW model4, and model6 Saved Games


# COMMON for all turbines
tsr      = 7.0 
pitch    = 0.0
azimuth  = 0.0
B        = 2  			# number of blades
tilt     = 0.0
precone  = 0.0
yaw      = 0.0
nSector  = 24  			# azimuthal discretization
shearExp = 0.0 			# power-law wind shear profile
## END - COMMON for all turbines



# CCBlade: for the DOE-RM1 45:1 scaling
m1_Uinf  = 1.9          # free stream velocity
m1_rho   = 1025.0 		# atmosphere (density) seawater
m1_mu    = 1.002e-3 	    # atmosphere (dynamic viscosity)
m1_hubHt = 30.0 		# hub-height reference height for power-law wind shear profile
m1_Rhub = 1.0
m1_Rtip = 10.0
# define the radius, chord, and pre-twist
m1_r = np.array([1.150,
1.450,
1.750,
2.050,
2.350,
2.650,
2.950,
3.250,
3.550,
3.850,
4.150,
4.450,
4.750,
5.050,
5.350,
5.650,
5.950,
6.250,
6.550,
6.850,
7.150,
7.450,
7.750,
8.050,
8.350,
8.650,
8.950,
9.250,
9.550,
9.850])
m1_chord = np.array([0.800,
0.894,
1.118,
1.386,
1.610,
1.704,
1.662,
1.619,
1.577,
1.534,
1.492,
1.450,
1.407,
1.365,
1.322,
1.279,
1.235,
1.192,
1.148,
1.103,
1.058,
1.012,
0.966,
0.920,
0.872,
0.824,
0.776,
0.726,
0.676,
0.626])
m1_theta = np.array([12.86,
12.86,
12.86,
12.86,
12.86,
12.86,
11.54,
10.44,
9.50,
8.71,
8.02,
7.43,
6.91,
6.45,
6.04,
5.68,
5.35,
5.05,
4.77,
4.51,
4.26,
4.03,
3.80,
3.57,
3.35,
3.13,
2.90,
2.67,
2.43,
2.18])
# place airfoils at appropriate radial stations
m1_airfoil_types    = [0]*9
m1_airfoil_types[0] = afinit('/mnt/data-RAID-1/Dropboxes/danny/Dropbox/uw/codes/MHK_ReferenceModel/Airfoil_Data/NACA6ccblade_1000.dat')
#m1_airfoil_types[0] = afinit('/mnt/data-RAID-1/Dropboxes/danny/Dropbox/uw/codes/MHK_ReferenceModel/Airfoil_Data/NACA6_1000.dat')
m1_airfoil_types[1] = afinit('/mnt/data-RAID-1/Dropboxes/danny/Dropbox/uw/codes/MHK_ReferenceModel/Airfoil_Data/NACA6_0864.dat')
m1_airfoil_types[2] = afinit('/mnt/data-RAID-1/Dropboxes/danny/Dropbox/uw/codes/MHK_ReferenceModel/Airfoil_Data/NACA6_0629.dat')
m1_airfoil_types[3] = afinit('/mnt/data-RAID-1/Dropboxes/danny/Dropbox/uw/codes/MHK_ReferenceModel/Airfoil_Data/NACA6_0444.dat')
m1_airfoil_types[4] = afinit('/mnt/data-RAID-1/Dropboxes/danny/Dropbox/uw/codes/MHK_ReferenceModel/Airfoil_Data/NACA6_0329.dat')
m1_airfoil_types[5] = afinit('/mnt/data-RAID-1/Dropboxes/danny/Dropbox/uw/codes/MHK_ReferenceModel/Airfoil_Data/NACA6_0276.dat')
m1_airfoil_types[6] = afinit('/mnt/data-RAID-1/Dropboxes/danny/Dropbox/uw/codes/MHK_ReferenceModel/Airfoil_Data/NACA6_0259.dat')
m1_airfoil_types[7] = afinit('/mnt/data-RAID-1/Dropboxes/danny/Dropbox/uw/codes/MHK_ReferenceModel/Airfoil_Data/NACA6_0247.dat')
m1_airfoil_types[8] = afinit('/mnt/data-RAID-1/Dropboxes/danny/Dropbox/uw/codes/MHK_ReferenceModel/Airfoil_Data/NACA6_0240.dat')
m1_af_idx           = [0,1,2,3,4,5,6,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]

# CCBlade: for the model4
m4_Uinf  = 0.9          # free stream velocity
m4_rho   = 997.0 		# atmosphere (density) seawater
m4_mu    = 1.002e-3   	# atmosphere (dynamic viscosity)
m4_hubHt = 0.4 			# hub-height reference height for power-law wind shear profile
m4_Rhub  = 0.028575
m4_Rtip  = 0.225
# define the radius, chord, and pre-twist
m4_r = np.array([0.031849,
	  0.038396,
	  0.044944,
	  0.051491,
	  0.058039,
	  0.064586,
	  0.071134,
	  0.077681,
	  0.084229,
	  0.090776,
	  0.097324,
	  0.103871,
	  0.110419,
	  0.116966,
	  0.123514,
	  0.130061,
	  0.136609,
	  0.143156,
	  0.149704,
	  0.156251,
	  0.162799,
	  0.169346,
	  0.175894,
	  0.182441,
	  0.188989,
	  0.195536,
	  0.202084,
	  0.208631,
	  0.215179,
	  0.221726])
m4_chord = np.array([0.050444,
		  0.044850,
		  0.040888,
		  0.037827,
		  0.035357,
		  0.033308,
		  0.031551,
		  0.030026,
		  0.028685,
		  0.027491,
		  0.026416,
		  0.025436,
		  0.024532,
		  0.023689,
		  0.022895,
		  0.022145,
		  0.021426,
		  0.020726,
		  0.020040,
		  0.019363,
		  0.018689,
		  0.018012,
		  0.017330,
		  0.016632,
		  0.015918,
		  0.015190,
		  0.014432,
		  0.013647,
		  0.012841,
		  0.011987])
m4_theta = np.array([20.070254,
				  16.379868,
				  13.859551,
				  11.975563,
				  10.505297,
				   9.326087,
				   8.347700,
				   7.527315,
				   6.832259,
				   6.237268,
				   5.722592,
				   5.272650,
				   4.875064,
				   4.519952,
				   4.199397,
				   3.911213,
				   3.646985,
				   3.398958,
				   3.163755,
				   2.939738,
				   2.723885,
				   2.510965,
				   2.299911,
				   2.087942,
				   1.872547,
				   1.653753,
				   1.426453,
				   1.190646,
				   0.948268,
				   0.689477])
# place airfoils at appropriate radial stations
m4_airfoil_types    = [0]*1
m4_airfoil_types[0] = afinit('/mnt/data-RAID-1/danny/paper2_CCBlade/airfoils/UW_Labscale_v2/NACA_4415_lowReynolds.dat')
m4_af_idx           = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# CCBlade: for the model6 Saved Games
m6_Uinf  = 0.9          # free stream velocity
m6_rho   = 997.0 		# atmosphere (density) seawater
m6_mu    = 1.002e-3   	# atmosphere (dynamic viscosity)
m6_hubHt = 0.4 			# hub-height reference height for power-law wind shear profile
m6_Rhub  = 0.05
m6_Rtip  = 0.225
m6_r     = np.array([0.0529,
0.0587,
0.0646,
0.0704,
0.0762,
0.0821,
0.0879,
0.0938,
0.0996,
0.1054,
0.1112,
0.1171,
0.1229,
0.1287,
0.1346,
0.1404,
0.1462,
0.1521,
0.1579,
0.1638,
0.1696,
0.1754,
0.1812,
0.1871,
0.1929,
0.1987,
0.2046,
0.2104,
0.2163,
0.2221])
m6_chord = np.array([0.0521,
0.0483,
0.0452,
0.0425,
0.0401,
0.0379,
0.0360,
0.0343,
0.0327,
0.0313,
0.0300,
0.0288,
0.0278,
0.0268,
0.0260,
0.0252,
0.0246,
0.0240,
0.0234,
0.0230,
0.0226,
0.0223,
0.0220,
0.0218,
0.0216,
0.0215,
0.0214,
0.0214,
0.0214,
0.0214])
m6_theta = np.array([19.415,
15.804,
13.374,
11.582,
10.203,
9.113,
8.221,
7.486,
6.874,
6.361,
5.927,
5.558,
5.241,
4.967,
4.729,
4.525,
4.346,
4.187,
4.042,
3.913,
3.795,
3.685,
3.580,
3.481,
3.384,
3.287,
3.191,
3.092,
2.993,
2.887])
m6_airfoil_types    = [0]*1
m6_airfoil_types[0] = afinit('/mnt/data-RAID-1/danny/paper2_CCBlade/airfoils/UW_Labscale_v2/NACA_4415_lowReynolds.dat')
m6_af_idx           = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


# CCBlade: for the model6 Saved Games, now with multiple Reynolds numbers airfoil data
m66_Uinf  = 0.9          # free stream velocity
m66_rho   = 997.0 		# atmosphere (density) seawater
m66_mu    = 1.002e-3   	# atmosphere (dynamic viscosity)
m66_hubHt = 0.4 			# hub-height reference height for power-law wind shear profile
m66_Rhub  = 0.05
m66_Rtip  = 0.225
m66_r     = np.array([0.0529,
0.0587,
0.0646,
0.0704,
0.0762,
0.0821,
0.0879,
0.0938,
0.0996,
0.1054,
0.1112,
0.1171,
0.1229,
0.1287,
0.1346,
0.1404,
0.1462,
0.1521,
0.1579,
0.1638,
0.1696,
0.1754,
0.1812,
0.1871,
0.1929,
0.1987,
0.2046,
0.2104,
0.2163,
0.2221])
m66_chord = np.array([0.0521,
0.0483,
0.0452,
0.0425,
0.0401,
0.0379,
0.0360,
0.0343,
0.0327,
0.0313,
0.0300,
0.0288,
0.0278,
0.0268,
0.0260,
0.0252,
0.0246,
0.0240,
0.0234,
0.0230,
0.0226,
0.0223,
0.0220,
0.0218,
0.0216,
0.0215,
0.0214,
0.0214,
0.0214,
0.0214])
m66_theta = np.array([19.415,
15.804,
13.374,
11.582,
10.203,
9.113,
8.221,
7.486,
6.874,
6.361,
5.927,
5.558,
5.241,
4.967,
4.729,
4.525,
4.346,
4.187,
4.042,
3.913,
3.795,
3.685,
3.580,
3.481,
3.384,
3.287,
3.191,
3.092,
2.993,
2.887])
m66_airfoil_types    = [0]*1
m66_airfoil_types[0] = afinit('/mnt/data-RAID-1/danny/FrenchNavalAcademy/starccm_Flume/CCBlade_UW_turbines/airfoils/UW_Labscale_v2/NACA_4415_multiple_Reynolds.dat')
#m66_airfoil_types[0] = afinit('/mnt/data-RAID-1/danny/FrenchNavalAcademy/starccm_Flume/CCBlade_UW_turbines/airfoils/UW_Labscale_v2/test_Re_42000.dat')
#m66_airfoil_types[0] = afinit('/mnt/data-RAID-1/danny/FrenchNavalAcademy/starccm_Flume/CCBlade_UW_turbines/airfoils/UW_Labscale_v2/test_Re_330000.dat')
m66_af_idx           = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


# CCBlade: for the model67-SavedGames the wind-tunnel mod, with multiple Reynolds numbers airfoil data
scale     = 3.731         # geometric scaling factor from water to air
m67_Uinf  = 1.13          # free stream velocity
m67_rho   = 1.1767 		  # atmosphere (density) air
m67_mu    = 1.85508E-5    # atmosphere (dynamic viscosity) air
m67_hubHt = 0.4*scale 	  # hub-height reference height for power-law wind shear profile
m67_Rhub  = 0.05*scale
m67_Rtip  = 0.225*scale
m67_r     = scale * np.array([0.0529,
0.0587,
0.0646,
0.0704,
0.0762,
0.0821,
0.0879,
0.0938,
0.0996,
0.1054,
0.1112,
0.1171,
0.1229,
0.1287,
0.1346,
0.1404,
0.1462,
0.1521,
0.1579,
0.1638,
0.1696,
0.1754,
0.1812,
0.1871,
0.1929,
0.1987,
0.2046,
0.2104,
0.2163,
0.2221])
m67_chord = scale * np.array([0.0521,
0.0483,
0.0452,
0.0425,
0.0401,
0.0379,
0.0360,
0.0343,
0.0327,
0.0313,
0.0300,
0.0288,
0.0278,
0.0268,
0.0260,
0.0252,
0.0246,
0.0240,
0.0234,
0.0230,
0.0226,
0.0223,
0.0220,
0.0218,
0.0216,
0.0215,
0.0214,
0.0214,
0.0214,
0.0214])
m67_theta = np.array([19.415,
15.804,
13.374,
11.582,
10.203,
9.113,
8.221,
7.486,
6.874,
6.361,
5.927,
5.558,
5.241,
4.967,
4.729,
4.525,
4.346,
4.187,
4.042,
3.913,
3.795,
3.685,
3.580,
3.481,
3.384,
3.287,
3.191,
3.092,
2.993,
2.887])
m67_airfoil_types    = [0]*1
m67_airfoil_types[0] = afinit('/mnt/data-RAID-1/danny/FrenchNavalAcademy/starccm_Flume/CCBlade_UW_turbines/airfoils/UW_Labscale_v2/NACA_4415_multiple_Reynolds.dat')
m67_af_idx           = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]



# question ... what is the proper format of AeroDyn files now?  data starts on line 14 or 15

#
#
## load all airfoils
#airfoil_types = [0]*1
##airfoil_types[0] = afinit('/mnt/data-RAID-1/danny/paper2_AirfoilPreppy/Airfoils/UTK/NACA_011.dat')
#airfoil_types[0] = afinit('/mnt/data-RAID-1/danny/paper2_CCBlade/airfoils/UW_Labscale_v2/NACA_4415_lowReynolds.dat')






## for the model4 and model6 Saved Games
## place airfoils at appropriate radial stations
#airfoil_types    = [0]*1
## place at appropriate radial stations
#af_idx    = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#
#m1_
#m4_
#m6_



# build the airfoil objects
m1_af = [0]*len(m1_r)
for i in range(len(m1_r)):
    m1_af[i] = m1_airfoil_types[m1_af_idx[i]]
    
m4_af = [0]*len(m4_r)
for i in range(len(m4_r)):
    m4_af[i] = m4_airfoil_types[m4_af_idx[i]]

m6_af = [0]*len(m6_r)
for i in range(len(m6_r)):
    m6_af[i] = m6_airfoil_types[m6_af_idx[i]]

m66_af = [0]*len(m66_r)
for i in range(len(m66_r)):
    m66_af[i] = m66_airfoil_types[m66_af_idx[i]]

m67_af = [0]*len(m67_r)
for i in range(len(m67_r)):
    m67_af[i] = m67_airfoil_types[m67_af_idx[i]]
    
# Next, construct the CCBlade object
# CCBlade provides a few additional options in its constructor. 
# The other options are shown in the following example with their default values.

#rotor = CCBlade(r, chord, theta, af, Rhub, Rtip, B, rho, mu,
#                precone, tilt, yaw, shearExp, hubHt, nSector,
#                tiploss=True, hubloss=True, wakerotation=True, usecd=True, iterRe=1)

# The parameters tiploss and hubloss toggle Prandtl tip and hub losses repsectively. 
# The parameter wakerotation toggles wake swirl (i.e., a′=0). 
# The parameter usecd can be used to disable the inclusion of drag in the 
# calculation of the induction factors (it is always used in calculations of the 
# distributed loads). However, doing so may cause potential failure in the 
# solution methodology (see [4]). In practice, it should work fine, but special care 
# for that particular case has not yet been examined, and the default implementation 
# allows for the possibility of convergence failure. 
# All four of these parameters are True by default. 
# The parameter iterRe is for advanced usage. 
# Referring to [4], this parameter controls the number of internal iterations on the Reynolds number. 
# One iteration is almost always sufficient, but for high accuracy in the Reynolds number 
# iterRe could be set at 2. Anything larger than that is unnecessary.

m1_rotor = CCBlade(m1_r, m1_chord, m1_theta, m1_af, m1_Rhub, m1_Rtip, B, m1_rho, m1_mu,
                precone, tilt, yaw, shearExp, m1_hubHt, nSector)
m4_rotor = CCBlade(m4_r, m4_chord, m4_theta, m4_af, m4_Rhub, m4_Rtip, B, m4_rho, m4_mu,
                precone, tilt, yaw, shearExp, m4_hubHt, nSector)
m6_rotor = CCBlade(m6_r, m6_chord, m6_theta, m6_af, m6_Rhub, m6_Rtip, B, m6_rho, m6_mu,
                precone, tilt, yaw, shearExp, m6_hubHt, nSector)
m66_rotor = CCBlade(m66_r, m66_chord, m66_theta, m66_af, m66_Rhub, m66_Rtip, B, m66_rho, m66_mu,
                precone, tilt, yaw, shearExp, m66_hubHt, nSector)
m66yaw20_rotor = CCBlade(m66_r, m66_chord, m66_theta, m66_af, m66_Rhub, m66_Rtip, B, m66_rho, m66_mu,
                precone, tilt, 20.0, shearExp, m66_hubHt, nSector)
m67_rotor = CCBlade(m67_r, m67_chord, m67_theta, m67_af, m67_Rhub, m67_Rtip, B, m67_rho, m67_mu,
                precone, tilt, yaw, shearExp, m67_hubHt, nSector)
                
# convert to RPM
m1_Omega = m1_Uinf*tsr/m1_Rtip * 30.0/pi  
m4_Omega = m4_Uinf*tsr/m4_Rtip * 30.0/pi
m6_Omega = m6_Uinf*tsr/m6_Rtip * 30.0/pi
m66_Omega = m66_Uinf*tsr/m66_Rtip * 30.0/pi
m67_Omega = m67_Uinf*tsr/m67_Rtip * 30.0/pi

m66yaw_Uinf  = 1.2
m66yaw_Omega = m66yaw_Uinf*tsr/m66_Rtip * 30.0/pi

# Evaluate the distributed loads at a chosen set of operating conditions.
m1_Np, m1_Tp = m1_rotor.distributedAeroLoads(m1_Uinf, m1_Omega, pitch, azimuth)
m4_Np, m4_Tp = m4_rotor.distributedAeroLoads(m4_Uinf, m4_Omega, pitch, azimuth)
m6_Np, m6_Tp = m6_rotor.distributedAeroLoads(m6_Uinf, m6_Omega, pitch, azimuth)
m66_Np, m66_Tp = m66_rotor.distributedAeroLoads(m66_Uinf, m66_Omega, pitch, azimuth)
m66yaw20_Np, m66yaw20_Tp = m66yaw20_rotor.distributedAeroLoads(m66yaw_Uinf, m66yaw_Omega, pitch, azimuth)
m67_Np, m67_Tp = m67_rotor.distributedAeroLoads(m67_Uinf, m67_Omega, pitch, azimuth)








###############################################################################
# Plot the flapwise and lead-lag aerodynamic loading

# plot
m1_rstar = (m1_r - m1_Rhub) / (m1_Rtip - m1_Rhub)
m4_rstar = (m4_r - m4_Rhub) / (m4_Rtip - m4_Rhub)
m6_rstar = (m6_r - m6_Rhub) / (m6_Rtip - m6_Rhub)
m66_rstar = (m66_r - m66_Rhub) / (m66_Rtip - m66_Rhub)
#m66yaw20_rstar = (m66_r - m66_Rhub) / (m66_Rtip - m66_Rhub)
m67_rstar = (m67_r - m67_Rhub) / (m67_Rtip - m67_Rhub)

# append zero at root and tip
m1_rstar = np.concatenate([[0.0], m1_rstar, [1.0]])
m1_Np    = np.concatenate([[0.0], m1_Np, [0.0]])
m1_Tp    = np.concatenate([[0.0], m1_Tp, [0.0]])

m4_rstar = np.concatenate([[0.0], m4_rstar, [1.0]])
m4_Np    = np.concatenate([[0.0], m4_Np, [0.0]])
m4_Tp    = np.concatenate([[0.0], m4_Tp, [0.0]])

m6_rstar = np.concatenate([[0.0], m6_rstar, [1.0]])
m6_Np    = np.concatenate([[0.0], m6_Np, [0.0]])
m6_Tp    = np.concatenate([[0.0], m6_Tp, [0.0]])

m66_rstar = np.concatenate([[0.0], m66_rstar, [1.0]])
m66_Np    = np.concatenate([[0.0], m66_Np, [0.0]])
m66_Tp    = np.concatenate([[0.0], m66_Tp, [0.0]])

#m66yaw20_rstar = np.concatenate([[0.0], m66_rstar, [1.0]])
m66yaw20_Np    = np.concatenate([[0.0], m66yaw20_Np, [0.0]])
m66yaw20_Tp    = np.concatenate([[0.0], m66yaw20_Tp, [0.0]])

m67_rstar = np.concatenate([[0.0], m67_rstar, [1.0]])
m67_Np    = np.concatenate([[0.0], m67_Np, [0.0]])
m67_Tp    = np.concatenate([[0.0], m67_Tp, [0.0]])


plt.figure(1)
plt.plot(m4_rstar, m4_Tp, label='lead-lag model4', linestyle=':')
plt.plot(m4_rstar, m4_Np, label='flapwise model4', linestyle=':')
plt.plot(m6_rstar, m6_Tp, label='lead-lag model6-SavedGames', linestyle='--')
plt.plot(m6_rstar, m6_Np, label='flapwise model6-SavedGames', linestyle='--')
plt.plot(m66_rstar, m66_Tp, label='lead-lag model66-SavedGames', linestyle='-')
plt.plot(m66_rstar, m66_Np, label='flapwise model66-SavedGames', linestyle='-')
plt.plot(m66_rstar, m66yaw20_Tp, label='lead-lag model66-SavedGames yaw 20', linestyle='-')
plt.plot(m66_rstar, m66yaw20_Np, label='flapwise model66-SavedGames yaw 20', linestyle='-')
#plt.plot(m67_rstar, m67_Tp, label='lead-lag model67', linestyle='-')
#plt.plot(m67_rstar, m67_Np, label='flapwise model67', linestyle='-')
plt.xlabel('blade fraction')
plt.ylabel('distributed aerodynamic loads (N)')
plt.legend(loc='upper left')
plt.grid()
plt.show()
plt.savefig('compare_m4_m6_m66_yaw_m67_AeroForces.png')
plt.close(1)




# To get the power, thrust, and torque at the same conditions 
# (in both absolute and coefficient form), use the evaluate method. 
# This is generally used for generating power curves so it expects 
# array_like input. For this example a list of size one is used.
# Note that the outputs are numpy arrays (of length 1 for this example). 
#m1_P,  m1_T,  m1_Q  = m1_rotor.evaluate([m1_Uinf], [m1_Omega], [pitch])
m1_CP, m1_CT, m1_CQ = m1_rotor.evaluate([m1_Uinf], [m1_Omega], [pitch], coefficient=True)

#m4_P,  m4_T,  m4_Q  = m4_rotor.evaluate([m4_Uinf], [m4_Omega], [pitch])
m4_CP, m4_CT, m4_CQ = m4_rotor.evaluate([m4_Uinf], [m4_Omega], [pitch], coefficient=True)

#m6_P,  m6_T,  m6_Q  = m6_rotor.evaluate([m6_Uinf], [m6_Omega], [pitch])
m6_CP, m6_CT, m6_CQ = m6_rotor.evaluate([m6_Uinf], [m6_Omega], [pitch], coefficient=True)

#m66_P,  m66_T,  m66_Q  = m66_rotor.evaluate([m66_Uinf], [m66_Omega], [pitch])
m66_CP, m66_CT, m66_CQ = m66_rotor.evaluate([m66_Uinf], [m66_Omega], [pitch], coefficient=True)

m67_CP, m67_CT, m67_CQ = m67_rotor.evaluate([m67_Uinf], [m67_Omega], [pitch], coefficient=True)

print 'model1 CP =', m1_CP
print 'model1 CT =', m1_CT
print 'model1 CQ =', m1_CQ

print 'model4 CP =', m4_CP
print 'model4 CT =', m4_CT
print 'model4 CQ =', m4_CQ

print 'model6 CP =', m6_CP
print 'model6 CT =', m6_CT
print 'model6 CQ =', m6_CQ

print 'model66 CP =', m66_CP
print 'model66 CT =', m66_CT
print 'model66 CQ =', m66_CQ

print 'model67 CP =', m66_CP
print 'model67 CT =', m66_CT
print 'model67 CQ =', m66_CQ

# Note that the outputs are numpy arrays (of length 1 for the previous example). 
# To generate a nondimensional power curve (λ vs cp):
# note, velocity and rpm have a small amount of Reynolds number dependence

# all turbines will run at the same same TSRs
param_tsr = np.linspace(2, 12, 20)

# model 1 at full-scale
param_rpm = m1_Omega * np.ones_like(param_tsr)
param_Uin = param_rpm*pi/30.0 * m1_Rtip/param_tsr
param_deg = np.zeros_like(param_tsr)
param_m1_CP, param_m1_CT, param_m1_CQ = m1_rotor.evaluate(param_Uin, param_rpm, param_deg, coefficient=True)

# model4
param_rpm = m4_Omega * np.ones_like(param_tsr)
param_Uin = param_rpm*pi/30.0 * m4_Rtip/param_tsr
param_m4_CP, param_m4_CT, param_m4_CQ = m4_rotor.evaluate(param_Uin, param_rpm, param_deg, coefficient=True)

# model6 Saved-Games
param_rpm = m6_Omega * np.ones_like(param_tsr)
param_Uin = param_rpm*pi/30.0 * m6_Rtip/param_tsr
param_m6_CP, param_m6_CT, param_m6_CQ = m6_rotor.evaluate(param_Uin, param_rpm, param_deg, coefficient=True)

# model66 Saved-Games
param_rpm = m66_Omega * np.ones_like(param_tsr)
param_Uin = param_rpm*pi/30.0 * m66_Rtip/param_tsr
param_m66_CP, param_m66_CT, param_m66_CQ = m66_rotor.evaluate(param_Uin, param_rpm, param_deg, coefficient=True)

# model66 Saved-Games yaw 20
param_rpm = m66yaw_Omega * np.ones_like(param_tsr)
param_Uin = param_rpm*pi/30.0 * m66_Rtip/param_tsr
param_m66yaw20_CP, param_m66yaw20_CT, param_m66yaw20_CQ = m66yaw20_rotor.evaluate(param_Uin, param_rpm, param_deg, coefficient=True)

# model67
param_rpm = m67_Omega * np.ones_like(param_tsr)
param_Uin = param_rpm*pi/30.0 * m67_Rtip/param_tsr
param_m67_CP, param_m67_CT, param_m67_CQ = m67_rotor.evaluate(param_Uin, param_rpm, param_deg, coefficient=True)

# this is WT_Perf calculations on the model4
wtp_tsr = np.array([2,
2.2,
2.4,
2.6,
2.8,
3,
3.2,
3.4,
3.6,
3.8,
4,
4.2,
4.4,
4.6,
4.8,
5,
5.2,
5.4,
5.6,
5.8,
6,
6.2,
6.4,
6.6,
6.8,
7,
7.2,
7.4,
7.6,
7.8,
8,
8.2,
8.4,
8.6,
8.8,
9,
9.2,
9.4,
9.6,
9.8,
10,
10.2,
10.4,
10.6,
10.8,
11,
11.2,
11.4,
11.6,
11.8,
12])
wtp_Cp = np.array([0.031,
0.04,
0.0509,
0.0646,
0.0811,
0.1011,
0.1246,
0.1508,
0.1785,
0.2068,
0.2346,
0.2633,
0.2889,
0.3118,
0.3339,
0.3547,
0.3746,
0.3922,
0.4081,
0.4245,
0.4348,
0.443,
0.4499,
0.4557,
0.4605,
0.4644,
0.4674,
0.4693,
0.4703,
0.4705,
0.4698,
0.4683,
0.4658,
0.4627,
0.4589,
0.4545,
0.4499,
0.445,
0.4402,
0.4354,
0.4305,
0.4255,
0.4203,
0.4149,
0.4093,
0.4032,
0.3967,
0.3899,
0.3827,
0.3754,
0.3677])


plt.figure(2)
#plt.plot(tsr, CP, label='CCBlade')
plt.plot(param_tsr, param_m1_CP, linewidth=2, linestyle='-', label='CCBlade - DOE-RM1 full-scale')
plt.plot(param_tsr, param_m4_CP, linewidth=3, linestyle='-.', label='CCBlade - model4')
plt.plot(param_tsr, param_m6_CP, linewidth=2, linestyle='--', label='CCBlade - model6 Saved-Games')
plt.plot(param_tsr, param_m66_CP, linewidth=2, linestyle=':', label='CCBlade - model66 Saved-Games')
plt.plot(param_tsr, param_m67_CP, linewidth=2, linestyle='-', label='CCBlade - model67')
plt.plot(param_tsr, param_m66yaw20_CP, linewidth=3, linestyle=':', label='CCBlade - model66 Saved-Games yaw 20')
plt.plot(wtp_tsr, wtp_Cp,        linewidth=3, linestyle='-.', label='WT_Perf - model4')
plt.xlabel('$\lambda$')
plt.ylabel('$c_p$')
plt.legend(loc='bottom right')
plt.grid()
plt.show()
plt.savefig('compare_CPvsTSR_m1_m4_m6_m66_yaw_m67.png')
plt.close(2)


# SAVE some data to text files
np.savetxt('param_tsr.txt', param_tsr, delimiter=',')
np.savetxt('param_m1_CP.txt', param_m1_CP, delimiter=',')
np.savetxt('param_m4_CP.txt', param_m4_CP, delimiter=',')
np.savetxt('param_m6_CP.txt', param_m6_CP, delimiter=',')
np.savetxt('param_m66_CP.txt', param_m66_CP, delimiter=',')
np.savetxt('param_m66yaw20_CP.txt', param_m66yaw20_CP, delimiter=',')
np.savetxt('param_m67_CP.txt', param_m67_CP, delimiter=',')








# Plot the chord Reynolds number along the blade at different tip-speed-ratios.
#exp_Uinf  = np.array([0.9])
#exp_tsr   = np.array([6.2, 7, 8.0])
#exp_Omega = np.array([236.82, 267.38, 305.58])
#exp_Uinf  = np.array([1.0])
#exp_tsr   = np.array([6.2, 7, 8.0])
#exp_Omega = np.array([263.13, 297.08, 339.53])
exp_Uinf     = np.array([1.13])
exp_Uinf_m67 = np.array([4.4111])
exp_Uinfyaw  = np.array([1.20])
#exp_tsr   = np.array([6.2, 7, 8.0])
#exp_Omega = np.array([289.44, 326.79, 373.48])
#exp_Uinf  = np.array([1.2])
#exp_tsr   = np.array([6.2, 7, 8.0])
#exp_Omega = np.array([315.76, 356.50, 407.43])
   
   
rpm_tsr7     = 7*30*exp_Uinf/(3.14159*0.225)
rpm_tsr7_m67 = 7*30*exp_Uinf_m67/(3.14159*0.225*scale)
rpm_tsr7_yaw = 7*30*exp_Uinfyaw/(3.14159*0.225)
   
#u_local = np.sqrt(exp_Uinf**2 + (r*exp_Omega[0]*pi/30)**2)
#RE_local = chord * u_local * rho / mu

m4_u_local  = np.sqrt(exp_Uinf**2 + (m4_r*rpm_tsr7*pi/30)**2)
m4_RE_local = m4_chord * m4_u_local * m4_rho / m4_mu

m6_u_local  = np.sqrt(exp_Uinf**2 + (m6_r*rpm_tsr7*pi/30)**2)
m6_RE_local = m6_chord * m6_u_local * m6_rho / m6_mu

m66_u_local  = np.sqrt(exp_Uinf**2 + (m66_r*rpm_tsr7*pi/30)**2)
m66_RE_local = m66_chord * m66_u_local * m66_rho / m66_mu

m67_u_local  = np.sqrt(exp_Uinf_m67**2 + (m67_r*rpm_tsr7_m67*pi/30)**2)
m67_RE_local = m67_chord * m67_u_local * m67_rho / m67_mu

plt.figure(3)
plt.plot(m4_r/m4_Rtip, m4_RE_local, linewidth=3, label='model4')
plt.plot(m6_r/m6_Rtip, m6_RE_local, linewidth=3, label='model6-SavedGames')
plt.plot(m66_r/m66_Rtip, m66_RE_local,  linestyle=':',linewidth=3, label='model66-SavedGames')
plt.plot(m67_r/m67_Rtip, m67_RE_local, linewidth=3, label='model67')
#plt.plot(m66_r/m66_Rtip, m66yaw20_RE_local, linewidth=3, label='model66-SavedGames yaw 20')
plt.title('Reynolds at TSR 7')
plt.xlabel('$r/R$')
plt.ylabel('$Re_c$')
plt.legend(loc='bottom right')
plt.grid()
plt.show()
plt.savefig('compare_Reynolds_m4_m6_m66_m67.png')
plt.close(3)



#x, y components of wind in blade-aligned coordinate system
m4_Vx, m4_Vy, _, _, _, _ = m4_rotor._CCBlade__windComponents(m4_Uinf,m4_Omega,pitch)
m6_Vx, m6_Vy, _, _, _, _ = m6_rotor._CCBlade__windComponents(m6_Uinf,m6_Omega,pitch)

## but Vx and Vy do not have induction. This will return with induction effects
#alpha, W, Re = _bem.relativewind(phi, a, ap, Vx, Vy, self.pitch,
#                                             chord, theta, self.rho, self.mu)
#
#fzero, a, ap = m4_rotor._CCBlade__runBEM(
#
#alpha, W, Re = relativeWind(phi, a, ap, Vx, Vy, pitch, &
#    chord, theta, rho, mu, alpha, W, Re)
#! out 
#real(dp), intent(out) :: alpha, W, Re
    
# local inflow angle \phi
# magnitude of the inflow velocity W
# W = sqrt((Vx*(1-a))**2 + (Vy*(1+ap))**2)

m4_wtp_aoa = np.array([2.64,
6.54,
8.36,
9.03,
9.05,
8.80,
8.44,
8.06,
7.70,
7.36,
7.06,
6.76,
6.50,
6.24,
6.03,
5.83,
5.64,
5.47,
5.32,
5.17,
5.06,
4.96,
4.87,
4.78,
4.68,
4.56,
4.42,
4.17,
3.68,
2.94])
m4_wtp_afa = np.array([22.71,
22.92,
22.22,
21.00,
19.56,
18.12,
16.79,
15.59,
14.54,
13.60,
12.78,
12.04,
11.38,
10.76,
10.23,
 9.74,
 9.29,
 8.87,
 8.49,
 8.11,
 7.78,
 7.47,
 7.17,
 6.87,
 6.55,
 6.22,
 5.84,
 5.36,
 4.63,
 3.63])
m6_wtp_aoa = np.array([-0.49,
 1.81,
 3.18,
 4.04,
 4.54,
 4.81,
 4.93,
 4.94,
 4.92,
 4.86,
 4.78,
 4.67,
 4.55,
 4.44,
 4.30,
 4.16,
 4.00,
 3.85,
 3.70,
 3.52,
 3.35,
 3.15,
 2.96,
 2.74,
 2.51,
 2.23,
 1.89,
 1.49,
 1.00,
 0.36])
m6_wtp_afa = np.array([18.93,
17.62,
16.55,
15.62,
14.75,
13.93,
13.15,
12.43,
11.80,
11.22,
10.70,
10.23,
 9.79,
 9.41,
 9.02,
 8.69,
 8.35,
 8.03,
 7.74,
 7.43,
 7.14,
 6.84,
 6.54,
 6.22,
 5.89,
 5.51,
 5.08,
 4.58,
 4.00,
 3.25])


plt.figure(4)
plt.plot(m4_r/m4_Rtip, m4_wtp_aoa, linewidth=3, label='WT-Perf angle-of-attack: model4')
plt.plot(m6_r/m6_Rtip, m6_wtp_aoa, linewidth=3, label='WT-Perf angle-of-attack: model6-SavedGames')
plt.plot(m4_r/m4_Rtip, m4_wtp_afa, linewidth=3, label='WT-Perf airflow angle: model4')
plt.plot(m6_r/m6_Rtip, m6_wtp_afa, linewidth=3, label='WT-Perf airflow angle: model6-SavedGames')
plt.title('TSR 7, 359 rev/min, inflow 1.2 m/s')
plt.xlabel('$r/R$')
plt.ylabel('$angle [deg]$')
plt.legend(loc='top right')
plt.grid()
plt.show()
plt.savefig('compare_AoA_AfA_m4_m6.png')
plt.close(4)

# plot the velocity vs Power, Thrust Coef.
#m1_P,  m1_T,  m1_Q  = m1_rotor.evaluate([m1_Uinf], [m1_Omega], [pitch])
#table_Uinf = [1.2, 1.3]
#table_tsr7 = 7*30*table_Uinf/(3.14159*m4_Rtip)
#rpm_tsr7 = 7*30*1.2/(3.14159*0.225)


table_tsr   = 7
table_Uinf  = np.linspace(0.1, 3.0, 20)
table_rpm   = table_tsr*30*table_Uinf/(3.14159*m4_Rtip)
table_pitch = [0]*table_Uinf.size

table_Uinf_m67  = np.linspace(0.1, 10.0, 20)
table_rpm_m67   = table_tsr*30*table_Uinf_m67/(3.14159*m67_Rtip)

m4_P,  m4_T,  m4_Q  = m4_rotor.evaluate(table_Uinf, table_rpm, table_pitch)
m4_CP, m4_CT, m4_CQ = m4_rotor.evaluate(table_Uinf, table_rpm, table_pitch, coefficient=True)
m6_P,  m6_T,  m6_Q  = m6_rotor.evaluate(table_Uinf, table_rpm, table_pitch)
m6_CP, m6_CT, m6_CQ = m6_rotor.evaluate(table_Uinf, table_rpm, table_pitch, coefficient=True)
m66_P,  m66_T,  m66_Q  = m66_rotor.evaluate(table_Uinf, table_rpm, table_pitch)
m66_CP, m66_CT, m66_CQ = m66_rotor.evaluate(table_Uinf, table_rpm, table_pitch, coefficient=True)
m66yaw20_P,  m66yaw20_T,  m66yaw20_Q  = m66yaw20_rotor.evaluate(table_Uinf, table_rpm, table_pitch)
m66yaw20_CP, m66yaw20_CT, m66yaw20_CQ = m66yaw20_rotor.evaluate(table_Uinf, table_rpm, table_pitch, coefficient=True)
m67_P,  m67_T,  m67_Q  = m67_rotor.evaluate(table_Uinf_m67, table_rpm_m67, table_pitch)
m67_CP, m67_CT, m67_CQ = m67_rotor.evaluate(table_Uinf_m67, table_rpm_m67, table_pitch, coefficient=True)

m4_power_table       = np.column_stack([table_Uinf, m4_P, m4_CT, table_rpm])
m6_power_table       = np.column_stack([table_Uinf, m6_P, m6_CT, table_rpm])
m66_power_table      = np.column_stack([table_Uinf, m66_P, m66_CT, table_rpm])
m66yaw20_power_table = np.column_stack([table_Uinf, m66yaw20_P, m66yaw20_CT, table_rpm])
m67_power_table      = np.column_stack([table_Uinf_m67, m67_P, m67_CT, table_rpm_m67])


np.savetxt('starccm_model4_VDM-1DM_TSR=7.csv',        m4_power_table,       delimiter=',', fmt='%1.3f', header="WindSpeed_m/s,Power_Watts,ThrustCoefficient,RotorSpeed_rev/min")
np.savetxt('starccm_model6_VDM-1DM_TSR=7.csv',        m6_power_table,       delimiter=',', fmt='%1.3f', header="WindSpeed_m/s,Power_Watts,ThrustCoefficient,RotorSpeed_rev/min")
np.savetxt('starccm_model66_VDM-1DM_TSR=7.csv',       m66_power_table,      delimiter=',', fmt='%1.3f', header="WindSpeed_m/s,Power_Watts,ThrustCoefficient,RotorSpeed_rev/min")
np.savetxt('starccm_model66_VDM-1DM_TSR=7_yaw20.csv', m66yaw20_power_table, delimiter=',', fmt='%1.3f', header="WindSpeed_m/s,Power_Watts,ThrustCoefficient,RotorSpeed_rev/min")
np.savetxt('starccm_model67_VDM-1DM_TSR=7.csv',       m67_power_table,      delimiter=',', fmt='%1.3f', header="WindSpeed_m/s,Power_Watts,ThrustCoefficient,RotorSpeed_rev/min")


plt.figure(5)
plt.xlim(0, 10)
plt.ylim(0, 300)
plt.plot(table_Uinf, m4_P, linewidth=3, label='CCBlade: model4')
plt.plot(table_Uinf, m6_P, linewidth=3, label='CCBlade: model6-SavedGames')
plt.plot(table_Uinf, m66_P, linewidth=3, label='CCBlade: model66-SavedGames')
plt.plot(table_Uinf, m66yaw20_P, linewidth=3, label='CCBlade: model66-SavedGames yaw 20')
plt.plot(table_Uinf_m67, m67_P, linewidth=3, label='CCBlade: model67')
plt.title('power curves')
plt.xlabel('$flow speed [m/s]$')
plt.ylabel('$power [W]$')
plt.legend(loc='best')
plt.grid()
plt.show()
plt.savefig('compare_PowerCurves_m4_m6_m66_yaw_m67.png')
plt.close(5)

plt.figure(6)
plt.plot(table_Uinf, m4_CT, linewidth=3, label='CCBlade: model4')
plt.plot(table_Uinf, m6_CT, linewidth=3, label='CCBlade: model6-SavedGames')
plt.plot(table_Uinf, m66_CT, linewidth=3, label='CCBlade: model66-SavedGames')
plt.plot(table_Uinf, m66yaw20_CT, linewidth=3, label='CCBlade: model66-SavedGames yaw 20')
plt.plot(table_Uinf_m67, m67_CT, linewidth=3, label='CCBlade: model67')
plt.title('thrust coefficient')
plt.xlabel('$flow speed [m/s]$')
plt.ylabel('$C_T [-]$')
plt.legend(loc='best')
plt.grid()
plt.show()
plt.savefig('compare_CtCurves_m4_m6_m66_yaw_m67.png')
plt.close(6)


# to use the VDM-BEM, must use a compressible solver, so apply Reynolds scaling
#of factor Radius_water / Radius_air = 0.268
#m6_scaled_r     = m6_r / 0.268
#m6_scaled_chord = m6_chord / 0.268
m6_scaled_rotor = CCBlade(m6_r/0.268, m6_chord/0.268, m6_theta, m6_af, m6_Rhub/0.268, m6_Rtip/0.268, B, 1.176673, 1.8e-5,
                precone, tilt, yaw, shearExp, m6_hubHt/0.268, nSector)

m6_scaled_geom = np.column_stack([m6_r/m6_Rtip, m6_chord/0.268, m6_theta, [0]*m6_r.size])
np.savetxt('starccm_model6_BEM_BladeGeom_WindTunnel.csv', m6_scaled_geom, delimiter=',', fmt='%1.3f', header="r_R,chord,pre-twist,sweep")
m6_geom = np.column_stack([m6_r/m6_Rtip, m6_chord, m6_theta, [0]*m6_r.size])
np.savetxt('starccm_model6_BEM_BladeGeom_Flume.csv', m6_geom, delimiter=',', fmt='%1.3f', header="r_R,chord,pre-twist,sweep")


## now plot the Torque vs RPM curves for different inflow speeds
# perturb the operating points
#

    
param_rpm = np.linspace(200, 600, 100)
param_deg = [0.0]*param_rpm.size

param_Uin = [0.9]*param_rpm.size
op1_P, op1_T, op1_Q = m66_rotor.evaluate(param_Uin, param_rpm, param_deg)

param_Uin = [1.13]*param_rpm.size
op2_P, op2_T, op2_Q = m66_rotor.evaluate(param_Uin, param_rpm, param_deg)

param_Uin = [1.2]*param_rpm.size
op3_P, op3_T, op3_Q = m66_rotor.evaluate(param_Uin, param_rpm, param_deg)



plt.figure(7)
plt.plot(param_rpm, op1_Q, linewidth=3, label='op1: inflow 0.9 m/s')
plt.plot(param_rpm, op2_Q, linewidth=3, label='op2: inflow 1.13 m/s')
plt.plot(param_rpm, op3_Q, linewidth=3, label='op3: inflow 1.2 m/s')
plt.title('model66:torque')
plt.xlabel('$rotor speed [rev / min]$')
plt.ylabel('$torque [N-m]$')
plt.legend(loc='best')
plt.grid()
plt.show()
plt.savefig('compare_Spd-vs-Torque_m66.png')
plt.close(7)


# save to the FAST format for variable speed control (make sure there is no negative torques)
m66_Spd_Trq     = np.column_stack([param_rpm, op2_Q])
#np.savetxt('openFAST_v7__Spd-vs-Trq_mps1p13.dat', m66_Spd_Trq, delimiter=',', fmt='%1.3f', header="rev/min, torque[N-m]")




