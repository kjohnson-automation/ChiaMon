import shutil
import sys, os

import matplotlib.pyplot as plt

platform = sys.platform


class HDD():
    """ class for hard disk drives """
    def __init__(self, drive_letter:str):
        """ initializes the HDD class with its basic information, provides
        class for monitoring and getting all information we need """
        # Assumes the drive later is in the proper syntax based on OS for now
        self.drive = drive_letter
        print(f"Disk Letter: {self.drive}")
        hdd_info = shutil.disk_usage(self.drive)
        # sets attributes in gib 1 << 30 uses bitmanipulation to divide it by
        # 2^30
        self.size = hdd_info.total // (1<<30)
        self.free = hdd_info.free // (1<<30)
        self.used = hdd_info.used // (1<<30)

    def update_drive_info(self):
        """ updates the free space on drive """
        update_info = shutil.disk_usage(self.drive)
        self.free = update_info.free // (1<<30)
        self.used = update_info.used // (1<<30)

    def drive_plot(self):
        """ creates plot info for current drive usage """
        self.update_drive_info()
        labels = ["Free Space", "Used"]
        # Odd behavior on the mac where used shows up at 14GiB when it should
        # be roughly 198, trying a different attempt
        #sizes = [(self.free/self.size) * 100, (self.used/self.size) * 100]
        used = self.size - self.free
        sizes = [(self.free/self.size)*100, (used/self.size)*100]
        explode = (0, 0.1)
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct="%1.1f%%",
                shadow=True, startangle=90)
        ax1.axis("equal")
        # plt.show(block=False)

