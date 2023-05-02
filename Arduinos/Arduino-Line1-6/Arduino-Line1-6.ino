void setup() {
  // Begin the Serial at 9600 Baud
  Serial.begin(19200);
}

void loop() {
  

  int analog_line1 = analogRead(A0);
  int analog_line2 = analogRead(A1);
  int analog_line3 = analogRead(A2);
  int analog_line4 = analogRead(A3);
  int analog_line5 = analogRead(A4);
  int analog_line6 = analogRead(A5);

  Serial.print("Line1"); Serial.print(String(analog_line1));
  Serial.print(" Line2"); Serial.print(String(analog_line2));
  Serial.print(" Line3"); Serial.print(String(analog_line3));
  Serial.print(" Line4"); Serial.print(String(analog_line4));
  Serial.print(" Line5"); Serial.print(String(analog_line5));
  Serial.print(" Line6"); Serial.println(String(analog_line6));
}