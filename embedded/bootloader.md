# Bootloader
The bootloader is a program stored in reserved flash memory that can:
- initialize a device,
- update firmware images,
- and possibly perform some integrity checks.

Bootloading a firmware update image can be accomplished in two ways. The first is Over-The-Air (OTA), that is, through the wireless
network for example Bluetooth. The second is through a hardwired link to the device (UART, SPI).

Silicon Labs networking devices use bootloaders that perform firmware updates in two different modes:
- standalone (also called standalone bootloaders) 
- application (also called application bootloaders). 

Application bootloaders are further divided into those that use:
- external storage for the download update image,
- and those that use local storage.

# Standalone
A standalone bootloader is a program that uses an external communication interface, such as UART or SPI, or over the air to get an application image.
Standalone firmware update is a single-stage process that allows the application image to be placed into flash memory, overwriting
the existing application image, without the participation of the application itself. Very little interaction occurs between the standalone
bootloader and the application running in flash. In general, the only time that the application interacts with the bootloader is when it
requests a reboot into the bootloader. Once the bootloader is running, it receives firmware update packets containing the (new) firmware
image either by physical connections such as UART or SPI, or by the radio (over-the-air).
When the firmware update process is initiated, the new code overwrites the existing stack and application code. If any errors occur
during this process, the application cannot be recovered, and the process must start over.

# Application Bootloader
An application bootloader begins the firmware update process after the running application has completely downloaded the update image
file. The application bootloader expects that the image either lives in external memory (EEPROM) accessible by the bootloader or in a portion
of main flash memory (if the chip has sufficient memory to support this local storage model). In any case the region where it is stores is called download space.
The entire image is downloaded before the firmware update process is started.

# Gecko Bootloader
It uses a specially-formatted update image file called a GBL file.
Series 1 device: minimal first stage bootloader used to update the main bootloader
Series 2 deivce: the first stage bootloader is replaced by the Secure Engine and the Gecko bootloader is only the main. 

The Gecko bootloader has 3 components of the bootloader:
- core : main funcitons of the bootloader (funcitonality to write to the internal main flash, perform a bootloader update, reset into the application)
- driver: hardware drivers to use the different component of the bootloader
- component/plugin: All parts of the main bootloader that are either optional or selectable for different configurations are implemented
as components/plugins. Each component/plugin has a generic header file, and one or more implementations. The current release contains components for functionality like UART and SPI communication protocols, SPI flash storage, internal flash storage, and different cryptographic operations.

# Features
Gecko Bootloader features include:
- Field-updateable: field update capability is provided by the SE To perform a main bootloader update, the running main bootloader verifies the integrity and authenticity of the bootloader update image, writes it to internal flash, and requests that the SE installs the update. The SE optionally verifies the authenticity of the main bootloader update image before copying it to the main bootloader location, completing the update.
- Secure boot: Secure boot is designed to prevent an untrusted application from running on the device. When Secure Boot is enabled, the bootloader enforces cryptographic signature verification of the application image on every boot using asymmetric cryptography. The application was created and signed by a trusted party.
- Signed GBL firmware update image file: The Gecko Bootloader supports enforcing cryptographic signature verification of the update image file in addition to Secure Boot. This allows the bootloader and application to verify that the application or bootloader update comes from a trusted source before starting the
update process. The public key is the same key as for secure boot.
- Encrypted GBL firmware update image file: The GBL update file can also be encrypted to prevent the firmware code extraction.


The Gecko bootloader of series 2 devices consists only of the main stage bootloader, which is upgradable via the Secure Engine SE. The Se installs an image at address 0x0in the internal flash

# Bluetooth OTA
This is the firmware upgrade method used in SoC-mode Bluetooth applications. A GBL image containing the new firmware is sent to target device via a Bluetooth connection. The firmware upgrade image can be applied immediately, overwriting the original application, or can be stored to an empty flash area and applied later. In the former case, *AppLoader* must be used, which is a standalone application used for firmware upgrade, while in the latter case, the firmware upgrade must be managed by the user application.
AppLoader is a small standalone application that is required to support in-place OTA updates. AppLoader can run independently of the user application. It contains a minimal version of the Bluetooth stack, including only those features that are necessary to perform the OTA update. Any Bluetooth features that are not necessary to support OTA updates are disabled in AppLoader to minimize the flash
footprint.


## keywords
- Internal Storage Bootloader or In-place OTA DFU Bootloader
