from functions.plot_amplitude import plot_amplitude
from functions.plot_correlogram import plot_correlogram
from functions.plot_waveform import plot_waveform


def plot_unit_quality(sort_data):
    sort_data = plot_waveform(sort_data)
    sort_data = plot_correlogram(sort_data)
    sort_data = plot_amplitude(sort_data)
