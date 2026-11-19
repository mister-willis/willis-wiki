const int STEP_PIN = 2;
const int DIR_PIN = 3;
const int HALF_PERIOD_US = 5000;

void moveDial(int count, bool dir) {
  digitalWrite(DIR_PIN, dir);
  delayMicroseconds(5);

  for (int i = 0; i < count * 5; i++) {
    digitalWrite(STEP_PIN, HIGH);
    delayMicroseconds(HALF_PERIOD_US);
    digitalWrite(STEP_PIN, LOW);
    delayMicroseconds(HALF_PERIOD_US);
  }
}

void setup() {
  pinMode(STEP_PIN, OUTPUT);
  pinMode(DIR_PIN, OUTPUT);

  moveDial(40, true);
}

void loop() {
  // put your main code here, to run repeatedly:

}
