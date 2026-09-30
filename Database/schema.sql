-- This file is used to create the database for ths python game

PRAGMA foreign_keys = ON;

CREATE TABLE "Players" (
	"userID"	INTEGER NOT NULL,
	"username"	TEXT NOT NULL DEFAULT 'NONE',
	"dateOfCreation"	datetime DEFAULT CURRENT_TIMESTAMP,
	"password"	TEXT NOT NULL DEFAULT '$argon2id$v=19$m=102400,t=2,p=8$z8g0SwOprb22S4TIUFY6XQ$KXyDiJBddHHOfRT9c6/+HQ', 
	PRIMARY KEY("userID" AUTOINCREMENT)
);

CREATE TABLE "Data" (
	"dataID"	INTEGER NOT NULL,
	"playerID"	INTEGER NOT NULL DEFAULT 0,
	"playerWins"	INTEGER NOT NULL DEFAULT 0,
	"houseWins"	INTEGER NOT NULL DEFAULT 0,
	"winPercentage"	TEXT NOT NULL DEFAULT '0%',
	PRIMARY KEY("dataID" AUTOINCREMENT),
	FOREIGN KEY("playerID") REFERENCES "Players"("userID")
);
