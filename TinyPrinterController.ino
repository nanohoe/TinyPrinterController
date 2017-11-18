const int switchPin = 0;
const int statusPin = A1;

const int onPin = 3;
const int donePin = 4;

unsigned long lastloop = 0;
unsigned long lastprint = 0;

byte printstatus = 0;

void setup() {
  pinMode(statusPin, INPUT);
  pinMode(switchPin, INPUT);
  pinMode(onPin, INPUT);
  pinMode(donePin, INPUT);
}

int getStatus() {
  int value = 0;
  for (int i = 1; i<=10; i++) {
    value = value + analogRead(statusPin);
    delay(2);
  }
  value = value / 10;
  return value;
}
void buttonPress(byte Pin) {
  pinMode(Pin, OUTPUT);
  digitalWrite(Pin, HIGH);
  delay(200);
  pinMode(Pin, INPUT);
}

void loop() {
  unsigned long currenttime = millis();
  int s = getStatus();
  if (digitalRead(onPin) == HIGH) {
    lastprint = currenttime;
    if (s < 30) {
      buttonPress(switchPin);
    }
  } else {
    if (currenttime - lastprint > 3*60*1000) {
      // it's been 3 minutes
      if (s > 40) {
        // printer is on
        buttonPress(switchPin);
      }
    }
  }
  if (currenttime < lastloop) {
    // millis() counter has reached overflow
  }
  lastloop = currenttime;
  delay(100);
}
