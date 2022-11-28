from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Hugo Nijdam"
PAGE_ICON = ":wave:"
NAME = "Hugo Nijdam"
DESCRIPTION = """
Hosting Support Specialist, guiding customers on their journey of websites and hosting.
"""
EMAIL = "hnijdam@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/",
    "LinkedIn": "https://nl.linkedin.com/in/hugonijdam",
    "Github": "https://github.com/hnijdam",
    "Twitter": "https://twitter.com/superhuuuug",
}
PROJECTS = {
     "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/sb0A9i6d320",
     "🏆 Webapp portfolio - written in streamlit Python and digital resume": "https://hugonijdam.onrender.com/",
     "🏆 PowerShell CLI domain info tool - made it to make my work a lot easyer": "https://github.com/hnijdam/PowerShell-projects",
     "🏆 Password generator - This PowerShell CLI tool gives 5 random passwords at once": "https://github.com/hnijdam/PowerShell-projects",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFILE PICTURE ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open (resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2, = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" :page_facing_up: Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("📧", EMAIL)

# --- SOCIAL LINKS --- 
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - ✔️ 12 Years experience on IT Customer Service 
    - ✔️ Strong hands on mentality and excellent team player
    - ✔️ Good understanding of webhosting and all kind of IT related subjects
    - ✔️ Also experienced in Sales and Account management 
    """
)

# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
    - 🤖 Programming:  PHP, MySQL, PowerShell, Shell scripting and Python
    - 😏 Hosting Panels: Cpanel, PHPMyAdmin, Plesk
    - 👉 Front end: HTML, CSS, JS
    - 🗄️ Databases: MySQL/MariaDB, Postgres
    - ♊ Microsoft, Linux hybrid worker
    - 🏢 M365 understanding en experience managing platform    
    """
)


# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

#--- JOB 1
st.write("", "**Support Specialist | Yourhosting B.V.**")
st.write("06/2020 - Present")
st.write(
    """
- ➡️ Customer guide, helping customers along the way of their webhosting journey.
- ➡️ Being the guide to induct new colleagues and learning them the basics
- ➡️ Proud member of the staff association, organising events  
"""
)

#--- JOB 2
st.write("🚧", "**Technical Account manager | Total Wall B.V.**")
st.write("02/2019 - 01/2021")
st.write(
    """
- ➡️ Facade inspections to inspect possible defects on corroded wall ties 
- ➡️ Writing architectural reports
- ➡️ Sales and aftersales  
"""
)

#--- JOB 3
st.write("👷", "**Account manager | Premtech B.V.**")
st.write("2018 - 2019")
st.write(
    """
- ➡️ Acquisition New business
- ➡️ Managing exsisting accounts and expanding
- ➡️ Product and application training 
"""
)




# --- Project and Accomplishments ---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")