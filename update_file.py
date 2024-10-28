import os
import json
import shutil

with open("config.json") as f:
    file_paths = json.load(f)['file_paths']

resume_path = "resume.pdf"
cv_path = "detailed_cv.pdf"

resume_name = "aman_singh_resume.pdf"
cv_name = "aman_singh_cv.pdf"

if __name__ == "__main__":
    """ Using this script to copy resume to other parts of my computer when I push changed to resume, using git hooks """
    for fp in file_paths:
        shutil.copyfile(resume_path, os.path.join(fp, resume_name))
        shutil.copyfile(cv_path, os.path.join(fp, cv_name))
