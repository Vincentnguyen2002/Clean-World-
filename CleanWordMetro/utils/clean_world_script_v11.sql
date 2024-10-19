DROP DATABASE IF EXISTS clean_world;
CREATE DATABASE clean_world;
USE clean_world;

DROP TABLE IF EXISTS country;
CREATE TABLE country (
	id int(11) NOT NULL AUTO_INCREMENT,
    name varchar(20),
    isClean tinyint(1) default 0,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS city;
CREATE TABLE city (
	id int(11) NOT NULL AUTO_INCREMENT,
    name varchar(20),
    country int(11),
    isClean tinyint(1) default 0,
  
    PRIMARY KEY (id),
--    --  key fk_city_to_country (country),
    constraint fk_city_to_country foreign key (country) references country(id) On delete no action on update cascade
);

DROP TABLE IF EXISTS player;
CREATE TABLE player (
	id int(11) NOT NULL AUTO_INCREMENT,
    name varchar(20),
    resStat int(11),
    location int(11),
    isInCity tinyint(1) default 1,
	energy int(5),
	isNew tinyint(1) default 1,
    PRIMARY KEY (id),
    -- KEY fk_player_to_city (location),
    constraint fk_player_to_city foreign key(location) references city(id) On delete no action on update cascade
    );
    
DROP TABLE IF EXISTS robotType;
CREATE TABLE robotType (
	id int(11) NOT NULL AUTO_INCREMENT,
    name varchar(20),
    description varchar(50),
    PRIMARY KEY (id)
    );
    
DROP TABLE IF EXISTS robot;
CREATE TABLE robot (
	id int(11) NOT NULL AUTO_INCREMENT,
    name varchar(20),
    type int(11),
    pollustat int(11),
    location int(11),
    PRIMARY KEY (id),
    -- KEY fk_robot_to_city (location),
--     KEY fk_robot_to_robotType(type),
    constraint fk_robot_to_city foreign key(location) references city(id) On delete no action on update cascade,
	constraint fk_robot_to_robotType foreign key(type) references robottype(id) On delete no action on update cascade
    );
    
DROP TABLE IF EXISTS match_game;
CREATE TABLE match_game (
	id int(11) NOT NULL AUTO_INCREMENT,
    player_id int(11),
    robot_id int(11),
    isWin tinyInt(1),
    PRIMARY KEY (id),
   --  KEY fk_match_to_player (player_ID),
--     KEY fk_match_to_robot(robot_ID),
    constraint fk_match_to_player foreign key(player_ID) references player(id) On delete no action on update cascade,
	constraint fk_match_to_robot foreign key(robot_ID) references robot(id) On delete no action on update cascade
    );
    
DROP TABLE IF EXISTS quiz_question;
CREATE TABLE quiz_question (
	id int(11) NOT NULL AUTO_INCREMENT,
    text varchar(255),
    location_id int(11),
    PRIMARY KEY (id),
    constraint fk_quiz_question_to_location foreign key(location_id) references city(id) on delete no action on update cascade
    ); 
    
DROP TABLE IF EXISTS quiz_question_option;
CREATE TABLE quiz_question_option (
	id int(11) NOT NULL AUTO_INCREMENT,
    text varchar(255),
    quiz_question_id int(11),
    is_correct tinyint(1),
    PRIMARY KEY (id),
    constraint fk_question_option_to_question foreign key(quiz_question_id) references quiz_question(id) on delete no action on update cascade
    ); 
    
DROP TABLE IF EXISTS quiz_user_answer;
CREATE TABLE quiz_user_answer (
	id int(11) NOT NULL AUTO_INCREMENT,
    player_id int(11),
    quiz_question_id int(11),
    quiz_answer_option_id int(11),
    is_correct tinyint(4),
    PRIMARY KEY (id),
    constraint fk_quiz_user_to_user foreign key(player_ID) references player(id) on delete no action on update cascade,
    constraint fk_quiz_user_to_question foreign key(quiz_question_ID) references quiz_question(id) on delete no action on update cascade
    ); 

 -- insert data into table
insert into country(name,isClean)
values ("Finland",0);
select * from country;

insert into city(name,country,isClean)
value("Helsinki",1,0), ("Vantaa",1,0);
select * from city;

insert into player(name,resStat,location,energy,isInCity,isNew)
value ("Trung",1,1,3,1,0), ("Huy",1,1,3,0,0);
select * from player;

insert into robottype(name,description)
value ("Normal","Normal Robot is normal"), ("Boss","Boss robot guards the factory");
select * from robottype;

insert into robot(name,type,pollustat,location)
value("Robot11",1,1,1),("Robot12",1,2,1),("Robot13",1,3,1),("Robot14",1,4,1),("Boss1",2,5,1),
("Robot21",1,6,2),("Robot22",1,7,2),("Robot23",1,8,2),("Robot24",1,9,2),("Boss2",2,10,2);
select * from robot;

insert into match_game(player_id,robot_id,isWin)
value(1,1,1),(1,2,0);
select * from match_game;

insert into quiz_question(text,location_id)
values ("What are Finnish households encouraged to recycle?",1),
("Which of the following is a common eco-friendly cleaning practice in Finland?",1),
("How is hazardous waste typically disposed of in Finland?",1),
("Jokamiehenoikeus or Everyman Right  allows people who live in Finland to:",1),
("Finland has a national program called 'Siisti Biitsi', which focuses on keeping the beaches clean. What does 'Siisti Biitsi' mean in English?",1),
("What are the primary sources of water pollution in Pakistan?’",2),
("What is a significant contributor to air pollution in major cities of Pakistan?",2),
("What is the major source of indoor air pollution in many rural areas of Pakistan, leading to health issues?",2),
("Which of the following environmental issues is a significant concern in Pakistan?",2),
("Which of the following environmental factors exacerbates air pollution in Pakistan's major cities?",2);

select * from quiz_question;    

insert into quiz_question_option(text,quiz_question_id,is_correct)
values ("Electronics and appliances",1,0), ("Hazardous chemicals",1,0),("Garden waste",1,0),("Glass, paper, and certain plastics",1,1),
("Using harsh chemical cleaners",2,0), ("Using single-use plastic cleaning tools ",2,0),("Using environmentally friendly cleaning products",2,1),("Disposing of cleaning waste in water bodies",2,0),
("It is thrown in regular household trash.",3,0),("It is recycled along with regular waste.",3,0),("It is taken to specialized collection points.",3,1),("It is buried in backyard pits.",3,0),
("Drive off-road vehicles anywhere in the wilderness",4,0),("Camp and pick berries and mushrooms on public and private lands",4,1),("Dump household waste in nature reserves",4,0),("Cut down trees in national parks for firewood",4,0),
("Beautiful Beaches",5,0),("Clean Coast",5,1),("Sunny Shores",5,0),("Pristine Seashores",5,0),
("Industrial discharge and agricultural runoff",6,1),("Volcanic activity and seismic disturbances",6,0),("Deforestation and urbanization",6,0),("Solar radiation and atmospheric dust",6,0),
("Excessive use of bicycles and electric vehicles",7,0),("Low population density and limited industrial activity",7,0),("High-quality public transportation systems",7,0),("Vehicular emissions and industrial pollutants",7,1),
("Factory emissions",8,0),("Agricultural practices",8,0),("Cooking with solid fuels like wood or dung",8,1),("Vehicle exhaust",8,0),
("Excessive rainfall and flooding",9,0),("Air pollution from industrial emissions",9,1),("Frequent earthquakes and tsunamis",9,0),("Abundant forest cover and biodiversity",9,0),
("Frequent sandstorms from neighboring deserts",10,0),("High-altitude geographical location",10,0),("Seasonal monsoon rains reducing pollution levels",10,0),("Geographic topography trapping pollutants",10,1);
select * from quiz_question_option;

-- insert into -- quiz_user_answer(player_ID,quiz_question_ID,quiz_answer_option_ID,is_correct)
-- values (1,1,3,0);
-- select * from quiz_question;
-- select * from quiz_user_answer;
-- update quiz_question
-- set text = "'4', 'Finland\'s Everyman\'s Right (Jokamiehenoikeus) allows people to:', '1'


    
    