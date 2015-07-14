/* Define pinout of Arduino to match physical connections */
define PWMA 3
define AIN1 0
define AIN2 1
define PWMB 5
define BIN1 2
define BIN2 4
define STBY 6

void setup() {

/* Define all 7 pins as outputs to the TB6612FNG driver */
pinMode(PWMA,OUTPUT);
pinMode(AIN1,OUTPUT);
pinMode(AIN2,OUTPUT);
pinMode(PWMB,OUTPUT);
pinMode(BIN1,OUTPUT);
pinMode(BIN2,OUTPUT);
pinMode(STBY,OUTPUT);

}

void loop() {
  
  startUp();
  goForward();
  delay(5500);
  turnAround();
  goForward();
  delay(5500);
  turnAround();
  goBackward();
  delay(5500);
  rotateLeft();
  delay(560);
  rotateRight();
  delay(560);
  goForward();
  delay(3000);
  applyBrakes();
  delay(2000);
  }

/* Function definitions */
/* Due to variations in motor output, it was found that */
/* a duty cycle of 233 on the left motor and 255 on the */
/* right motor is necessary for approximately straight  */
/* line, full speed travel                              */
/* Testing revealed Clusterbot will do 27 rotations per */
/* minute, with motors turning in opposite direction at */
/* full duty cycle.  This "constant" was used to        */
/* determine the length of time to turn to make 90, 180,*/
/* and 360 degree turns.                                */

void goForward ()
{
  digitalWrite (AIN1,HIGH);
  digitalWrite (AIN2,LOW);
  analogWrite(PWMA,234);
  digitalWrite (BIN1,HIGH);
  digitalWrite (BIN2,LOW);
  analogWrite(PWMB,255);  
}

void goBackward ()
{
  digitalWrite (AIN1,LOW);
  digitalWrite (AIN2,HIGH);
  analogWrite(PWMA,233);
  digitalWrite (BIN1,LOW);
  digitalWrite (BIN2,HIGH);
  analogWrite(PWMB,255);  
}

void rotateRight ()
{
  digitalWrite (AIN1,HIGH);
  digitalWrite (AIN2,LOW);
  analogWrite(PWMA,255);
  digitalWrite (BIN1,LOW);
  digitalWrite (BIN2,HIGH);
  analogWrite(PWMB,255);  
}

void rotateLeft ()
{
  digitalWrite (AIN1,LOW);
  digitalWrite (AIN2,HIGH);
  analogWrite(PWMA,255);
  digitalWrite (BIN1,HIGH);
  digitalWrite (BIN2,LOW);
  analogWrite(PWMB,255);  
}

void veerLeft ()
{
  digitalWrite (AIN1,HIGH);
  digitalWrite (AIN2,LOW);
  analogWrite(PWMA,190);
  digitalWrite (BIN1,HIGH);
  digitalWrite (BIN2,LOW);
  analogWrite(PWMB,255);  
}

void veerRight ()
{
  digitalWrite (AIN1,HIGH);
  digitalWrite (AIN2,LOW);
  analogWrite(PWMA,255);
  digitalWrite (BIN1,HIGH);
  digitalWrite (BIN2,LOW);
  analogWrite(PWMB,190);  
}

void applyBrakes ()
{
  digitalWrite (AIN1,HIGH);
  digitalWrite (AIN2,HIGH);
  analogWrite(PWMA,255);
  digitalWrite (BIN1,HIGH);
  digitalWrite (BIN2,HIGH);
  analogWrite(PWMB,255);  
}

void startUp ()
{
  digitalWrite(STBY,HIGH);
}

void turnAround()
{
  rotateLeft();
  delay(1370);
}

void shutDown ()
{
  digitalWrite(STBY,LOW);
}
