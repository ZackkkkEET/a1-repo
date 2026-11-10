 LDR Sensor Calibration Report
 Hardware Configuration
 **Sensor Type:** LDR (Photoresistor) in a voltage divider circuit with a 10kΩ fixed resistor.
 **Analog Pin:** GPIO 34 (ESP32 ADC1) with `ADC.ATTN_11DB` attenuation.

 Calibration Anchors
To find stable operating thresholds, multiple raw ADC readings were sampled and averaged ($n = 10$).

 **Dark Anchor (Fully Covered):**
 **Raw ADC Value:** `18500` *(Replace with your actual covered number)*
 **Method:** Covered the LDR completely with a finger in standard ambient room lighting to simulate total darkness.
 **Bright Anchor (Flashlight):**
 **Raw ADC Value:** `52100` *(Replace with your actual flashlight number)*
 **Method:** Shined a smartphone flashlight directly onto the face of the LDR at a ~2 cm distance.

 Calculated Thresholds for Hysteresis
**Turn-ON Threshold (Dark trigger):** `< 20000`
**Turn-OFF Threshold (Bright trigger):** `> 40000`
