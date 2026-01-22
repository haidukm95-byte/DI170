CREATE DATABASE Countries;
CREATE TABLE Countries(
    name VARCHAR(100) UNIQUE NOT NULL, 
    capital VARCHAR(100) NOT NULL, 
    flag TEXT NOT NULL, 
    subregion VARCHAR(200), 
    population INTEGER NOT NULL
    );


