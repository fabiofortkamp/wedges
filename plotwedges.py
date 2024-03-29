import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, FancyArrowPatch
import numpy as np
from math import pi

FIGSIZE_INCHES = 5

def create_magnet_IV_figure_quadrant(params):
    """
    Return (fig,axes) correspondent to a figure of the
    first quadrant of magnet IV.
    The size of the figure is controlled by FIGSIZE_INCHES"""

    fig = plt.figure(figsize=(FIGSIZE_INCHES, FIGSIZE_INCHES))
    axes = fig.add_subplot(111, aspect='equal')

    R4 = params['R4']
    R3 = params['R3']
    r_lim = 1.1*R4

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

    alpha_degress = params['alpha_values']
    alpha = np.deg2rad(alpha_degress)
    alpha_text = ["%d°" %(phi,) for phi in alpha_degress]

    x_mean = r_mean * np.cos(phi_mean)
    y_mean = r_mean * np.sin(phi_mean)

    xtail = x_mean - l/2 * np.cos(alpha)
    ytail = y_mean - l/2 * np.sin(alpha)

    dxarrow = l*np.cos(alpha)
    dyarrow = l*np.sin(alpha)

    xhead = xtail + dxarrow
    yhead = ytail + dyarrow

    r_text_width = 7.5e2 * R3
    x_text_width = r_text_width * np.cos(phi_mean)
    y_text_width = r_text_width * np.sin(phi_mean)
    text_width = ["%d°" %(phi,) for phi in delta_phi_S_values]

    r_angular = 9.5e2 * R3
    phi_initial_rad = np.deg2rad(phi_initial)
    phi_final_rad = np.deg2rad(phi_final)

    x_angular_tail = r_angular * np.cos(phi_initial_rad)
    y_angular_tail = r_angular * np.sin(phi_initial_rad)

    x_angular_head = r_angular * np.cos(phi_final_rad)
    y_angular_head = r_angular * np.sin(phi_final_rad)

    dx_angular = x_angular_head - x_angular_tail
    dy_angular = y_angular_head - y_angular_tail 

    for i in range(0, n_IV):
        magnet_segment_1q = Wedge((0, 0),
                               1e3 * R4,
                               phi_initial[i],
                               phi_final[i],
                               1e3 * width_IV,
                               color='k',
                               fill=False)
        axes.add_artist(magnet_segment_1q)

        axes.arrow(
        xtail[i], ytail[i], 
        dxarrow[i], dyarrow[i],
        width=0.8,
        head_width=8,
        ec='k',
        fc='k')

        axes.text(
            1.05*xhead[i],
            1.05*yhead[i],
            alpha_text[i],
            fontsize=14
        )

        axes.text(
            x_text_width[i],
            y_text_width[i],
            text_width[i])

        fa = FancyArrowPatch(
            (x_angular_tail[i], y_angular_tail[i]),
            (x_angular_head[i], y_angular_head[i]),
            connectionstyle="arc3,rad=.1",
            arrowstyle="<|-|>, head_length=3, head_width=3",
            linewidth=0.8,
            ec='k',
            fc='k'
        )
        axes.add_patch(fa)

    axes.text(
        0,
        0,
        """
        Angular
        widths
        """,
        ha='left'
        )

    axes.text(
        0.05,0.95,
        "Arrows angles are in respect to x axis",
        transform=axes.transAxes)

    axes.text(
        0.05, 0.7,
        "ID = %.2f mm\nOD = %.2f mm""" %(2e3*R3,2e3*R4),
        transform=axes.transAxes
    )

    return fig, axes

