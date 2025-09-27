import sqlite3
import re
from email.message import EmailMessage
from email.parser import BytesParser

NEW_MESSAGE_RE = re.compile(b"^From ", re.MULTILINE)


def parse_mbox_and_store_db(mbox_file, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY,
            subject TEXT,
            body TEXT
        )
    ''')

    with open(mbox_file, 'rb') as f:
        message_starts = [m.start() for m in re.finditer(NEW_MESSAGE_RE, f.read())]
        message_starts.append(f.tell())
        f.seek(0)

        total_emails = len(message_starts) - 1
        print(f"Found {total_emails} emails to process.")

        for i in range(total_emails):
            start_pos = message_starts[i]
            end_pos = message_starts[i + 1]

            f.seek(start_pos)
            message_bytes = f.read(end_pos - start_pos)

            msg = BytesParser().parsebytes(message_bytes)

            subject = msg.get('subject', '')
            body = ''
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == 'text/plain':
                        body = part.get_payload(decode=True).decode('utf-8', 'ignore')
                        break
            else:
                body = msg.get_payload(decode=True).decode('utf-8', 'ignore')

            cursor.execute("INSERT INTO emails (subject, body) VALUES (?, ?)", (subject, body))

            # --- Progress Tracking Added Here ---
            if (i + 1) % 100 == 0:  # Print a message every 100 emails
                conn.commit()  # Commit changes periodically
                print(f"Processed {i + 1} of {total_emails} emails...")

    conn.commit()  # Final commit
    conn.close()
    print("Parsing and database storage complete.")


parse_mbox_and_store_db('allmail.mbox', 'emails.db')