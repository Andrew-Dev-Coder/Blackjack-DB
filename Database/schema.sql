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

-- Uncomment this section to have a populated database
/*
INSERT INTO "Players" (username, password) 
VALUES ('Jace', '$argon2id$v=19$m=102400,t=2,p=8$o2II9UcENcc5k5ikpeZyPw$RWOMOY8indklWJPaI3Ri8Q'), 
('John', '$argon2id$v=19$m=102400,t=2,p=8$euOZKJyQbR3/t4r5hZBIYQ$XbtHTe5fI1Ay0wt1YqHqmA'), 
('Joel', '$argon2id$v=19$m=102400,t=2,p=8$JUE+cleDHT8F0eVBNkbLYg$SjbKOn3MS/rLKmuIDNSsMg'), 
('Lachlan', '$argon2id$v=19$m=102400,t=2,p=8$JZEVyfyFMu43yAkwpcuLNQ$1I+9c4F76wFUbmklux7s3A'), 
('Glenn', '$argon2id$v=19$m=102400,t=2,p=8$UOsCqv1RCs20+l0ZFwiUIg$YKEwURitqyOHzuOTUFGw1w'), 
('Tia', '$argon2id$v=19$m=102400,t=2,p=8$l0xlGiNxHVyWimVbd+rfvA$am2iT6ifl0csG0TaauMXnw'),
('Casey', '$argon2id$v=19$m=102400,t=2,p=8$fWdXinO1b78TDBELo2GN/w$OHu7AzlsFTkOAZFqajWp+w'),
('Nadia', '$argon2id$v=19$m=102400,t=2,p=8$eW1X9WWBf55tnNlj4hWpwg$WJXbd4ixPPVXKN12w/SPng'),
('Eddie', '$argon2id$v=19$m=102400,t=2,p=8$U/FNFuzp4hb/w0xODnce+A$ZmS+MSZR8JOYwwtC5DW/Eg');
*/