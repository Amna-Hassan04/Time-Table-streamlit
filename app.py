import streamlit as st
import pandas as pd

# Title
st.title("Student Day Timetable Planner")

# Input: Number of tasks for the day
num_tasks = st.number_input("Enter the number of tasks/classes/activities for the day", min_value=1, step=1)

# Input: Add each task's name, start time, and end time
tasks = []
for i in range(num_tasks):
    st.subheader(f"Task {i+1}")
    task_name = st.text_input(f"Task {i+1} Name", key=f"task_{i}_name")
    start_time = st.time_input(f"Start Time for Task {i+1}", key=f"start_time_{i}")
    end_time = st.time_input(f"End Time for Task {i+1}", key=f"end_time_{i}")
    
    if task_name and start_time and end_time:
        tasks.append({"Task": task_name, "Start Time": start_time, "End Time": end_time})

# Display Timetable
if tasks:
    st.subheader("Your Timetable for the Day")
    df = pd.DataFrame(tasks)
    st.dataframe(df)

    # Option to download timetable as CSV
    csv = df.to_csv(index=False)
    st.download_button("Download Timetable as CSV", data=csv, file_name='timetable.csv', mime='text/csv')

# Additional info
st.info("Plan your day efficiently! Ensure to allocate sufficient breaks between tasks.")
