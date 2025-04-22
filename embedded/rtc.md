# RTC Timer
The RTC timer (Real-Time Clock timer) in the STM32G031KT microcontroller is a low-power timer designed to keep track of real-time information (such as date and time) even when the main system is in a low-power mode or powered off (if supplied by a backup battery).
The RTC timer is a a BCD timer counter, i.e. a Binary-Coded Decimal (BCD) based counter that is used to measure time intervals or count events, where the output is represented in BCD format.

## Key Features of the RTC in STM32G031KT:
1. Time and Date Keeping: Tracks hours, minutes, seconds, day, month, and year with leap year correction.
1. Alarm Function: Programmable alarms to trigger interrupts at specific times.
1. Wake-Up Timer: Can periodically wake up the microcontroller from low-power modes.
1. Backup Domain: Retains the RTC configuration and time when the main power supply is off (if a backup power source is provided).
1. Calibration: Allows fine adjustment of clock accuracy.
1. Low Power Operation: Operates independently of the main clock using its own LSE (Low-Speed External) or LSI (Low-Speed Internal) oscillator.

## How It Works:
1. Clock Source: The RTC uses a separate clock source:
    - LSE: A 32.768 kHz external crystal (better accuracy for real-time applications).
    - LSI: Internal 32 kHz RC oscillator (lower accuracy but no external component required).
1. Backup Domain: The RTC registers and time values are stored in the Backup domain, which remains powered via the VBAT pin when the main supply is off.

## Typical Use Cases:
1. Timekeeping: Maintaining real-time information (time/date). Useful for applications that require accurate time tracking (e.g., data logging, event recording).
1. Alarm Generation: Triggering tasks at specified times (e.g., daily notifications, scheduled tasks). Useful in periodic system wake-ups.
1. Low-Power Wake-Up: Waking the microcontroller from STOP or STANDBY mode to conserve energy. Ideal for battery-powered devices (e.g., smartwatches, sensors).
1. Time stamping: Logging event timestamps. Useful for data acquisition and event monitoring.
1. Watchdog-like Functionality: Using the RTC wake-up timer as a fallback watchdog mechanism.

## Example RTC Workflow (STM32G031KT):
1. Initialize RTC: Configure the RTC peripheral and set the clock source (LSE or LSI).
1. Set Date & Time: Program the RTC registers with the current time.
1. Configure Alarms (Optional): Set up an alarm to trigger at a specific time.
1. Enable Wake-Up (Optional): Program the RTC wake-up timer to periodically wake the microcontroller.
1. Enter Low Power Mode (Optional): Transition the microcontroller to a low-power state.
1. Interrupt Handling: Respond to RTC events using interrupts (e.g., update display on alarm trigger).


## How to setup the wakeup interrupt
The wakeup timer uses a subdivided clock derived from either the LSE, LSI, or RTC clock. Specifically, the CK_SPRE clock (which is 32.768 kHz divided by 16) is often used for accurate timing.

When using:

LSE (Low-Speed External): 32,768 Hz (typical crystal)
LSI (Low-Speed Internal): ~32 kHz (factory-calibrated, less accurate)
RTC Clock Input: Configurable source from RCC

### RTC Wakeup Timer Formula

The RTC wakeup timer is driven by a clock source, typically **LSE (Low-Speed External)**, **LSI (Low-Speed Internal)**, or the **RTC clock** itself. The most common configuration is to use **CK_SPRE** derived from **LSE**, which is divided by **16**.

#### RTC Wakeup Timer Clock Source:

- **LSE (Low-Speed External)**: 32,768 Hz (e.g., crystal oscillator)
- **LSI (Low-Speed Internal)**: ~32 kHz (factory-calibrated)
- **RTC Clock**: Configurable from RCC (e.g., through a PLL)

The RTC wakeup counter counts how many CK_SPRE pulses have occurred. When the counter reaches the value you set, an interrupt is triggered.

Let:

𝑓_RTC  = RTC wakeup clock frequency (e.g., 2,048 Hz for CK_SPRE)
T = Desired wakeup interval in seconds
AutoReload = Value to load into the wakeup counter
Since the counter increments every 
1/𝑓_RTC seconds, and you want the interrupt after T seconds:

𝑇 = (AutoReload + 1)/𝑓_RTC
 
Rearrange to solve for the AutoReload value:

AutoReload = (𝑇×𝑓_RTC)−1

When using **CK_SPRE** (which is the RTC clock divided by 16):

f_RTC = 32,768 / 16 = 2,048 Hz

This means that the RTC clock frequency is **2,048 Hz** (approximately).

#### Formula to Calculate AutoReload Value:

Given:

- T= Desired wakeup interval (in seconds)
- f_RTC = RTC wakeup clock frequency (in Hz)
- AutoReload = Value to load into the wakeup counter

The formula to compute the **AutoReload** value for the wakeup timer is:

AutoReload = (T * f_RTC) - 1


For example, if using **LSE** with **CK_SPRE**:


f_RTC= 2,048 Hz


The formula becomes:

AutoReload= T * 2048 - 1

#### Example Calculation:

To get a wakeup interval of **200 ms** (0.2 seconds):

AutoReload = 0.2 * 2048 - 1 = 409.6 \approx 409

Thus, **AutoReload = 409** for a **200 ms** interval.

---

### Quick Reference Table for Common Intervals:

| **Interval (ms)** | **AutoReload Value** |
|-------------------|----------------------|
| 100 ms            | 204                  |
| 200 ms            | 409                  |
| 500 ms            | 1023                 |
| 1 second          | 2047                 |
| 2 seconds         | 4095                 |
