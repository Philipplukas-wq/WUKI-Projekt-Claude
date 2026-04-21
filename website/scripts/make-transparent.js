/**
 * Entfernt den weißen Hintergrund aus wuki.png
 * und speichert wuki-transparent.png mit echtem Alpha-Kanal.
 *
 * Algorithmus:
 *   - Pixel nahe Weiß (R,G,B alle > 240)      → vollständig transparent
 *   - Pixel im Übergangsbereich (180–240)       → weiche Transparenz (Anti-Aliasing)
 *   - Dunkle Pixel (Linien der Zeichnung)       → vollständig deckend
 */

const { PNG } = require("pngjs");
const fs = require("fs");
const path = require("path");

const SRC = path.resolve(__dirname, "../../Bild von Wuki.png");
const DST = path.resolve(__dirname, "../public/wuki-transparent.png");

const src = PNG.sync.read(fs.readFileSync(SRC));
const dst = new PNG({ width: src.width, height: src.height });

const WHITE_THRESHOLD = 240; // Pixel heller als dieser Wert → transparent
const EDGE_THRESHOLD  = 180; // Übergangsbereich für weiches Anti-Aliasing

for (let y = 0; y < src.height; y++) {
  for (let x = 0; x < src.width; x++) {
    const i = (src.width * y + x) * 4;

    const r = src.data[i];
    const g = src.data[i + 1];
    const b = src.data[i + 2];

    // Helligkeit: wie nah ist das Pixel an Weiß?
    const brightness = (r + g + b) / 3;

    dst.data[i]     = r;
    dst.data[i + 1] = g;
    dst.data[i + 2] = b;

    if (brightness >= WHITE_THRESHOLD) {
      // Hintergrund → vollständig transparent
      dst.data[i + 3] = 0;
    } else if (brightness >= EDGE_THRESHOLD) {
      // Übergang → Alpha linear von 0 bis 255
      const alpha = Math.round(
        ((WHITE_THRESHOLD - brightness) / (WHITE_THRESHOLD - EDGE_THRESHOLD)) * 255
      );
      dst.data[i + 3] = alpha;
    } else {
      // Linie der Zeichnung → vollständig deckend
      dst.data[i + 3] = 255;
    }
  }
}

fs.writeFileSync(DST, PNG.sync.write(dst));
console.log(`✓ Gespeichert: ${DST}`);
console.log(`  Originalgröße: ${src.width} × ${src.height} px`);
