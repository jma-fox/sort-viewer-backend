import matplotlib.pyplot as plt
import spikeinterface.full as si
import streamlit as st


def plot_waveform(sort_data):
    analysis = sort_data["analysis"]
    unit = sort_data["unit"]
    channel = sort_data["channel"]

    fig, ax = plt.subplots()
    si.plot_unit_waveforms(
        analysis, 
        unit_ids=[unit],
        channel_ids=[channel],
        ax=ax, 
        plot_legend=False, 
        same_axis=True
    )

    ax.set_title("")

    with st.expander("Waveform", expanded=True):
        st.pyplot(fig)
        plt.close(fig)

    return sort_data
