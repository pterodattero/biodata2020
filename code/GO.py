#Generator for UniProt entries
from lxml import etree

def get_entries(f):
    entry = ''
    for line in f:
        line = line.decode()
        if line.startswith("<entry"):
            entry = ''
        entry += line
        if line.startswith("</entry>"):
            yield entry
            entry = ''


def parse_xml_entry(xml):
    root = etree.fromstring(xml)
    accession = root.find("accession", root.nsmap).text
    annotations = []
    for dbReference in root.findall("dbReference", root.nsmap):
        if dbReference.get("type") == "GO":
            annotations.append(dbReference.get("id"))
    return accession, annotations


def parse_obo(obo_file):
    # Parse the ontology, exclude obsolete terms
    graph = {}  # { term_id : term_object }
    obj = {}  # { id: term_id, name: definition, is_a: list_of_parents, is_obsolete: True, namespace: namespace }
    with open(obo_file) as f:
        for line in f:
            line = line.strip().split(": ")
            if line and len(line) > 1:
                # print(line)
                k, v = line[:2]
                if k == "id" and v.startswith("GO:"):
                    obj["id"] = v
                elif k == "name":
                    obj["def"] = v
                elif k == "is_a" and v.startswith("GO:"):
                    obj.setdefault("is_a", []).append(v.split()[0])
                elif k == "is_obsolete":
                    obj["is_obsolete"] = True
                elif k == "namespace":
                    obj["namespace"] = v
            else:
                if obj.get("id") and not obj.get("is_obsolete"):
                    if "is_a" not in obj:
                        obj["is_root"] = True
                    graph[obj["id"]] = obj
                    # print(obj)
                obj = {}
    return graph


def get_ancestors(graph):
    """
    Build a dictionary of ancestors
    and calculate term depth (shortest path)
    """

    roots = set()
    for node in graph:
        if graph[node].get("is_root"):
            roots.add(node)

    depth = {}
    ancestors = {}  # { term : list_of_ancestor_terms }
    for node in graph:
        c = 0
        node_ancestors = []
        node_parents = graph[node].get("is_a")

        # Loop parents levels (parents of parents) until no more parents
        while node_parents:
            c += 1

            # Set root
            if node not in depth and roots.intersection(set(node_parents)):
                depth[node] = c

            # Add ancestors
            node_ancestors.extend(node_parents)

            # Update the list of parents (1 level up)
            node_parents = [term for parent in node_parents for term in graph[parent].get("is_a", [])]

        ancestors[node] = set(node_ancestors)
    return ancestors, depth, roots


def get_children(ancestors):
    children = {}  # { node : list_of_children }, leaf terms are not keys
    for node in ancestors:
        for ancestor in ancestors[node]:
            children.setdefault(ancestor, set()).add(node)
    return children

