// Bänkprov av fällservot: ESP32 som servotestare. Styr över USB, 115200 baud.
//   1500 + Enter   gå till pulsen 1500 µs (första kommandot måste vara 1500)
//   + eller -      ändra 10 µs
//   x              stäng av pulserna (servot slutar styra)
//   =647 + Enter   hoppa direkt till 647 µs utan ramp. Bara för CR Touch:
//                  en ramp sveper genom andra kommandovärden (t.ex. 1782 = självtest).
//                  Använd aldrig = med servot inkopplat.
// Skydd: inga pulser vid start, gränser 500-2500 µs och långsam rampning,
// så att ett skrivfel inte kan slå servot i ändläget i full fart.

const int PIN = 18;
const int FREKV = 50;
const int BITAR = 14;
const int MIN_US = 500, MAX_US = 2500;
const int RAMP_US = 2;          // per 10 ms, alltså 200 µs per sekund

int mal = 0, nu = 0;            // 0 = inga pulser
bool paslagen = false;
String tal;

void skriv(int us) {
  ledcWrite(PIN, (uint32_t)us * 16383UL / 20000UL);
}

void stang() {
  ledcWrite(PIN, 0);
  paslagen = false;
  mal = nu = 0;
  Serial.println("AV: inga pulser. Skriv 1500 för att börja igen.");
}

void satt(int us) {
  if (!paslagen && us != 1500) {
    Serial.println("Första kommandot måste vara 1500 (mittläget).");
    return;
  }
  if (us < MIN_US || us > MAX_US) {
    Serial.println("Utanför 500-2500 µs, ignoreras.");
    return;
  }
  if (!paslagen) {
    paslagen = true;
    nu = us;
    skriv(nu);
  }
  mal = us;
  Serial.print("Mål: ");
  Serial.print(mal);
  Serial.println(" µs");
}

bool hopp = false;              // raden började med '=': inget rampande

void hoppa(int us) {
  if (us < MIN_US || us > MAX_US) {
    Serial.println("Utanför 500-2500 µs, ignoreras.");
    return;
  }
  paslagen = true;
  nu = mal = us;
  skriv(nu);
  Serial.print("Hopp (ingen ramp): ");
  Serial.print(nu);
  Serial.println(" µs");
}

void setup() {
  Serial.begin(115200);
  if (!ledcAttach(PIN, FREKV, BITAR)) { Serial.println("FEL: pulsgenerator kunde inte startas"); while (true) delay(1000); }
  ledcWrite(PIN, 0);
  delay(500);
  Serial.println("Servoprov. Inga pulser ännu. Skriv 1500 och Enter.");
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();
    if (c == 'x') { tal = ""; hopp = false; stang(); }
    else if (c == '=') { tal = ""; hopp = true; }
    else if (c == '+' && paslagen) { tal = ""; satt(mal + 10); }
    else if (c == '-' && paslagen) { tal = ""; satt(mal - 10); }
    else if (isDigit(c)) tal += c;
    else if (c == '\n' || c == '\r') {
      if (tal.length()) { if (hopp) hoppa(tal.toInt()); else satt(tal.toInt()); }
      tal = "";
      hopp = false;
    }
  }
  if (paslagen && nu != mal) {
    nu += constrain(mal - nu, -RAMP_US, RAMP_US);
    skriv(nu);
  }
  delay(10);
}
