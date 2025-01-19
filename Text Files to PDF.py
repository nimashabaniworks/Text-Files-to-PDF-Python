from fpdf import FPDF

def txt_to_pdf():
    input_file = input("Enter the path to the text file (txt): ")
    output_file = input("Enter the output PDF file name: ")
    
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        for line in lines:
            pdf.cell(200, 10, txt=line.strip(), ln=True)
        
        pdf.output(output_file)
        print(f"PDF saved as: {output_file}")
    
    except FileNotFoundError:
        print("File not found!")
