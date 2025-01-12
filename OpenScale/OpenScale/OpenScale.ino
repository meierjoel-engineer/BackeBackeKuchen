#include "Adafruit_HX711.h"
#include <Wire.h> //Needed to talk to on board TMP102 temp sensor

// Define the pins for the HX711 communication
const uint8_t DATA_PIN = 2;  // Can use any pins!
const uint8_t CLOCK_PIN = 3; // Can use any pins!
Adafruit_HX711 hx711(DATA_PIN, CLOCK_PIN);

float getLocalTemperature()
{
  Wire.requestFrom(0x49, 2);
  byte MSB = Wire.read();
  byte LSB = Wire.read();
  //It's a 12bit int, using two's compliment for negative
  int TemperatureSum = ((MSB << 8) | LSB) >> 4;
  float celsius = TemperatureSum * 0.0625;
  return celsius;
}

void setup() {
  Serial.begin(115200);
  hx711.begin();
  Wire.begin();
}

void loop() {
  int32_t weightB32 = hx711.readChannelBlocking(CHAN_A_GAIN_128);
  float localTemperature = getLocalTemperature();

  Serial.println(String(weightB32) + "," + String(localTemperature));
}
