"""version 0.1.0"""
from matplotlib.backends.backend_pdf import PdfPages
from extend_samples.src.get_pdf_pages import get_pdf_pages


def test_0():
    """
    Test 0

    Test creating empty PdfPages object
    """
    file_name = "abc.pdf"
    expected_value = PdfPages(file_name)._file
    result = get_pdf_pages(file_name)._file

    assert result == expected_value
