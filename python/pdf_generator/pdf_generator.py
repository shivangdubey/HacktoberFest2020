from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


# function which generates pdf 
def generate_file(filename, title, additional_info, table_data):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]
  report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info, empty_line, report_table])
    
    
    
table_data=[
  ['Thing Name', 'Expense', 'Saving'],
  ['Sugar', 50, 2.0],
  ['Chocolates',100, 5],
  ['Fruits', 500, 100],
  ['Vegetables', 300, 25],
  ['Transport fairs', 800, 30]]
  
# sending data to generate_file function
generate_file("MyReport.pdf", "Monthly Expenses & savings", "This reports contains monthly expenses and savings and it is beneficial to have a pdf of that data.", table_data)
