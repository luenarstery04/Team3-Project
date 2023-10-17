CREATE TABLE `users` (
  `id` integer PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `username` varchar(150) UNIQUE,
  `password` varchar(128),
  `user_name` varchar(100),
  `email` varchar(50) UNIQUE,
  `user_genre` varchar(50)
);

CREATE TABLE `Albums` (
  `album_id` varchar(50) PRIMARY KEY NOT NULL,
  `album_name` varchar(150),
  `album_artist` varchar(50),
  `album_genre` varchar(50),
  `album_image` varchar(200),
  `album_release_date` date
);

CREATE TABLE `Tracks` (
  `track_id` varchar(50) PRIMARY KEY NOT NULL,
  `track_name` varchar(150),
  `album_id` varchar(50) NOT NULL,
  `album_name` varchar(150)
);

CREATE TABLE `Liked_Album` (
  `LA_id` integer PRIMARY KEY NOT NULL,
  `id` integer NOT NULL,
  `album_id` varchar(50) NOT NULL
);

CREATE TABLE `Play_list` (
  `playlist_id` integer PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `username` varchar(150) NOT NULL,
  `track_id` varchar(50) NOT NULL
);

CREATE TABLE `audio_features` (
  `track_id` varchar(50) PRIMARY KEY NOT NULL,
  `acousticness` float,
  `danceability` float,
  `energy` float,
  `loudness` float,
  `speechiness` float,
  `tempo` float,
  `valence` float
);

ALTER TABLE `Tracks` ADD FOREIGN KEY (`album_id`) REFERENCES `Albums` (`album_id`);

ALTER TABLE `Liked_Album` ADD FOREIGN KEY (`id`) REFERENCES `users` (`id`);

ALTER TABLE `Liked_Album` ADD FOREIGN KEY (`album_id`) REFERENCES `Albums` (`album_id`);

ALTER TABLE `Play_list` ADD FOREIGN KEY (`track_id`) REFERENCES `Tracks` (`track_id`);

ALTER TABLE `Play_list` ADD FOREIGN KEY (`username`) REFERENCES `users` (`username`);

ALTER TABLE `audio_features` ADD FOREIGN KEY (`track_id`) REFERENCES `Tracks` (`track_id`);
