import os
from pyPdf import PdfFileReader, PdfFileWriter
from tempfile import NamedTemporaryFile
from PythonMagick import Image

reader = PdfFileReader(open("126.pdf", "rb"))
for page_num in xrange(reader.getNumPages()):
    writer = PdfFileWriter()
    writer.addPage(reader.getPage(page_num))
    temp = NamedTemporaryFile(prefix=str(page_num), suffix=".pdf", delete=False)
    writer.write(temp)
    temp.close()

    im = Image()
    im.density("300") # DPI, for better quality
    im.read(temp.name)
    im.write("test/some_%d.jpg" % (page_num))

    os.remove(temp.name)