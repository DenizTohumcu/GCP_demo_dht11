import DHT11 as dht

if __name__ == '__main__':
    pi = dht.pigpio.pi()
    sensor = dht.DHT11(pi, 26)
    for d in sensor:
        print("temperature: {}".format(d['temperature']))
        print("humidity: {}".format(d['humidity']))
        dht.time.sleep(1)
    sensor.close()