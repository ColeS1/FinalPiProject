//THIS IS FOR THE 2ND RACK (LINES 7-12)

void setup() {
  // Begin the Serial at 9600 Baud
  Serial.begin(19200);
}

void loop() {
  

  int analog_line7 = analogRead(A0); //Checks the state of pin A0
  int analog_line8 = analogRead(A1); //Checks the state of pin A1
  int analog_line9 = analogRead(A2); //Checks the state of pin A2
  int analog_line10 = analogRead(A3);//Checks the state of pin A3
  int analog_line11 = analogRead(A4);//Checks the state of pin A4
  int analog_line12 = analogRead(A5);//Checks the state of pin A5

  Serial.print(" Line7"); Serial.print(String(analog_line7));   //Serial prints Line7 and the respective analog value
  Serial.print(" Line8"); Serial.print(String(analog_line8));   //Serial prints Line8 and the respective analog value
  Serial.print(" Line9"); Serial.print(String(analog_line9));   //Serial prints Line9 and the respective analog value
  Serial.print(" LineA"); Serial.print(String(analog_line10));  //Serial prints LineA and the respective analog value
  Serial.print(" LineB"); Serial.print(String(analog_line11));  //Serial prints LineB and the respective analog value
  Serial.print(" LineC"); Serial.println(String(analog_line12));//Serial prints LineC and the respective analog value

  //Yeah I be using them Hex values for 10,11,12, just get wit it
}

