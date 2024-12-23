# NewsFinder

## Overview
NewsFinder is a Python tool designed to search and retrieve relevant news articles based on a specified topic. The tool integrates powerful technologies like Tavily, SmartScraper (from ScrapeGraph), and OpenAI to provide accurate and well-structured information.

### Key Features
- **Search Relevant URLs**: Utilizes Tavily to find URLs related to the specified topic.
- **Scrape News Content**: Leverages SmartScraper to extract titles, descriptions, and links from the retrieved URLs.
- **Structured Output**: Provides results in a structured format using Pydantic schemas for easy processing.
- **Customizable and Modular**: Includes distinct modules for scraping, searching, and managing data.

---

## Project Structure
The project is organized as follows:

```
NewsFinder/
├── newsfinder/
│   ├── __init__.py
│   ├── scraper.py       # Handles scraping operations
│   ├── search.py        # Manages URL search functionality
│   ├── schemas.py       # Defines data schemas with Pydantic
│   └── utils.py         # Utility functions (e.g., API key management)
├── tests/               # Contains unit tests
│   ├── __init__.py
│   ├── test_scraper.py
│   ├── test_search.py
│   └── test_integration.py
├── main.py              # Entry point of the tool
├── .env.example         # Example file for environment variables
├── requirements.txt     # Project dependencies
├── setup.py             # Package setup
└── README.md            # Project documentation
```

---

## Prerequisites
Before running NewsFinder, ensure you have the following:

- Python 3.8 or later
- API keys for the following services:
  - **ScrapeGraph**: `SGAI_API_KEY`
  - **Tavily**: `TAVILY_API_KEY`
  - **OpenAI**: `OPENAI_API_KEY`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/newsfinder.git
   cd newsfinder
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment variables by creating a `.env` file or exporting them:
   ```
   SGAI_API_KEY=your_scrapegraph_api_key
   TAVILY_API_KEY=your_tavily_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```
   Alternatively, copy `.env.example` to `.env` and populate it with your API keys.

---

## Usage

To use NewsFinder, run the `main.py` script:

```bash
python -m newsfinder.main
```

You will be prompted to enter a topic:

```
Enter a topic to search for: Climate Change
```

The tool will:
1. Search for URLs related to "Climate Change" using Tavily.
2. Scrape articles from the retrieved URLs using SmartScraper.
3. Display a list of article titles and their respective links.

---

## Testing

Unit tests are included in the `tests/` directory. To run the tests:

```bash
pytest tests/
```

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Commit your changes and open a pull request.

---

## Acknowledgments

- **Tavily** for URL search capabilities.
- **SmartScraper** by ScrapeGraph for scraping functionality.
- **OpenAI** for advanced processing capabilities.

Happy coding!
