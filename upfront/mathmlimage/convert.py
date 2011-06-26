import sys, os
import subprocess

from svgmath.mathhandler import MathHandler
from svgmath.tools.saxtools import XMLGenerator
from StringIO import StringIO
from xml import sax
from lxml import etree
from xml.dom import minidom
from xml.dom import Node

_handler = None

def convert(mathml, format='PNG'):
    """ Use ImageMagick to convert svg to image.
    
        ImageMagick binaries must be available on the path.
    """

    mml_format = 'presentation'
    if "<apply>" in mathml:
        mml_format = 'content'

    if mml_format == 'content':
        xslfile = open('mathmlc2p.xsl')
        xslfile = xslfile.decode('utf-8')
        styleDoc = etree.parse(StringIO(xslfile))
        transform = etree.XSLT(styleDoc)
        doc = etree.parse(StringIO(mathml))
        result = transform(doc)
        res = transform.tostring(result)

        # Convert content mathML to presentation only mathML
        xmldoc = minidom.parseString(res).documentElement
    else:
        xmldoc = minidom.parseString(mathml).documentElement

    svgfile = StringIO()

    cwd = os.path.dirname(__file__)
    # TODO: read config location from environment
    config = open('%s/svgmath.xml' % cwd).read()

    # Create the converter as a content handler. 
    saxoutput = XMLGenerator(svgfile, 'utf-8')

    # The MathHandler parses the config file every time which is
    # very expensive. Cache the handler and override its 'ouput'
    # attribute with 'saxoutput' defined above.
    global _handler
    if _handler is None:
        _handler = MathHandler(saxoutput, StringIO(config))

    handler = _handler
    handler.output = saxoutput
    
    # Parse input file with a namespace-aware SAX parser
    parser = sax.make_parser()
    parser.setFeature(sax.handler.feature_namespaces, 1)
    parser.setContentHandler(handler)       
    try:
        parser.parse(StringIO(xmldoc.toxml('utf-8')))
    except:
        print xmldoc.toxml('utf-8')
        raise
    
    format_arg = '%s:-' % format
    svgfile.seek(0)
    process = subprocess.Popen(['convert', '-', format_arg],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate(svgfile.read())

    return stdout
