import requests
from bs4 import BeautifulSoup
import customtkinter as ctk
from datetime import datetime, timedelta
from PIL import Image
import os
import sys
import tkinter as tk


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Brandons Course Enroller")
        self.geometry("900x830")
        self.enrollments = []
        self.session = requests.Session()
        self.scheduled_time = None
        self.resizable(False, False)

        self.icon_image = tk.PhotoImage(
            file=resource_path("assets/icon.png")
        )
        self.iconphoto(True, self.icon_image)

        self.footer_frame = ctk.CTkFrame(
            self,
            corner_radius=12,
            border_width=1,
            fg_color=("#f3f4f6", "#1d1f24")
        )
        self.footer_frame.pack(fill="x", side="bottom", padx=12, pady=(0, 10))

        self.scheduled_time_label = ctk.CTkLabel(
            self.footer_frame,
            text="Scheduled time: not set",
            text_color=("#4b5563", "#9ca3af"),
            anchor="w"
        )
        self.scheduled_time_label.pack(side="left", padx=14, pady=10, fill="x", expand=True)

        

        self.countdown_label = ctk.CTkLabel(
            self.footer_frame,
            text="No schedule yet",
            text_color=("#4b5563", "#9ca3af"),
            anchor="e"
        )
        self.countdown_label.pack(side="right", padx=14, pady=10)

        self.show_login()

    def show_login(self):
        self.login_frame = ctk.CTkFrame(self)
        self.login_frame.pack(pady=20, padx=20, fill="both", expand=True)
        

        """ self.header_image = ctk.CTkImage(
            light_image=Image.open("assets/header.png"),
            dark_image=Image.open("assets/header.png"),
            size=(600, 200)
        ) """
        self.background_image = ctk.CTkImage(
            light_image=Image.open(resource_path("assets/background.png")),
            dark_image=Image.open(resource_path("assets/background.png")),
            size=(900, 760)
        )

        self.header_label = ctk.CTkLabel(
            self.login_frame,
            image=self.background_image,
            text=""
        )

        self.header_label.place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )

        self.login_panel = ctk.CTkFrame(
            self.login_frame,
            corner_radius=5,
            width="300",
            fg_color="#1E293B",
        )

        self.login_panel.place(
            relx=0.56,
            rely=0.54,
            anchor="center"
        )

        self.login_lable = ctk.CTkLabel(
            self.login_panel,
            text="Login using your university credentials",
            text_color="#F5F1E8",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.login_lable.pack()
        self.login_panel.pack_propagate(False)

        self.username_entry = ctk.CTkEntry(self.login_panel, placeholder_text="Username")
        self.username_entry.pack(pady=10, padx=20, fill="x")

        self.password_entry = ctk.CTkEntry(self.login_panel, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=10, padx=20, fill="x")
        self.password_entry.bind("<Return>", lambda _: self.login())

        self.login_button = ctk.CTkButton(self.login_panel, text="Login", command=self.login)
        self.login_button.pack(pady=10, padx=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f"Logging in with username: {username} and password: {password}")
        loginUrl = "https://elearning.hs-flensburg.de/index.php"

        r = self.session.get(loginUrl)
        r.raise_for_status()

        soup = BeautifulSoup(r.text, "html.parser")
        securityToken = soup.find("input", {"name": "security_token"})["value"]
        loginTicket = soup.find("input", {"name": "login_ticket"})["value"]

        data = {
            "loginname": username,
            "password": password,
            "security_token": securityToken,
            "login_ticket": loginTicket,
            "resolution": "",
            "Login": ""
        }

        print("Logging in...")
        r = self.session.post(loginUrl, data=data)
        print(r.status_code)
        print(r.url)
        print(self.session.cookies)
        if r.url == "https://elearning.hs-flensburg.de/index.php":
            self.error_label = ctk.CTkLabel(self.login_frame, text="Login failed. Please check your username and password.", text_color="red")  
            self.error_label.pack(pady=10)
            print("Login failed. Please check your username and password.")
        else:
            print("Login successful!")
            self.show_course_enrollment()

    def show_course_enrollment(self):
        if hasattr(self, "login_frame"):
            self.login_frame.destroy()  # Remove the login frame

        self.scroll_frame = ctk.CTkScrollableFrame(self)
        self.scroll_frame.pack(fill="both", expand=True, padx=12, pady=(12, 0))

        

        ctk.CTkLabel(
            self.scroll_frame,
            text="Course Enrollment",
            font=ctk.CTkFont(size=22, weight="bold")
        ).pack(pady=(10, 8), padx=20, anchor="w")

        ctk.CTkLabel(
            self.scroll_frame,
            text="Enter the course URLs you want to enroll in below. You can add multiple course URLs by clicking the '+' button.",
            justify="left",
            wraplength=680
        ).pack(pady=(0, 12), padx=20, anchor="w")

        self.prep_status_label = ctk.CTkLabel(
            self.scroll_frame,
            text="Enrollment preparation not started yet.",
            text_color=("#4b5563", "#9ca3af"),
            anchor="w"
        )
        self.prep_status_label.pack(pady=(0, 10), padx=20, anchor="w")

        self.addButton = ctk.CTkButton(self.scroll_frame, text="+", command=lambda:self.add_entry(), width=30, height=30, corner_radius=15)
        self.addButton.pack(pady=5)

        self.secondPanel = ctk.CTkFrame(
                                    self.scroll_frame,
                                    corner_radius=12,
                                    border_width=1,
                                    fg_color=("#f3f4f6", "#1d1f24"),
                                    height=300
                                )
        self.secondPanel.pack(fill="x", padx=100, pady=(50, 0))
        self.secondPanel.pack_propagate(False)
        
        self.enterTimePanel = ctk.CTkFrame(
                                    self.secondPanel,
                                    corner_radius=12,
                                    border_width=1,
                                    fg_color=("#f3f4f6", "#1d1f24"),
                                    width=500,
                                    height=0
                                )

        self.enterTimePanel.pack_propagate(False)
        self.enterTimePanel.grid_propagate(False)

        self.timeInfoLabel = ctk.CTkLabel(
            self.enterTimePanel,
            text="Enter the time you want to get enrolled (usually the time courses are getting unlocked)",
            font=ctk.CTkFont(size=13),
            text_color=("#4b5563", "#9ca3af")
        )

        self.timeInfoLabel.grid(row=0, column=0, padx=5, columnspan=2, pady=5, sticky="w")
        # Schedule Enrollment Time Inputs   
        self.scheduleHourLabel = ctk.CTkLabel(self.enterTimePanel, text="Hours(0-23):")
        self.scheduleHourLabel.grid(row=1, column=0, padx=(0,35), pady=5, sticky="e")

        self.hour_var = ctk.IntVar(value=0)
        self.scheduleHourEntry = ctk.CTkEntry(self.enterTimePanel, textvariable=self.hour_var)
        self.scheduleHourEntry.grid(row=2, column=0, padx=(10, 0), pady=5, sticky="e")

        self.scheduleMinuteLabel = ctk.CTkLabel(self.enterTimePanel, text="Minutes (0-59):")
        self.scheduleMinuteLabel.grid(row=1, column=1, padx=(35, 0), pady=5, sticky="w")

        self.minute_var = ctk.IntVar(value=0)
        self.scheduleMinuteEntry = ctk.CTkEntry(self.enterTimePanel, textvariable=self.minute_var)
        self.scheduleMinuteEntry.grid(row=2, column=1, padx=0, pady=5, sticky="w")

        self.enrollButton = ctk.CTkButton(self.scroll_frame, text="Apply", command=lambda: self.enroll_courses())
        self.enrollButton.pack(pady=0, after=self.addButton)

        self.scheduleButton = ctk.CTkButton(self.enterTimePanel, text="Schedule enrollment", command=lambda: self.schedule_enrollment(), state="disabled")
        self.scheduleButton.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        self.add_entry()  # Add the first entry field by default

    def schedule_enrollment(self):
        hour = int(self.hour_var.get())
        minute = int(self.minute_var.get())
        print(f"Scheduling enrollment at {hour}:{minute}")

        now = datetime.now()
        self.scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if self.scheduled_time < now:
            self.scheduled_time += timedelta(days=1)

        delay = (self.scheduled_time - now).total_seconds()
        self.scheduled_time_label.configure(
            text=f"Scheduled time: {self.scheduled_time.strftime('%H:%M')}"
        )
        self.countdown_label.configure(text="Waiting for enrollment time...")

        self.update_countdown()
        self.after(int(delay * 1000), self.apply_enrollments)

    def show_results(self, results):
        if hasattr(self, "results_frame") and self.results_frame.winfo_exists():
            self.results_frame.destroy()

        self.results_frame = ctk.CTkFrame(
            self.scroll_frame,
            corner_radius=12,
            border_width=1,
            fg_color=("#f8fafc", "#1f2937")
        )
        self.results_frame.pack(fill="x", padx=20, pady=(10, 20))

        ctk.CTkLabel(
            self.results_frame,
            text="Enrollment Results",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=16, pady=(14, 8))

        for result in results:
            status_color = "#16a34a" if result["status"] == "Success" else "#dc2626"
            row = ctk.CTkFrame(self.results_frame, fg_color=("white", "#111827"), corner_radius=8)
            row.pack(fill="x", padx=12, pady=(0, 8))

            ctk.CTkLabel(row, text=result["status"], text_color=status_color, width=10, anchor="w").pack(side="left", padx=(12, 10), pady=8)
            ctk.CTkLabel(row, text=f"{result['type']}: {result['module']}", anchor="w", justify="left").pack(side="left", fill="x", expand=True, padx=(0, 12), pady=8)

        self.prep_status_label.configure(
            text="Enrollment preparation completed. The enrollment process is ready.",
            text_color="green"
        )

    def update_countdown(self):
        if self.scheduled_time is None:
            self.countdown_label.configure(text="No schedule yet")
            return

        remaining = self.scheduled_time - datetime.now()

        if remaining.total_seconds() <= 0:
            self.countdown_label.configure(text="Enrollment is running...")
            return

        total_seconds = int(remaining.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        self.countdown_label.configure(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        self.after(100, self.update_countdown)


    entries = []
    entry_labels = {}

    def add_entry(self):
        entry = ctk.CTkEntry(
            self.scroll_frame,
            placeholder_text="Enter course URL"
        )
        entry.pack(
            pady=0,
            before=self.addButton,
            fill="x",
            padx=20,
        )

        label = ctk.CTkLabel(
            self.scroll_frame,
            text="",
            font=ctk.CTkFont(size=11),
            text_color=("#6b7280", "#9ca3af"),
            height=15,
            anchor="w"
        )
        label.pack(
            before=self.addButton,
            fill="x",
            padx=20,
            pady=0
        )

        self.entries.append(entry)
        self.entry_labels[entry] = label

    def set_entry_label(self, entry, text, text_color=None):
        label = self.entry_labels.get(entry)
        if label is None:
            return
        label.configure(text=text, text_color=text_color or ("#6b7280", "#9ca3af"))

    def animate_panel_close(self, target, height):
        if height <= 0:
            target.pack_forget()
            return

        target.configure(height=height)

        self.after(
            10,
            lambda: self.animate_panel_close(target, height - 10)
        )

    def animate_panel_open(self,target, height, target_height):

        if height >= target_height:
            target.configure(height=target_height)
            return

        target.configure(height=height)

        self.after(
            10,
            lambda: self.animate_panel_open(target, height + 15, target_height)
        )

    def showPanel(self, target, target_height):
        target.pack(expand=True)
        self.animate_panel_open(target, 0, target_height)

    def print_entries(self):
        for entry in self.entries:
            print(entry.get())


    def show_labor_courses(self, articleNames):
        self.labor_page = ctk.CTkToplevel(self)
        self.labor_page.title("Labor Courses")
        self.labor_page.geometry("400x400")
        self.labor_page.grab_set()  # Make the labor page modal

        selected = ctk.IntVar(value=-1)  # Variable to hold the selected index

        def select_labor_course(self, index):
            selected.set(index)
            self.labor_page.destroy()  # Close the labor page


        for i, name in enumerate(articleNames):
            button = ctk.CTkButton(
                self.labor_page,
                text=name,
                command=lambda i=i: select_labor_course(self, i)
            )
            button.pack(pady=5, padx=20, fill="x")

        self.labor_page.wait_window()  # Wait for the labor page to be closed before continuing
        return selected.get()  # Return the selected index



    def enroll_courses(self):
        # Add unfilled entries to the courseUrls list
        courseUrls = [entry.get() for entry in self.entries if entry.get()]
        print(f"Enrolling in courses: {courseUrls}")
        # Here you would add the code to enroll in the courses using the courseUrls list
        self.labors = []
        self.courses = []

        for entry in self.entries:
            courseUrl = entry.get().strip()
            if not courseUrl:
                self.set_entry_label(entry, "")
                continue

            r = self.session.get(courseUrl)
            r.raise_for_status()
            soup = BeautifulSoup(r.text, "html.parser")

            if courseUrl.find("statusgroups") != -1:
                section = soup.find("section", class_="contentbox course-statusgroups")
                self.articles = section.find_all("article", recursive=False)
                print(f"Found {len(self.articles)} labor courses in {courseUrl}")
                articleNames = [article.find("h1").text.strip() for article in self.articles if article.find("h1")]
                laborChoice = self.show_labor_courses(articleNames)

                labor = {"url": courseUrl}
                labor["laborId"] = self.articles[int(laborChoice)]["id"]
                labor["courseName"] = soup.find("title").text.strip()
                labor["courseId"] = courseUrl.split("?cid=")[1]
                labor["enrollmentUrl"] = f"https://elearning.hs-flensburg.de/dispatch.php/course/statusgroups/join/{labor['laborId']}?cid={labor['courseId']}"
                self.labors.append(labor)
                self.set_entry_label(entry, labor["courseName"])
                print(f"Enrolling in labor course {articleNames[laborChoice]} | ({labor['laborId']}) for course {labor['courseId']}...")
            else:
                securityToken = soup.find("input", {"name": "security_token"})["value"]
                course = {"url": courseUrl}
                if courseUrl.find("details/index/") != -1:
                    course["courseId"] = courseUrl.split("/details/index/")[1]
                elif courseUrl.find("details?sem_id=") != -1:
                    course["courseId"] = courseUrl.split("?cid=")[1]
                else:
                    self.set_entry_label(entry, "Invalid URL", text_color="red")
                    error_label = ctk.CTkLabel(self.scroll_frame, text=f"Invalid course URL: {courseUrl}", text_color="red")
                    error_label.pack(pady=10)
                    print(f"Invalid course URL: {courseUrl}")
                    continue
                course["courseName"] = soup.find("title").text.strip()
                course["securityToken"] = securityToken
                enrollment_link = soup.find("a", {"data-dialog": "size=big"})
                if enrollment_link is None:
                    raise ValueError(f"No enrollment link found for course {courseUrl}")
                course["enrollmentUrl"] = f"{enrollment_link.get('href')}?apply=1"
                self.courses.append(course)
                self.set_entry_label(entry, course["courseName"])
                print(f"Enrolling in course {course['courseId']} with security token {course['securityToken']}...")
        self.showPanel(self.enterTimePanel, 200)
        self.scheduleButton.configure(state="normal")
        self.prep_status_label.configure(
            text="Enrollment preparation completed. The enrollment is ready to start.",
            text_color="green"
        )


    def apply_enrollments(self):
        results = []
        for course in self.courses:
            r = self.session.post(course["enrollmentUrl"], 
                                  data={
                                      "security_token": course["securityToken"],
                                      "apply": "1",
                                      "yes": ""
                                      })
            
            r.raise_for_status()
            if r.status_code == 200:
                results.append({"module": course["courseName"], 
                                "status": "Success",
                                "type": "Course",
                                "url": course["url"]})
            else:
                results.append({"module": course["courseName"], 
                                "status": "Failed",
                                "type": "Course",
                                "url": course["url"]})
            print(f"Enrolled in course {course['courseName']}.")

        for labor in self.labors:
            r = self.session.get(labor["enrollmentUrl"])
            r.raise_for_status()
            if r.status_code == 200:
                results.append({"module": labor["courseName"], 
                                "status": "Success",
                                "type": "Labor Course",
                                "url": labor["url"]})
            else:
                results.append({"module": labor["courseName"], 
                                "status": "Failed",
                                "type": "Labor Course",
                                "url": labor["url"]})
            print(f"Enrolled in labor course {labor['laborId']} for course {labor['courseName']}.")

        self.show_results(results)

        

    



""" 

############ Login ##############



############ Course Enrollment ##############




"""
app = App()
app.mainloop() 