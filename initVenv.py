# pylint: disable=invalid-name
import platform
import os
import shutil
import subprocess
import sys


if __name__ == '__main__':
    # Install virtual environment
    venvPath = os.path.normpath(os.path.join(__file__, '..', '.venv'))
    if os.path.isdir(venvPath):
        shutil.rmtree(venvPath)
    venvCall = [sys.executable, '-m', 'venv', venvPath]
    subprocess.check_call(venvCall)

    # Update pip
    if platform.system() == 'Windows':
        pythonExe = os.path.join(venvPath, 'Scripts', 'python.exe')
        pipExe = os.path.join(venvPath, 'Scripts', 'pip.exe')
        pipSyncExe = os.path.join(venvPath, 'Scripts', 'pip-sync.exe')
    else:
        pythonExe = os.path.join(venvPath, 'bin', 'python')
        pipExe = os.path.join(venvPath, 'bin', 'pip')
        pipSyncExe = os.path.join(venvPath, 'bin', 'pip-sync')

    updatePipCommand = [pythonExe, '-m', 'pip', 'install', '--upgrade', 'pip>=21.3.1']
    subprocess.check_call(updatePipCommand)

    # Update pip-tools
    installPipToolsCmd = [pipExe, 'install', 'pip-tools>=6.4.0']
    subprocess.check_call(installPipToolsCmd)

    # Install dependencies
    reqTxt = os.path.normpath(os.path.join(__file__, '..', 'requirements.txt'))
    pipToolsSyncCmd = [pipSyncExe, reqTxt]
    subprocess.check_call(pipToolsSyncCmd)
