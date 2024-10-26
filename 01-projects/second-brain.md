# Project Title: Second Brain

Idea inspires from [My custom second brain setup](https://luhr.co/blog/2023/04/19/my-custom-second-brain-setup-part-1-why-go-custom/), basic idea behind this is using version control system as your second brain or personal knowledge base. Main goal of building this application is to have custom build second brain app where we can add new features as needed and most of all its free.
This application / system is to be used for long term. Goal of this system is to be easy to maintain and write documents or any text.
Core functionality or principal it should provide is ability to note down stuff, organize new ideas act as personal diary all this using markdown as file format

## Goals  

- Build personal knowledge base system backed by version control system.

## Requirements

Specify the features or functionalities required for the project.

- [x] Ability to sync with github
- [x] Ability to create new todo using CLI using template
- [x] Ability to create new project document using CLI using template
- [x] To have setup script which will work on any operating system
- [ ] Dockerize project
- [ ] Serve markdown files from web server
  - [ ] Use library to serve project directory as web pages
  - [ ] Markdown pages should be editable from browser

## Features

### Edit markdowns from browser

- Use flask server to sever files to web browser
- Flask server should also take post request with file to update file locally
- Use js library to render markdown content using editor
- On client side core, add listeners which will sync file to flask

Using [ShowdownJS](https://github.com/showdownjs/showdown) as frontend editor library.

## Resources and Links

- [Building a Second Brain: The Definitive Introductory Guide](https://fortelabs.com/blog/basboverview/): Introduction to Building a Second Brain, the proven method to organize your digital life.
- [My custom second brain setup, part 1: Why go custom?](https://luhr.co/blog/2023/04/19/my-custom-second-brain-setup-part-1-why-go-custom/): Blog for using VCS such as Github as second brain.

---

**Created on:**  2024-07-29  
**Last Modified on:**  2024-07-29
