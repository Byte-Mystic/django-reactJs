<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>django-reactJs
</h1>
<h3>◦ Django meets React: Unleash unparalleled web development power!</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/SVG-FFB13B.svg?style&logo=SVG&logoColor=black" alt="SVG" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style&logo=HTML5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/React-61DAFB.svg?style&logo=React&logoColor=black" alt="React" />

<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Django-092E20.svg?style&logo=Django&logoColor=white" alt="Django" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
</p>
<img src="https://img.shields.io/github/languages/top/Byte-Mystic/django-reactJs?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/Byte-Mystic/django-reactJs?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/Byte-Mystic/django-reactJs?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/Byte-Mystic/django-reactJs?style&color=5D6D7E" alt="GitHub license" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running django-reactJs](#-running-django-reactJs)
    - [🧪 Tests](#-tests)
- [🛣 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The project is a web application that allows users to create, update, and delete notes. It provides a Django backend for managing API endpoints and a React frontend for the user interface. The core functionalities include retrieving a list of notes, retrieving a specific note, creating a new note, updating an existing note, and deleting a note. The project's purpose is to provide a simple and intuitive way for users to manage their notes, enhancing their productivity and organization. Its value proposition lies in the seamless integration of the Django backend and React frontend, offering an efficient and user-friendly note-taking experience.

---

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a typical Django architecture, with separation between frontend and backend using Django for the backend and React for the frontend. It incorporates a RESTful API for managing notes. The architecture allows for easy scalability and maintenance.                                                                                                            |
| 📄 | **Documentation**  | The codebase provides some documentation through comments in code files and a README file. However, the documentation could be more comprehensive, including an overview of the system, explanations of major components and their dependencies, and instructions on how to set up and run the project.                                                                          |
| 🔗 | **Dependencies**   | The codebase relies on several external libraries, including Django, Django Rest Framework, react-router-dom, and many others. These libraries provide essential functionality and make development faster and more efficient. However, managing and updating multiple dependencies can become challenging over time.                                                                                                                               |
| 🧩 | **Modularity**     | The project has well-organized directory structure, separating frontend and backend code. It follows the Django app structure and adheres to React's component-based architecture. The use of separate views, models, and serializers in the backend and separate components in the frontend promotes modularity and code reusability.                                                                                                         |
| 🧪 | **Testing**        | The codebase includes a placeholder for tests in the `api/tests.py` file, but no actual tests are implemented. Testing is crucial for ensuring the correctness of the code, and implementing a comprehensive testing strategy, including unit tests and integration tests, would enhance the reliability and stability of the system.                                                                         |
| ⚡️ | **Performance**    | It is difficult to determine the performance of the system without additional information. However, the codebase utilizes Django and React frameworks, which are known for their efficiency and performance optimizations. As long as proper coding practices and optimization techniques are followed, the system should perform well, providing a smooth user experience.                                                                                        |
| 🔐 | **Security**       | The codebase incorporates several security measures, such as token-based authentication for the API, password validation settings in Django, and the use of Django's built-in security features. However, without a detailed security analysis, it is difficult to provide a comprehensive assessment. Nevertheless, the system seems to have basic security measures in place.                                                |
| 🔀 | **Version Control**| The codebase utilizes Git for version control. Git allows multiple developers to collaborate efficiently, track changes, and revert to previous versions if needed. However, it's essential to ensure that proper branching and merging strategies are followed to avoid conflicts and maintain a clean commit history.                                                                                     |
| 🔌 | **Integrations**   | The system seems to be self-contained, with no apparent external system integrations. However, the use of Django Rest Framework allows for easy integration with other systems or services, making it easier to expand the functionality of the app. Integration with databases, servers, or external APIs can be achieved using Django's capabilities and various Django packages.                                               |
| 📶 | **Scalability**   

---


## 📂 Repository Structure

```sh
└── django-reactJs/
    ├── .gitignore
    ├── README.md
    ├── api/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations/
    │   │   ├── 0001_initial.py
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── frontend/
    │   ├── .gitignore
    │   ├── README.md
    │   ├── package-lock.json
    │   ├── package.json
    │   ├── public/
    │   │   ├── favicon.ico
    │   │   ├── index.html
    │   │   ├── logo192.png
    │   │   ├── logo512.png
    │   │   ├── manifest.json
    │   │   └── robots.txt
    │   └── src/
    │       ├── App.css
    │       ├── App.js
    │       ├── assets/
    │       │   ├── add.svg
    │       │   └── arrow-left.svg
    │       ├── components/
    │       │   ├── AddButton.js
    │       │   ├── Header.js
    │       │   └── ListItem.js
    │       ├── index.js
    │       └── pages/
    │           ├── NotePage.js
    │           └── NotesListPage.js
    ├── manage.py
    ├── mynotes/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── requirements.txt
```


---

## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                         | Summary                                                                                                                                                                                                                                                                                                 |
| ---                                                                                          | ---                                                                                                                                                                                                                                                                                                     |
| [requirements.txt](https://github.com/Byte-Mystic/django-reactJs/blob/main/requirements.txt) | The code uses Django framework for building web applications, supported by asgiref and sqlparse libraries. It also incorporates Django Rest Framework for creating RESTful APIs. Additionally, django-cors-headers handles Cross-Origin Resource Sharing. The code relies on pytz for timezone support. |
| [manage.py](https://github.com/Byte-Mystic/django-reactJs/blob/main/manage.py)               | This code is the command-line utility for Django. It sets the environment, imports necessary modules, and executes administrative tasks specified through the command line.                                                                                                                             |

</details>

<details closed><summary>Mynotes</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                |
| [settings.py](https://github.com/Byte-Mystic/django-reactJs/blob/main/mynotes/settings.py) | This code is the Django settings file for a "mynotes" project. It includes configuration settings such as secret key, debug mode, allowed hosts, installed apps, middleware, templates, database settings, password validation, internationalization, static files, and REST framework configuration. It also allows for cross-origin resource sharing (CORS) and uses token-based authentication. |
| [urls.py](https://github.com/Byte-Mystic/django-reactJs/blob/main/mynotes/urls.py)         | The code provides URL configuration for the "mynotes" project using Django framework. It includes paths for the admin panel, API endpoints, and a default path that displays an index.html template.                                                                                                                                                                                               |
| [wsgi.py](https://github.com/Byte-Mystic/django-reactJs/blob/main/mynotes/wsgi.py)         | This code is the WSGI configuration for the "mynotes" Django project. It sets up the WSGI callable object named "application" and gets the Django application object to handle incoming requests and serve responses.                                                                                                                                                                              |
| [asgi.py](https://github.com/Byte-Mystic/django-reactJs/blob/main/mynotes/asgi.py)         | The code defines the ASGI configuration for the "mynotes" project. It exposes an ASGI callable named "application" using the get_asgi_application() function from Django. The settings module is set to "mynotes.settings" using os.environ.setdefault().                                                                                                                                          |

</details>

<details closed><summary>Api</summary>

| File                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                    |
| [tests.py](https://github.com/Byte-Mystic/django-reactJs/blob/main/api/tests.py)             | This code imports the TestCase class from the Django test module and creates a placeholder for tests to be defined.                                                                                                                                                                                                                                                    |
| [urls.py](https://github.com/Byte-Mystic/django-reactJs/blob/main/api/urls.py)               | This code defines URL patterns for a Django app. It maps different paths to corresponding views: getRoutes, getNotes, createNote, updateNote, deleteNote, and getNote. Each path has a unique name for easy referencing in the app.                                                                                                                                    |
| [views.py](https://github.com/Byte-Mystic/django-reactJs/blob/main/api/views.py)             | The code provides a set of API endpoints for managing notes. It allows users to retrieve a list of notes, retrieve a specific note, create a new note, update an existing note, and delete a note. The code utilizes Django for the backend and implements the necessary methods for interacting with the Notes model using the NoteSerializer for data serialization. |
| [models.py](https://github.com/Byte-Mystic/django-reactJs/blob/main/api/models.py)           | This code defines a Django model called "Notes" with a body field that stores text. It also includes timestamp fields for tracking when the note was last updated and when it was created. The __str__ method returns the first 50 characters of the note's body.                                                                                                      |
| [admin.py](https://github.com/Byte-Mystic/django-reactJs/blob/main/api/admin.py)             | The code imports the Notes model and registers it with the Django admin site, allowing for easy management and interaction with the Notes data through the admin interface.                                                                                                                                                                                            |
| [apps.py](https://github.com/Byte-Mystic/django-reactJs/blob/main/api/apps.py)               | The code is a Django configuration that manages the core functionalities of the "api" app, including automatic field generation and handling of a big auto field. It ensures proper naming and setup for the app's functionality.                                                                                                                                      |
| [serializers.py](https://github.com/Byte-Mystic/django-reactJs/blob/main/api/serializers.py) | This code defines a serializer for the Notes model using the Django REST Framework. It automatically converts Notes objects into JSON representations.                                                                                                                                                                                                                 |

</details>

<details closed><summary>Migrations</summary>

| File                                                                                                      | Summary                                                                                                                                                                                    |
| ---                                                                                                       | ---                                                                                                                                                                                        |
| [0001_initial.py](https://github.com/Byte-Mystic/django-reactJs/blob/main/api/migrations/0001_initial.py) | This code is a Django migration that creates a "Notes" model with fields for body, updated timestamp, and created timestamp. The "Notes" model will have an auto-incrementing primary key. |

</details>

<details closed><summary>Public</summary>

| File                                                                                             | Summary                                                                                                                                                                                                                                                                                                  |
| ---                                                                                              | ---                                                                                                                                                                                                                                                                                                      |
| [robots.txt](https://github.com/Byte-Mystic/django-reactJs/blob/main/frontend/public/robots.txt) | The code follows the standard guidelines of the Robots Exclusion Protocol by using a user-agent wildcard and allowing access to all pages. It ensures that web crawlers can freely access and index the website, effectively allowing search engines to display the website's content in search results. |
| [index.html](https://github.com/Byte-Mystic/django-reactJs/blob/main/frontend/public/index.html) | This code is the basic structure of an HTML file for a React app. It includes meta tags, links to resources, and a div element for rendering the app.                                                                                                                                                    |

</details>

<details closed><summary>Src</summary>

| File                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                         |
| [App.css](https://github.com/Byte-Mystic/django-reactJs/blob/main/frontend/src/App.css)   | The code provided sets the base styles for a web application. It defines colors, fonts, and basic CSS styles. It also includes styles for a container, app header, notes, and a floating button. The app header contains a title and a button. The notes section includes a list of notes with titles and timestamps. The floating button allows users to create new notes. |
| [App.js](https://github.com/Byte-Mystic/django-reactJs/blob/main/frontend/src/App.js)     | This code sets up a React application with routing capabilities using React Router. It renders a header component and defines two routes-one for a notes list page and another for a note page with dynamic ID. The app component is exported as the default for use in other modules.                                                                                      |
| [index.js](https://github.com/Byte-Mystic/django-reactJs/blob/main/frontend/src/index.js) | This code creates a React application that renders the component `<App />` into the HTML element with the ID `root`. It uses `StrictMode` to enable additional checks and warnings during development. The `ReactDOM.createRoot` function is used to create a root element for rendering the app.                                                                           |

</details>

<details closed><summary>Components</summary>

| File                                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                   |
| ---                                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                       |
| [AddButton.js](https://github.com/Byte-Mystic/django-reactJs/blob/main/frontend/src/components/AddButton.js) | The code defines a React component called AddButton which renders a Link with a floating button appearance. When the button is clicked, it navigates to a route'/note/new'. The button displays an add icon, which is an SVG image imported from the'../assets/add.svg' file.                                                                                                             |
| [Header.js](https://github.com/Byte-Mystic/django-reactJs/blob/main/frontend/src/components/Header.js)       | The code defines a React component called Header, which returns a div containing a heading with the text "Note List" and a CSS class of "app-header". It is typically used to display a header section in a React application.                                                                                                                                                            |
| [ListItem.js](https://github.com/Byte-Mystic/django-reactJs/blob/main/frontend/src/components/ListItem.js)   | This code defines a React functional component called "ListItem". It takes in a "note" object as a prop, and it renders a link to a specific note. The component also extracts the note's title, content, and updated time using helper functions. The extracted data is then rendered within a div, with the title displayed in an h3 tag and the content and time displayed in a p tag. |

</details>

<details closed><summary>Pages</summary>

| File                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [NotesListPage.js](https://github.com/Byte-Mystic/django-reactJs/blob/main/frontend/src/pages/NotesListPage.js) | This code is a React functional component that displays a list of notes. It fetches the data from an API endpoint and updates the state with the notes received. The notes are then mapped to individual ListItem components to be rendered. The component also includes an AddButton component for adding new notes.                                                                                                                                  |
| [NotePage.js](https://github.com/Byte-Mystic/django-reactJs/blob/main/frontend/src/pages/NotePage.js)           | The code is a React component that represents a note page. It retrieves a specific note based on the provided ID, allows the user to create, update, or delete notes, and navigates back to the home page. The note content is displayed in a textarea and changes are saved accordingly. It also provides a delete button for existing notes and a done button for new notes. The code utilizes various React hooks and the react-router-dom library. |

</details>

---

## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Dependency 1`

`- ℹ️ Dependency 2`

`- ℹ️ ...`

### 🔧 Installation

1. Clone the django-reactJs repository:
```sh
git clone https://github.com/Byte-Mystic/django-reactJs
```

2. Change to the project directory:
```sh
cd django-reactJs
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Running django-reactJs

```sh
python manage.py runserver
```


---


## 🛣 Roadmap

> - [X] `ℹ️  Task 1: Implement Authentication using JWT`
> - [ ] `ℹ️  Task 2: Implement Authentication with google`


---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---
