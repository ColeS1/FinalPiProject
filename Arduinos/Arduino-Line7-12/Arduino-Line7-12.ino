void setup() {
  // Begin the Serial at 9600 Baud
  Serial.begin(19200);
}

void loop() {
  

  int analog_line7 = analogRead(A0);
  int analog_line8 = analogRead(A1);
  int analog_line9 = analogRead(A2);
  int analog_line10 = analogRead(A3);
  int analog_line11 = analogRead(A4);
  int analog_line12 = analogRead(A5);

  Serial.print(" Line7"); Serial.print(String(analog_line7));
  Serial.print(" Line8"); Serial.print(String(analog_line8));
  Serial.print(" Line9"); Serial.print(String(analog_line9));
  Serial.print(" LineA"); Serial.print(String(analog_line10));
  Serial.print(" LineB"); Serial.print(String(analog_line11));
  Serial.print(" LineC"); Serial.println(String(analog_line12));
}

