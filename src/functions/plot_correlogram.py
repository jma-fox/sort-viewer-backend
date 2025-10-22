import matplotlib.pyplot as plt
import spikeinterface.full as si
import streamlit as st


def plot_correlogram(sort_data):
    analysis = sort_data["analysis"]
    unit = sort_data["unit"]

    fig, ax = plt.subplots()
    si.plot_autocorrelograms(analysis, unit_ids=[unit], ax=ax)
    ax.set_title("")

    with st.expander("Autocorrelogram", expanded=True):
        st.pyplot(fig)
        plt.close(fig)

    return sort_data
