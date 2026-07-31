# tasks.py

from celery import shared_task
from ftplib import FTP
from .models import Ticket_Uploader, Tickets
from django.core.files.storage import FileSystemStorage

@shared_task
def pp(name):
    print("name")
@shared_task
def upload_file_to_ftp(uploaded_file_path, filename, ticket_id):
    ftp_server = "c351797.parspack.net"
    ftp_user = "N2cgs5rAAERZcSy3"
    ftp_password = "4fJIKS8vRX4a6504J77io7RCk7v2spKr"
    print(1)

    try:
        print("2")
        ftp = FTP(ftp_server)
        ftp.login(user=ftp_user, passwd=ftp_password)
        print("3")
        with open(uploaded_file_path, "rb") as file:
            ftp.storbinary(f"STOR /{filename}", file)

        ftp.quit()
        print(4)
        # ساخت لینک دانلود
        download_link = f"https://dl4.codena.org/{filename}"
        print(download_link)

        fs = FileSystemStorage()

        fs.delete(filename)
        ticket = Tickets.objects.get(id=ticket_id)
        # ذخیره اطلاعات در مدل
        Ticket_Uploader.objects.create(
            file_name=filename,
            file_url=download_link,
            ticket=ticket
        )

        return download_link

    except Exception as e:
        return str(e)
