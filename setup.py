from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'utility library for pdf manupulation'
LONG_DESCRIPTION = 'A package that aprovides various functionalities for pdfs such as compressing, splittin, merging and converting to various formats.'

setup(
    name="pdfutil",
    version=VERSION,
    author="Nitesh (limelight)",
    author_email="<ritu10mali@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pdf2docx', 'pdf2image', 'pdf2pptx', 'PDFNetPython3', 'PyMuPDF', 'PyPDF2'],
    keywords=['python', 'pdf', 'compress', 'pdf to pptx', 'pdf to doc', 'merge pdf', 'split pdf', 'pdf to image'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)