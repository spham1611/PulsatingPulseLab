### General pulse instruction ###

with pulse.build(backend=backend) as inst_x_fullpi_12:
    drive_chan = pulse.drive_channel(qubit)
    pulse.play(pulse.Gaussian(duration=drive_duration_12,
                              amp=drive_amplitude_12,
                              sigma=drive_sigma_12), drive_chan)
                              
inst_x_fullpi_12.draw()

### ibmq_manila ###

"""
    The following parameteres were last 
    updated on 14rd September, 2022
    + Qubit: 0
    + Backend: ibmq_manila
"""

# Pulse parameters
drive_duration_01 = 160
drive_sigma_01 = 40
drive_amplitude_01 = 0.17102045531902912

