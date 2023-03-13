@echo off
cd C:\Users\LENOVO\Desktop\DeepSort_2\yolov7
python detect_or_track.py --weights best50eps.pt --source "pigtest.mp4" --view-img --track --classes 1 2
pause