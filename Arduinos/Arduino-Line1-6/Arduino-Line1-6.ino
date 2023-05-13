//THIS IS FOR THE 1ST RACK (LINES 1-6)

void setup() {
  // Begin the Serial at 19200 Baud
  Serial.begin(19200);
}

void loop() {
  

  int analog_line1 = analogRead(A0); //Checks the state of pin A0
  int analog_line2 = analogRead(A1); //Checks the state of pin A1
  int analog_line3 = analogRead(A2); //Checks the state of pin A2
  int analog_line4 = analogRead(A3); //Checks the state of pin A3
  int analog_line5 = analogRead(A4); //Checks the state of pin A4
  int analog_line6 = analogRead(A5); //Checks the state of pin A5

  Serial.print("Line1"); Serial.print(String(analog_line1));   //Serial prints Line1 and the respective analog value
  Serial.print(" Line2"); Serial.print(String(analog_line2));  //Serial prints Line2 and the respective analog value
  Serial.print(" Line3"); Serial.print(String(analog_line3));  //Serial prints Line3 and the respective analog value
  Serial.print(" Line4"); Serial.print(String(analog_line4));  //Serial prints Line4 and the respective analog value
  Serial.print(" Line5"); Serial.print(String(analog_line5));  //Serial prints Line5 and the respective analog value
  Serial.print(" Line6"); Serial.println(String(analog_line6));//Serial prints Line6 and the respective analog value
}