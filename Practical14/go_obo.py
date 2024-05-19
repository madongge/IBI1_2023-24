import xml.sax
import xml.dom.minidom
import matplotlib.pyplot as plt
import datetime

# Define the XML file path
XML_FILE = '/Users/madongge/Downloads/IBI1/IBI1_2023-24/Practical14/go_obo.xml'

# Function to parse XML using DOM API
def parse_xml_dom(xml_file):
    start_time = datetime.datetime.now()
    dom_tree = xml.dom.minidom.parse(xml_file)
    terms = dom_tree.getElementsByTagName('term')
    
    mf_count = 0
    bp_count = 0
    cc_count = 0
    
    for term in terms:
        namespace = term.getElementsByTagName('namespace')[0].firstChild.data
        if namespace == 'molecular_function':
            mf_count += 1
        elif namespace == 'biological_process':
            bp_count += 1
        elif namespace == 'cellular_component':
            cc_count += 1
    
    end_time = datetime.datetime.now()
    return mf_count, bp_count, cc_count, end_time - start_time

# Function to parse XML using SAX API
class GoHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.mf_count = 0
        self.bp_count = 0
        self.cc_count = 0
        self.current_namespace = ""
    
    def startElement(self, name, attrs):
        if name == 'namespace':
            self.current_namespace = ""
    
    def characters(self, content):
        self.current_namespace += content
    
    def endElement(self, name):
        if name == 'namespace':
            if self.current_namespace == 'molecular_function':
                self.mf_count += 1
            elif self.current_namespace == 'biological_process':
                self.bp_count += 1
            elif self.current_namespace == 'cellular_component':
                self.cc_count += 1

def parse_xml_sax(xml_file):
    start_time = datetime.datetime.now()
    handler = GoHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(xml_file)
    end_time = datetime.datetime.now()
    return handler.mf_count, handler.bp_count, handler.cc_count, end_time - start_time

# Main function
def main():
    # Parse XML using DOM
    mf_dom, bp_dom, cc_dom, time_dom = parse_xml_dom(XML_FILE)
    
    # Parse XML using SAX
    mf_sax, bp_sax, cc_sax, time_sax = parse_xml_sax(XML_FILE)
    
    # Print results
    print("Results using DOM:")
    print("Molecular Function:", mf_dom)
    print("Biological Process:", bp_dom)
    print("Cellular Component:", cc_dom)
    print("Time taken by DOM:", time_dom)
    print()
    print("Results using SAX:")
    print("Molecular Function:", mf_sax)
    print("Biological Process:", bp_sax)
    print("Cellular Component:", cc_sax)
    print("Time taken by SAX:", time_sax)
    
    # Plot the results
    labels = ['Molecular Function', 'Biological Process', 'Cellular Component']
    dom_counts = [mf_dom, bp_dom, cc_dom]
    sax_counts = [mf_sax, bp_sax, cc_sax]
    
    x = range(len(labels))
    width = 0.35
    
    fig, ax = plt.subplots()
    rects1 = ax.bar(x, dom_counts, width, label='DOM')
    rects2 = ax.bar([p + width for p in x], sax_counts, width, label='SAX')
    
    ax.set_ylabel('Counts')
    ax.set_title('GO Term Counts by Ontology')
    ax.set_xticks([p + width / 2 for p in x])
    ax.set_xticklabels(labels)
    ax.legend()
    
    plt.show()

if __name__ == "__main__":
    main()
