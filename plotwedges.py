import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

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
    delta_phi_S_IV = params['delta_phi_S_IV']
    for i in range(0, n_IV):
        theta_0 = i * delta_phi_S_IV
        theta_1 = (i + 1) * delta_phi_S_IV
        magnet_segment = Wedge((0, 0),
                               1e3 * R4,
                               theta_0,
                               theta_1,
                               1e3 * width_IV,
                               color='k',
                               fill=False)
        axes.add_artist(magnet_segment)

    return fig, axes

params = {
    'R1': 30e-3,
    'R2': 126e-3,
    'R3': 173e-3,
    'R4': 396e-3,
    'R5': 414e-3,
    'n_IV': 5,
    'delta_phi_S_IV': 12,
    }

fig, axes = create_magnet_IV_figure_template(params)
plt.show()