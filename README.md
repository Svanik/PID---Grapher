# **PID Grapher**
___
##### By: Svanik Dani

This is a simple PID Grapher made for FRC Team 5895.

#### Json File-Explained
___
The Json file titled Variables.json is used for assigning variables that will be used in the graphing Script.

The items that need to be changed are labeled CHANGE THIS:
- Setpoint is the name of the column in the CSV file referring to the setpoint.
- Speed is the name of the column in the CSV file referring to the current speed of the object.
- Object is the object being tracked. IE: Flywheel, Motor, etc.
- Path is the path to the CSV file. If the python script and the CSV file are in the same folder you can simply put "filename.csv" into the path. Otherwise, you need the full path to the file.

#### Usage of the PID.exe
After you set the JSON Variables simply click on the PID.exe to produce the graph. The graph will include a line for the setpoint and another line for the Time vs Speed. The setpoint line will be in blue and the PID line in red.