import subprocess
import threading

def run_script(script_name):
    subprocess.run(["python", script_name])

if __name__ == "__main__":
    script1_thread = threading.Thread(target=run_script, args=("photo.py",))
    script2_thread = threading.Thread(target=run_script, args=("input.py",))

    script1_thread.start()
    script2_thread.start()

    script1_thread.join()
    script2_thread.join()

    print("Both scripts have finished executing.")