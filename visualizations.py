"""
# -- ------------------------------------------------------------------------------------------------------------------------ -- #   
# -- project: MonteCarlo-Simulations                                                                                             -- #           
# -- script: visualizations.py : Python script with visualizations functionalities                                            -- #                 
# -- author: EstebanMqz                                                                                                       -- #  
# -- license: CC BY 3.0                                                                                                       -- #
# -- repository: https://github.com/EstebanMqz/MonteCarlo-Simulations/blob/main/visualizations.py                                -- #           
# -- ------------------------------------------------------------------------------------------------------------------------ -- #  
"""

from os import path
#Dependencies
import functions as fn
import data as dt
import main
#Libraries in vs
import pandas as pd
import matplotlib.pyplot as plt


def MC_plot(simulations, E_V, xlabel , ylabel, i_capital, f_capital, N):
    """Plots a line plot of events for n Monte Carlo simulations.
    Parameters
    ----------
    simulation : pandas.DataFrame
        Dataframe of Monte Carlo simulations.
    E_V : pandas.DataFrame
        The expected value of the simulation.
    xlabel : str
        The label of the x-axis.
    ylabel : str
        The label of the y-axis.
    i_capital : int
        The initial value of the variable to be simulated.
    f_capital : int
        The final value of the variable simulated.
    N : int
        Events simulated.
    Returns
    -------
    line_plot : matplotlib.pyplot
        Plot of events time-series for N MonteCarlo simulations.
    """

    #If ROI is negative make the color red, otherwise green.
    ROI = round((E_V.iloc[-1][0] / E_V.iloc[0][0]) - 1, 6)
    color = ["red" if ROI < 0 else "green"][0]

    #Style.
    plt.style.use('dark_background')
    plt.rc('grid', linestyle="--", color='gray')
    plt.rc('ytick', labelsize=13, color='lightgreen')
    plt.rc('xtick', labelsize=13, color = color)
    
    #Line subplots in a figure.
    fig, ax = plt.subplots(figsize = (18, 10))
    #Simulations. 
    simulations.plot(ax = ax, xlabel = xlabel, ylabel = ylabel, title = ("Expected Value of Capital over time in " + str(N) + 
                    " Monte Carlo simulations went from " + str(i_capital)+ " to: "  + str(f_capital)), linewidth = 0.15).legend().remove()
    
    #capital_lines, negative line & win/loss for simulations. 
    plt.axhline(y = i_capital, color = "white", linewidth = .8)
    plt.axhline(y = f_capital, color = color, linewidth = .8)
    plt.axhline(y = 0, color = color, linewidth = .4, linestyle = "--")
    plt.axhspan(i_capital, f_capital, facecolor = color, alpha = 0.2)
    #Expected Values.
    E_V.plot(ax = ax, color = color, linewidth = 1)
    #ROI.
    plt.text(0.5, 0.5, "Expected ROI ≈ " + str(ROI), fontsize=13, color=color, transform=ax.transAxes, position = (0.8, 0.65))

    #Style.
    plt.grid(True)
    plt.grid(which='both', color='gray', linestyle='--', alpha = 0.8)
    #x-y ticks.
    ax.xaxis.label.set_size(15), ax.yaxis.label.set_size(15)
    plt.xticks(range(0, 100, 5), [str(i) for i in range(0, 100, 5)])
    plt.yticks(range(0, int(round(simulations.max().max(), 0)), 5), [str(i) + "$" for i in range(0, int(round(simulations.max().max(), 0)), 5)])
    
    return plt.show()

def hist_plot(simulation, xlabel , ylabel, n_games, n, i_capital, color):
    """Plots a hist plot of the final capital in Monte Carlo simulations.
    Parameters
    ----------
    coin_simulation : pandas.DataFrame
        The capital of the player at each coin toss.
    xlabel : str
        The label of the x-axis.
    ylabel : str
        The label of the y-axis.
    n_games : int
        The number of games played.
    n : int
        The number of simulations of n games planned to play.
    i_capital : int
        The initial capital of the player.
    f_capital : int
        The final capital of the player.
    Returns
    -------
    line_plot : matplotlib.pyplot
        The line plot of the capital over time in n Monte Carlo simulations.
    """

    plt.title("Final capital after planned " + str(n_games) + " games with starting capital of " + str(i_capital)
          + " calculated with " + str(n) + " planned played games simulations (Monte Carlo")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    #Hist plot
    plt.hist(simulation, bins = 20, color = color, width = 5, edgecolor='black', density=True)[2]
    plt.gcf().set_size_inches(12, 8)

    return plt.show()
