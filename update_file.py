import os
import shutil

file_paths = [
    "C:\\Users\\itsam\\OneDrive\\Documents\\resume",
    "C:\\Users\\itsam\\iCloud Drive\\iCloudDrive\\Documents\\resumes\\pdfs",
]
resume_path = "resume.pdf"

file_name = "aman_singh_resume.pdf"

if __name__ == "__main__":

    for fp in file_paths:
        shutil.copyfile(resume_path, os.path.join(fp, file_name))
