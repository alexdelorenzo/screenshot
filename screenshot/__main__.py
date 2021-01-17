from detect import mac, linux, windows


if mac:
  from .mac.capture import run

else:
  raise Exception("Your operating system isn't supported by screenshot.")


if __name__ == "__main__":
  run()
