
const byte ENC_A = 2; //kodlayıcı darbesi A 
const byte ENC_B = 3; //kodlayıcı darbesi B
const byte IN4 = 4; //Motor sürücü için: motor ileri
const byte IN3 = 5; //Motor sürücü için: motor geri
const byte ENB = 6; //Motor sürücü için: motor hızı
int encoder = 0;
double pv_speed = 0;//şuanki hız 
double set_speed = 0;//istenilen hız
int timer1_counter; //zamanlayıcı için
double error_speed = 0; //hız hatası = set_speed - pv_speed
double error_speed_pre = 0;  //son hız hatası
double error_speed_sum = 0;  //toplam hız hatası
double ENB_pulse =0;   //bu değer 0~255
double Kp = 0;
double Ki = 0;
double Kd = 0;
String mySt = "";
char myChar;
boolean stringComplete = false; //dizenin tamamlanıp tamamlanmadığı
boolean motor_start = false;
double ENB_pulse_base = 0;
boolean A, B;

void setup() {

  pinMode(ENC_A, INPUT_PULLUP);
  pinMode(ENC_B, INPUT_PULLUP);
  pinMode(IN4, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(ENB, OUTPUT);
  attachInterrupt(digitalPinToInterrupt(ENC_A), readEncoder, RISING);//kesinti meydana geldiğinde fonksiyon readEncoder'a dallan
  // 9600 bps'de seri bağlantı noktasını başlatın:
  Serial.begin(9600);
  //--------------------------zamanlayıcı kurulumu
  noInterrupts();           // tüm kesmeleri devre dışı bırak
  TCCR1A = 0;
  TCCR1B = 0;
  timer1_counter = 59286;   // ön yükleme zamanlayıcısı 0.1 saniye için 59286

  TCNT1 = timer1_counter;   // ön yükleme zamanlayıcısı
  TCCR1B |= (1 << CS12);    // 256 ölçek
  TIMSK1 |= (1 << TOIE1);   // zamanlayıcı taşma kesintisini etkinleştir
  interrupts();             // tüm kesintileri etkinleştir
  //--------------------------zamanlayıcı kurulumu

  while (!Serial) {
    ; //seri bağlantı noktasının bağlanmasını bekleyin
  }

  //--------------stop motor
  digitalWrite(IN4, 0);
  digitalWrite(IN3, 0);
  analogWrite(ENB, 0);
  //-----------------------
}

void loop() {

  if (stringComplete) {
    // port alma işlemi tamamlandığında dizeyi temizle
    mySt = "";  //mySt, '\n' alınana kadar boş kalır
    stringComplete = false;
  }
  //PyQt5'den komut alma
  if (mySt.substring(0,5) == "start") {
      if(set_speed > 0){
      digitalWrite(IN4, 1);     //motoru çalıştır ileri hareket 
      digitalWrite(IN3, 0);
      motor_start = true;
      }
      else if(set_speed < 0) {
      digitalWrite(IN4,0);      //motoru çalıştır geri hareket
      digitalWrite(IN3,1);
      motor_start = true;
      }
  
  }
  else if (mySt.substring(0,4) == "stop") {
    digitalWrite(IN4, 0);
    digitalWrite(IN3, 0);     //motoru durdur
    motor_start = false;
  }
  else if (mySt.substring(0,9) == "set_speed"){
    set_speed = mySt.substring(9,mySt.length()).toFloat();  //set_speed'den sonra dizeyi al  
  }
  else if (mySt.substring(0,2) == "Kp"){
    Kp = mySt.substring(2,mySt.length()).toFloat(); //Kp'den sonra dize al  
  }
  else if (mySt.substring(0,2) == "Ki"){
    Ki = mySt.substring(2,mySt.length()).toFloat(); //Ki'den sonra dize al

  }
  else if (mySt.substring(0,2) == "Kd"){
    Kd = mySt.substring(2,mySt.length()).toFloat(); //Kd'den sonra dize al
  } 

}

void readEncoder() {//bu fonksiyon kodlayıcı sayılarını bulmak için

  A = digitalRead(ENC_A);
  B = digitalRead(ENC_B);

  if (A == HIGH) {
    if (B == HIGH) {
      encoder--; //yeni darbede azalan kodlayıcı
    }
    else {
      encoder++; //yeni darbede artan kodlayıcı
    }
  }
  else {
    if (B == HIGH) {
      encoder++; //artan
    }
    else {
      encoder--; //azalan
    }
  }
}

void sendToPC(double* data)//verileri byte'lara bölen fonksiyon
{
  byte* byteData = (byte*)(data);//bir byte işaretçisine yayınlama
  Serial.write(byteData, 4);//PC'ye Seri yoluyla gönder
}

ISR(TIMER1_OVF_vect)        // kesme servisi rutini - her 0.1 saniyede bir
{
  TCNT1 = timer1_counter;   // zamanlayıcıyı kur
  pv_speed = 600.0 * (encoder / 200.0) / 0.1;//motor hızını hesapla
  double value = pv_speed;
  sendToPC(&value);
  encoder = 0;
  
  if (motor_start){
    error_speed = abs(set_speed) - abs(pv_speed);
    ENB_pulse = error_speed*Kp + error_speed_sum*Ki + (error_speed - error_speed_pre)*Kd;
    error_speed_pre = error_speed;   //son hata
    error_speed_sum += error_speed; //hata toplamı
    if (error_speed_sum >4000) error_speed_sum = 4000;
    if (error_speed_sum <-4000) error_speed_sum = -4000;

  } 
  
  else{
    error_speed = 0;
    error_speed_pre = 0;
    error_speed_sum = 0;
    ENB_pulse_base = 0;
    ENB_pulse = 0;
  }
    
  if (ENB_pulse <255 & ENB_pulse >0) {
    analogWrite(ENB, ENB_pulse); //motor hızını ayarla
  }
  else {
    if (ENB_pulse > 255) {
      analogWrite(ENB, 255);
    }
    else {
      analogWrite(ENB, 0);
    }
  }
}

void serialEvent() {
  while (Serial.available()) {
    // yeni byte al
    char inChar = (char)Serial.read();
    // inputString'e ekleyin:
    if (inChar != '\n') {
      mySt += inChar;
    }
    // gelen karakter yeni bir satırsa, bir bayrak ayarlayın
     // böylece ana döngü bu konuda bir şeyler yapabilir:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
