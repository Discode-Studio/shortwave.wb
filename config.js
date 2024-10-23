// If you use this please specify multiple kiwis so you don't just camp on a single one!
// URL format: http://kiwi.com:8073/?keys=x - timeout - 24h usage limit (time limits in minutes, null means no limit)
const kiwilistDay = [
    { url: "http://okno.ddns.net:8073/?keys=x", timeout: 24, timelimit: null },
    { url: "http://188.162.63.103:8073/?keys=x", timeout: 30, timelimit: 120 },
    { url: "http://37.33.50.162:8073/?keys=x", timeout: 30, timelimit: 120 }
];

const kiwilistNight = [
    { url: "http://kiwi-kuo.aprs.fi:8073/?keys=x", timeout: 30, timelimit: 120 },
    { url: "http://188.162.63.103:8073/?keys=x", timeout: 30, timelimit: 120 },
    { url: "http://warszawa.proxy.kiwisdr.com:8073/?keys=x", timeout: 120, timelimit: 120 },
];

const reloadMinutes = 25; // max time until next reload after finding a receiver
const retryMinutes = 1; // time until retrying when finding a suitable receiver failed 

const kiwiConfig = {
    freq: "4770",
    mode: "usb",
    zoom: "12",
    startPass: "0",
    endPass: "4000",
    colormap: "4",
    volume: "180",
};

const config = {
    timeout: 3000, // timeout when probing kiwi - in milliseconds
    scoreSNRMult: 1, // SNR score multiplier
    scoreUsageMult: 20, // usage score multiplier (usage is value 0 - 1 1 being lowest usage)
    scoreTimeMult: 1, // time score multiplier (time is minutes passed since SDR last used)
    usageDisallowTolerance: 2, // kiwi cannot be used when there is less than x minutes left (value in minutes)
};

// on error a fallback kiwi may be used. This kiwi must have no time limits at all
const fallback = true;
const fallbackUrl = "http://kiwi-vih.aprs.fi:8073/?keys=x";
const fallbackReloadMinutes = 30;
