CREATE DATABASE lms_db;

USE lms_db;

CREATE TABLE `books` (
  `id` integer PRIMARY KEY,
  `name` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `total_copies` integer NOT NULL,
  `lended_copies` integer NOT NULL
);

CREATE TABLE `users` (
  `id` integer PRIMARY KEY,`
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255),
  `email` varchar(255) NOT NULL,
  `registered_on` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `lendings` (
  `id` integer PRIMARY KEY,
  `book_id` integer NOT NULL,
  `user_id` integer NOT NULL,
  `date_issued` datetime NOT NULL,
  `date_due` datetime NOT NULL
);

ALTER TABLE `lendings` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `lendings` ADD FOREIGN KEY (`book_id`) REFERENCES `books` (`id`);

