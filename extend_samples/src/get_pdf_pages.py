"""version 0.1.0"""
from matplotlib.backends.backend_pdf import PdfPages


def get_pdf_pages(file_name: str) -> PdfPages:
    """
    Create empty PdfPages object

    Parameters
    ----------
    file_name: str

    Returns
    -------
    PdfPages
    """
    return PdfPages(file_name)
