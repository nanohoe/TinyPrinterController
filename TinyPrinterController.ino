const int switchPin = 0;
const int statusPin = A1;

const int onPin = 3;
const int donePin = 4;

const int togglePin = 3;
const int feedbackPin = 4;

unsigned long lasttoggle = 0;

unsigned long lastloop = 0;
unsigned long lastprint = 0;

byte printstatus = 0;

void setup() {
  pinMode(statusPin, INPUT);
  pinMode(switchPin, INPUT);
  pinMode(togglePin, INPUT);
  pinMode(feedbackPin, OUTPUT);
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
  if (digitalRead(togglePin) == HIGH) {
    // we shall switch
    if ((currenttime - lasttoggle) > 1000) {
      // last switch occured more than 1 second ago
      buttonPress(switchPin);
      lasttoggle = currenttime;  
    }
  }
  if (s > 50) {
    digitalWrite(feedbackPin, HIGH);
  } else {
    digitalWrite(feedbackPin, LOW);
  }
  delay(50);
}
