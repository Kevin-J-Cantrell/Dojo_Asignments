SELECT * FROM friendships;
SELECT * FROM users;
INSERT INTO users (first_name, last_name) 
VALUES('Amy', 'Rant'),('Kermit', 'The frog'),('Mark', 'Brant'),('Bryan', 'Cole'),('John', 'Reese'),('Kevin', 'Duran');

INSERT INTO friendships (user_id, friendship_id) 
VALUES(1,2),(1,4),(1,6);

INSERT INTO friendships (user_id, friendship_id) 
VALUES(2,1),(2,3),(2,5);

INSERT INTO friendships (user_id, friendship_id) 
VALUES(3,2),(3,5);

INSERT INTO friendships (user_id, friendship_id) 
VALUES(4,3);

INSERT INTO friendships (user_id, friendship_id) 
VALUES(5,1),(5,6);

INSERT INTO friendships (user_id, friendship_id) 
VALUES(6,2),(6,3);

SELECT users.first_name , users.last_name , user2.first_name as friend_first_name, user2.last_name as friend_last_name  FROM users
JOIN friendships ON friendships.user_id = users.id
LEFT JOIN users as user2 ON friendships.friendship_id = user2.id;

