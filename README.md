# Movie Recommender System 🎬

A Content-Based Movie Recommender System built with Python, Streamlit, and Machine Learning. The application suggests similar movies based on user selection and fetches corresponding movie posters dynamically from the TMDB (The Movie Database) API.

---

## 🚀 Live Demo
You can deploy this repository directly to **[Streamlit Community Cloud](https://share.streamlit.io/)** or **[Hugging Face Spaces](https://huggingface.co/spaces)**.

---

## 🛠️ Features
* **Content-Based Recommendation**: Uses Cosine Similarity on processed movie tags (genres, keywords, cast, crew, etc.) to recommend the top 5 most similar movies.
* **Dynamic Poster Fetching**: Integrates with the TMDB API to pull movie posters.
* **Resilient API Fallback**: Includes connection timeout checks and a fallback placeholder image in case of offline usage, network failures, or rate-limited API keys to prevent page crashes.
* **Interactive UI**: Clean, responsive Streamlit dashboard with a dropdown menu and side-by-side movie columns.

---

## 📁 Project Structure
```text
├── app.py                  # Main Streamlit web application
├── main.ipynb              # Jupyter notebook with Data Analysis & Model Training
├── movies.pkl              # Serialized DataFrame containing movie information
├── similarity.pkl          # Cosine similarity matrix (Git LFS tracked)
├── requirements.txt        # Python package dependencies
├── setup.sh                # Automation script for local environment configuration
├── .gitignore              # Files to ignore in Git
└── .gitattributes          # Git LFS tracking configuration for large pickle/CSV files
```

---

## 💻 Local Setup & Execution

### Prerequisites
Make sure you have Python 3.9+ and pip installed on your system.

### Option A: Automatic Setup (Recommended)
We have included a `setup.sh` script to automate virtual environment creation and package installation:

1. Open your terminal and navigate to the project directory.
2. Run the setup script:
   ```bash
   ./setup.sh
   ```
3. Activate the environment and launch the app:
   ```bash
   source .venv/bin/activate
   streamlit run app.py
   ```

### Option B: Manual Setup
If you prefer configuring the environment manually:

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   ```
2. Activate the virtual environment:
   * **Mac/Linux**: `source .venv/bin/activate`
   * **Windows**: `.venv\Scripts\activate`
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## 🌐 Deployment Instructions

### Streamlit Community Cloud (Free)
1. Push this repository to your GitHub account.
2. Visit [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
3. Click **New app**, select your repository, set the main branch to `main`, and set the file path to `app.py`.
4. Click **Deploy**.

### Hugging Face Spaces (Free)
Since the `similarity.pkl` file is ~184MB, make sure you have **Git LFS** installed before deploying:
1. Install Git LFS: `brew install git-lfs && git lfs install`
2. Create a new Space on Hugging Face using the **Streamlit** SDK.
3. Add the Hugging Face Space as a remote:
   ```bash
   git remote add hf https://huggingface.co/spaces/<your-username>/<your-space-name>
   ```
4. Push your changes:
   ```bash
   git push -u hf main
   ```
