import syst.tools.threadpool as tp

from traceback import format_exc


THREADS_FOR_HANDLERS_PROCESSING = 10

handlers = []   # [[name, handler, filter]]
threadpool = tp.ThreadPool(THREADS_FOR_HANDLERS_PROCESSING, exit_when_no_events=False)
threadpool.start()


def handler(name=None, _filter=None):
    assert name is not None

    if _filter is None:
        name, _filter = name.__name__, name

    def decorator(func):
        handlers.append((name, func, _filter))

        return func

    return decorator


def add_handler(name, handler_func, _filter):
    handlers.append((name, handler_func, _filter))


def process_update(wrapper, obj, threaded=True, check_all=True):
    for name, func, _filter in handlers:
        if _filter(obj):
            if threaded:
                threadpool.add_event(func, (wrapper, obj))
            else:
                try:
                    func(wrapper, obj)
                except:
                    print(format_exc())

            if not check_all:
                return
