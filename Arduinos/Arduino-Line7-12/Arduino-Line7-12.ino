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

  Serial.print(" Line 7: "); Serial.print(String(analog_line7));
  Serial.print(" Line 8: "); Serial.print(String(analog_line8));
  Serial.print(" Line 9: "); Serial.print(String(analog_line9));
  Serial.print(" Line 10: "); Serial.print(String(analog_line10));
  Serial.print(" Line 11: "); Serial.print(String(analog_line11));
  Serial.print(" Line 12: "); Serial.println(String(analog_line12));
}

