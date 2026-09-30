-- This file puts artificial data into the database, ONLY user after running the main schema.sql file

INSERT INTO "Players" ("userID", "username", "password") 
VALUES ('61', 'Jace', '$argon2id$v=19$m=102400,t=2,p=8$o2II9UcENcc5k5ikpeZyPw$RWOMOY8indklWJPaI3Ri8Q'), 
(50, 'John', '$argon2id$v=19$m=102400,t=2,p=8$euOZKJyQbR3/t4r5hZBIYQ$XbtHTe5fI1Ay0wt1YqHqmA'), 
(51, 'Joel', '$argon2id$v=19$m=102400,t=2,p=8$JUE+cleDHT8F0eVBNkbLYg$SjbKOn3MS/rLKmuIDNSsMg'), 
(52, 'Lachlan', '$argon2id$v=19$m=102400,t=2,p=8$JZEVyfyFMu43yAkwpcuLNQ$1I+9c4F76wFUbmklux7s3A'), 
(53, 'Glenn', '$argon2id$v=19$m=102400,t=2,p=8$UOsCqv1RCs20+l0ZFwiUIg$YKEwURitqyOHzuOTUFGw1w'), 
(54, 'Tia', '$argon2id$v=19$m=102400,t=2,p=8$l0xlGiNxHVyWimVbd+rfvA$am2iT6ifl0csG0TaauMXnw'),
(55, 'Casey', '$argon2id$v=19$m=102400,t=2,p=8$fWdXinO1b78TDBELo2GN/w$OHu7AzlsFTkOAZFqajWp+w'),
(56, 'Nadia', '$argon2id$v=19$m=102400,t=2,p=8$eW1X9WWBf55tnNlj4hWpwg$WJXbd4ixPPVXKN12w/SPng'),
(57, 'Eddie', '$argon2id$v=19$m=102400,t=2,p=8$U/FNFuzp4hb/w0xODnce+A$ZmS+MSZR8JOYwwtC5DW/Eg'),
(58, 'Ray', '$argon2id$v=19$m=102400,t=2,p=8$NBMdGtmdedy2W9w5nQCoag$t3m7E/j0f4PbA2krWgb4QQ'),
(59, 'Shawn', '$argon2id$v=19$m=102400,t=2,p=8$/QU7EdsML2+V8ecEz55YXQ$zZMvwxoa3L9UxN6RxAtRbw'),
(60, 'Shane', '$argon2id$v=19$m=102400,t=2,p=8$lL2FkOtNLi9sFIsAQcbxaA$DY3ixeZzDNwpnj5cD3V32w');

INSERT INTO "Data" ("playerID", "playerWins", "houseWins", "winPercentage")
VALUES (50, 70, 45, '60.87%'),
(51, 0, 100, '0.0%'),
(52, 34, 90, '27.42%'),
(53, 100, 100, '50.0%'),
(54, 86, 43, '66.67%'),
(55, 78, 34, '69.64%'),
(56, 78, 90, '46.43%'),
(57, 54, 50, '51.92%'),
(58, 600, 79, '88.37%'),
(59, 345, 300, '53.49%'),
(60, 6, 5, '54.55%'),
(61, 15, 50, '23.08%');