import matplotlib.pyplot as plt
import spikeinterface.full as si
import streamlit as st


def plot_amplitude(sort_data):
    analysis = sort_data["analysis"]
    unit = sort_data["unit"]

    fig, ax = plt.subplots()
    si.plot_amplitudes(analysis, unit_ids=[unit], ax=ax, plot_legend=False)

    with st.expander("Amplitude", expanded=True):
        st.pyplot(fig)
        plt.close(fig)

    return sort_data
