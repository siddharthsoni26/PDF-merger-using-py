from PyPDF2 import PdfMerger

merger = PdfMerger()

merger.append("Solutions QP.pdf")
merger.append("JD for PEGA 2023.pdf")

merger.write("mergeg.pdf")
merger.close()