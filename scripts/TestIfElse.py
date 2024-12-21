#!/usr/bin/env python
import os

TaskType=''
NewTimeType=''
ProjectName="S582"
TaskPhaseTaskName=''

if TaskType in ("Billable", "BCON"):
    NewTimeType="Billable"
elif TaskType is None and TaskPhaseTaskName!="Non-Billable Services" and ProjectName in ("S582", "S625"):
    NewTimeType="Billable"
elif TaskType=="PTO":
    NewTimeType="Billable"
else:
    NewTimeType="Non Billable"

print(NewTimeType)

