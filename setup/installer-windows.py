import subprocess
import urllib.request
import os

def install_software(package):
    try:
        if package == 'firefox':
            # Download Firefox installer
            url = 'https://download-installer.cdn.mozilla.net/pub/firefox/releases/141.0/win32/en-US/Firefox%20Setup%20141.0.exe'
            installer_path = 'firefox_installer.exe'
            urllib.request.urlretrieve(url, installer_path)
            # Install Firefox silently
            subprocess.check_call([installer_path, '-ms'])
            # Delete the installer file
            os.remove(installer_path)
        else:
            subprocess.check_call(['pip', 'install', package])
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}")