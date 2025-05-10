import subprocess

def main():
    # Fork a child process (equivalent to creating a subprocess in Python)
    print("Parent process executing...")
    try:
        # Execute 'ls -l' command in the child process
        subprocess.run(["ls", "-l"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        exit(1)  # Exit the process with failure status
    else:e
        print("Child process completed")
        exit(0)  # Exit the process with success status

if __name__ == "__main__":
    main()
