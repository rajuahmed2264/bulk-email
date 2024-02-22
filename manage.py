import os
from get_data_from_base import get_data_from_base_f
from send_email import send_email_f
from update_base import upload_invoic_to_base

def manage():
    base_id = 'NKmUbtpsDa2xK3svXGcuOquRsTd'
    tbl_id = 'tblfT8vZXbWdZvq6'
    data_from_base = get_data_from_base_f(base_id, tbl_id)
    for record in data_from_base:
        record_id = record['record_id']
        send_status = record['fields']['email_send_status']

        rec_email = ''
        try:
            try:
                rec_email = record['fields']['email']['text']
                if rec_email == '':
                    rec_email = record['fields']['email']
            except:
                rec_email = record['fields']['email']
                if rec_email == '':
                    
                    rec_email = record['fields']['email']['text']
                

        except:
            rec_email = ''

        try:
  
            restaurant_name = record['fields']['Restaurant Name']

        except:
            restaurant_name = ''
        with open('email.html', 'r') as body:
        
            email_body = body.read()



        if rec_email == None:
            rec_email = ''
        if send_status == None:
            send_status = False


        
        if rec_email != '' and send_status == False:
            email_body = email_body.replace('[record_id]', record_id)
            email_body = email_body.replace('[email]', rec_email)
            email_body = email_body.replace('[tbl_id]', tbl_id)
            email_body = email_body.replace('[base_id]', base_id)
            email_body = email_body.replace('[restaurant_name]', restaurant_name)

            email_data = {
                'subject': "Cut Your UberEats Commission Fees by Thousands!",
                "receipt_email": rec_email,
                'body': email_body
            }


            success = send_email_f(email_data)

            if success:
                print("Email sent successfully.")
            else:
                print("Failed to send email.")

            
            upload_invoic_to_base(record_id=record_id, base_id = base_id, tbl_id= tbl_id)






