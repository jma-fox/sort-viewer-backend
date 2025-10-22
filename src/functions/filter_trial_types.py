

def filter_trial_types(task_data):
    task_data = task_data[task_data["Outcome"].isin(["Correct", "Miss"])]
    rf_x = task_data["RfPosX"].iloc[0]
    rf_y = task_data["RfPosY"].iloc[0]
    task_data = task_data[(task_data["TargPosX"] == rf_x) & (task_data["TargPosY"] == rf_y)]

    return task_data
