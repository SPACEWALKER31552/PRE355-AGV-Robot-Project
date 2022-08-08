import board
import busio

print("Hello blinka!")
print(board.SCL)
print(board.SDA)
## try to create i2c device

i2c = busio.I2C(board.SCL, board.SDA)
print("i2c ok")

print("done")
