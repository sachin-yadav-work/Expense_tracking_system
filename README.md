# 💰 Expense Tracking System

A Python-based application that helps users track and manage their expenses effectively. This project uses a modular structure with clear separation between backend logic, frontend interface, and test cases.

## 📁 Project Structure

```text
Expense_tracking_system/
├── backend_c/        # Backend logic and database interactions
├── frontend_c/       # Frontend interface for user interactions
├── tests/            # Unit and integration tests
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.x
- MySQL (for database operations)
- pip (Python package manager)

### ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/sachin-yadav-work/Expense_tracking_system.git
   cd Expense_tracking_system
   ```

2. **(Optional) Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your MySQL credentials**

   Update the database connection settings in `backend_c/db_helper.py` with your local MySQL credentials.

## 🧪 Running the Application

- Run backend and frontend Python scripts as needed.
- To run all tests:

   ```bash
   python -m unittest discover tests
   ```

## 📦 Dependencies

Dependencies are listed in `requirements.txt`. To regenerate it (after adding/removing packages):

```bash
pipreqs . --force
```

## 📄 License

This project is licensed under the MIT License.

## 🙌 Acknowledgments

- Python  
- MySQL  
- PyCharm  
- GitHub

## ✍️ Author

**Sachin Yadav**  
GitHub: [sachin-yadav-work](https://github.com/sachin-yadav-work)
