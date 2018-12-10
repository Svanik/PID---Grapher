# Importing all libraries used for this project
import matplotlib.pyplot as plt
import pandas as pd
import json

# Set plot style
plt.style.use('ggplot')

Variables = json.loads(open('Variables.json').read())

# Create a Pandas dataframe from the 
df = pd.read_csv(Variables['Path'])

# Plot Information
plt.plot(df.index.get_values(),df[Variables["Speed"]])
plt.xlabel("Time")
plt.ylabel("Speed" + "(RPS)")
plt.title(Variables["Object"] + "PID")
plt.axhline(y = max(df[Variables['Setpoint']]), color='b')
plt.show()