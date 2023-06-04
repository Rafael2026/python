from PDFNetPython3 import PDFDoc, Optimizer, SDFDoc

doc = PDFDoc("PDF filepath")
doc.InitSecurityHandler()
Optimizer.Optimize(doc)
doc.Save("PDF filepath", SDFDoc.e_linearized)
doc.Close()