from resume_reader import extract_text_from_pdf
from job_reader import read_job_description
from matcher import match_resume

def main():
    print("Resume Analyzer & Job Matcher\n")

    #Get resume path
    resume_path = input("Enter FULL path to your resume (PDF): ").strip()

    try:
        resume_text = extract_text_from_pdf(resume_path)
        if not resume_text:
            print("Could not extract text from resume.")
            return
    except Exception as e:
        print("Error reading resume:", e)
        return

    #Job input choice
    choice = input("\nEnter job description manually? (yes/no): ").strip().lower()

    if choice == "yes":
        print("\nPaste Job Description (press Enter twice to finish):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        job_text = " ".join(lines)
    else:
        job_path = input("Enter FULL path to job.txt: ").strip()
        job_text = read_job_description(job_path)

        if not job_text:
            print("Could not read job description.")
            return

    score, matched, missing = match_resume(resume_text, job_text)

    
    print("\nRESULT")
    print(f"\nMatch Score: {score:.2f}%")

    print("\nMatched Keywords:")
    print(", ".join(matched) if matched else "None")

    print("\nMissing Keywords:")
    print(", ".join(missing) if missing else "None")


if __name__ == "__main__":
    main()