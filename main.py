import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.documents import Document
from langchain.chains.summarize import load_summarize_chain
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, PageBreak
import win32print


######################
# Printer Management #
######################

def list_printers():
    printers = [printer[2] for printer in
                win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)]
    return printers


def is_printer_available(printer_name):
    printers = list_printers()
    return printer_name in printers


def print_pdf_windows(filepath, printer_name=None):
    printer = printer_name or win32print.GetDefaultPrinter()
    if not is_printer_available(printer):
        print(f"Printer '{printer}' is not available.")
        return
    try:
        hPrinter = win32print.OpenPrinter(printer)
        win32print.StartDocPrinter(hPrinter, 1, ("LangChain Research", None, "RAW"))
        win32print.StartPagePrinter(hPrinter)
        with open(filepath, "rb") as pdf_file:
            win32print.WritePrinter(hPrinter, pdf_file.read())
        win32print.EndPagePrinter(hPrinter)
        win32print.EndDocPrinter(hPrinter)
        win32print.ClosePrinter(hPrinter)
        print(f"Printed PDF to: {printer}")
    except Exception as e:
        print(f"Failed to print: {e}")


#################
# PDF Generation#
#################

def make_pretty_pdf(summary, topic, filename="summary.pdf"):
    styles = getSampleStyleSheet()
    # Custom style for justified paragraphs
    body_style = ParagraphStyle(name='Body', parent=styles['Normal'], alignment=4, fontSize=12, spaceAfter=12)
    doc = SimpleDocTemplate(filename, pagesize=LETTER,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=72)
    flowables = []
    # Title
    flowables.append(Paragraph(f"{topic} — AI Research Summary", styles['Title']))
    flowables.append(Spacer(1, 16))

    # Heading
    flowables.append(Paragraph("Key Takeaways", styles['Heading2']))
    flowables.append(Spacer(1, 10))

    # Extract bullets (basic sentence splitting for demo; tune as needed)
    bullet_points = [point.strip("•-* ") for point in summary.split('.') if len(point.strip()) > 16]
    flowables.append(ListFlowable(
        [ListItem(Paragraph(bp, styles['Normal']), bulletColor='black') for bp in bullet_points],
        bulletType='bullet', start='circle'))
    flowables.append(Spacer(1, 16))

    # Heading
    flowables.append(Paragraph("Full Summary", styles['Heading2']))
    flowables.append(Spacer(1, 10))
    flowables.append(Paragraph(summary, body_style))

    flowables.append(PageBreak())

    # Page numbers callback
    def add_page_number(canvas, doc):
        page_num = canvas.getPageNumber()
        text = f"Page {page_num}"
        canvas.setFont("Helvetica", 9)
        canvas.drawRightString(LETTER[0] - 40, 20, text)

    doc.build(flowables, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return filename


###################
# LangChain/Groq  #
###################

def research_and_summarize(topic):
    load_dotenv()
    groq_api = os.getenv("GROQ_API_KEY")
    # Replace with a real research method if needed
    raw_text = f"{topic}: AI is transforming healthcare with predictive diagnostics, robotic surgery, personalized medicine, and more. It enables faster data processing, better decision support, and enhanced patient outcomes."
    docs = [Document(page_content=raw_text)]
    llm = ChatGroq(
        groq_api_key=groq_api,
        model_name="llama3-70b-8192",
        temperature=0
    )
    chain = load_summarize_chain(llm, chain_type="stuff")
    summary = chain.run(docs)
    return summary


#################################
# Main: Interactive Demo Script #
#################################

if __name__ == "__main__":
    Topic = input()
    topic = Topic
    print("Checking available printers...")
    printers = list_printers()
    print("Available printers:")
    for printer in printers:
        print(" -", printer)
    if not printers:
        print("No printers found.")
        exit()

    summary = research_and_summarize(topic)
    print("\nGenerated summary:\n", summary)

    pdf_path = make_pretty_pdf(summary, topic)
    print("PDF generated:", pdf_path)

    # Choose printer and print (default or by name)
    try:
        print_choice = input("Enter printer name to use (leave empty for default): ").strip()
        printer_to_use = print_choice if print_choice else None
        if printer_to_use and not is_printer_available(printer_to_use):
            print(f"Printer '{printer_to_use}' not available. Using default instead.")
            printer_to_use = None
        print_pdf_windows(pdf_path, printer_to_use)
    except Exception as e:
        print("Printing failed:", e)
