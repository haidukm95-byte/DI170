WEATHER MONITOR v 1.0

This Python- and SQL-powered program allows to watch current weather of any location throughout the world!

HOW DOES IT WORK:
WARNING! This is early version! The only interface available is cmd/terminal.

1. What does it contain of?
  menu.py - the main executable module;
  Weather.py - the body module (e.g. consists main performing code while menu.py consists menu and the code which is required to launch the rest of the processes;
  favorites.py - module which interacts with SQL-based table of selected favorite locations;
  history.py - module which interacts with SQL-based table of queries' history;
  sql_connect.py - module which performs SQL queries;
  tables.sql - here is two our SQL tables' creation process codified. The tables are the only depositories of queries' history and favorite locations.

2. So, how to run it finally?
   I. To make the program work correctly all the files stated above have to be located at the same directory.
   II. Navigate through cmd/terminal (depends on OS) to the directory where menu.py is situated along with the rest of the files.
   III. Run menu.py
   IV. Follow the guidance within the program
   ???
   PROFIT!

Made by:
Marko Haiduk: main coding, SQL
ClaudeCode AI Checker: code debugging and fixing errors
Software used:
PgAdmin4
VSCode
api.openweathermap.org (API of openweathermap.org internet resource), the main and only source of weather data (for using it personal subscription is required!)
Contacts:
email: haidukm95@gmail.com


