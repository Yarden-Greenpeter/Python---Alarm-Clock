import tkinter as tk

class AlarmClockGUI:
    def __init__(self, master):
        self.master = master
        master.title("Alarm Clock")

        # Set window size with 16:9 ratio
        width = 800
        height = 450
        master.geometry(f"{width}x{height}")

        # Center the window on the screen
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_position = (screen_width - width) // 2
        y_position = (screen_height - height) // 2
        master.geometry(f"+{x_position}+{y_position}")

        # Create and configure buttons
        self.my_alarms_button = tk.Button(master, text="My Alarms", command=self.my_alarms_action)
        self.my_alarms_button.pack(pady=20)

        self.new_alarm_button = tk.Button(master, text="New Alarm", command=self.new_alarm_action)
        self.new_alarm_button.pack(pady=20)

        self.settings_button = tk.Button(master, text="Settings", command=self.settings_action)
        self.settings_button.pack(pady=20)

    def my_alarms_action(self):
        print("My Alarms button clicked")

    def new_alarm_action(self):
        print("New Alarm button clicked")

    def settings_action(self):
        print("Settings button clicked")

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClockGUI(root)
    root.mainloop()