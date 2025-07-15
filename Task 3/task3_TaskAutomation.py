import re

def extract_emails(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()

        # Regular expression to find email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, content)

        if emails:
            with open(output_file, 'w') as file:
                for email in emails:
                    file.write(email + '\n')
            print(f"✅ {len(emails)} email(s) extracted and saved to '{output_file}'")
        else:
            print("⚠️ No email addresses found in the file.")

    except FileNotFoundError:
        print("❌ Input file not found. Please check the file name or path.")

# Example usage
input_filename = "sample_text.txt"
output_filename = "extracted_emails.txt"

extract_emails(input_filename, output_filename)
