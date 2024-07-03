# Research, Capstone, and Thesis Repository and Management System

This is a side project to do during free time. It is intended to serve as a mini-library that hosts every student's research papers or theses.

### Applying and learning SOLID Principles and TDD while developing the project.

### Learning how to use Docker for development and Docker Compose to configure our development server.

## Code Formatting

1. Ditched Black formatting.
2. Will be applying Linting (flake8) instead through Docker Compose.

## Testing

1. Will be using Django test suite.
2. Setup tests per Django app.
3. Run the tests through Docker Compose.

## List of Modules: (WIP & Tentative)

### Administrator

1. User/Staff Management (CRUD)
2. Student Management (CRUD)
3. Research, Capstone, or Thesis Management (CRUD)
4. File Management (CRUD)
5. File Request Portal + Approval Management (Auditing)
6. Report Generation

### User/Staff

1. Profile Management
2. File Request Portal + Approval Management
3. Student Management (Read)

### Students

1. Profile Management
2. Group Assignation and Invite
3. View Research Papers
4. File Request Portal

### General Features

1. Keyword search form and filter functionality
2. Live chat help desk(?) with Django Channels
