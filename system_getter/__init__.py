import sys


if sys.platform in ['linux', 'linux2']:
    from .linux_title_getter import window_title
elif sys.platform in ['Windows', 'win32', 'cygwin']:
    from .windows_title_getter import window_title
else:
    print(f"sys.platform={sys.platform} not supported!")