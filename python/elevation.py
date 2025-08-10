# UAC elevation check (windows only- no effect on linux (including bad effects))
# place at top of script if entire script requires administrative privelages
# (e.g., installing packages, updates, modifying files in protected directories)

import pyuac

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Script reqires UAC Elevation. Relaunching with UAC prompt...")
        pyuac.runAsAdmin()
    else: 
        print("Scipt is running with UAC elevation.")