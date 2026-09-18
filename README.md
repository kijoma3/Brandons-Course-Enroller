<img width="2048" height="768" alt="Brandons Course Enroller" src="https://github.com/user-attachments/assets/c9a8e4c4-9b0b-4d5d-9f83-dc4b22ced5a3" />

# Brandons Course Enroller

A desktop application for **automated and scheduled course enrollment in Stud.IP**, developed and tested for **Flensburg University of Applied Sciences (Hochschule Flensburg)**.

Instead of manually waiting for course registration to open, you can prepare multiple course and laboratory-group enrollments in advance and schedule them for a specific time.

> [!NOTE]
> This application was developed specifically for the Stud.IP instance used by Hochschule Flensburg.
> Compatibility with other Stud.IP installations is not guaranteed.

## Features

- Schedule course enrollments for a specific time
- Prepare multiple course enrollments at once
- Select laboratory groups before registration opens
- Automatic Stud.IP login and session handling
- Enrollment status feedback
- Graphical user interface
- Linux and Windows support
- No separate Python installation required when using the prebuilt releases

---

## How to use it

### 1. Log in

Log in using your university credentials.

<kbd>
  <img width="804" height="518" alt="Login screen" src="https://github.com/user-attachments/assets/d7551df6-eb75-4d34-aeab-d9bcdb952b13" />
</kbd>

<br><br>

### 2. Add your courses

Enter the URLs of the courses you want to enroll in.

For a normal course, use the URL of its **overview page**.

If you want to enroll in a specific laboratory group, use the URL of the corresponding **group overview page** instead.

<kbd>
  <img width="857" height="689" alt="Course URL input" src="https://github.com/user-attachments/assets/f07352e9-90d8-4df5-877c-9eebd6999df3" />
</kbd>

<br><br>

**Example: Course overview page**

<kbd>
  <img width="1920" height="628" alt="Stud.IP course overview page" src="https://github.com/user-attachments/assets/52f96abd-fcf7-4a19-bc42-c0f052be557e" />
</kbd>

<br>

<sub>Overview page of a course</sub>

<br><br>

**Example: Laboratory group overview**

<kbd>
  <img width="1439" height="559" alt="Stud.IP laboratory group overview" src="https://github.com/user-attachments/assets/e403f3b0-9c45-49ed-b612-eec649e55981" />
</kbd>

<br>

<sub>Overview page of a laboratory group</sub>

<br><br>

### 3. Prepare the enrollment

Press **Apply** to prepare your enrollments.

If one of the provided URLs contains multiple laboratory groups, the application will ask you which group you want to join.

<kbd>
  <img width="760" height="469" alt="Laboratory group selection" src="https://github.com/user-attachments/assets/29483433-c6c9-4638-8a2c-c5d7f8901c99" />
</kbd>

<br><br>

### 4. Select the enrollment time

Use the hour and minute input fields to specify when the enrollment requests should be sent.

<kbd>
  <img width="826" height="443" alt="Enrollment time selection" src="https://github.com/user-attachments/assets/88c22d81-7cc2-46b3-a04a-80275c606297" />
</kbd>

<br><br>

### 5. Schedule the enrollment

Press **Schedule enrollment** to start the timer.

The application will display the selected enrollment time and a countdown.

<kbd>
  <img width="826" height="443" alt="Schedule enrollment screen" src="https://github.com/user-attachments/assets/924543d0-6351-4c2b-91e6-e3bc7905792a" />
</kbd>

<br><br>

<kbd>
  <img width="884" height="164" alt="Enrollment countdown" src="https://github.com/user-attachments/assets/118fe04c-fff6-4184-b27f-14d82fcb9e5a" />
</kbd>

<br><br>

### 6. Check the results

When the countdown reaches zero, the application sends the prepared enrollment requests.

A feedback panel will then display the status of each enrollment.

<kbd>
  <img width="837" height="246" alt="Enrollment feedback panel" src="https://github.com/user-attachments/assets/0b7f6712-4042-4bc6-8d38-273c87773ecc" />
</kbd>

<br>

<sub>Enrollment feedback panel</sub>

<br><br>

<kbd>
  <img width="551" height="180" alt="Successfully enrolled course" src="https://github.com/user-attachments/assets/c205052b-45a9-4590-be11-10c7079414f0" />
</kbd>

<br>

<sub>Successfully enrolled course</sub>

<br><br>

<kbd>
  <img width="1134" height="62" alt="Successfully enrolled laboratory group" src="https://github.com/user-attachments/assets/96dfc023-5847-4c8e-a612-1def1748149a" />
</kbd>

<br>

<sub>Successfully enrolled laboratory group</sub>

---

## Installation

Prebuilt versions are available for Linux and Windows.

### Linux

Download the latest `.deb` package.

Install it using:

```bash
sudo apt install ./course-enroller.deb
```

After installation, launch **Brandons Course Enroller** from your application menu or run:

```bash
course-enroller
```

### Windows

Download the latest Windows executable:

```text
course-enroller.exe
```

No installation or separate Python installation is required. Simply launch the executable.

> [!TIP]
> Prebuilt versions should preferably be downloaded from the
> [Releases](../../releases) section of this repository.

---

## Build from source

If you prefer to run the application directly from source, clone the repository:

```bash
git clone https://github.com/kijoma3/Brandons-Course-Enroller.git
cd Brandons-Course-Enroller
```

Create a virtual environment:

### Linux

```bash
python3 -m venv .env
source .env/bin/activate
```

### Windows

```powershell
py -m venv .env
.env\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python main.py
```

---

## Technologies

The application is written in Python and uses:

- **CustomTkinter** for the graphical user interface
- **Requests** for HTTP communication and session handling
- **Beautiful Soup** for parsing Stud.IP pages
- **Pillow** for image handling
- **PyInstaller** for standalone application builds

---

## Privacy & Security

This application requires your university credentials in order to authenticate with Stud.IP.

Your credentials are used exclusively to authenticate your session with the university's Stud.IP system. The application does not intentionally transmit your credentials to the developer or to third-party servers.

> [!IMPORTANT]
> Before using the application with real university credentials, you are encouraged to review the source code yourself. Never enter your credentials into a modified or untrusted build of this application.

---

## Limitations

- The application was developed and tested using the **Stud.IP installation of Hochschule Flensburg**.
- Other universities may use different Stud.IP versions, configurations or enrollment procedures.
- Compatibility with other Stud.IP installations is therefore not guaranteed.
- Successful enrollment cannot be guaranteed. Availability, server load, network conditions and changes to Stud.IP may affect enrollment.
- Changes to the Hochschule Flensburg Stud.IP system may require updates to this application.

---

## Disclaimer

This project is an independent student project and is **not affiliated with, endorsed by, or officially supported by Hochschule Flensburg or Stud.IP**.

Use this application at your own responsibility and make sure that automated enrollment does not violate the rules or terms applicable to your university's systems.

---

## License

No license has been specified yet.
