import datetime, threading, smtplib
import patient_data
from hkqueue import HkQueue

def schedule_email(user):
    if not (user.email_timer is None):
        print("Cancelling sending of email for " + user.email)
        user.email_timer.cancel()

    time_now = datetime.datetime.now()
    minute_of_day = time_now.hour * 60 + time_now.minute
    when_to_send_email = user.appointment_time - minute_of_day + user.travel_time
    t = threading.Timer(when_to_send_email * 60, send_email, [user])
    t.start()

    print("Scheduling to send an email in " + str(when_to_send_email) + "mins - "
            + str(datetime.datetime.now() + datetime.timedelta(minutes=when_to_send_email)))
    user.email_timer = t


def send_email(user):
    sender = 'hackkosice2019cakaren@gmail.com'
    receivers = [user.email]

    message = "From: Totally Awesome Project <hackkosice2019cakaren@gmail.com>\n" + \
    "To: Totally Awesome Person <{}>\n".format(user.email) + \
    "Subject: Appointment with your doctor\n\n" + \
    "Hey, you! You have an appointment at {}th minute of this day! Get yo' ass here.\n".format(user.appointment_time)

    print(message)

    try:
        smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtpObj.login("hackkosice2019cakaren", "hackkosice")
        smtpObj.sendmail(sender, receivers, message)         
        smtpObj.quit()
        print("Email sent to " + user.email)
    except:
        print("Sending email to " + user.email + " failed")

if __name__ == "__main__":
    ja = patient_data.PatientData(123, 'matej.genci@gmail.com', 1600, 30)
    ty = patient_data.PatientData(321, 'sara.kutkova@gmail.com', 1200, 24)
    send_email(ja)
    send_email(ty)