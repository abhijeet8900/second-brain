# Finance Tracker

Created: December 4, 2023 8:43 AM

POC Sheet: https://docs.google.com/spreadsheets/d/1vVhJWYIJt0ulSh4w-vFSH4RstqEafXSzopaGlJnqM1Q/edit#gid=0

## Steps :

- Finalize Requirements for applications
- Decide features for initial release
- Write down the flow for the application
- Decide tech stack ✅
- Decide how to deploy the application
- Database Design
- Setup Repo’s and DB instance ✅
- Setup frontend application
- Setup backend application
- List out screens

## Tech Stack  :

- Version Control:  GitHub ☑️
- Use docker containers
- Front end / Mobile :
    - **VueJs** ☑️
    - Setup Ref: [https://medium.com/simform-engineering/building-awesome-pwas-using-six-leading-frontend-frameworks-61bb7c280c4f](https://medium.com/simform-engineering/building-awesome-pwas-using-six-leading-frontend-frameworks-61bb7c280c4f)
- Back end ( Middleware ):   Flask  + PyMongo ( MongoDB connector ) ☑️
- Database:  MongoDB ☑️

## Infrastructure :

Cloud Platform:  Google Cloud Platform, AWS, 

## Deployment :

- How will our application be deployed?
- CICD for application: Jenkins
- Deployment for frontend : [https://dashboard.render.com/static/srv-cm1ejbi1hbls73aho9e0/settings](https://dashboard.render.com/static/srv-cm1ejbi1hbls73aho9e0/settings)

## Database

**Dashboard:** [https://cloud.mongodb.com/v2/6578b9edac44bd162c544bd0#/overview](https://cloud.mongodb.com/v2/6578b9edac44bd162c544bd0#/overview)

**Design Best practices reference:** https://www.mongodb.com/developer/products/mongodb/mongodb-schema-design-best-practices/

## DB Credentials :

- Username : `ghosty`
- Password: `8900`

## ERD :

POC: [https://dbdiagram.io/d/Finance-Tracker-6572051456d8064ca099ea15](https://dbdiagram.io/d/Finance-Tracker-6572051456d8064ca099ea15)

[https://dbdiagram.io/e/6572051456d8064ca099ea15/657548ad56d8064ca0b8631a](https://dbdiagram.io/e/6572051456d8064ca099ea15/657548ad56d8064ca0b8631a)

- MySQL Setup Script
    
    ```sql
    -- Setup Script  
    USE finance_tracker;
    
    CREATE TABLE `users` (
      `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
      `first_name` VARCHAR(255),
      `last_name` VARCHAR(255),
      `email` VARCHAR(255) NOT NULL,
      `phone_no` VARCHAR(255),
      `user_name` VARCHAR(255) UNIQUE NOT NULL,
      `password` VARCHAR(255) NOT NULL
    );
    
    CREATE TABLE `groups` (
      `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
      `name` VARCHAR(255) NOT NULL,
      `created_at` DATETIME NOT NULL,
      `created_by` INT NOT NULL,
      FOREIGN KEY (`created_by`) REFERENCES `users` (`id`)
    );
    
    CREATE TABLE `group_tags` (
      `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
      `group_id` INT NOT NULL,
      `name` VARCHAR(255) NOT NULL,
      FOREIGN KEY (`group_id`) REFERENCES `groups` (`id`)
    );
    
    CREATE TABLE `transaction_types` (
        `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        `name` VARCHAR(255) NOT NULL
    );
    
    CREATE TABLE `payment_methods` (
      `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
      `name` VARCHAR(255) NOT NULL
    );
    
    CREATE TABLE `transactions` (
      `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
      `timestamp` DATETIME NOT NULL,
      `transaction_type_id` INT NOT NULL,
      `paying_for` VARCHAR(255) NOT NULL,
      `group_id` INT NOT NULL,
      `comment` VARCHAR(255),
      `payment_method_id` INT NOT NULL,
      `recorded_by` INT NOT NULL,
      FOREIGN KEY (`group_id`) REFERENCES `groups` (`id`),
      FOREIGN KEY (`transaction_type_id`) REFERENCES `transaction_types` (`id`),
      FOREIGN KEY (`payment_method_id`) REFERENCES `payment_methods` (`id`),
      FOREIGN KEY (`recorded_by`) REFERENCES `users` (`id`)
    );
    
    CREATE TABLE `user_groups` (
      `group_id` INT NOT NULL,
      `user_id` INT NOT NULL,
      FOREIGN KEY (`group_id`) REFERENCES `groups` (`id`),
      FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
    );
    
    CREATE TABLE `transaction_tags` (
      `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
      `group_tag_id` INT NOT NULL,
      `transaction_id` INT NOT NULL,
      FOREIGN KEY (`group_tag_id`) REFERENCES `group_tags` (`id`),
      FOREIGN KEY (`transaction_id`) REFERENCES `transactions` (`id`)
    );
    
    ALTER TABLE `users` ADD FOREIGN KEY (`id`) REFERENCES `groups` (`created_by`);
    
    ALTER TABLE `group_tags` ADD FOREIGN KEY (`group_id`) REFERENCES `groups` (`id`);
    
    ALTER TABLE `user_groups` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
    
    ALTER TABLE `user_groups` ADD FOREIGN KEY (`group_id`) REFERENCES `groups` (`id`);
    
    ALTER TABLE `transaction_tags` ADD FOREIGN KEY (`transaction_id`) REFERENCES `transactions` (`id`);
    
    ALTER TABLE `transaction_tags` ADD FOREIGN KEY (`group_tag_id`) REFERENCES `group_tags` (`id`);
    
    ALTER TABLE `groups` ADD FOREIGN KEY (`id`) REFERENCES `transactions` (`group_id`);
    
    ALTER TABLE `transaction_types` ADD FOREIGN KEY (`id`) REFERENCES `transactions` (`transaction_type_id`);
    
    ALTER TABLE `payment_methods` ADD FOREIGN KEY (`id`) REFERENCES `transactions` (`payment_method_id`);
    
    ALTER TABLE `users` ADD FOREIGN KEY (`id`) REFERENCES `transactions` (`recorded_by`);
    ```
    

## MongoDB Design :

![Untitled](Finance%20Tracker%20552f029869734082a5fca0fa0efcb61e/Untitled.png)

## UI

Frontend Login : [https://dev.to/nagatodev/how-to-add-login-authentication-to-a-flask-and-react-application-23i7](https://dev.to/nagatodev/how-to-add-login-authentication-to-a-flask-and-react-application-23i7)