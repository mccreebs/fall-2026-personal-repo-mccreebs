clc
clear all;

s = serialport('COM7', 19200, "Timeout", 15);

plateLoaderMenuControl(s);




