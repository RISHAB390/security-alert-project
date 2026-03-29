import time
import os

LOG_FILE = "server_logs.txt"

def monitor_logs():
    print("Security System Active. Monitoring for threats...")
    
    # Open the file and move to the end so we only see NEW logs
    with open(LOG_FILE, "r") as f:
        f.seek(0, os.SEEK_END)
        
        while True:
            line = f.readline()
            if not line:
                time.sleep(1) # Wait for a new line to be written
                continue
            
            # --- DETECTION LOGIC ---
            if "CRITICAL" in line:
                print(f"🚨 ALERT: Severe Threat Detected! -> {line.strip()}")
                log_security_event(line)
            
            elif "WARNING" in line:
                print(f"⚠️ WARNING: Suspicious activity -> {line.strip()}")

def log_security_event(event_details):
    # This fulfills the "Logs security events" requirement
    with open("security_alerts.log", "a") as alert_file:
        alert_file.write(f"ALERT LOGGED: {event_details}")

if __name__ == "__main__":
    # Create the file if it doesn't exist
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, 'w').close()
    monitor_logs()