#Last login: Thu Aug  1 20:35:39 on ttys001
 ~  ls                                                                      ok
Applications Documents    Library      Music        Public
Desktop      Downloads    Movies       Pictures     finder

 ~  cd .                                                                    ok

 ~  cd ..                                                                   ok

 !w /Users  ls                                                              ok
Ghost           Shared          abhijeettilekar

 !w /Users  cd ..                                                           ok

 !w /  cd Volumes/Projects/Personal-Projects/second-brain/01-projects       ok

 !w /Volumes/P/P/second-brain/01-projects  test/project-data-migration ?2  ls
Automatic Wifi Switcher 5e2fe78d270f41a58ed2df953bdfb764.md
Enterprise Dashboard - Sprih b5066c1499d24f3e83826046a8acc5de
Enterprise Dashboard - Sprih b5066c1499d24f3e83826046a8acc5de.md
Finance Plan 2024 41833a51b5d249d5a8776af628ac5ba0
Finance Plan 2024 41833a51b5d249d5a8776af628ac5ba0.md
Finance Tracker 552f029869734082a5fca0fa0efcb61e
Finance Tracker 552f029869734082a5fca0fa0efcb61e.md
Front End Developer Roadmap ef5c9bae1722449fbb7ab9c372ebdee0
Front End Developer Roadmap ef5c9bae1722449fbb7ab9c372ebdee0.md
Home Server 48ad101ac57841b5811234915ab12fb9.md
Keyboard Tester Web App b200a61e3bd14caa818b33bf9055fd5b.md
Portfolio 2ff80a6f7f434c1aa023d935bc53832b.md
Spotify Music Player afcf5a3c5ea746729abb0bd7e53439a0.md
investment-plan.md
readme.md
statement-parser.md

 !w /Volumes/P/P/second-brain/01-projects  test/project-data-migration ?2  git checkout main
fatal: detected dubious ownership in repository at '/Volumes/Projects/Personal-Projects/second-brain'
To add an exception for this directory, call:

	git config --global --add safe.directory /Volumes/Projects/Personal-Projects/second-brain

 !w /Volumes/P/P/second-brain/01-projects  test/project-data-migration ?2  cd ..

 !w /Volumes/P/P/second-brain  test/project-data-migration ?2  ls           ok
00-inbox         03-resources     configs          requirements.txt
01-projects      04-archives      core             setup.py
02-areas         05-todos         init.py

 !w /Volumes/P/P/second-brain  test/project-data-migration ?2  git status   ok
fatal: detected dubious ownership in repository at '/Volumes/Projects/Personal-Projects/second-brain'
To add an exception for this directory, call:

	git config --global --add safe.directory /Volumes/Projects/Personal-Projects/second-brain

 !w /Volumes/P/P/second-brain  test/project-data-migration ?2  git config --global --add safe.directory /Volumes/Projects/Personal-Projects/second-brain

 !w /Volumes/P/P/second-brain  test/project-data-migration ?2  git status   ok
On branch test/project-data-migration
Your branch is up to date with 'origin/test/project-data-migration'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	01-projects/investment-plan.md
	01-projects/statement-parser.md

nothing added to commit but untracked files present (use "git add" to track)

 !w /Volumes/P/P/second-brain  test/project-data-migration ?2  git stash -u

 !w /Volumes/P/P/second-brain  test/project-data-migration ?2  git checkout main
fatal: Unable to create '/Volumes/Projects/Personal-Projects/second-brain/.git/index.lock': Permission denied

 !w /Volumes/P/P/second-brain  test/project-data-migration ?2  sudo git checkout
 main
Password:
Switched to branch 'main'
Your branch is behind 'origin/main' by 8 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

 !w /Volumes/P/P/second-brain  main <8 ?2  git pull                         ok
error: cannot open '.git/FETCH_HEAD': Permission denied

 !w /Volumes/P/P/second-brain  main <8 ?2  sudo git pull                 1 err
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/abhijeet8900/second-brain/'

 !w /Volumes/P/P/second-brain  main <8 ?2  git config --global user.email "abhijeet8900@gmail.com"

 !w /Volumes/P/P/second-brain  main <8 ?2  git config --global user.name "abhijeet8900
dquote> "

 !w /Volumes/P/P/second-brain  main <8 ?2  git config --global user.name "abhijeet8900"

 !w /Volumes/P/P/second-brain  main <8 ?2  sudo git pull                    ok
Username for 'https://github.com': ^C

 !w /Volumes/P/P/second-brain  main <8 ?2                          INT  4m 42s

 !w /Volumes/P/P/second-brain  main <8 ?2                                  INT

 !w /Volumes/P/P/second-brain  main <8 ?2  git config --global credential.helper store

 !w /Volumes/P/P/second-brain  main <8 ?2  sudo git pull                    ok
Username for 'https://github.com': abhijeet8900
Password for 'https://abhijeet8900@github.com':
Updating 67aae84..7ab9cdf
Fast-forward
 01-projects/readme.md       |  3 ---
 01-projects/second-brain.md | 43 +++++++++++++++++++++++++++++++++
# Project Title: statement-parser

## Overview

**Description:**
Briefly describe the project idea. What is the project about?

**Goals:**

- Goal 1: Define a clear objective.
- Goal 2: Outline additional aims.

## Action Items

**Tasks:**
List the actionable items you need to complete. Check them off as you go.

- [ ] Task 1: Short description of what needs to be done.
- [ ] Task 2: Short description of what needs to be done.

## Requirements

**Functional:**
01-projects/statement-parser.md                               1,1            Top
 Project Title: statement-parser

## Overview

**Description:**  
Briefly describe the project idea. What is the project about?

**Goals:**  

- Goal 1: Define a clear objective.
- Goal 2: Outline additional aims.

## Action Items

**Tasks:**  
List the actionable items you need to complete. Check them off as you go.

- [ ] Task 1: Short description of what needs to be done.
- [ ] Task 2: Short description of what needs to be done.

## Requirements

**Functional:**  
Specify the features or functionalities required for the project.

- Requirement 1: Describe the functionality.
- Requirement 2: Describe another functionality.

**Non-Functional:**  
Outline any performance or quality attributes required.

- Requirement 1: Describe the non-functional requirement.
- Requirement 2: Describe another non-functional requirement.

## Notes

**Additional Information:**  
Any extra observations or thoughts related to the project.

- Note 1: Briefly explain or elaborate.
- Note 2: Briefly explain or elaborate.

## References

**Resources and Links:**  
Include any relevant resources, articles, or references.

- [Reference 1](URL): Short description of what the reference is about.
- [Reference 2](URL): Short description of what the reference is about.

---

**Created on:** 2024-08-01  
**Last Modified on:** 2024-08-01