def create_magnet_IV_figure_full(params):
    """
    Return (fig,axes) correspondent to a figure of the
    first quadrant of magnet IV.
    The size of the figure is controlled by FIGSIZE_INCHES,
    using the double of its values"""

    fig = plt.figure(figsize=(2*FIGSIZE_INCHES, 2*FIGSIZE_INCHES))
    axes = fig.add_subplot(111, aspect='equal')

    R4 = params['R4']
    R3 = params['R3']
    r_lim = 1.2e3*R4

    axes.set_ylim(-r_lim, r_lim)
    axes.set_xlim(-r_lim, r_lim)

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

    alpha_degress = params['alpha_values']
    alpha = np.deg2rad(alpha_degress)
    alpha_text = ["%d°" %(phi,) for phi in alpha_degress]

    x_mean = r_mean * np.cos(phi_mean)
    y_mean = r_mean * np.sin(phi_mean)

    xtail = x_mean - l/2 * np.cos(alpha)
    ytail = y_mean - l/2 * np.sin(alpha)

    dxarrow = l*np.cos(alpha)
    dyarrow = l*np.sin(alpha)

    xhead = xtail + dxarrow
    yhead = ytail + dyarrow

    r_text_width = 7.5e2 * R3
    x_text_width = r_text_width * np.cos(phi_mean)
    y_text_width = r_text_width * np.sin(phi_mean)
    text_width = ["%d°" %(phi,) for phi in delta_phi_S_values]

    r_angular = 9.5e2 * R3
    phi_initial_rad = np.deg2rad(phi_initial)
    phi_final_rad = np.deg2rad(phi_final)

    x_angular_tail = r_angular * np.cos(phi_initial_rad)
    y_angular_tail = r_angular * np.sin(phi_initial_rad)

    x_angular_head = r_angular * np.cos(phi_final_rad)
    y_angular_head = r_angular * np.sin(phi_final_rad)

    dx_angular = x_angular_head - x_angular_tail
    dy_angular = y_angular_head - y_angular_tail 

    for i in range(0, n_IV):
        magnet_segment_1q = Wedge((0, 0),
                               1e3 * R4,
                               phi_initial[i],
                               phi_final[i],
                               1e3 * width_IV,
                               color='k',
                               fill=False)
        axes.add_artist(magnet_segment_1q)

        
        magnet_segment_2q = Wedge((0, 0),
                               1e3 * R4,
                               180 - phi_final[i],
                               180 - phi_initial[i],
                               1e3 * width_IV,
                               color='k',
                               fill=False)
        axes.add_artist(magnet_segment_2q)

        magnet_segment_3q = Wedge((0, 0),
                               1e3 * R4,
                               180 + phi_initial[i],
                               180 + phi_final[i],
                               1e3 * width_IV,
                               color='k',
                               fill=False)
        axes.add_artist(magnet_segment_3q)
        
        magnet_segment_4q = Wedge((0, 0),
                               1e3 * R4,
                               360 - phi_final[i],
                               360 - phi_initial[i],
                               1e3 * width_IV,
                               color='k',
                               fill=False)
        axes.add_artist(magnet_segment_4q)

        axes.arrow(
        xtail[i], ytail[i], 
        dxarrow[i], dyarrow[i],
        width=0.8,
        head_width=8,
        ec='k',
        fc='k')

        axes.arrow(
        -xhead[i], yhead[i], 
        dxarrow[i], -dyarrow[i],
        width=0.8,
        head_width=8,
        ec='k',
        fc='k')
        
        axes.arrow(
        xtail[i], -ytail[i], 
        dxarrow[i], -dyarrow[i],
        width=0.8,
        head_width=8,
        ec='k',
        fc='k')

        axes.arrow(
        -xhead[i], -yhead[i], 
        dxarrow[i], dyarrow[i],
        width=0.8,
        head_width=8,
        ec='k',
        fc='k')

        axes.text(
            1.05*xhead[i],
            1.05*yhead[i],
            alpha_text[i],
            fontsize=14
        )

        axes.text(
            x_text_width[i],
            y_text_width[i],
            text_width[i])

        fa = FancyArrowPatch(
            (x_angular_tail[i], y_angular_tail[i]),
            (x_angular_head[i], y_angular_head[i]),
            connectionstyle="arc3,rad=.1",
            arrowstyle="<|-|>, head_length=3, head_width=3",
            linewidth=0.8,
            ec='k',
            fc='k'
        )
        axes.add_patch(fa)

    axes.text(
        0.05,0.95,
        "Arrows angles are in respect to x axis",
        transform=axes.transAxes,
        fontsize=16)

    axes.text(
        0.4, 0.8,
        "ID = %.2f mm\nOD = %.2f mm""" %(2e3*R3,2e3*R4),
        transform=axes.transAxes,
        fontsize=16
    )

    return fig, axes

params = {
    'R3': 173e-3,
    'R4': 397e-3,
    'n_IV': 5,
    'phi_S_IV': 60
    }

fractions_phi_S = np.array([20,20,20,20,20])

assert sum(fractions_phi_S) == 100

params['delta_phi_S_values'] = np.array(fractions_phi_S)/100 * params["phi_S_IV"]

params['alpha_values'] = np.array([6,23,73,116,144])

fig, axes = create_magnet_IV_figure_full(params)

plt.show()