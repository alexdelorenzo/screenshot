try:
    from Quartz import CGWindowListCopyWindowInfo, kCGWindowListExcludeDesktopElements, kCGNullWindowID, kCGWindowNumber, \
                       kCGWindowName, kCGWindowOwnerName, kCGWindowListOptionAll, kCGWindowListOptionOnScreenOnly, \
                       kCGWindowListOptionOnScreenAboveWindow, kCGWindowListOptionOnScreenBelowWindow, \
                       kCGWindowListOptionIncludingWindow

except ImportError as ex:
    raise ImportError("Please install pyobjc-framework-Quartz via pip.") from ex


options = {'all_windows': kCGWindowListOptionAll,
           'on_screen_only': kCGWindowListOptionOnScreenOnly,
           'above_window': kCGWindowListOptionOnScreenAboveWindow,
           'below_window': kCGWindowListOptionOnScreenBelowWindow,
           'include_window': kCGWindowListOptionIncludingWindow,
           'exclude_desktop': kCGWindowListExcludeDesktopElements}

user_options_str = 'exclude_desktop on_screen_only'

summer = lambda *opts: sum(options[opt] for opt in opts if opt in options)
user_options = summer(*user_options_str.split())


def get_window_info(options: int=user_options, relative_to: bool=kCGNullWindowID) -> list:
    return CGWindowListCopyWindowInfo(options, relative_to)


def gen_ids_from_info(windows: iter) -> iter:
    for win_dict in windows:
        owner = win_dict.get('kCGWindowOwnerName', '')
        name = win_dict.get('kCGWindowName', '')
        num = win_dict.get('kCGWindowNumber', '')

        yield num, owner, name


def print_window_ids(windows: iter):
    for info in windows:
        print(*info)


def gen_window_ids(parent: str, title: str='', *args, options=str) -> iter:
    options = summer(*options.split(' '))
    windows = get_window_info(options)
    parent, title = parent.lower(), title.lower()

    for num, owner, name in gen_ids_from_info(windows):
        if parent in owner.lower():
            if title:
                if title in name.lower():
                    yield num
            else:
                yield num