# Log-Archive-Tool

https://roadmap.sh/projects/log-archive-tool

Here are the detailed steps to run this program in English:

1. **Save the File**
   - First, save the program code into a file with `.py` extension
   - For example: `log_archive.py`

2. **Give Execution Permission** (For Unix/Linux systems)
```bash
chmod +x log_archive.py
```

3. **How to Run the Program**

There are several ways to run this program:

**Method 1 - Using Python directly:**
```bash
python log_archive.py /path/to/logs
```
or
```bash
python3 log_archive.py /path/to/logs
```

**Method 2 - Run as script** (Unix/Linux):
```bash
./log_archive.py /path/to/logs
```

**Practical Usage Examples:**

1. If logs are in `/var/log` directory:
```bash
python log_archive.py /var/log
```

2. If logs are in current directory:
```bash
python log_archive.py ./logs
```

4. **Expected Results**:
   - Program will create a new directory named `archived_logs`
   - Inside that directory, there will be an archive file with format: `logs_archive_20241028_123456.tar.gz`
   - Log file `archive.log` will be created to record program activities

5. **Common Error Messages**:
   - If directory not found:
     ```
     Error: Directory /path/to/logs does not exist!
     ```
   - If argument is not provided:
     ```
     Usage: log-archive <log-directory>
     ```

6. **Checking Results**:
```bash
# View contents of archived_logs directory
ls -l archived_logs/

# View log file contents
cat archive.log
```

7. **To Extract Archive** (if needed):
```bash
cd archived_logs
tar -xzf logs_archive_20241028_123456.tar.gz
```

Additional Tips:
- Make sure Python 3 is installed on your system
- Ensure you have sufficient permissions to read the log directory and write to the destination directory
- For system directories like `/var/log`, you might need to run with sudo:
  ```bash
  sudo python log_archive.py /var/log
  ```

Key Points to Remember:
1. The program needs a directory path as an argument
2. It will create compressed archives in tar.gz format
3. All activities are logged in archive.log
4. The archive filename includes timestamp for easy tracking
5. Make sure you have enough disk space for the archives

Would you like me to explain any part in more detail?
