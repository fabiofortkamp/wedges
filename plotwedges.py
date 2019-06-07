import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import numpy as np

FIGSIZE_INCHES = 4

def create_magnet_IV_figure_template(params):
    """
    Return (fig,axes) correspondent to a figure of the
    first quadrant of magnet IV.
    The size of the figure is controlled by FIGSIZE_INCHES"""

    fig = plt.figure(figsize=(FIGSIZE_INCHES, FIGSIZE_INCHES))
    axes = fig.add_subplot(111, aspect='equal')

    R2 = params['R2']
    R1 = params['R1']
    R4 = params['R4']
    R3 = params['R3']
    R5 = params['R5']
    r_lim = R5

    axes.set_ylim(0, 1e3 * r_lim)
    axes.set_xlim(0, 1e3 * r_lim)

    axes.set_ylabel('y [mm]')
    axes.set_xlabel('x [mm]')

    width_IV = R4 - R3
    n_IV = int(params['n_IV'])
    
    delta_phi_S_values = params['delta_phi_S_values']
    phi_initial = np.append(np.array([0,]),np.cumsum(delta_phi_S_values)[:-1])
    phi_final = phi_initial + delta_phi_S_values

    
    r_mean  = 1e3 * (R4 + R3)/2
    l = 0.4*(r_mean * np.deg2rad(delta_phi_S_values))
    phi_mean = np.deg2rad(0.5 * (phi_initial + phi_final))

    alpha = np.deg2rad(params['alpha_values'])

    x_mean = r_mean * np.cos(phi_mean)
    y_mean = r_mean * np.sin(phi_mean)

    xtail = x_mean - l/2 * np.cos(alpha)
    ytail = y_mean - l/2 * np.sin(alpha)

    dxarrow = l*np.cos(alpha)
    dyarrow = l*np.sin(alpha)

    for i in range(0, n_IV):
        magnet_segment = Wedge((0, 0),
                               1e3 * R4,
                               phi_initial[i],
                               phi_final[i],
                               1e3 * width_IV,
                               color='k',
                               fill=False)
        axes.add_artist(magnet_segment)

        axes.arrow(
        xtail[i], ytail[i], 
        dxarrow[i], dyarrow[i],
        width=0.8,
        head_width=8,
        ec='k',
        fc='k')

    return fig, axes

params = {
    'R1': 30e-3,
    'R2': 126e-3,
    'R3': 173e-3,
    'R4': 396e-3,
    'R5': 414e-3,
    'n_IV': 3,
    'phi_S_IV': 45
    }

fractions_phi_S = np.array([40,40,20])

assert sum(fractions_phi_S) == 100

params['delta_phi_S_values'] = np.array(fractions_phi_S)/100 * params["phi_S_IV"]

params['alpha_values'] = np.array([11,90,108])

fig, axes = create_magnet_IV_figure_template(params)

plt.show()