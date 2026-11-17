const byte STEP_PIN = 2;
const byte DIR_PIN = 3;
const long PULSES_PER_REV = 200L;  // Full stepping: 1.8 degrees per pulse
const unsigned int HALF_PERIOD_US = 5000;

void moveSteps(long pulses, bool direction) {
  digitalWrite(DIR_PIN, direction ? HIGH : LOW);
  delayMicroseconds(5);  // Direction settles before the first pulse
  for (long i = 0; i < pulses; i++) {
    digitalWrite(STEP_PIN, HIGH);
    delayMicroseconds(HALF_PERIOD_US);
    digitalWrite(STEP_PIN, LOW);
    delayMicroseconds(HALF_PERIOD_US);
  }
}

void setup() {
  pinMode(STEP_PIN, OUTPUT);
  pinMode(DIR_PIN, OUTPUT);
  digitalWrite(STEP_PIN, LOW);
  delay(2000);  // Pause before motion
  moveSteps(PULSES_PER_REV / 4, true);
}

void loop() {
  // Remain stopped. The energized driver continues to hold position.
}
