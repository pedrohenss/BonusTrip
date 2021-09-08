import pandas as pd
from twilio.rest import Client

# Your Account SID
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token
auth_token  = "your_auth_token"
client = Client(account_sid, auth_token)

# Excel archives
list_months = ('january', 'february', 'march', 'april', 'may', 'june')

# "for" to create a loop, by running code repeatedly in a list
for month in list_months:
    list_sales = pd.read_excel (f'{month}.xlsx')
    if (list_sales ['Sales'] > 55000).any():
        salesman = list_sales.loc [list_sales ['Sales'] > 55000, 'Salesman'].values [0]
        sales = list_sales.loc [list_sales ['Sales'] > 55000, 'Sales'].values [0]
        # Enter the message that will be sent
        print (f'In {month} the salesman {salesman} reached the target of {sales} and won the bonus!')
        message = client.messages.create(
            # Your phone number
            to="+**********",
            # Twilio phone number
            from_="+**********",
            body=f'In {month} the salesman {salesman} reached the target of {sales} and won the bonus!')
        print(message.sid)