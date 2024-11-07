# NOMA Semantic Communication Simulation in LTspice

This repository contains an LTspice simulation file for a semantic communication-based multi-task processing system over a Non-Orthogonal Multiple Access (NOMA) wireless channel. This setup demonstrates the superposition of signals from multiple tasks and includes noise modeling to simulate realistic transmission conditions.

## Project Structure
- **CU Encoder**: Common Unit encoder source shared by all tasks.
- **SU Encoders**: Specific Unit encoders for each task:
  - **Binary Classification (Task 1)**: Represented by a 0.5V signal.
  - **Categorical Classification (Task 2)**: Represented by a 1.5V signal.
- **AWGN Channel**: Gaussian noise source representing channel noise.
- **Transmission Line**: Simulates the shared wireless channel for NOMA.

## Components and Configuration
- **CU Encoder**: Voltage source with a 1V amplitude and 1kHz frequency.
- **Binary Task (SU1)**: 0.5V amplitude, 2kHz frequency.
- **Categorical Task (SU2)**: 1.5V amplitude, 3kHz frequency.
- **AWGN Noise**: Random voltage source with mean 0 and standard deviation 0.05V.
- **Low-Pass Filters**: Each SU signal is passed through an RC filter to isolate it at the receiver.

## Simulation Setup
1. Run a **Transient Analysis** to visualize time-domain behavior.
2. Use **Fourier Analysis** to evaluate spectral efficiency.
3. To assess Bit Error Rate (BER), export data to MATLAB or Python.

## How to Use
1. Download the `.asc` file and open it in LTspice.
2. Run simulations using **Transient Analysis** or **Fourier Analysis** as described.
3. Adjust component values as needed to explore different signal strengths or noise levels.

## Notes
This simulation is a conceptual model and may require adjustments for specific real-world scenarios.
