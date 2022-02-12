import os

log_dir = '/root/mm-tts/logs-mmspeech/'

# unzip the zip files to log directory and delete them thereafter
os.makedirs(log_dir, exist_ok=True)
os.system(f'''
    unzip step-*.zip -d {log_dir}
    unzip events-*.zip -d {log_dir}
    rm step-*.zip
    rm events-*.zip
''')