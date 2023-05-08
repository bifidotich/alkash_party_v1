cd /d %~dp0
call venv\Scripts\activate.bat 
pip install PyInstaller
call pyinstaller --onefile --hidden-import=pytorch --collect-data torch --copy-metadata torch --copy-metadata tqdm --copy-metadata regex --copy-metadata requests --copy-metadata tokenizers --copy-metadata packaging --copy-metadata filelock --copy-metadata numpy main.py
cmd.exe