# [SPI vs I2C](https://www.arrow.com/en/research-and-events/articles/spi-vs-i2c-protocols-pros-and-cons)

## I2C Advantages

Users may prefer the I2C protocol for specific applications for two main reasons.

1. **Simplicity**. The most apparent difference between I2C and SPI is that I2C works as a 2-wire bus, needing only serial data (SDA) and serial clock (SCK) lines for data transmission and synchronization. SPI, on the other hand, requires four wires to control a single slave: SCK, master out slave in (MOSI), master in slave out (MISO), and slave select (SS).

2. **Easy add-ons**. When users need more than one slave device, SPI implements an additional SS pin for each one. When an I2C system needs to implement new slave devices, they can simply “clip on” to the existing bus using a 7-bit addressing system to identify each module. This I2C scheme requires a proper address configuration but avoids the burden of extra wiring for each device.

## SPI Advantages
While I2C’s wiring simplicity and standardization are significant advantages, SPI has some attractive features as well.

1. **Communication**. Separate MISO/MOSI data lines mean that it’s capable of full-duplex communication, as opposed to *I2C’s half-duplex operation*, meaning that data send and receive transmissions must alternate.

2. **Speed**. I2C originally defined data transfer rates at 100kbps, though we have seen it bump up to 400kbps or even up to 5Mbps in Ultra Fast-mode. SPI, however, does not define a top—or any—communications speed, and can be implemented at speeds of 10 Mbps or more.