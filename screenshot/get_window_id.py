from typing import Iterable, List, Dict, AnyStr, Union, Iterator, Tuple

try:
    from Quartz import CGWindowListCopyWindowInfo, kCGWindowListExcludeDesktopElements, kCGNullWindowID, \
        kCGWindowNumber, kCGWindowName, kCGWindowOwnerName, kCGWindowListOptionAll, kCGWindowListOptionOnScreenOnly, \
        kCGWindowListOptionOnScreenAboveWindow, kCGWindowListOptionOnScreenBelowWindow, \
        kCGWindowListOptionIncludingWindow

except ImportError as ex:
    raise ImportError("Please install pyobjc-framework-Quartz via pip and then try again.") from ex


WindowInfo = Dict[AnyStr, Union[AnyStr, int]]

WINDOW_OPTIONS = {'all_windows': kCGWindowListOptionAll,
                  'on_screen_only': kCGWindowListOptionOnScreenOnly,
                  'above_window': kCGWindowListOptionOnScreenAboveWindow,
                  'below_window': kCGWindowListOptionOnScreenBelowWindow,
                  'include_window': kCGWindowListOptionIncludingWindow,
                  'exclude_desktop': kCGWindowListExcludeDesktopElements}

USER_OPTS_STR = 'exclude_desktop on_screen_only'


def build_option_bitmask(*opts: Iterable[str]) -> int:
    return sum(WINDOW_OPTIONS[opt] for opt in opts if opt in WINDOW_OPTIONS)


USER_OPTIONS = build_option_bitmask(*USER_OPTS_STR.split(' '))


def get_window_info(options: int = USER_OPTIONS,
                    relative_to: int = kCGNullWindowID) -> List[WindowInfo]:
    return CGWindowListCopyWindowInfo(options, relative_to)


def gen_ids_from_info(windows: Iterable[WindowInfo]) -> Iterator[Tuple[int, str, str]]:
    for win_dict in windows:
        owner = win_dict.get('kCGWindowOwnerName', '')
        name = win_dict.get('kCGWindowName', '')
        num = win_dict.get('kCGWindowNumber', '')

        yield num, owner, name


def print_window_ids(windows):
    for info in windows:
        print(*info)


def gen_window_ids(parent: str, title: str = '', options: str = USER_OPTS_STR,
                   relative_to: bool = kCGNullWindowID) -> Iterator[int]:
    options = build_option_bitmask(*options.split(' '))
    windows = get_window_info(options, relative_to)
    parent, title = parent.lower(), title.lower()

    for num, owner, name in gen_ids_from_info(windows):
        if parent in owner.lower():
            if title:
                if title in name.lower():
                    yield num
            else:
                yield num
