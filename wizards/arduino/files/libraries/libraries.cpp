#include <Arduino.h>

#if USE_EEPROM
#include "EEPROM.cpp"
#endif

#if USE_ETHERNET
#include "Ethernet.cpp"
#include "EthernetClient.cpp"
#include "EthernetServer.cpp"
#include "EthernetUdp.cpp"
#endif

#if USE_FIRMATA
#include "Firmata.cpp"
#endif

#if USE_LCD
#include "LiquidCrystal.cpp"
#endif

#if USE_LCD4884
#include "LCD4884.cpp"
#endif

#if USE_OBD
#include "OBD.cpp"
#endif

#if USE_SD
#include "SD.cpp"
#include "Sd2Card.cpp"
#include "SdFile.cpp"
#include "SdVolume.cpp"
#include "File.cpp"
#endif

#if USE_SERVO
#include "Servo.cpp"
#endif

#if USE_SOFTSERIAL
#include "SoftwareSerial.cpp"
#endif

#if USE_SPI
#include "SPI.cpp"
#endif

#if USE_STEPPER
#include "stepper.cpp"
#endif

#if USE_TINYGPS
#include "TinyGPS.cpp"
#endif

#if USE_WIRE
#include "Wire.cpp"
#include "twi.c"
#endif

