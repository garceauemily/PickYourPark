# Pick Your Park: A Parking Lot Utilization Monitoring System
#### Greg Andrews, Jack Bjelland, John Broughton, Emily Garceau, Chandler Todd, Mason Young

![From left to right: Chandler, Jack, John, Emily, Greg, Mason](https://github.com/garceauemily/PickYourPark/blob/main/posternight.jpg)

## Directory Overview
### client

This directory contains the scripts and modules that are loaded on the Raspberry Pi. Everything is written in Python.

### server

This directory contains scripts and modules that are run on a host laptop, as well as the database file. These scripts use the Django Python framework, Chartjs, and the SQLite3 database.

## Abstract

Parking at Clemson University is notoriously difficult for students, even those with valid parking passes. Driving around and searching for a spot often leads commuters to be late for class, however, this problem could be mitigated by providing students with information on parking lot availability before they start driving to campus. This project designs and implements a small-scale parking lot utilization monitoring system that can be applied on a larger scale to work on Clemson’s campus. This system uses FSRs embedded inside speed bumps as the primary detection system for cars entering and exiting a given parking lot. When an FSR detects the weight of a vehicle, it triggers an RFID scanner to check whether the vehicle has a valid parking pass. The collected data is processed by a Raspberry Pi that wirelessly transmits the information to a central server hosted on a laptop. The server accepts incoming connections and stores the received data in a database table. This data is displayed on an online dashboard that updates the number of available parking spaces in a given parking lot in real time. This dashboard allows commuters to eliminate time wasted driving around looking for an available parking space.

A special thank you to Dr. Hasan Raza and the Holcombe Department of Electrical and Computer Engineering at Clemson University.
