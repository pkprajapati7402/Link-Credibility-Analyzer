

# Link Safety and Credibility Analyzer

## Overview
The Link Safety and Credibility Analyzer is a web application that allows users to paste URLs sourced from social media or other platforms to automatically check and analyze their safety and credibility. The application evaluates the URL's reputation, checks for potential malware or phishing attempts, and analyzes the content to determine if it is misleading or safe to browse. The results are presented with a percentage score and color-coded clearance (red, yellow, green) indicating the safety level.

## Features
- **User Input:** Paste a URL into a text field.
- **Link Analysis:** Analyze the URL for:
  - Domain reputation
  - Presence of malware or phishing attempts
  - Content analysis for misleading information
  - Data privacy practices
- **Results Display:** Provides a percentage score and color-coded safety status (red, yellow, green).
- **Database:** Stores analyzed URLs and their scores for faster future analysis.

## Technologies Used
- **Frontend:** React.js, HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **Database:** PostgreSQL/MySQL
- **APIs:** Google Safe Browsing API, VirusTotal API
- **Natural Language Processing (NLP):** TextBlob, BeautifulSoup

## Installation

### Prerequisites
- Node.js and npm (for the frontend)
- Python and pip (for the backend)
- PostgreSQL/MySQL (for the database)

### Clone the Repository
```bash
git clone https://github.com/yourusername/link-safety-analyzer.git
cd link-safety-analyzer
```

### Frontend Setup
1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

### Backend Setup
1. Navigate to the `backend` directory:
   ```bash
   cd ../backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the `backend` directory and add your Google Safe Browsing API key:
   ```
   GOOGLE_SAFE_BROWSING_API_KEY=your_google_safe_browsing_api_key
   ```
5. Run the Flask server:
   ```bash
   flask run
   ```

## Usage
1. Start both the frontend and backend servers.
2. Open the frontend application in your browser (typically at `http://localhost:3000`).
3. Enter a URL in the text field and submit.
4. View the analysis results with a percentage score and color-coded safety status.

## Project Structure
```
link-safety-analyzer/
|-- frontend/
|   |-- public/
|   |   |-- index.html
|   |-- src/
|   |   |-- App.js
|   |   |-- index.js
|   |-- package.json
|-- backend/
|   |-- app.py
|   |-- requirements.txt
|-- .env
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Acknowledgements
- [Google Safe Browsing API](https://developers.google.com/safe-browsing/)
- [VirusTotal API](https://www.virustotal.com/)
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

## Contact
For questions or suggestions, please open an issue or contact the project maintainer at krypto.etox@gmail.com
