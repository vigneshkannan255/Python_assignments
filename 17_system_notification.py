import pynotify
pynotify.init("sample_notification")
notification = pynotify.Notification('Hello world')
notification.set_timeout(2000)
notification.show()
