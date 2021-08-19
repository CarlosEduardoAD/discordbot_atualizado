-- DISCORD BOT --

This code is still in development, but is like 93% done, I will bring more updates until it's done

TO DO:
----- Run and keep it alive at a cloud server
----- Add ban system (maybe, still considering it)

DOING: 

DONE:
----- Add a update system
----- Improve the bot
----- Add a insert system
----- Bot structure
----- Reply system
----- Basic conversation bot -> client and client -> bot
----- SQLite3 database

NOT POSSIBLE: 

---- Add delete system
Why?
The main problem is that when you use the DELETE query on sql, he will delete the DATA/VALUE on the cell, NOT the cell, this means that 
it will always be a blank space on the table* , and that can be dificult to solve on the future, keepin' in mind that the own discord API 
gives me a error each time that I try to send a empty message, which it's quite obvious lol, because he can't send a null value. My solution tho was put
a update system, which makes the almost the same work, the User will input the message he wants to insert and then change the past one put his input.

*Sql is used for relational databases, if you delete a single cell in a row, this row will have less cells than the other ones, in the end, the relational database wont be relational anymore (keepin' in mind that are elements that are < then the others), I don't know if this is possible with other db paradigms, such as document-oriented (mongodb),
or the graph ones (GraphQL) but i know that you can't do that type of action in sql.

EXAMPLE (PT):

  User input: $substituir
              Como vai ? <- "This value is the one that will update"
              Olá < "This value is the one that will be updated"

EXAMPLE (EN):
  User input: $Update
              How you doin' ?
              Sup 
              
That means that I shouldn't use the delete query keepin' in mind your explanation ?
Quick and Short Awnser: nope
Long Awnser: It depends actually, when you just need to delete something from a table that won't affect any other application (Code, API, cloud functions etc...) you 
             can use it safely, cause at least it won't affect most of the fuctions of your application, the main problem is when you NEED to return values of db -> application,
             unless that the API/Library/Framework has a catch system to this type of error, you may have some problems with read-errors. I am not a professional programmer
             (actually i'm a pretty amateur one lol) but I just wanted to share this event that happened with me.
             
