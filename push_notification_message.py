import firebase_admin
from firebase_admin import credentials, messaging, get_app


def initialize_firebase_app():
    firebase_cred = credentials.Certificate('path_to_yourproject_firebase_adminsdk.json')
    firebase_app = firebase_admin.initialize_app(firebase_cred)
    return firebase_app

def send_token_push(title, body, tokens, app_name='default'):
    firebase_app = firebase_admin.get_app(name=app_name)
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        tokens=tokens
    )
    response = messaging.send_each_for_multicast(message)
    print(response)
    if response.failure_count > 0:
        print(f'Failed to send push notification to some devices: {response.errors}')
    else:
        print('Push notification sent successfully to all devices.')

def send_push_notification(title,message_body,tokens):
    try:
        try:
            firebase_app = get_app()
            app_name = firebase_app.name
            print("APP NAME :         ",app_name)
        except:
            firebase_app = initialize_firebase_app()
            app_name = firebase_app.name
            print(app_name)

        send_token_push(title, message_body, tokens, app_name)

    except Exception as e:
        print(e)

title = 'Dr Joseph'
message_body = "test message"
tokens = ['e6BUg8V3StixZyoueFrRfS:APA91bEux-g55tfq7qxTKeC-gK_PqjpuTjH-s7mI6piNG2E3_X_Qty6XRbzhJ-3NMHWniyRB81EfKrz50u_W9nsklrJa0mQqC9hJRrV33zErGnFWJI3Kywow8i7bPneIgxJWiBoewg8d']

send_push_notification(title,message_body,tokens)
