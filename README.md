# Cross_Device_Integration_Using_AI

A Python application demonstrating AI-driven cross-device data processing, PDF report generation, and Windows printer integration using LangChain and Groq APIs.

## 📋 Overview

This project showcases how to:
- Retrieve AI-powered research summaries via LangChain/Groq
- Generate styled PDF reports with ReportLab
- Manage and print PDFs on Windows printers via `win32print`

## ✨ Key Features

### 🖥️ Cross-Device AI Research
- **LangChain Groq Integration**: Fetch summaries using the ChatGroq model
- **Document Processing**: Use LangChain's `load_summarize_chain` for text summarization

### 📄 PDF Report Generation
- **ReportLab**: Create professional PDF reports with title, bullets, and full summary sections
- **Custom Styles**: Justified paragraphs, bullet lists, and page numbers
- **Page Formatting**: Letter-size layout with consistent margins and typography

### 🖨️ Windows Printer Integration
- **Win32print**: Enumerate available printers and send raw PDF data to be printed
- **Printer Availability Check**: Validate if a specified printer is present
- **Default Printer Usage**: Fallback to system default if no printer name provided

### Future Integrations will be Updated
---

## 🛠️ Technical Stack

- **Python**: 3.x
- **LangChain**: Core and Groq integration
- **ReportLab**: PDF generation
- **pywin32**: Windows printing support
- **dotenv**: Environment variable management

## 📁 Project Structure

```
Cross_device_integration_using_AI/
├── main.py                 # Main script for AI summarization, PDF creation, and printing
├── requirements.txt        # Python dependencies
├── summary_better.pdf      # Sample generated PDF report
├── README.md               # Project documentation
└── LICENSE                 # MIT license
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Windows OS for printer integration
- Valid GROQ_API_KEY in a `.env` file

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mananjp/Cross_device_integration_using_AI.git
   cd Cross_device_integration_using_AI
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment variables:
   ```bash
   echo "GROQ_API_KEY=your_api_key" > .env
   ```

## 💡 Usage

Run the main script and follow the prompts:
```bash
python main.py
```
- Enter the **topic** to research
- View AI-generated summary in console
- A **PDF report** (`summary.pdf`) will be created
- Select a printer to **print** the report or press Enter to use default

## 🧩 Functions

### `list_printers()`
Returns a list of available Windows printers.

### `is_printer_available(printer_name)`
Checks if a given printer name exists.

### `print_pdf_windows(filepath, printer_name=None)`
Prints a PDF file to the specified or default Windows printer.

### `make_pretty_pdf(summary, topic, filename="summary.pdf")`
Generates a styled PDF report containing key takeaways and full summary.

### `research_and_summarize(topic)`
Fetches an AI-generated summary for the provided topic using Groq.

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

*Built with ❤️ for seamless AI research and cross-device workflows*
