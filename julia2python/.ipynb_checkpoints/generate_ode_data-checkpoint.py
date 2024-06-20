import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import argparse
import os

def Arrhenius(logA, Ea, T):
    R = 1.98720425864083e-3
    k = np.exp(logA) * np.exp(-Ea / R / T)
    return k

def trueODEfunc(y, t, k):
    dydt = np.zeros(len(y))
    r1 = k[0] * y[0] * y[1]
    r2 = k[1] * y[2] * y[1]
    r3 = k[2] * y[3] * y[1]
    dydt[0] = -r1
    dydt[1] = -r1 - r2 - r3
    dydt[2] = r1 - r2
    dydt[3] = r2 - r3
    dydt[4] = r3
    dydt[5] = r1 + r2 + r3
    return dydt

def main(output_dir, n_exp, datasize, tstep, noise, ns):
    tspan = [0.0, datasize * tstep]
    tsteps = np.linspace(tspan[0], tspan[1], datasize)

    logA = np.array([18.60, 19.13, 7.93])
    Ea = np.array([14.54, 14.42, 6.47])

    u0_list = np.random.rand(n_exp, ns + 1).astype(np.float32)
    u0_list[:, 0:2] = u0_list[:, 0:2] * 2.0 + 0.2
    u0_list[:, 2:ns] = 0.0
    u0_list[:, ns] = u0_list[:, ns] * 20.0 + 323.0

    ode_data_list = np.zeros((n_exp, ns, datasize), dtype=np.float32)

    for i in range(n_exp):
        u0 = u0_list[i, :]
        k = Arrhenius(logA, Ea, u0[-1])
        ode_data = odeint(trueODEfunc, u0[:-1], tsteps, args=(k,))
        ode_data += np.random.randn(*ode_data.shape) * ode_data * noise
        ode_data_list[i, :, :] = ode_data.T

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(n_exp):
        fig, axs = plt.subplots(ns, 1, figsize=(10, 15))
        for j in range(ns):
            axs[j].plot(tsteps, ode_data_list[i, j, :], label=f"Species {j+1}")
            axs[j].set_xlabel("Time")
            axs[j].set_ylabel("Concentration")
            axs[j].legend()
        plt.suptitle(f"Experiment {i+1}")
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.savefig(os.path.join(output_dir, f"experiment_{i+1}.png"))
        plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and visualize ODE data.")
    parser.add_argument("--output_dir", type=str, default="output", help="Directory to save the plots.")
    parser.add_argument("--n_exp", type=int, default=10, help="Number of experiments to generate.")
    parser.add_argument("--datasize", type=int, default=50, help="Number of data points per experiment.")
    parser.add_argument("--tstep", type=float, default=1, help="Time step between data points.")
    parser.add_argument("--noise", type=float, default=0.05, help="Noise level to add to the data.")
    parser.add_argument("--ns", type=int, default=6, help="Number of species in the reaction.")
    args = parser.parse_args()
    main(args.output_dir, args.n_exp, args.datasize, args.tstep, args.noise, args.ns)
