import streamlit as st
import spikeinterface.full  as si
import pandas as pd

from functions.filter_trial_types import filter_trial_types
from functions.get_trial_frames import get_trial_frames
from functions.get_spike_data import get_spike_data
from functions.plot_all_units import plot_all_units
from functions.plot_unit_quality import plot_unit_quality


def streamlit_app():
    st.set_page_config(page_title="Sort Viewer")
    st.title("Sort Viewer")

    if 'sort_data' not in st.session_state:
        st.session_state['sort_data'] = None

    task_file_path = st.text_input("Enter path to task file:", "")
    sorting_path = st.text_input("Enter path to sorting:", "")

    st.write("")

    event_name = st.text_input("Event Name:", value='gabors_on_time')
    frame_start = float(st.text_input("Frame Start (s):", value='-0.5'))
    frame_end = float(st.text_input("Frame End (s):", value='1.0'))

    st.write("")

    if st.button("Load Sort Data"):
        sorting = si.load(sorting_path)
        unit_ids = sorting.get_unit_ids()
        task_data = pd.read_csv(task_file_path)
        task_data = filter_trial_types(task_data)
        time_range = (frame_start, frame_end)
        trial_frames = get_trial_frames(task_data, time_range, event_name)

        sort_data = {
            "sorting_path": sorting_path,
            "sorting": sorting,
            "task_data": task_data,
            "unit_ids": unit_ids,
            "trial_frames": trial_frames
        }

        st.session_state['sort_data'] = sort_data

    st.write("")

    sort_data = st.session_state.get('sort_data', None)

    if sort_data is not None:
        task_data = sort_data['task_data']
        trial_frames = sort_data['trial_frames']
        unit_ids = sort_data['unit_ids']

        trial_num = st.slider("Trial Frame:", 1, len(trial_frames), 1)
        trial_frame = trial_frames[trial_num - 1]

        sort_data.update({"trial_frame": trial_frame})

        plot_all_units(sort_data)

        analysis_path = st.text_input("Enter path to analysis:", "")

        if analysis_path:
            analysis = si.load(analysis_path)
            unit = st.selectbox("Select Unit:", unit_ids)
            template_channels = si.get_template_extremum_channel(analysis)
            channel = template_channels[unit]

            sort_data.update({
                "analysis": analysis,
                "unit": unit,
                "channel": channel
            })

            plot_unit_quality(sort_data)

            spike_data = get_spike_data(sort_data)
            file_name = f"unit_{unit}_spikes.csv"

            st.download_button(
                label="Download Unit",
                data=spike_data.to_csv(index=False).encode('utf-8'),
                file_name=file_name,
                mime='text/csv'
            )


if __name__ == "__main__":
    streamlit_app()
