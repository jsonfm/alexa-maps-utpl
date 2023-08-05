// Tec UTPL codigo
#ifdef ARDUINO_ARCH_ESP32
#include <WiFi.h>
#else
#include <ESP8266WiFi.h>
#endif

#include <Espalexa.h>
#include <HTTPClient.h>
#include <WiFiManager.h>

int Led = 1;
int America = 23;
int Europa = 22;
int Asia = 21;
int Africa = 19;
int Oceania = 18;
int Antartida = 16;

// const char* ssid ="Juanjo";
// const char* password ="Juanjo2000";

Espalexa alexita;

void FuncionAmerica(uint8_t brightness);
void FuncionEuropa(uint8_t brightness);
void FuncionAsia(uint8_t brightness);
void FuncionAfrica(uint8_t brightness);
void FuncionOceania(uint8_t brightness);
void FuncionAntartida(uint8_t brightness);

void setup()
{
  // Initialize Serial Monitor
  Serial.begin(115200);
  // Connect to Wi-Fi
  WiFiManager wifiManager;
  // Intentar conectarse a la red Wi-Fi
  if (!wifiManager.autoConnect("AP_Global_CAMPUS"))
  {
    Serial.println("Error al conectarse al punto de acceso");
    delay(3000);
    ESP.restart();
  }
  Serial.print("Conectado a ");
  Serial.println(WiFi.SSID());
  Serial.print("Dirección IP: ");
  Serial.println(WiFi.localIP());

  pinMode(America, OUTPUT);
  pinMode(Europa, OUTPUT);
  pinMode(Asia, OUTPUT);
  pinMode(Africa, OUTPUT);
  pinMode(Oceania, OUTPUT);
  pinMode(Antartida, OUTPUT);

  ConectarWifi();

  alexita.begin();
}

void loop()
{
  ConectarWifi();
  alexita.loop();
  delay(1);
}

void ConectarWifi()
{
  WiFiManager wifiManager;
  // Intentar conectarse a la red Wi-Fi
  if (!wifiManager.autoConnect("AP_Global"))
  {
    Serial.println("Error al conectarse al punto de acceso");
    delay(3000);
    ESP.restart();
  }
  Serial.print("Conectado a ");
  Serial.println(WiFi.SSID());
  Serial.print("Dirección IP: ");
  Serial.println(WiFi.localIP());
}
// Continente America
void FuncionAmerica(uint8_t brightness)
{
  Serial.print("Funcion America - ");

  if (brightness)
  {
    digitalWrite(America, 1);
    Serial.println(" Apagar América ");
    digitalWrite(America, LOW);
  }
  else
  {
    digitalWrite(America, 0);
    Serial.println(" Encender America ");
    digitalWrite(America, HIGH);
  }
}
// Continente Europa
void FuncionEuropa(uint8_t brightness)
{
  Serial.print("Funcion Europa -");

  if (brightness)
  {
    digitalWrite(Europa, 1);
    Serial.println(" Apagar Europa ");
    digitalWrite(Europa, LOW);
  }
  else
  {
    digitalWrite(Europa, 0);
    Serial.println(" Encender Europa ");
    digitalWrite(Europa, HIGH);
  }
}

// Continente Asia
void FuncionAsia(uint8_t brightness)
{
  Serial.print("Funcion Asia -");

  if (brightness)
  {
    digitalWrite(Asia, 1);
    Serial.println(" Apagar Asia ");
    digitalWrite(Asia, LOW);
  }
  else
  {
    digitalWrite(Asia, 0);
    Serial.println(" Encender Asia ");
    digitalWrite(Asia, HIGH);
  }
}

// Continente Africa
void FuncionAfrica(uint8_t brightness)
{
  Serial.print("Funcion Africa -");

  if (brightness)
  {
    digitalWrite(Africa, 1);
    Serial.println(" Apagar Africa ");
    digitalWrite(Africa, LOW);
  }
  else
  {
    digitalWrite(Africa, 0);
    Serial.println(" Encender Africa ");
    digitalWrite(Africa, HIGH);
  }
}

// Continente Oceania
void FuncionOceania(uint8_t brightness)
{
  Serial.print("Funcion Oceania -");

  if (brightness)
  {
    digitalWrite(Oceania, 1);
    Serial.println("Apagar Oceania ");
    digitalWrite(Oceania, LOW);
  }
  else
  {
    digitalWrite(Oceania, 0);
    Serial.println(" Encender Oceania ");
    digitalWrite(Oceania, HIGH);
  }
}

// Continente Antartida
void FuncionAntartida(uint8_t brightness)
{
  Serial.print("Funcion Antartida -");

  if (brightness)
  {
    digitalWrite(Antartida, 1);
    Serial.println(" Apagar Antartida ");
    digitalWrite(Antartida, LOW);
  }
  else
  {
    digitalWrite(Antartida, 0);
    Serial.println(" Encender Anrartida");
    digitalWrite(Antartida, HIGH);
  }
}
