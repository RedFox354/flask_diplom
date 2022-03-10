DROP TABLE IF EXISTS data;

CREATE TABLE data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ip TEXT NOT NULL,
    url TEXT NOT NULL,
    isAutomated TEXT NOT NULL,
    appName TEXT NOT NULL,
    appVersion TEXT NOT NULL,
    cookieEnabled TEXT NOT NULL,
    geolocation TEXT NOT NULL,
    platform TEXT NOT NULL,
    userAgent TEXT NOT NULL,
    javaEnabled TEXT NOT NULL,
    Height INTEGER NOT NULL,
    Width INTEGER NOT NULL,
    OutHeight INTEGER NOT NULL,
    OutWidth INTEGER NOT NULL,
    Opener TEXT NOT NULL,
    evalBrowser INTEGER NOT NULL,
    result TEXT NOT NULL DEFAULT 'undefined'
);
