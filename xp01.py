drive_duration_sec = 1.2e-07
drive_sigma_sec = 1.5e-08
pi_amp = 0.09299941682393557
drive_sigma = 67

with pulse.build(backend=backend, name=r'$X_{\pi}^{01}$ sched') as pi01:
    drive_duration = get_closest_multiple_of_16(pulse.seconds_to_samples(drive_duration_sec))
    drive_sigma = pulse.seconds_to_samples(drive_sigma_sec)
    drive_chan = pulse.drive_channel(qubit)
    pulse.play(pulse.Gaussian(duration=drive_duration,
                              amp=pi_amp,
                              sigma=drive_sigma,
                              name=r'$X_{\pi}^{01}$'), drive_chan)
                              
pi01.draw()