#define PHOTORESISTOR A12
#define lumArraySize 100

unsigned long lastTimeLumMeasured = millis();
unsigned long delayMeasurement = 50;
int lumDataArray[lumArraySize] = { 0 };

void fillArray(int lumData, int index){
  // byte lumDataArray;
  lumDataArray[index] = lumData;
  // return lumDataArray;
}

int avgLum(int lumArray){
  long lumAvg = 0;
  for (int i = 0; i < lumArraySize ; i++){
    lumAvg += lumDataArray[i];
  } 
  lumAvg = lumAvg/lumArraySize;
  return lumAvg;
}

void setup() {
  Serial.begin(115200);
}

void loop() {
  unsigned long timeNow = millis();
  for (int i = 0; i < lumArraySize; i++){
    if ((timeNow - lastTimeLumMeasured) >= delayMeasurement){
      lastTimeLumMeasured = timeNow;
      int luminosity = analogRead(PHOTORESISTOR);
      fillArray(luminosity, i);
    }
  }
  int averageLuminosity = avgLum(lumDataArray);
  Serial.println(averageLuminosity);
}
