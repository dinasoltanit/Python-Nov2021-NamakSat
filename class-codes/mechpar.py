# this program is going to calculate the Thrust available for us.

from numpy import pi
import matplotlib.pyplot as plt

def knots_to_ftpersec(speed):
    
    # speed is the user input and is in Knots
    return speed * 1.68781

def thrust_req(rho_inf, v_inf, s, cd0, k, w):
    
    # s : A/C's wetted area
    # cd0 ~ profile drag
    # k : induced drag constant
    # w : weight
    # cl : lift coeff.
    q = 0.5 * rho_inf * (v_inf **2) * s
    cl = w / q
    th_req = q * (cd0 + k * cl**2)
    return th_req

weight = 200000 # lb
wing_area = 1318 # ft^2
wing_span = 117.416666667 # ft
cd0 = 0.0185
thrust = 66000 # lb of thrust total
aspect_ratio = wing_span**2 / wing_area
e = 0.92
K = 1 / (pi * e * aspect_ratio)
rho_sl = 23.77E-4 # in slugs/ft^3

x_vals_sl = []
for i in range(80, 750, 10):
    x_vals_sl = [i for i in range(80, 750, 10)]
    x_vals_sl_knots = [knots_to_ftpersec(i) for i in range(80,750,10)]
    
tr_sl = []# list of thrust required values at sea level
for airspeed in x_vals_sl:
    #airspeed_fps= knots_to_ftpersec(airspeed)
    #thrust_calculated = thrust_req( rho_sl, knots_to_ftpersec(airspeed),wing_area, cd0, K, weight )
    #tr_sl = [thrust_calculated for airspeed in x_vals_sl]
    tr_sl = [thrust_req(rho_sl, knots_to_ftpersec(airspeed), wing_area, cd0, K, weight) for airspeed in x_vals_sl]

plt.subplot(3, 1, 1)
plt.plot(x_vals_sl, tr_sl, 'k-', label=r"$T_R$ at Sea Level")

TA_sl = 0.7 * thrust
th_avi = [TA_sl for _ in x_vals_sl]

takeoff_vel_sl = [180, 180]
cruise_velocity_sl_values = [11000, 46500]
#
plt.plot(x_vals_sl, th_avi, 'k--',
          label='$T_A$ at Sea Level ({:,.1f} lb)'.format(TA_sl))
#
plt.plot(takeoff_vel_sl, cruise_velocity_sl_values, 'b-.',
         label="Takeoff Velocity ({} knots)".format(takeoff_vel_sl[0]))
plt.ylim(5000, 50000)
plt.xlim(50, 1550)
plt.ylabel('Thrust (lb)')
plt.xlabel('Velocity (kts)')
plt.title('Thrust Required & Thrust Available Curves')
plt.legend(loc='lower right')



