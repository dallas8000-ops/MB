from fpdf import FPDF

def create_pdf(input_txt, output_pdf):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    with open(input_txt, 'r', encoding='utf-8') as f:
        for line in f:
            pdf.multi_cell(0, 10, line.strip())

    pdf.output(output_pdf)

if __name__ == "__main__":
    create_pdf("blog_page_steps.txt", "blog_page_steps.pdf")