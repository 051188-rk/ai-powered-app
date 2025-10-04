import time
def stream_to_text(generator):
    buf = ''
    for chunk in generator:
        buf += chunk
        yield buf
        time.sleep(0.01)
