📊 Excel Dashboard Web Application












A backend-powered Excel dashboard system that allows users to upload Excel files, process large datasets, and retrieve structured insights through REST APIs.

The project focuses on backend data processing, asynchronous task handling, and scalable API design.

🚀 Key Features

✔ Upload Excel files for data processing
✔ Extract and store structured data in database
✔ REST API for dashboard data retrieval
✔ Seller and brand data management
✔ Scalable backend architecture
✔ Background task processing support

🏗 System Architecture
             User / Client
                  │
                  ▼
          Django REST API
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
   Database            Redis Cache
     (SQLite)              │
                           ▼
                     Celery Workers
                   (Async Processing)
🛠 Tech Stack
Backend

Python

Django

Django REST Framework

Database

SQLite

Caching & Background Tasks

Redis

Celery

Development Tools

Git

GitHub

📂 Project Structure
excel-dashboard/
│
├── excel_dash_app/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── tasks.py
│
├── dashboard_project/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
├── requirements.txt
└── README.md
⚙ Installation Guide
1️⃣ Clone the Repository
git clone https://github.com/saransh-debug/your-repository-name.git
cd your-repository-name
2️⃣ Create Virtual Environment
python -m venv venv

Activate the environment

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Apply Database Migrations
python manage.py makemigrations
python manage.py migrate
5️⃣ Run Development Server
python manage.py runserver

Application will start at:

http://127.0.0.1:8000/
📡 API Endpoints
Method	Endpoint	Description
GET	/api/dashboard/	Retrieve dashboard data
POST	/api/upload/	Upload Excel file
GET	/api/sellers/	Fetch seller information
GET	/api/brands/	Retrieve available brands
📊 Data Processing Workflow
Upload Excel File
        │
        ▼
Data Parsing
        │
        ▼
Database Storage
        │
        ▼
API Fetch Request
        │
        ▼
Structured Dashboard Response
🔮 Future Enhancements

📊 Interactive charts and visual analytics

📈 Real-time dashboard updates

☁ Cloud deployment support

🔐 Authentication & role-based access

🧠 AI-based data insights

👨‍💻 Author

Saransh Bhardwaj

📧 bhardwajsaransh08@gmail.com

💻 GitHub: https://github.com/saransh-debug

⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.



