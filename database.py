import sqlite3
import os

# ================= DATABASE PATH =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "atmiya.db")

# ================= CONNECT DATABASE =================
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# ================= CREATE USERS TABLE =================
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    password TEXT
)
""")

# ================= CREATE ENQUIRIES TABLE =================
cursor.execute("""
CREATE TABLE IF NOT EXISTS enquiries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT UNIQUE,
    answer TEXT
)
""")

# ================= CLEAR OLD ENQUIRIES =================
cursor.execute("DELETE FROM enquiries")

# ================= INSERT ENQUIRY DATA =================
data = [
    (
        "admission",
        "Admissions are open for undergraduate and postgraduate programs such as B.Tech, MBA, MCA, B.Sc, BCA, BBA, B.Com and more at Atmiya University, Rajkot."
    ),
    (
        "courses",
        "Atmiya University offers programs in Engineering, Management, Computer Applications, Science, Arts and Commerce including B.Tech, MBA, MCA, B.Sc, BCA, BBA and B.Com."
    ),
    (
        "fees",
        "Approximate fee structure at Atmiya University (Rajkot): B.Tech ~₹85,000 per year (total ~₹3.3 L for 4 years), B.Sc ~₹55,000–58,000 per year, BCA ~₹58,000–84,000 per year, BBA ~₹50,000–1,00,000 per year, B.Com ~₹1.17–2.83 L total. Fees may vary by specialization and academic year."
    ),
    (
        "hostel",
        "Hostel facilities are available for both boys and girls at Atmiya University. Approximate hostel fees are ₹72,000–₹80,000 per year. Mess charges are separate and may vary. Hostel fees are not included in academic fees."
    ),
    (
        "contact",
        "You can contact Atmiya University via email at info@atmiyauni.ac.in or visit the official website for more details."
    ),
    (
        "location",
        "Atmiya University is located at Yogidham Gurukul, Kalawad Road, Maruti Nagar, Nana Mava, Rajkot – 360005, Gujarat, India."
    ),
    (
        "admission_btech",
        "Admissions are open for B.Tech (Engineering) at Atmiya University, Rajkot. The program duration is 4 years."
    ),
    (
        "admission_mba",
        "Admissions are open for MBA (Master of Business Administration) at Atmiya University, Rajkot. The program duration is 2 years."
    ),
    (
        "admission_mca",
        "Admissions are open for MCA (Master of Computer Applications) at Atmiya University, Rajkot. The program duration is 2 years."
    ),
    (
        "admission_bsc",
        "Admissions are open for B.Sc (Science) programs at Atmiya University, Rajkot. The program duration is 3 years."
    ),
    (
        "admission_bca",
        "Admissions are open for BCA (Bachelor of Computer Applications) at Atmiya University, Rajkot. The program duration is 3 years."
    ),
    (
        "admission_bba",
        "Admissions are open for BBA (Bachelor of Business Administration) at Atmiya University, Rajkot. The program duration is 3 years."
    ),
    (
        "admission_bcom",
        "Admissions are open for B.Com (Commerce) programs at Atmiya University, Rajkot. The program duration is 3 years."
    ),
    (
        "campus_facility",
        "Atmiya University campus in Rajkot offers modern facilities including well-equipped classrooms, laboratories, library, computer labs, Wi-Fi, sports grounds, auditorium, seminar halls, hostel for boys and girls, cafeteria, and medical facilities."
    ),
    (
        "hostel_facility",
        "Atmiya University provides separate hostel facilities for boys and girls. Hostel rooms are well-furnished with basic amenities. Approximate hostel fees are ₹72,000–₹80,000 per year, with mess charges being separate. Security and 24/7 support are available for students."
    ),
    (
        "contact_general",
        "Atmiya University contact details: Phone: +91-0281-2563445. Email: admin@atmiyauni.ac.in. Website: https://atmiyauni.ac.in. Address: Yogidham Gurukul, Kalawad Road, Maruti Nagar, Nana Mava, Rajkot – 360005, Gujarat, India."
    ),
    (
        "about_university",
        "Atmiya University was established in 2018 under the Gujarat Private University Act. It focuses on holistic education, human values, and skill development through academic and practical learning."
    ),
    (
        "admission_process",
        "Admissions are conducted through the Admission Core Committee as per Gujarat government guidelines, such as ACPC for Engineering, MBA, MCA and Pharmacy programs, ensuring a transparent counseling and selection process. Eligibility criteria depend on course-specific requirements."
    ),
    (
        "placement_overview",
        "Atmiya University has a Training & Placement Cell that supports students with career development, soft skill workshops, resume building, and placement drives."
    ),
    (
        "placements_data",
        "Median salary: UG 3-year ₹2.50 LPA, UG 4-year ₹3.60 LPA, PG ₹2.40 LPA. Highest packages exceed ₹9 LPA."
    ),
    (
        "tp_cell_details",
        "The Training & Placement Cell conducts career guidance, internships, workshops, and mock interviews."
    ),
    (
        "academic_practice",
        "The university emphasizes experiential and practical learning through internships, fieldwork, industry visits, and projects."
    ),
    (
        "startup_initiatives",
        "Atmiya University promotes entrepreneurship through startup events, mentoring, and incubation support."
    ),
    (
        "scholarships_overview",
        "Atmiya University offers merit-based, need-based, and government scholarships with application guidance."
    )
]

cursor.executemany(
    "INSERT INTO enquiries (question, answer) VALUES (?, ?)",
    data
)

# ================= COMMIT & CLOSE =================
conn.commit()
conn.close()

print("✅ atmiya.db created/updated successfully with FULL data.")
