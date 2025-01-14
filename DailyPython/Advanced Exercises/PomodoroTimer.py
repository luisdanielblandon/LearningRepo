# This app uses the Pomodoro technique to help you stay productive by timing
# work sessions and breaks.
# Each Pomodoro session is 25 minutes of focused work, followed by a 5-minute
# break. The user can start, pause, and reset sessions. After every four
# Pomodoros, a longer break of 15 minutes is added.

#  Required libraries: tkinter, time


import tkinter as tk
from tkinter import messagebox
import time

class PomodoroTimer:
      def __init__(self, master):
            self.master = master
            master.title("Pomodoro Timer")
      
            self.is_running = False
            self.is_paused = False
            self.is_break = False
            self.is_long_break = False
            self.pomodoro_count = 0
      
            self.work_time = 25 * 60
            self.short_break_time = 5 * 60
            self.long_break_time = 15 * 60
      
            self.time_left = self.work_time
      
            self.label = tk.Label(master, text="00:00", font=("Helvetica", 48))
            self.label.pack()
      
            self.start_button = tk.Button(master, text="Start", command=self.start)
            self.start_button.pack()
      
            self.pause_button = tk.Button(master, text="Pause", command=self.pause)
            self.pause_button.pack()
      
            self.reset_button = tk.Button(master, text="Reset", command=self.reset)
            self.reset_button.pack()
      
      def start(self):
            if not self.is_running:
                  self.is_running = True
                  self.update()
                  self.start_button.config(state=tk.DISABLED)
      
      def pause(self):
            if self.is_running:
                  if not self.is_paused:
                      self.is_paused = True
                  else:
                      self.is_paused = False
                  self.update()
      
      def reset(self):
            self.is_running = False
            self.is_paused = False
            self.is_break = False
            self.is_long_break = False
            self.pomodoro_count = 0
            self.time_left = self.work_time
      
            self.label.config(text="00:00")
            self.start_button.config(state=tk.NORMAL)
      
      def update(self):
            if self.is_running and not self.is_paused:
                  if self.time_left > 0:
                        self.time_left -= 1
                        self.update_label()
                        self.label.after(1000, self.update)
                  else:
                        if self.is_break:
                              self.is_break = False
                              self.pomodoro_count += 1
                              if self.pomodoro_count % 4 == 0:
                                    self.is_long_break = True
                                    self.time_left = self.long_break_time
                              else:
                                    self.time_left = self.short_break_time
                        else:
                              self.is_break = True
                              self.time_left = self.work_time
                              
                        self.update_label()
                        self.label.after(1000, self.update)
            else:
                  self.label.after_cancel(self.update)
                  
      def update_label(self):
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            self.label.config(text=f"{minutes:02d}:{seconds:02d}")
            if self.is_break:
                  self.master.config(bg="lightgreen")
            else:
                  self.master.config(bg="white")
            if self.is_long_break:
                  self.master.config(bg="lightblue")
            if self.time_left == 0:
                  messagebox.showinfo("Pomodoro Timer", "Time's up!")
                  
root = tk.Tk()
my_timer = PomodoroTimer(root)
root.mainloop()
      