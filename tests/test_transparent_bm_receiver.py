from loraspi.LoRaTransparent import LoRaTransparentBM
from time import sleep


if __name__ == '__main__':
    relay = LoRaTransparentBM()
    try:
        relay.start()
        sleep(1)
        while True:
            relay.send_message(b"hellowo")
            sleep(1)
    except KeyboardInterrupt:
        relay.stop()
        relay.join()
