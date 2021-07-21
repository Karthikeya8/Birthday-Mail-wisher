import pandas
import datetime as dt
from random import choice
import smtplib
letter_templates_list = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
birthday_person = pandas.read_csv("birthdays.csv")
birthday_person = birthday_person.to_dict(orient='records')
now = dt.datetime.now()
birthday_month = now.month
birthday = now.day
for value in birthday_person:
    if value['month'] == birthday_month and value['day'] == birthday:
        chosen_letter = choice(letter_templates_list)
        with open(f"letter_templates/{chosen_letter}") as file:
            start_letter = file.read()
            start_letter = start_letter.replace("[NAME]", value['name'])
            start_letter = start_letter.replace("Angela", 'Karthikeya_Mad')
        my_email = 'ur-@gmail.com'
        password = 'ur-pass'
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=value['email'], msg='Subject:Happy Birthday!'
                                                                                               f'\n\n {start_letter}')




