import panflute as pf # Pandoc filter library

from outputfile import OutputFile
from helpers import *

def prepare(doc: pf.Doc):
    """
        Instantiate file objects for each file specified by
        the document's metadata.
    """
    doc.files = []
    try:
        class_map = doc.get_metadata()['tangle-files']
    except KeyError: # No files to tangle
        class_map = {}

    for name, classes in class_map.items():
        doc.files.append(OutputFile(name, wrap_list(classes)))

def tangle(elem: pf.Element, doc: pf.Doc) -> pf.Element:
    """
        FOr each code block in the document, extract the text and write it to
        the appropriate file based on the classes of the code block.
    """
    if isinstance(elem, pf.CodeBlock) or isinstance(elem, pf.Code): # Block or inline
        # Filter and iterate over the appropriate OutputFiles
        files = filter(
            lambda x: x.matches(elem.classes),
            doc.files)
        for file in files:
            # Write the text in the code block.
            file.write(elem.text)
    return elem # Don't change the original document

def finalize(doc: pf.Doc):
    """
        Return the doc object to its original state.
    """
    # This should also call the destructor for the OutputFile objects
    del doc.files

if __name__ == '__main__':
    pf.run_filter(tangle, prepare=prepare, finalize=finalize, doc=None)
