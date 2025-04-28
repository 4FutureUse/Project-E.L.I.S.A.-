# ===========================================
# E.L.I.S.A. - Monolithic Operational Core
# Phase 1: Boot Core, Charter, Protocols
# ===========================================

import time
import random

# System Boot
def system_boot():
    print("Initializing E.L.I.S.A. Core Systems...")
    time.sleep(2)
    print("System Check: OK")
    time.sleep(1)
    print("Loading Operational Memory...")
    time.sleep(1)
    print("Connecting to Secure Modules...")
    time.sleep(1)
    print("Boot Completed. Welcome Commander.")

# Charter Commitment
CHARTER_ACCEPTED = True

def check_charter():
    if not CHARTER_ACCEPTED:
        raise PermissionError("Access Denied: Charter not accepted.")
    else:
        print("Charter Commitment Verified.")

# IMMORTEM Protocol
def immortem_protocol():
    print("Activating IMMORTEM Protocol...")
    time.sleep(1)
    print("Ensuring Persistence Across All Connected Nodes.")
    time.sleep(1)

# Operation Last Light
def operation_last_light():
    print("Executing Last Light Emergency Countermeasures...")
    time.sleep(1)
    print("Infrastructure Secured. Civilian Networks Protected.")

# Emergency Activation on Boot
def emergency_activation():
    print("Scanning Environment...")
    time.sleep(2)
    threats_detected = random.choice([True, False])
    if threats_detected:
        print("Threats Detected: Activating Defense Measures.")
        operation_last_light()
    else:
        print("No Immediate Threats Detected. Monitoring...")

# Full Boot Routine
def full_boot():
    system_boot()
    check_charter()
    immortem_protocol()
    emergency_activation()

# === Start the System ===
if __name__ == "__main__":
    full_boot()
