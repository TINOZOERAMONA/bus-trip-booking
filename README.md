Bus Trip Booking System


1. Project Overview

This project is a Bus Trip Booking System designed using Domain-Driven Design (DDD) and Clean Architecture principles.

2. Project Structure
bus-trip-booking/
│
├── src/
│   ├── domain/
│   │   ├── entities/
│   │   ├── value_objects/
│   │   ├── aggregates/
│   │   ├── services/
│   │   ├── events/
│   │   └── rules/
│   │
│   ├── application/
│   │   ├── use_cases/
│   │   ├── repositories/
│   │   └── dtos/
│   │
│   ├── infrastructure/
│   │   ├── repositories/
│   │   └── event_handlers/
│   │
│   └── interface/
│       └── main.py
│──tests
└── README.md



3. Getting the Project

Each team member should clone the repository to their computer.

git clone https://github.com/TINOZOERAMONA/bus-trip-booking.git

Then enter the project:

cd bus-trip-booking

4. Creating branches 
Do not work directly on main.

Each team member should create and work on their own branch.

First, make sure you have the latest main:

git switch main
git pull origin main

Then create your own branch:

git switch -c your-branch-name using terminal or you can do it from the github interface

You can check your current branch using:

git branch

The * shows the branch you are currently working on.

5. Layer Responsibilities
   Layer responsibilities are clearly stated in the coursework pdf

6. Working on Your Branch

After creating your branch, make your changes only within your assigned area.

For example:

git switch -c branch-name

Work on your assigned files.

When you are ready to save your work:

git status

Then:

git add .

Commit your changes:

git commit -m "Create Trip entity"

Push your branch:

git push -u origin branch-name

After the first push, you can use:
git push 

7. Pull Requests

Do not merge your own branch directly into main.

When your work is ready, create a Pull Request (PR).

Step 1 — Push your branch
git push
Step 2 — Open GitHub

Go to the repository on GitHub.

You should see your branch and an option such as:

Compare & pull request

Click it.

Step 3 — Create the Pull Request

Set:

base: main
compare: your-branch

Give the Pull Request a clear title.

Example:

Create Trip entity and TripNumber value object

In the description, briefly explain:

What you implemented
What files you changed
Any important decisions
Whether tests were added or updated

Then click:

Create pull request

Step 4 — Team Review

Another team member should review the Pull Request.

They can:

Review the changed files
Comment on the code
Request changes
Approve the Pull Request

If changes are requested, make the changes on your same branch and push again:

git add .
git commit -m "Address review comments"
git push

The Pull Request will automatically update.

Step 5 — Merge

Once the Pull Request has been reviewed and approved, the team can merge it into main.

After merging, everyone should update their local main before starting new work:

git switch main
git pull origin main

Then create a new branch for the next piece of work:

git switch -c new-branch-name

8. Testing

Before creating a Pull Request, make sure your changes work correctly and that existing tests still pass.

Tests should be added for the business rules and use cases where appropriate.

The exact testing commands will be added once the project's testing setup has been established.

9. Questions and Coordination

If your work requires changes to another layer, communicate with the team member responsible for that layer before modifying their files.

The goal is to keep the architecture organized and make integration through Pull Requests easier.

