import datetime, threading, smtplib
import patient_data

def schedule_email(user):
    when_to_send_email = datetime.timedelta(minutes=user.appointment_time) \
                            - datetime.timedelta(minutes=user.travel_time)
    delta_seconds = when_to_send_email.total_seconds()
    t = threading.Timer(delta_seconds, send_email, [user])
    t.start()
    return (user, t)

def send_email(user):
    sender = 'hackkosice2019cakaren@gmail.com'
    receivers = [user.email]

    message = """From: Totally Awesome Project <hackkosice2019cakaren@gmail.com>
    To: Totally Awesome Person <{}>
    Hey, you! You have an appointment at {}th minute of this day! Get yo' ass here.
    """.format(user.email, user.appointment_time)

    print(message)

    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpObj.login("hackkosice2019cakaren", "hackkosice")
    smtpObj.sendmail(sender, receivers, message)         
    smtpObj.quit()
    print("Email sent to " + user.email)

if __name__ == "__main__":
    ja = patient_data.PatientData(123, 'matej.genci@gmail.com', 1600, 30)
    ty = patient_data.PatientData(321, 'sara.kutkova@gmail.com', 1200, 24)
    send_email(ja)
    send_email(ty)