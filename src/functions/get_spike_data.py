import spikeinterface.full as si
import pandas as pd


def get_unit_spikes(unit_data):
    sorting = unit_data["sorting"]
    analysis = unit_data["analysis"]
    unit = unit_data["unit"]

    sampling_frequency = sorting.get_sampling_frequency()
    template_channels = si.get_template_extremum_channel(analysis)

    spike_samples = sorting.get_unit_spike_train(unit)
    channel = template_channels[unit]

    unit_spikes = []
    for spike_sample in spike_samples:
        spike_time = spike_sample / sampling_frequency
        unit_spikes.append({'spike_times': spike_time, 'units': unit, 'channels': channel})

    unit_spikes = pd.DataFrame(unit_spikes)

    return unit_spikes

def get_spike_data(sort_data):
    sorting = sort_data['sorting']
    channel = sort_data["channel"]
    unit = sort_data["unit"]

    sampling_frequency = sorting.get_sampling_frequency()
    spike_samples = sorting.get_unit_spike_train(unit)

    unit_spikes = []
    for spike_sample in spike_samples:
        spike_time = spike_sample / sampling_frequency
        unit_spikes.append({'spike_times': spike_time, 'units': unit, 'channels': channel})

    unit_spikes = pd.DataFrame(unit_spikes)

    return unit_spikes
