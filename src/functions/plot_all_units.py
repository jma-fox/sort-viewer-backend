import streamlit as st
import spikeinterface.full as si
import matplotlib.pyplot as plt


def plot_all_units(sort_data):
    sorting = sort_data["sorting"]
    trial_frame = sort_data["trial_frame"]

    with st.expander("All Units", expanded=True):
        fig, ax = plt.subplots()
        si.plot_rasters(sorting, ax=ax, time_range=trial_frame)
        ax.set_ylabel('Unit')
        ax.set_xlabel('Time (s)')
        st.pyplot(fig)
        plt.close(fig)
