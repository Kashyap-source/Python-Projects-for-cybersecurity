# keylogger

Keyloggers are programs that capture your key strokes.
They can be used to keep logs of everything you press on the keyboard but on the 
flip side it can be used for malicious purposes as well.

The keylogger that I've made is a basic keylogger with not much functionality as the ones available in market today.
It captures your keystrokes and saves them in a file "keylogger.txt".

It then sends the contents of the file(i.e. the keystrokes) to your email id.

With some extra lines of code, it can also send the keystrokes at regular intervals.
But that is a project for another time.

I have not made it executable so one has to explicitely call it.

SYNTAX : python keylogger.py

[NOTE: You need to press esc key to exit out the keylogger.]

You need to have pynput , smtplib and ssl installed.

While python comes with the library smtplib and ssl preinstalled.

You can install pynput with :

     pip install pynput

**What is Pynput?**

The pynput library allows you to control and monitor/listen to your input devices such as they keyboard and mouse. The pynput. mouse allows you control and monitor the mouse, while the pynput. keyboard allows you to control and monitor the keyboard.

**What is Smtplib?**

The smtplib module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon. ... An SMTP instance encapsulates an SMTP connection. It has methods that support a full repertoire of SMTP and ESMTP operations.

**What SSL means?**

Secure Sockets Layer
SSL stands for Secure Sockets Layer and, in short, it's the standard technology for keeping an internet connection secure and safeguarding any sensitive data that is being sent between two systems, preventing criminals from reading and modifying any information transferred, including potential personal details.
