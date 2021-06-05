import shutil
import sys, os

platform = sys.platform


class HDD():
    """ class for hard disk drives """
    def __init__(self, drive_letter:str):
        """ initializes the HDD class with its basic information, provides class for monitoring and getting all information we need """
        # platform = sys.platform
        # if "win" in platform and not drive_letter.endswith(":{os.path.sep}"):
        #     self.drive = f"{drive_letter}:{os.path.sep}"
        # elif "darwin" in platform and not drive_letter.endswith("{os.path.sep}"):
        #     self.drive = f"{drive_letter}{os.path.sep}"
        # else:
        #     self.drive = drive_letter
        self.drive = drive_letter
        print(f"Disk Letter: {self.drive}")
        hdd_info = shutil.disk_usage(self.drive)
        # sets attributes in gib
        self.size = hdd_info.total // (1<<30)
        self.free = hdd_info.free // (1<<30)
        self.used = hdd_info.used // (1<<30)

    def update_drive_info(self):
        """ updates the free space on drive """
        update_info = shutil.disk_usage(self.drive)
        self.free = hdd_info.free // (1<<30)
        self.used = hdd_info.used // (1<<30)
